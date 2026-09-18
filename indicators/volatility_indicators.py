"""
Volatility Indicators
=====================

Pure calculation layer for volatility measurements.

Responsibilities:
- Returns
- True Range
- Realized Volatility
- Volatility Percentile

No trading decisions.
No BUY/SELL/HOLD.
No hard-coded market assumptions.
"""

from __future__ import annotations

import math
from typing import Iterable


Number = float | int


def _to_float_series(values: Iterable[Number], name: str) -> list[float]:
    result = [float(value) for value in values]

    if not result:
        raise ValueError(f"{name} must not be empty")

    if any(not math.isfinite(value) for value in result):
        raise ValueError(f"{name} contains non-finite values")

    return result


def _validate_period(period: int) -> int:
    if isinstance(period, bool) or not isinstance(period, int):
        raise TypeError("period must be an integer")

    if period <= 0:
        raise ValueError("period must be greater than zero")

    return period


def _validate_ohlc(
    high: list[float],
    low: list[float],
    close: list[float],
) -> None:
    if not (len(high) == len(low) == len(close)):
        raise ValueError("high, low and close must have equal length")

    for i, (h, l, c) in enumerate(zip(high, low, close)):
        if h < l:
            raise ValueError(f"high must be >= low at index {i}")

        if not l <= c <= h:
            raise ValueError(
                f"close must be between low and high at index {i}"
            )


def returns(
    close: Iterable[Number],
) -> list[float | None]:
    """
    Calculate simple percentage returns.

    The first observation has no previous close, so its return is None.
    """
    prices = _to_float_series(close, "close")

    result: list[float | None] = [None]

    for i in range(1, len(prices)):
        previous = prices[i - 1]
        current = prices[i]

        if previous == 0:
            result.append(None)
        else:
            result.append((current / previous) - 1.0)

    return result


def log_returns(
    close: Iterable[Number],
) -> list[float | None]:
    """
    Calculate continuously compounded returns.

    Non-positive prices are invalid for logarithmic returns.
    """
    prices = _to_float_series(close, "close")

    if any(price <= 0 for price in prices):
        raise ValueError("close must contain only positive values")

    result: list[float | None] = [None]

    for i in range(1, len(prices)):
        result.append(math.log(prices[i] / prices[i - 1]))

    return result


def true_range(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number],
) -> list[float]:
    """
    Calculate True Range.

    For the first observation:
        TR = high - low

    Thereafter:
        TR = max(
            high - low,
            abs(high - previous_close),
            abs(low - previous_close)
        )
    """
    h = _to_float_series(high, "high")
    l = _to_float_series(low, "low")
    c = _to_float_series(close, "close")

    _validate_ohlc(h, l, c)

    result: list[float] = []

    for i in range(len(h)):
        if i == 0:
            result.append(h[i] - l[i])
        else:
            result.append(
                max(
                    h[i] - l[i],
                    abs(h[i] - c[i - 1]),
                    abs(l[i] - c[i - 1]),
                )
            )

    return result


def realized_volatility(
    close: Iterable[Number],
    period: int = 20,
    annualization_factor: float | None = None,
) -> list[float | None]:
    """
    Calculate rolling realized volatility from log returns.

    Result is rolling standard deviation.

    If annualization_factor is supplied, volatility is multiplied by
    sqrt(annualization_factor).

    Example:
        daily data -> annualization_factor commonly 252
        hourly data -> caller supplies the appropriate factor
    """
    period = _validate_period(period)

    if annualization_factor is not None:
        annualization_factor = float(annualization_factor)

        if (
            not math.isfinite(annualization_factor)
            or annualization_factor <= 0
        ):
            raise ValueError(
                "annualization_factor must be finite and greater than zero"
            )

    log_ret = log_returns(close)

    result: list[float | None] = [None] * len(log_ret)

    values = [
        value for value in log_ret
        if value is not None
    ]

    if len(values) < period:
        return result

    # Map rolling windows back to the original observation index.
    for i in range(period, len(log_ret)):
        window = log_ret[i - period + 1 : i + 1]

        if any(value is None for value in window):
            continue

        numeric = [float(value) for value in window]

        mean = sum(numeric) / len(numeric)

        variance = sum(
            (value - mean) ** 2
            for value in numeric
        ) / len(numeric)

        volatility = math.sqrt(variance)

        if annualization_factor is not None:
            volatility *= math.sqrt(annualization_factor)

        result[i] = volatility

    return result


def volatility_percentile(
    volatility: Iterable[Number | None],
    window: int = 252,
) -> list[float | None]:
    """
    Calculate the percentile rank of each volatility observation
    against the preceding rolling window.

    The current observation is included in its own comparison window.

    Output range:
        0.0 to 100.0
    """
    window = _validate_period(window)

    values = list(volatility)

    result: list[float | None] = [None] * len(values)

    for i, current in enumerate(values):
        if current is None:
            continue

        current_value = float(current)

        if not math.isfinite(current_value):
            raise ValueError(
                f"volatility contains non-finite value at index {i}"
            )

        start = max(0, i - window + 1)

        historical = [
            float(value)
            for value in values[start : i + 1]
            if value is not None
        ]

        if not historical:
            continue

        less = sum(
            value < current_value
            for value in historical
        )

        equal = sum(
            value == current_value
            for value in historical
        )

        # Mid-rank percentile for ties.
        rank = less + (equal + 1) / 2.0

        if len(historical) == 1:
            result[i] = 100.0
        else:
            result[i] = (
                (rank - 1.0)
                / (len(historical) - 1.0)
            ) * 100.0

    return result


def volatility_summary(
    close: Iterable[Number],
    period: int = 20,
) -> dict[str, float | None]:
    """
    Return the latest available volatility measurements.

    This is a calculation summary only; it does not interpret the result.
    """
    close_values = _to_float_series(close, "close")

    ret = returns(close_values)
    log_ret = log_returns(close_values)
    rv = realized_volatility(
        close_values,
        period=period,
    )

    latest_return = next(
        (
            float(value)
            for value in reversed(ret)
            if value is not None
        ),
        None,
    )

    latest_log_return = next(
        (
            float(value)
            for value in reversed(log_ret)
            if value is not None
        ),
        None,
    )

    latest_volatility = next(
        (
            float(value)
            for value in reversed(rv)
            if value is not None
        ),
        None,
    )

    return {
        "latest_return": latest_return,
        "latest_log_return": latest_log_return,
        "realized_volatility": latest_volatility,
    }


__all__ = [
    "returns",
    "log_returns",
    "true_range",
    "realized_volatility",
    "volatility_percentile",
    "volatility_summary",
]
