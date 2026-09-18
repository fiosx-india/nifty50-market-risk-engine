"""
Volume Indicators
=================

Pure volume/price-volume calculations.

Responsibilities:
- Relative Volume
- On-Balance Volume (OBV)
- Accumulation/Distribution
- Price-volume confirmation

No BUY / SELL / HOLD decisions.
No market-specific assumptions.
No hard-coded results.
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


def _period(period: int) -> int:
    if isinstance(period, bool) or not isinstance(period, int):
        raise TypeError("period must be an integer")

    if period <= 0:
        raise ValueError("period must be greater than zero")

    return period


def _same_length(*values: list[float]) -> None:
    lengths = {len(value) for value in values}

    if len(lengths) != 1:
        raise ValueError("all input series must have equal length")


def _validate_ohlc(
    high: list[float],
    low: list[float],
    close: list[float],
) -> None:
    _same_length(high, low, close)

    for i, (h, l, c) in enumerate(zip(high, low, close)):
        if h < l:
            raise ValueError(f"high must be >= low at index {i}")

        if not l <= c <= h:
            raise ValueError(
                f"close must be between low and high at index {i}"
            )


# ---------------------------------------------------------------------------
# Relative Volume
# ---------------------------------------------------------------------------


def relative_volume(
    volume: Iterable[Number],
    period: int = 20,
) -> list[float | None]:
    """
    Calculate current volume divided by rolling average volume.

    The current observation is included in the rolling window.
    """
    period = _period(period)
    values = _series(volume, "volume")

    if any(value < 0 for value in values):
        raise ValueError("volume must not contain negative values")

    result: list[float | None] = [None] * len(values)

    for i in range(period - 1, len(values)):
        window = values[i - period + 1 : i + 1]
        average = sum(window) / period

        if average == 0:
            result[i] = None
        else:
            result[i] = values[i] / average

    return result


# ---------------------------------------------------------------------------
# On-Balance Volume
# ---------------------------------------------------------------------------


def obv_series(
    close: Iterable[Number],
    volume: Iterable[Number],
) -> list[float]:
    """
    Calculate cumulative On-Balance Volume.

    Rules:
    - rising close  -> add volume
    - falling close -> subtract volume
    - unchanged     -> unchanged
    """
    prices = _series(close, "close")
    volumes = _series(volume, "volume")

    _same_length(prices, volumes)

    if any(value < 0 for value in volumes):
        raise ValueError("volume must not contain negative values")

    result: list[float] = [0.0]

    for i in range(1, len(prices)):
        previous = result[-1]

        if prices[i] > prices[i - 1]:
            result.append(previous + volumes[i])
        elif prices[i] < prices[i - 1]:
            result.append(previous - volumes[i])
        else:
            result.append(previous)

    return result


def obv(
    close: Iterable[Number],
    volume: Iterable[Number],
) -> float:
    """Return the latest OBV value."""
    return obv_series(close, volume)[-1]


# ---------------------------------------------------------------------------
# Accumulation / Distribution
# ---------------------------------------------------------------------------


def accumulation_distribution_series(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number],
    volume: Iterable[Number],
) -> list[float]:
    """
    Calculate cumulative Accumulation/Distribution Line.

    Money Flow Multiplier:

        ((Close - Low) - (High - Close)) / (High - Low)

    Money Flow Volume:

        multiplier * volume
    """
    h = _series(high, "high")
    l = _series(low, "low")
    c = _series(close, "close")
    v = _series(volume, "volume")

    _validate_ohlc(h, l, c)
    _same_length(h, v)

    if any(value < 0 for value in v):
        raise ValueError("volume must not contain negative values")

    result: list[float] = []
    cumulative = 0.0

    for high_value, low_value, close_value, volume_value in zip(
        h,
        l,
        c,
        v,
    ):
        spread = high_value - low_value

        if spread == 0:
            multiplier = 0.0
        else:
            multiplier = (
                (close_value - low_value)
                - (high_value - close_value)
            ) / spread

        cumulative += multiplier * volume_value
        result.append(cumulative)

    return result


def accumulation_distribution(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number],
    volume: Iterable[Number],
) -> float:
    """Return the latest Accumulation/Distribution value."""
    return accumulation_distribution_series(
        high,
        low,
        close,
        volume,
    )[-1]


# ---------------------------------------------------------------------------
# Price-Volume Confirmation
# ---------------------------------------------------------------------------


def price_volume_confirmation(
    close: Iterable[Number],
    volume: Iterable[Number],
    period: int = 20,
) -> list[float | None]:
    """
    Calculate a descriptive price-volume confirmation metric.

    Formula:

        sign(price return) * relative volume

    Interpretation is intentionally left to higher layers.

    Positive:
        price increased while volume was above/below average according
        to the magnitude.

    Negative:
        price decreased.

    Zero:
        unchanged price.
    """
    period = _period(period)

    prices = _series(close, "close")
    volumes = _series(volume, "volume")

    _same_length(prices, volumes)

    if any(value < 0 for value in volumes):
        raise ValueError("volume must not contain negative values")

    rv = relative_volume(
        volumes,
        period=period,
    )

    result: list[float | None] = [None] * len(prices)

    for i in range(1, len(prices)):
        if rv[i] is None:
            continue

        if prices[i] > prices[i - 1]:
            result[i] = rv[i]
        elif prices[i] < prices[i - 1]:
            result[i] = -rv[i]
        else:
            result[i] = 0.0

    return result


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------


def volume_summary(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number],
    volume: Iterable[Number],
    period: int = 20,
) -> dict[str, float | None]:
    """Return the latest available volume-related measurements."""
    h = _series(high, "high")
    l = _series(low, "low")
    c = _series(close, "close")
    v = _series(volume, "volume")

    _validate_ohlc(h, l, c)
    _same_length(h, v)

    rv = relative_volume(v, period=period)
    obv_values = obv_series(c, v)
    ad_values = accumulation_distribution_series(h, l, c, v)
    pv_values = price_volume_confirmation(c, v, period=period)

    return {
        "relative_volume": rv[-1],
        "obv": obv_values[-1],
        "accumulation_distribution": ad_values[-1],
        "price_volume_confirmation": pv_values[-1],
    }


__all__ = [
    "relative_volume",
    "obv_series",
    "obv",
    "accumulation_distribution_series",
    "accumulation_distribution",
    "price_volume_confirmation",
    "volume_summary",
]
