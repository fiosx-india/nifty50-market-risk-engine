"""Core technical indicators.

Pure calculations only. No BUY/SELL decisions, scores, ranks, probabilities,
or recommendations.

The public functions preserve the existing module API by returning the latest
calculated value (or None when there is insufficient valid history).
"""

from __future__ import annotations

from math import isfinite
from typing import Any, Sequence


_EPS = 1e-12


def _numeric(values: Sequence[Any], name: str = "values") -> list[float]:
    """Convert a sequence to finite floats without destroying time alignment."""
    if values is None:
        raise ValueError(f"{name} cannot be None.")

    result: list[float] = []
    for value in values:
        if value is None:
            raise ValueError(f"{name} contains None; time-series alignment would be lost.")
        try:
            number = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{name} contains a non-numeric value.") from exc
        if not isfinite(number):
            raise ValueError(f"{name} contains a non-finite value.")
        result.append(number)
    return result


def _period(period: int) -> int:
    if isinstance(period, bool) or not isinstance(period, int) or period <= 0:
        raise ValueError("period must be a positive integer.")
    return period


def _aligned_ohlcv(
    high: Sequence[Any],
    low: Sequence[Any],
    close: Sequence[Any],
    volume: Sequence[Any] | None = None,
):
    h = _numeric(high, "high")
    l = _numeric(low, "low")
    c = _numeric(close, "close")

    if not (len(h) == len(l) == len(c)):
        raise ValueError("high, low and close must have equal lengths.")

    if volume is None:
        return h, l, c, None

    v = _numeric(volume, "volume")
    if len(v) != len(c):
        raise ValueError("volume must have the same length as high/low/close.")
    if any(x < 0 for x in v):
        raise ValueError("volume cannot be negative.")

    return h, l, c, v


def sma(values, period=20):
    """Simple moving average of the latest `period` observations."""
    p = _period(period)
    v = _numeric(values)
    if len(v) < p:
        return None
    return sum(v[-p:]) / p


def ema(values, period=20):
    """EMA using the standard SMA seed followed by recursive smoothing."""
    p = _period(period)
    v = _numeric(values)
    if len(v) < p:
        return None

    e = sum(v[:p]) / p
    alpha = 2.0 / (p + 1.0)
    for x in v[p:]:
        e = alpha * x + (1.0 - alpha) * e
    return e


def wma(values, period=20):
    """Weighted moving average with linearly increasing weights."""
    p = _period(period)
    v = _numeric(values)
    if len(v) < p:
        return None

    x = v[-p:]
    denominator = p * (p + 1) / 2.0
    return sum((i + 1) * z for i, z in enumerate(x)) / denominator


def roc(values, period=12):
    """Rate of change in percent over `period` observations."""
    p = _period(period)
    v = _numeric(values)
    if len(v) <= p:
        return None

    base = v[-p - 1]
    if abs(base) <= _EPS:
        return None
    return (v[-1] / base - 1.0) * 100.0


def momentum(values, period=10):
    """Price momentum: latest value minus value `period` observations earlier."""
    p = _period(period)
    v = _numeric(values)
    if len(v) <= p:
        return None
    return v[-1] - v[-p - 1]


def rsi(values, period=14):
    """Latest RSI using Wilder's smoothing.

    Returns None until enough price changes exist to form the initial average.
    """
    p = _period(period)
    v = _numeric(values)
    if len(v) <= p:
        return None

    changes = [v[i] - v[i - 1] for i in range(1, len(v))]
    gains = [max(change, 0.0) for change in changes]
    losses = [max(-change, 0.0) for change in changes]

    avg_gain = sum(gains[:p]) / p
    avg_loss = sum(losses[:p]) / p

    for gain, loss in zip(gains[p:], losses[p:]):
        avg_gain = ((p - 1) * avg_gain + gain) / p
        avg_loss = ((p - 1) * avg_loss + loss) / p

    if avg_loss <= _EPS:
        return 100.0
    if avg_gain <= _EPS:
        return 0.0

    rs = avg_gain / avg_loss
    return 100.0 - (100.0 / (1.0 + rs))


def atr(high, low, close, period=14):
    """Latest ATR using Wilder true-range smoothing."""
    p = _period(period)
    h, l, c, _ = _aligned_ohlcv(high, low, close)

    if len(c) <= p:
        return None

    true_ranges = [h[0] - l[0]]
    for i in range(1, len(c)):
        true_ranges.append(
            max(
                h[i] - l[i],
                abs(h[i] - c[i - 1]),
                abs(l[i] - c[i - 1]),
            )
        )

    if len(true_ranges) < p:
        return None

    atr_value = sum(true_ranges[:p]) / p
    for tr in true_ranges[p:]:
        atr_value = ((p - 1) * atr_value + tr) / p

    return atr_value


def bollinger(values, period=20, deviations=2):
    """Latest Bollinger middle/upper/lower bands."""
    p = _period(period)
    if isinstance(deviations, bool) or not isinstance(deviations, (int, float)):
        raise ValueError("deviations must be numeric.")
    d = float(deviations)
    if d < 0 or not isfinite(d):
        raise ValueError("deviations must be finite and non-negative.")

    v = _numeric(values)
    if len(v) < p:
        return None

    x = v[-p:]
    mean = sum(x) / p
    variance = sum((z - mean) ** 2 for z in x) / p
    std = variance ** 0.5

    return {
        "middle": mean,
        "upper": mean + d * std,
        "lower": mean - d * std,
    }


def vwap(high, low, close, volume):
    """Volume-weighted average price across the supplied aligned series."""
    h, l, c, vol = _aligned_ohlcv(high, low, close, volume)

    if not h:
        return None

    volume_total = sum(vol)
    if volume_total <= _EPS:
        return None

    typical_price_volume = sum(
        ((h[i] + l[i] + c[i]) / 3.0) * vol[i]
        for i in range(len(h))
    )
    return typical_price_volume / volume_total


__all__ = [
    "sma",
    "ema",
    "wma",
    "roc",
    "momentum",
    "rsi",
    "atr",
    "bollinger",
    "vwap",
]
