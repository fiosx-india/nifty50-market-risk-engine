"""Volume and price-volume evidence.

Validation-focused volume observations. These functions calculate descriptive
evidence only; they do not produce trading decisions.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import isfinite
from typing import Any


def _numeric_sequence(values: Sequence[Any], name: str) -> list[float]:
    result: list[float] = []
    for value in values:
        number = float(value)
        if not isfinite(number):
            raise ValueError(f"{name} must contain only finite numbers")
        result.append(number)
    return result


def _positive_period(period: int) -> int:
    if isinstance(period, bool) or not isinstance(period, int) or period <= 0:
        raise ValueError("period must be a positive integer")
    return period


def relative_volume(volume: Sequence[Any], period: int = 20) -> float | None:
    """Return latest volume divided by the previous-period average volume."""
    period = _positive_period(period)
    values = _numeric_sequence(volume, "volume")
    if len(values) < period + 1:
        return None

    avg = sum(values[-period - 1:-1]) / period
    return values[-1] / avg if avg else None


def obv(close: Sequence[Any], volume: Sequence[Any]) -> float:
    """Return cumulative On-Balance Volume for the common observation range."""
    prices = _numeric_sequence(close, "close")
    volumes = _numeric_sequence(volume, "volume")

    if len(prices) < 2 or len(volumes) < 2:
        return 0.0

    count = min(len(prices), len(volumes))
    value = 0.0

    for i in range(1, count):
        if prices[i] > prices[i - 1]:
            value += volumes[i]
        elif prices[i] < prices[i - 1]:
            value -= volumes[i]

    return value


def accumulation_distribution(
    high: Sequence[Any],
    low: Sequence[Any],
    close: Sequence[Any],
    volume: Sequence[Any],
) -> float:
    """Return cumulative Accumulation/Distribution line value."""
    highs = _numeric_sequence(high, "high")
    lows = _numeric_sequence(low, "low")
    closes = _numeric_sequence(close, "close")
    volumes = _numeric_sequence(volume, "volume")

    count = min(len(highs), len(lows), len(closes), len(volumes))
    total = 0.0

    for i in range(count):
        h, l, c, v = highs[i], lows[i], closes[i], volumes[i]
        if h < l:
            raise ValueError("high cannot be below low")
        if c < l or c > h:
            raise ValueError("close must be within high/low range")

        money_flow_multiplier = (
            ((c - l) - (h - c)) / (h - l)
            if h != l
            else 0.0
        )
        total += money_flow_multiplier * v

    return total


def price_volume_confirmation(
    close: Sequence[Any], volume: Sequence[Any]
) -> dict[str, bool]:
    """Describe whether price and volume moved in the same direction."""
    prices = _numeric_sequence(close, "close")
    volumes = _numeric_sequence(volume, "volume")

    if len(prices) < 2 or len(volumes) < 2:
        return {"confirmed": False}

    price_up = prices[-1] > prices[-2]
    volume_up = volumes[-1] > volumes[-2]

    return {
        "price_up": price_up,
        "volume_up": volume_up,
        "confirmed": price_up == volume_up,
    }
