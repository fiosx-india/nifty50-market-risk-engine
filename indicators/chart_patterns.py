"""
Chart Pattern / Price Structure Indicators
===========================================

Pure price-structure calculations.

Responsibilities:
- Higher High
- Higher Low
- Lower High
- Lower Low
- Range levels
- Breakout
- Breakdown

This module does NOT:
- make BUY / SELL decisions
- calculate probabilities
- assign confidence
- infer causation
- use market-specific rules

Higher orchestration layers may combine these observations with
other evidence.
"""

from __future__ import annotations

import math
from typing import Iterable


Number = float | int


def _series(values: Iterable[Number], name: str) -> list[float]:
    result = [float(value) for value in values]

    if not result:
        raise ValueError(f"{name} must not be empty")

    if any(not math.isfinite(value) for value in result):
        raise ValueError(f"{name} contains non-finite values")

    return result


def _same_length(*values: list[float]) -> None:
    if len({len(value) for value in values}) != 1:
        raise ValueError("all input series must have equal length")


# ---------------------------------------------------------------------------
# Basic swing comparisons
# ---------------------------------------------------------------------------


def higher_high(
    previous_high: Number,
    current_high: Number,
) -> bool:
    """Return True when current high is greater than previous high."""
    previous = float(previous_high)
    current = float(current_high)

    if not math.isfinite(previous) or not math.isfinite(current):
        raise ValueError("high values must be finite")

    return current > previous


def higher_low(
    previous_low: Number,
    current_low: Number,
) -> bool:
    """Return True when current low is greater than previous low."""
    previous = float(previous_low)
    current = float(current_low)

    if not math.isfinite(previous) or not math.isfinite(current):
        raise ValueError("low values must be finite")

    return current > previous


def lower_high(
    previous_high: Number,
    current_high: Number,
) -> bool:
    """Return True when current high is lower than previous high."""
    previous = float(previous_high)
    current = float(current_high)

    if not math.isfinite(previous) or not math.isfinite(current):
        raise ValueError("high values must be finite")

    return current < previous


def lower_low(
    previous_low: Number,
    current_low: Number,
) -> bool:
    """Return True when current low is lower than previous low."""
    previous = float(previous_low)
    current = float(current_low)

    if not math.isfinite(previous) or not math.isfinite(current):
        raise ValueError("low values must be finite")

    return current < previous


# ---------------------------------------------------------------------------
# Series structure
# ---------------------------------------------------------------------------


def higher_high_series(
    highs: Iterable[Number],
) -> list[bool]:
    """
    Compare each high with the immediately preceding high.

    First observation has no predecessor and is False.
    """
    values = _series(highs, "highs")

    result = [False]

    for i in range(1, len(values)):
        result.append(values[i] > values[i - 1])

    return result


def higher_low_series(
    lows: Iterable[Number],
) -> list[bool]:
    """
    Compare each low with the immediately preceding low.

    First observation has no predecessor and is False.
    """
    values = _series(lows, "lows")

    result = [False]

    for i in range(1, len(values)):
        result.append(values[i] > values[i - 1])

    return result


def lower_high_series(
    highs: Iterable[Number],
) -> list[bool]:
    """
    Compare each high with the immediately preceding high.

    First observation has no predecessor and is False.
    """
    values = _series(highs, "highs")

    result = [False]

    for i in range(1, len(values)):
        result.append(values[i] < values[i - 1])

    return result


def lower_low_series(
    lows: Iterable[Number],
) -> list[bool]:
    """
    Compare each low with the immediately preceding low.

    First observation has no predecessor and is False.
    """
    values = _series(lows, "lows")

    result = [False]

    for i in range(1, len(values)):
        result.append(values[i] < values[i - 1])

    return result


# ---------------------------------------------------------------------------
# Range levels
# ---------------------------------------------------------------------------


def range_levels(
    high: Iterable[Number],
    low: Iterable[Number],
) -> dict[str, float]:
    """
    Return the overall observed high, low, midpoint and range width.
    """
    highs = _series(high, "high")
    lows = _series(low, "low")

    _same_length(highs, lows)

    if any(h < l for h, l in zip(highs, lows)):
        raise ValueError("high must be >= low")

    highest = max(highs)
    lowest = min(lows)

    return {
        "high": highest,
        "low": lowest,
        "midpoint": (highest + lowest) / 2.0,
        "range": highest - lowest,
    }


def rolling_range_levels(
    high: Iterable[Number],
    low: Iterable[Number],
    period: int,
) -> list[dict[str, float] | None]:
    """
    Calculate rolling high/low range levels.

    A value is returned only after a complete period is available.
    """
    if isinstance(period, bool) or not isinstance(period, int):
        raise TypeError("period must be an integer")

    if period <= 0:
        raise ValueError("period must be greater than zero")

    highs = _series(high, "high")
    lows = _series(low, "low")

    _same_length(highs, lows)

    if any(h < l for h, l in zip(highs, lows)):
        raise ValueError("high must be >= low")

    result: list[dict[str, float] | None] = [None] * len(highs)

    for i in range(period - 1, len(highs)):
        high_window = highs[i - period + 1 : i + 1]
        low_window = lows[i - period + 1 : i + 1]

        highest = max(high_window)
        lowest = min(low_window)

        result[i] = {
            "high": highest,
            "low": lowest,
            "midpoint": (highest + lowest) / 2.0,
            "range": highest - lowest,
        }

    return result


# ---------------------------------------------------------------------------
# Breakout / Breakdown
# ---------------------------------------------------------------------------


def breakout(
    close: Number,
    resistance: Number,
) -> bool:
    """
    Return True when close is strictly above the supplied resistance.
    """
    price = float(close)
    level = float(resistance)

    if not math.isfinite(price) or not math.isfinite(level):
        raise ValueError("close and resistance must be finite")

    return price > level


def breakdown(
    close: Number,
    support: Number,
) -> bool:
    """
    Return True when close is strictly below the supplied support.
    """
    price = float(close)
    level = float(support)

    if not math.isfinite(price) or not math.isfinite(level):
        raise ValueError("close and support must be finite")

    return price < level


def breakout_series(
    close: Iterable[Number],
    resistance: Iterable[Number],
) -> list[bool]:
    """Compare aligned close and resistance series."""
    closes = _series(close, "close")
    levels = _series(resistance, "resistance")

    _same_length(closes, levels)

    return [
        price > level
        for price, level in zip(closes, levels)
    ]


def breakdown_series(
    close: Iterable[Number],
    support: Iterable[Number],
) -> list[bool]:
    """Compare aligned close and support series."""
    closes = _series(close, "close")
    levels = _series(support, "support")

    _same_length(closes, levels)

    return [
        price < level
        for price, level in zip(closes, levels)
    ]


# ---------------------------------------------------------------------------
# Structure snapshot
# ---------------------------------------------------------------------------


def structure_snapshot(
    high: Iterable[Number],
    low: Iterable[Number],
) -> dict[str, object]:
    """
    Return descriptive price-structure observations.

    No directional trading decision is made here.
    """
    highs = _series(high, "high")
    lows = _series(low, "low")

    _same_length(highs, lows)

    return {
        "higher_high": higher_high_series(highs),
        "higher_low": higher_low_series(lows),
        "lower_high": lower_high_series(highs),
        "lower_low": lower_low_series(lows),
        "range_levels": range_levels(highs, lows),
    }


__all__ = [
    "higher_high",
    "higher_low",
    "lower_high",
    "lower_low",
    "higher_high_series",
    "higher_low_series",
    "lower_high_series",
    "lower_low_series",
    "range_levels",
    "rolling_range_levels",
    "breakout",
    "breakdown",
    "breakout_series",
    "breakdown_series",
    "structure_snapshot",
]
