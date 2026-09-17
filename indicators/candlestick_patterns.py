"""Candlestick pattern observations.

This module detects candle geometry and, when prior-candle context is supplied,
context-dependent patterns. It does not make BUY/SELL decisions.

Design goals:
- Preserve the existing public function names.
- Validate OHLC inputs and reject invalid candles.
- Keep time-series alignment intact.
- Distinguish geometric shape from contextual interpretation.
- Never emit trading decisions, scores, ranks, probabilities, or recommendations.
"""

from __future__ import annotations

from typing import Any, Mapping, Optional, Sequence


_EPS = 1e-12


def _ohlc(o: Any, h: Any, l: Any, c: Any) -> tuple[float, float, float, float]:
    """Convert and validate one OHLC candle."""
    try:
        o, h, l, c = map(float, (o, h, l, c))
    except (TypeError, ValueError) as exc:
        raise ValueError("OHLC values must be numeric.") from exc

    values = (o, h, l, c)
    if not all(map(lambda x: x == x, values)):  # NaN check
        raise ValueError("OHLC values must not contain NaN.")

    if h < l:
        raise ValueError("High cannot be lower than low.")

    if not (l <= o <= h and l <= c <= h):
        raise ValueError("Open and close must lie within the candle range.")

    return o, h, l, c


def _parts(o: float, h: float, l: float, c: float) -> tuple[float, float, float, float]:
    """Return body, upper shadow, lower shadow and range."""
    body = abs(c - o)
    upper = h - max(o, c)
    lower = min(o, c) - l
    range_ = h - l
    return body, upper, lower, range_


def _trend_from_closes(closes: Sequence[Any], lookback: int = 3) -> Optional[str]:
    """Infer simple prior trend from closes only.

    Returns:
        'bullish', 'bearish', or None when there is insufficient/flat context.
    """
    if lookback < 1:
        raise ValueError("lookback must be >= 1.")

    try:
        values = [float(x) for x in closes]
    except (TypeError, ValueError) as exc:
        raise ValueError("Prior closes must be numeric.") from exc

    if len(values) < lookback + 1:
        return None

    window = values[-(lookback + 1):]
    delta = window[-1] - window[0]

    if delta > _EPS:
        return "bullish"
    if delta < -_EPS:
        return "bearish"
    return None


def doji(o, h, l, c, threshold=0.10):
    """Detect a small-body candle relative to its full range."""
    if not 0 <= float(threshold) <= 1:
        raise ValueError("threshold must be between 0 and 1.")

    o, h, l, c = _ohlc(o, h, l, c)
    _, _, _, r = _parts(o, h, l, c)
    return bool(r > _EPS and abs(c - o) / r <= float(threshold))


def hammer(o, h, l, c):
    """Detect hammer-shaped candle geometry.

    Context is intentionally not assumed here. Use detect_last(..., prior_closes=...)
    when a contextual classification is required.
    """
    o, h, l, c = _ohlc(o, h, l, c)
    body, upper, lower, _ = _parts(o, h, l, c)
    body_ref = max(body, _EPS)

    return bool(lower >= 2.0 * body_ref and upper <= body_ref)


def inverted_hammer(o, h, l, c):
    """Detect inverted-hammer-shaped candle geometry."""
    o, h, l, c = _ohlc(o, h, l, c)
    body, upper, lower, _ = _parts(o, h, l, c)
    body_ref = max(body, _EPS)

    return bool(upper >= 2.0 * body_ref and lower <= body_ref)


def shooting_star(o, h, l, c):
    """Detect shooting-star-shaped candle geometry.

    A strict shooting-star interpretation also needs prior uptrend context.
    This low-level function therefore reports only the candle geometry, preserving
    the existing API. detect_last() can use prior_closes for context.
    """
    return inverted_hammer(o, h, l, c)


def hanging_man(o, h, l, c):
    """Detect hanging-man-shaped candle geometry.

    A strict hanging-man interpretation also needs prior uptrend context.
    This low-level function therefore reports only the candle geometry.
    """
    return hammer(o, h, l, c)


def bullish_engulfing(po, pc, o, c):
    """Detect a two-candle bullish engulfing body."""
    try:
        po, pc, o, c = map(float, (po, pc, o, c))
    except (TypeError, ValueError) as exc:
        raise ValueError("Engulfing inputs must be numeric.") from exc

    if pc >= po or c <= o:
        return False

    # Current real body must contain the previous real body.
    return bool(o <= pc and c >= po)


def bearish_engulfing(po, pc, o, c):
    """Detect a two-candle bearish engulfing body."""
    try:
        po, pc, o, c = map(float, (po, pc, o, c))
    except (TypeError, ValueError) as exc:
        raise ValueError("Engulfing inputs must be numeric.") from exc

    if pc <= po or c >= o:
        return False

    return bool(o >= pc and c <= po)


def spinning_top(o, h, l, c, threshold=0.35):
    """Detect a relatively small real body."""
    if not 0 <= float(threshold) <= 1:
        raise ValueError("threshold must be between 0 and 1.")

    o, h, l, c = _ohlc(o, h, l, c)
    _, _, _, r = _parts(o, h, l, c)
    return bool(r > _EPS and abs(c - o) / r <= float(threshold))


def marubozu(o, h, l, c, threshold=0.05):
    """Detect a candle whose shadows are small relative to its range."""
    if not 0 <= float(threshold) <= 1:
        raise ValueError("threshold must be between 0 and 1.")

    o, h, l, c = _ohlc(o, h, l, c)
    _, upper, lower, r = _parts(o, h, l, c)

    if r <= _EPS:
        return False

    t = float(threshold)
    return bool(upper / r <= t and lower / r <= t)


def _extract_candle(candle: Mapping[str, Any]) -> tuple[float, float, float, float]:
    """Extract one candle from a mapping using the established OHLC keys."""
    if not isinstance(candle, Mapping):
        raise TypeError("c must be a mapping containing open/high/low/close.")

    try:
        return _ohlc(
            candle["open"],
            candle["high"],
            candle["low"],
            candle["close"],
        )
    except KeyError as exc:
        raise KeyError("c must contain open, high, low and close.") from exc


def detect_last(
    c: Mapping[str, Any],
    *,
    prior_closes: Optional[Sequence[Any]] = None,
    prior_opens: Optional[Sequence[Any]] = None,
    trend_lookback: int = 3,
):
    """Detect patterns for one candle.

    `prior_closes` is optional. When supplied, it enables a context-aware
    distinction between hammer/inverted-hammer geometry and the conventional
    hanging-man/shooting-star context.

    The returned mapping contains observations only.
    """
    o, h, l, cl = _extract_candle(c)

    trend = _trend_from_closes(prior_closes, trend_lookback) if prior_closes is not None else None

    result = {
        "doji": doji(o, h, l, cl),
        "hammer": hammer(o, h, l, cl),
        "inverted_hammer": inverted_hammer(o, h, l, cl),
        "shooting_star": False,
        "hanging_man": False,
        "bullish_engulfing": False,
        "bearish_engulfing": False,
        "spinning_top": spinning_top(o, h, l, cl),
        "marubozu": marubozu(o, h, l, cl),
    }

    # Contextual interpretations:
    # - shooting star: inverted-hammer geometry after an uptrend
    # - hanging man: hammer geometry after an uptrend
    result["shooting_star"] = bool(
        result["inverted_hammer"] and trend == "bullish"
    )
    result["hanging_man"] = bool(
        result["hammer"] and trend == "bullish"
    )

    # Optional two-candle body patterns when the previous OHLC is available.
    if prior_opens is not None and prior_closes is not None:
        if len(prior_opens) and len(prior_closes):
            result["bullish_engulfing"] = bullish_engulfing(
                prior_opens[-1], prior_closes[-1], o, cl
            )
            result["bearish_engulfing"] = bearish_engulfing(
                prior_opens[-1], prior_closes[-1], o, cl
            )

    return result


__all__ = [
    "doji",
    "hammer",
    "inverted_hammer",
    "shooting_star",
    "hanging_man",
    "bullish_engulfing",
    "bearish_engulfing",
    "spinning_top",
    "marubozu",
    "detect_last",
]
