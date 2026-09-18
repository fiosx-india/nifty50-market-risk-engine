"""
Momentum indicators.

Indicators:
- Stochastic %K / %D
- Williams %R
- CCI
- MFI

The implementations are deterministic and do not introduce trading
decisions or BUY/SELL logic.
"""

from __future__ import annotations

from typing import Sequence


def _validate_ohlc(
    high: Sequence[float],
    low: Sequence[float],
    close: Sequence[float],
) -> tuple[list[float], list[float], list[float]]:
    if not (len(high) == len(low) == len(close)):
        raise ValueError("high, low and close must have equal lengths")

    if not high:
        return [], [], []

    h = [float(x) for x in high]
    l = [float(x) for x in low]
    c = [float(x) for x in close]

    for index, (hi, lo, cl) in enumerate(zip(h, l, c)):
        if hi < lo:
            raise ValueError(
                f"high must be greater than or equal to low at index {index}"
            )

        if not (lo <= cl <= hi):
            raise ValueError(
                f"close must be within high/low range at index {index}"
            )

    return h, l, c


def _validate_period(period: int) -> int:
    period = int(period)

    if period <= 0:
        raise ValueError("period must be positive")

    return period


def _window(
    values: Sequence[float],
    end: int,
    period: int,
) -> Sequence[float] | None:
    start = end - period + 1

    if start < 0:
        return None

    return values[start : end + 1]


def stochastic(
    high: Sequence[float],
    low: Sequence[float],
    close: Sequence[float],
    period: int = 14,
) -> float | None:
    """
    Return the latest raw Stochastic %K.

    Formula:

        %K = 100 * (Close - LowestLow)
                   / (HighestHigh - LowestLow)

    The calculation uses the latest `period` observations.
    """
    h, l, c = _validate_ohlc(high, low, close)
    period = _validate_period(period)

    if len(c) < period:
        return None

    highest = max(h[-period:])
    lowest = min(l[-period:])
    current_close = c[-1]

    range_ = highest - lowest

    if range_ == 0:
        return 0.0

    return 100.0 * (current_close - lowest) / range_


def stochastic_series(
    high: Sequence[float],
    low: Sequence[float],
    close: Sequence[float],
    period: int = 14,
    smooth: int = 3,
) -> dict[str, list[float | None]]:
    """
    Return Stochastic %K and smoothed %D series.

    %K is calculated for every observation where enough history exists.

    %D is the simple moving average of the available %K values over
    `smooth` observations.
    """
    h, l, c = _validate_ohlc(high, low, close)
    period = _validate_period(period)
    smooth = _validate_period(smooth)

    k_values: list[float | None] = [None] * len(c)

    for index in range(len(c)):
        window_high = _window(h, index, period)
        window_low = _window(l, index, period)

        if window_high is None or window_low is None:
            continue

        highest = max(window_high)
        lowest = min(window_low)
        range_ = highest - lowest

        if range_ == 0:
            k_values[index] = 0.0
        else:
            k_values[index] = (
                100.0
                * (c[index] - lowest)
                / range_
            )

    d_values: list[float | None] = [None] * len(c)

    for index in range(len(c)):
        start = index - smooth + 1

        if start < 0:
            continue

        values = [
            value
            for value in k_values[start : index + 1]
            if value is not None
        ]

        if len(values) == smooth:
            d_values[index] = sum(values) / smooth

    return {
        "k": k_values,
        "d": d_values,
    }


def williams_r(
    high: Sequence[float],
    low: Sequence[float],
    close: Sequence[float],
    period: int = 14,
) -> float | None:
    """
    Return the latest Williams %R.

    Formula:

        %R = -100 * (HighestHigh - Close)
                    / (HighestHigh - LowestLow)

    Standard range is 0 to -100.
    """
    h, l, c = _validate_ohlc(high, low, close)
    period = _validate_period(period)

    if len(c) < period:
        return None

    highest = max(h[-period:])
    lowest = min(l[-period:])
    current_close = c[-1]

    range_ = highest - lowest

    if range_ == 0:
        return 0.0

    return -100.0 * (
        (highest - current_close) / range_
    )


def cci(
    high: Sequence[float],
    low: Sequence[float],
    close: Sequence[float],
    period: int = 20,
) -> float | None:
    """
    Commodity Channel Index.

    Uses:

        Typical Price = (H + L + C) / 3

        CCI = (TP - SMA(TP)) / (0.015 * MeanDeviation)
    """
    h, l, c = _validate_ohlc(high, low, close)
    period = _validate_period(period)

    if len(c) < period:
        return None

    typical = [
        (hi + lo + cl) / 3.0
        for hi, lo, cl in zip(h, l, c)
    ]

    window = typical[-period:]
    mean = sum(window) / period

    deviation = sum(
        abs(value - mean)
        for value in window
    ) / period

    if deviation == 0:
        return 0.0

    return (
        (typical[-1] - mean)
        / (0.015 * deviation)
    )


def mfi(
    high: Sequence[float],
    low: Sequence[float],
    close: Sequence[float],
    volume: Sequence[float],
    period: int = 14,
) -> float | None:
    """
    Money Flow Index.

    Returns the latest MFI value on a 0-100 scale.
    """
    h, l, c = _validate_ohlc(high, low, close)
    period = _validate_period(period)

    if len(volume) != len(c):
        raise ValueError(
            "high, low, close and volume must have equal lengths"
        )

    if len(c) < period + 1:
        return None

    v = [float(x) for x in volume]

    typical = [
        (hi + lo + cl) / 3.0
        for hi, lo, cl in zip(h, l, c)
    ]

    positive_flow = 0.0
    negative_flow = 0.0

    start = len(c) - period

    for index in range(start, len(c)):
        raw_flow = typical[index] * v[index]

        if typical[index] > typical[index - 1]:
            positive_flow += raw_flow
        elif typical[index] < typical[index - 1]:
            negative_flow += raw_flow

    if negative_flow == 0:
        if positive_flow == 0:
            return 50.0
        return 100.0

    money_ratio = positive_flow / negative_flow

    return 100.0 - (
        100.0 / (1.0 + money_ratio)
    )


__all__ = [
    "stochastic",
    "stochastic_series",
    "williams_r",
    "cci",
    "mfi",
]
