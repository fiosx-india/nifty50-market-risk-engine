"""Multi-candle/chart pattern observations.

Descriptive pattern measurements only. No trading decisions.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import isfinite
from typing import Any


def _finite(values: Sequence[Any], name: str) -> list[float]:
    result = []
    for value in values:
        number = float(value)
        if not isfinite(number):
            raise ValueError(f"{name} must contain only finite numbers")
        result.append(number)
    return result


def _level(value: Any, name: str = "level") -> float:
    number = float(value)
    if not isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


def higher_high(high: Sequence[Any]) -> bool:
    values = _finite(high, "high")
    return len(values) >= 2 and values[-1] > values[-2]


def higher_low(low: Sequence[Any]) -> bool:
    values = _finite(low, "low")
    return len(values) >= 2 and values[-1] > values[-2]


def lower_high(high: Sequence[Any]) -> bool:
    values = _finite(high, "high")
    return len(values) >= 2 and values[-1] < values[-2]


def lower_low(low: Sequence[Any]) -> bool:
    values = _finite(low, "low")
    return len(values) >= 2 and values[-1] < values[-2]


def range_levels(
    high: Sequence[Any],
    low: Sequence[Any],
    lookback: int = 20,
) -> dict[str, float] | None:
    """Return observed resistance/support from the requested lookback."""
    highs = _finite(high, "high")
    lows = _finite(low, "low")

    if isinstance(lookback, bool) or not isinstance(lookback, int) or lookback <= 0:
        raise ValueError("lookback must be a positive integer")
    if len(highs) != len(lows):
        raise ValueError("high and low must have equal lengths")
    if any(h < l for h, l in zip(highs, lows)):
        raise ValueError("high cannot be below low")
    if len(highs) < lookback:
        return None

    return {
        "resistance": max(highs[-lookback:]),
        "support": min(lows[-lookback:]),
    }


def breakout(close: Sequence[Any], level: Any) -> bool:
    """Return whether the latest close is above the supplied level."""
    values = _finite(close, "close")
    return bool(values) and values[-1] > _level(level)


def breakdown(close: Sequence[Any], level: Any) -> bool:
    """Return whether the latest close is below the supplied level."""
    values = _finite(close, "close")
    return bool(values) and values[-1] < _level(level)
