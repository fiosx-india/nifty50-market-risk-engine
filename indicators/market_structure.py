"""
Market Structure Indicators
===========================

Pure price-structure observations.

Responsibilities:
- Swing high / swing low detection
- Market structure state
- Break of Structure (BOS)
- Liquidity zones

This module only produces observations.
It does not make trading decisions.
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


def _validate_period(period: int) -> int:
    if isinstance(period, bool) or not isinstance(period, int):
        raise TypeError("period must be an integer")

    if period <= 0:
        raise ValueError("period must be greater than zero")

    return period


def swing_points(
    high: Iterable[Number],
    low: Iterable[Number],
    left: int = 1,
    right: int = 1,
) -> dict[str, list[bool]]:
    """
    Detect local swing highs and swing lows.

    A swing high occurs when the current high is greater than all
    highs in the left and right observation windows.

    A swing low occurs when the current low is lower than all
    lows
    in the left and right observation windows.

    Boundary observations without a complete window are False.
    """
    left = _validate_period(left)
    right = _validate_period(right)

    highs = _series(high, "high")
    lows = _series(low, "low")

    _same_length(highs, lows)

    swing_high = [False] * len(highs)
    swing_low = [False] * len(lows)

    start = left
    end = len(highs) - right

    for i in range(start, end):
        left_highs = highs[i - left : i]
        right_highs = highs[i + 1 : i + right + 1]

        left_lows = lows[i - left : i]
        right_lows = lows[i + 1 : i + right + 1]

        if (
            highs[i] > max(left_highs)
            and highs[i] > max(right_highs)
        ):
            swing_high[i] = True

        if (
            lows[i] < min(left_lows)
            and lows[i] < min(right_lows)
        ):
            swing_low[i] = True

    return {
        "swing_high": swing_high,
        "swing_low": swing_low,
    }


def structure_state(
    high: Iterable[Number],
    low: Iterable[Number],
) -> list[str]:
    """
    Describe local structure transitions.

    Possible values:
    - "HH"
    - "HL"
    - "LH"
    - "LL"
    - "NEUTRAL"

    The classification is based only on the immediately preceding
    high/low observation.
    """
    highs = _series(high, "high")
    lows = _series(low, "low")

    _same_length(highs, lows)

    result = ["NEUTRAL"]

    for i in range(1, len(highs)):
        higher_h = highs[i] > highs[i - 1]
        lower_h = highs[i] < highs[i - 1]

        higher_l = lows[i] > lows[i - 1]
        lower_l = lows[i] < lows[i - 1]

        if higher_h and higher_l:
            result.append("HH_HL")
        elif lower_h and lower_l:
            result.append("LH_LL")
        elif higher_h:
            result.append("HH")
        elif lower_h:
            result.append("LH")
        elif higher_l:
            result.append("HL")
        elif lower_l:
            result.append("LL")
        else:
            result.append("NEUTRAL")

    return result


def bos(
    close: Iterable[Number],
    swing_high: Iterable[Number],
    swing_low: Iterable[Number],
) -> dict[str, list[bool]]:
    """
    Detect Break of Structure relative to the latest confirmed
    swing levels.

    bullish_bos:
        close moves strictly above the latest confirmed swing high.

    bearish_bos:
        close moves strictly below the latest confirmed swing low.

    The current observation is compared only with previously known
    swing levels, preventing lookahead from the current candle.
    """
    closes = _series(close, "close")
    highs = _series(swing_high, "swing_high")
    lows = _series(swing_low, "swing_low")

    _same_length(closes, highs, lows)

    bullish = [False] * len(closes)
    bearish = [False] * len(closes)

    latest_high: float | None = None
    latest_low: float | None = None

    for i in range(len(closes)):
        if i > 0:
            if highs[i - 1]:
                latest_high = max(
                    [
                        value
                        for j, value in enumerate(highs[:i])
                        if value
                    ],
                    default=None,
                )

            if lows[i - 1]:
                latest_low = min(
                    [
                        value
                        for j, value in enumerate(lows[:i])
                        if value
                    ],
                    default=None,
                )

        if latest_high is not None:
            bullish[i] = closes[i] > latest_high

        if latest_low is not None:
            bearish[i] = closes[i] < latest_low

    return {
        "bullish_bos": bullish,
        "bearish_bos": bearish,
    }


def liquidity_zones(
    high: Iterable[Number],
    low: Iterable[Number],
    tolerance: float = 0.001,
) -> dict[str, list[dict[str, float]]]:
    """
    Identify repeated high/low price areas.

    Prices are grouped when their relative difference is within
    the supplied tolerance.

    This is a structural observation, not a prediction.
    """
    if not isinstance(tolerance, (int, float)):
        raise TypeError("tolerance must be numeric")

    tolerance = float(tolerance)

    if not math.isfinite(tolerance):
        raise ValueError("tolerance must be finite")

    if tolerance < 0:
        raise ValueError("tolerance must not be negative")

    highs = _series(high, "high")
    lows = _series(low, "low")

    _same_length(highs, lows)

    def _group(values: list[float]) -> list[dict[str, float]]:
        groups: list[dict[str, float]] = []

        for value in values:
            matched = False

            for group in groups:
                reference = group["price"]

                if reference == 0:
                    difference = abs(value - reference)
                else:
                    difference = abs(value - reference) / abs(reference)

                if difference <= tolerance:
                    count = group["count"]
                    group["price"] = (
                        reference * count + value
                    ) / (count + 1)
                    group["count"] = count + 1
                    matched = True
                    break

            if not matched:
                groups.append(
                    {
                        "price": value,
                        "count": 1.0,
                    }
                )

        return groups

    return {
        "high_zones": _group(highs),
        "low_zones": _group(lows),
    }


def market_structure_snapshot(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number] | None = None,
) -> dict[str, object]:
    """
    Return a combined structural observation snapshot.

    If close is supplied, BOS observations are included.
    """
    highs = _series(high, "high")
    lows = _series(low, "low")

    _same_length(highs, lows)

    swings = swing_points(highs, lows)
    state = structure_state(highs, lows)
    zones = liquidity_zones(highs, lows)

    result: dict[str, object] = {
        "swing_points": swings,
        "structure_state": state,
        "liquidity_zones": zones,
    }

    if close is not None:
        closes = _series(close, "close")
        _same_length(highs, closes)

        result["bos"] = bos(
            closes,
            swings["swing_high"],
            swings["swing_low"],
        )

    return result


__all__ = [
    "swing_points",
    "structure_state",
    "bos",
    "liquidity_zones",
    "market_structure_snapshot",
            ]
