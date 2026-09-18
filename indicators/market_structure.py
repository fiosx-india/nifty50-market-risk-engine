"""Market structure: swings, BOS and liquidity observations.

Descriptive market-structure evidence only. No trading decisions.
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


def _window_size(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")
    return value


def swing_points(
    high: Sequence[Any],
    low: Sequence[Any],
    left: int = 2,
    right: int = 2,
) -> list[dict[str, Any]]:
    """Identify local swing highs/lows using a symmetric observation window."""
    highs = _finite(high, "high")
    lows = _finite(low, "low")
    if len(highs) != len(lows):
        raise ValueError("high and low must have equal lengths")
    if any(h < l for h, l in zip(highs, lows)):
        raise ValueError("high cannot be below low")

    left = _window_size(left, "left")
    right = _window_size(right, "right")
    if len(highs) <= left + right:
        return []

    out = []
    for i in range(left, len(highs) - right):
        h_window = highs[i - left:i + right + 1]
        l_window = lows[i - left:i + right + 1]

        is_swing_high = highs[i] >= max(h_window)
        is_swing_low = lows[i] <= min(l_window)

        # A bar can legitimately be both when the window is degenerate.
        if is_swing_high:
            out.append({"index": i, "type": "swing_high", "price": highs[i]})
        if is_swing_low:
            out.append({"index": i, "type": "swing_low", "price": lows[i]})

    return out


def structure_state(
    high: Sequence[Any], low: Sequence[Any]
) -> dict[str, Any]:
    """Summarize the latest higher/lower swing relationships."""
    points = swing_points(high, low)
    swing_highs = [x["price"] for x in points if x["type"] == "swing_high"]
    swing_lows = [x["price"] for x in points if x["type"] == "swing_low"]

    return {
        "higher_high": len(swing_highs) > 1 and swing_highs[-1] > swing_highs[-2],
        "higher_low": len(swing_lows) > 1 and swing_lows[-1] > swing_lows[-2],
        "lower_high": len(swing_highs) > 1 and swing_highs[-1] < swing_highs[-2],
        "lower_low": len(swing_lows) > 1 and swing_lows[-1] < swing_lows[-2],
        "swings": points,
    }


def bos(
    close: Sequence[Any],
    prior_high: Any = None,
    prior_low: Any = None,
) -> dict[str, bool]:
    """Report whether the latest close is beyond supplied structure levels."""
    closes = _finite(close, "close")
    if not closes:
        return {"bullish": False, "bearish": False}

    bullish = (
        prior_high is not None
        and isfinite(float(prior_high))
        and closes[-1] > float(prior_high)
    )
    bearish = (
        prior_low is not None
        and isfinite(float(prior_low))
        and closes[-1] < float(prior_low)
    )

    return {"bullish": bullish, "bearish": bearish}


def liquidity_zones(
    high: Sequence[Any],
    low: Sequence[Any],
    tolerance: float = 0.001,
) -> list[dict[str, Any]]:
    """Group nearby high/low levels and retain levels touched at least twice."""
    highs = _finite(high, "high")
    lows = _finite(low, "low")
    if len(highs) != len(lows):
        raise ValueError("high and low must have equal lengths")
    if any(h < l for h, l in zip(highs, lows)):
        raise ValueError("high cannot be below low")

    tolerance = float(tolerance)
    if not isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and non-negative")

    levels = sorted(highs + lows)
    if not levels:
        return []

    zones = []
    for level in levels:
        if not zones:
            zones.append({"level": level, "touches": 1})
            continue

        reference = zones[-1]["level"]
        denominator = max(abs(level), 1e-12)
        if abs(level - reference) / denominator > tolerance:
            zones.append({"level": level, "touches": 1})
        else:
            zones[-1]["touches"] += 1

    return [zone for zone in zones if zone["touches"] >= 2]
