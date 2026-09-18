"""Volatility measurements.

Descriptive volatility calculations only. No trading or directional decisions.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import isfinite, sqrt
from typing import Any


def _finite_values(values: Sequence[Any], name: str) -> list[float]:
    result = []
    for value in values:
        number = float(value)
        if not isfinite(number):
            raise ValueError(f"{name} must contain only finite numbers")
        result.append(number)
    return result


def _positive_annualization(value: Any) -> float:
    number = float(value)
    if not isfinite(number) or number <= 0:
        raise ValueError("annualization must be a finite positive number")
    return number


def returns(close: Sequence[Any]) -> list[float]:
    """Return simple close-to-close returns without silently dropping zeros."""
    c = _finite_values(close, "close")
    result = []
    for i in range(1, len(c)):
        if c[i - 1] == 0:
            raise ValueError("cannot calculate return with zero prior close")
        result.append(c[i] / c[i - 1] - 1.0)
    return result


def realized_volatility(
    close: Sequence[Any], annualization: Any = None
) -> float | None:
    """Return sample standard deviation of close-to-close returns."""
    r = returns(close)
    if len(r) < 2:
        return None

    mean = sum(r) / len(r)
    variance = sum((value - mean) ** 2 for value in r) / (len(r) - 1)
    volatility = sqrt(variance)

    if annualization is not None:
        volatility *= sqrt(_positive_annualization(annualization))

    return volatility


def volatility_percentile(
    current: Any, history: Sequence[Any]
) -> float | None:
    """Return the inclusive empirical percentile of current in history."""
    current_value = float(current)
    if not isfinite(current_value):
        raise ValueError("current must be finite")

    h = sorted(_finite_values(history, "history"))
    if not h:
        return None

    return 100.0 * sum(value <= current_value for value in h) / len(h)


def true_range_series(
    high: Sequence[Any], low: Sequence[Any], close: Sequence[Any]
) -> list[float]:
    """Return true range from the second observation onward."""
    highs = _finite_values(high, "high")
    lows = _finite_values(low, "low")
    closes = _finite_values(close, "close")

    count = min(len(highs), len(lows), len(closes))
    for i in range(count):
        if highs[i] < lows[i]:
            raise ValueError("high cannot be below low")
        if closes[i] < lows[i] or closes[i] > highs[i]:
            raise ValueError("close must be within high/low range")

    return [
        max(
            highs[i] - lows[i],
            abs(highs[i] - closes[i - 1]),
            abs(lows[i] - closes[i - 1]),
        )
        for i in range(1, count)
    ]
