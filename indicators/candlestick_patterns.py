"""
Candlestick pattern detection.

Design rules:
- Basic candle geometry functions do not require market context.
- Contextual patterns may use prior closes when supplied.
- inverted_hammer is geometry-based.
- shooting_star requires prior upward context.
- No context must never invent a contextual shooting-star signal.
"""

from __future__ import annotations

from typing import Sequence


def _values(open_, high, low, close):
    o, h, l, c = map(float, (open_, high, low, close))

    if h < l:
        raise ValueError("high must be greater than or equal to low")

    if not (l <= o <= h):
        raise ValueError("open must be within high/low range")

    if not (l <= c <= h):
        raise ValueError("close must be within high/low range")

    return o, h, l, c


def _geometry(open_, high, low, close):
    o, h, l, c = _values(open_, high, low, close)

    body = abs(c - o)
    upper_wick = h - max(o, c)
    lower_wick = min(o, c) - l
    range_ = h - l

    return o, h, l, c, body, upper_wick, lower_wick, range_


def doji(open_, high, low, close, threshold: float = 0.10) -> bool:
    """
    Return True when the candle body is small relative to its range.
    """
    _, _, _, _, body, _, _, range_ = _geometry(
        open_, high, low, close
    )

    if range_ <= 0:
        return False

    return body / range_ <= float(threshold)


def hammer(open_, high, low, close) -> bool:
    """
    Geometry-only hammer detection.

    Long lower shadow, small body near the upper end,
    and limited upper shadow.
    """
    _, _, _, _, body, upper_wick, lower_wick, _ = _geometry(
        open_, high, low, close
    )

    reference_body = max(body, 1e-12)

    return (
        lower_wick >= 2.0 * reference_body
        and upper_wick <= reference_body
    )


def inverted_hammer(open_, high, low, close) -> bool:
    """
    Geometry-only inverted hammer detection.

    The candle has:
    - a relatively small real body,
    - a long upper shadow,
    - a small lower shadow.

    No trend/context information is required here.
    """
    _, _, _, _, body, upper_wick, lower_wick, _ = _geometry(
        open_, high, low, close
    )

    reference_body = max(body, 1e-12)

    return (
        upper_wick >= 2.0 * reference_body
        and lower_wick <= reference_body
    )


def shooting_star(
    open_,
    high,
    low,
    close,
    prior_closes: Sequence[float] | None = None,
) -> bool:
    """
    Detect a shooting star.

    Shooting star uses the same basic geometry as an inverted hammer,
    but requires evidence of an upward prior context.

    If prior_closes is not supplied, return False because the contextual
    requirement cannot be established.
    """
    if not inverted_hammer(open_, high, low, close):
        return False

    if prior_closes is None:
        return False

    closes = [float(value) for value in prior_closes]

    if len(closes) < 2:
        return False

    # Required context:
    # the prior sequence should show an upward progression.
    #
    # We deliberately use a simple, deterministic structural condition
    # rather than inventing a percentage threshold.
    return closes[-1] > closes[0]


def hanging_man(
    open_,
    high,
    low,
    close,
    prior_closes: Sequence[float] | None = None,
) -> bool:
    """
    Detect hanging-man geometry.

    Context can be supplied to distinguish it from a generic hammer,
    but the basic geometry remains hammer geometry.
    """
    if not hammer(open_, high, low, close):
        return False

    if prior_closes is None:
        return True

    closes = [float(value) for value in prior_closes]

    if len(closes) < 2:
        return False

    return closes[-1] > closes[0]


def bullish_engulfing(
    open_,
    high_,
    low_,
    close_,
    previous_open,
    previous_close,
) -> bool:
    """
    Detect a bullish engulfing candle.
    """
    o, _, _, c = _values(open_, high_, low_, close_)
    po = float(previous_open)
    pc = float(previous_close)

    previous_bearish = pc < po
    current_bullish = c > o

    return (
        previous_bearish
        and current_bullish
        and o <= pc
        and c >= po
    )


def bearish_engulfing(
    open_,
    high_,
    low_,
    close_,
    previous_open,
    previous_close,
) -> bool:
    """
    Detect a bearish engulfing candle.
    """
    o, _, _, c = _values(open_, high_, low_, close_)
    po = float(previous_open)
    pc = float(previous_close)

    previous_bullish = pc > po
    current_bearish = c < o

    return (
        previous_bullish
        and current_bearish
        and o >= pc
        and c <= po
    )


def spinning_top(
    open_,
    high_,
    low_,
    close_,
    max_body_ratio: float = 0.30,
) -> bool:
    """
    Detect a spinning-top style candle.
    """
    _, _, _, _, body, upper_wick, lower_wick, range_ = _geometry(
        open_, high_, low_, close_
    )

    if range_ <= 0:
        return False

    return (
        body / range_ <= float(max_body_ratio)
        and upper_wick > body
        and lower_wick > body
    )


def marubozu(
    open_,
    high_,
    low_,
    close_,
    tolerance: float = 0.05,
) -> bool:
    """
    Detect a near-marubozu candle.

    tolerance is expressed as a fraction of the candle range.
    """
    _, _, _, _, body, upper_wick, lower_wick, range_ = _geometry(
        open_, high_, low_, close_
    )

    if range_ <= 0:
        return False

    allowed = range_ * float(tolerance)

    return upper_wick <= allowed and lower_wick <= allowed


def detect_last(
    candle: dict,
    prior_closes: Sequence[float] | None = None,
) -> dict[str, bool]:
    """
    Detect supported patterns for the latest candle.

    Contextual patterns:
    - shooting_star requires prior_closes.
    - hanging_man uses prior_closes when available.

    Geometry-only patterns remain available without context.
    """
    required = ("open", "high", "low", "close")

    missing = [key for key in required if key not in candle]
    if missing:
        raise ValueError(
            f"candle missing required fields: {', '.join(missing)}"
        )

    o = candle["open"]
    h = candle["high"]
    l = candle["low"]
    c = candle["close"]

    return {
        "doji": doji(o, h, l, c),
        "hammer": hammer(o, h, l, c),
        "inverted_hammer": inverted_hammer(o, h, l, c),
        "shooting_star": shooting_star(
            o,
            h,
            l,
            c,
            prior_closes=prior_closes,
        ),
        "hanging_man": hanging_man(
            o,
            h,
            l,
            c,
            prior_closes=prior_closes,
        ),
        "bullish_engulfing": False,
        "bearish_engulfing": False,
        "spinning_top": spinning_top(o, h, l, c),
        "marubozu": marubozu(o, h, l, c),
    }


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
