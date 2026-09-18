"""
Trend Indicators
================

Production-safe trend indicator calculations.

Responsibilities:
- ADX / Directional Movement
- Supertrend inputs
- Ichimoku components

Rules:
- No market-specific decisions
- No BUY / SELL / HOLD decisions
- No hard-coded market results
- Deterministic calculations
- Validate inputs
- Preserve timestamp/order of observations
"""

from __future__ import annotations

from typing import Iterable, Sequence

import math


Number = float | int


def _to_float_series(values: Iterable[Number], name: str) -> list[float]:
    """Convert an iterable to finite floats without changing order."""
    result = [float(value) for value in values]

    if not result:
        raise ValueError(f"{name} must not be empty")

    if any(not math.isfinite(value) for value in result):
        raise ValueError(f"{name} contains non-finite values")

    return result


def _validate_same_length(
    high: Sequence[float],
    low: Sequence[float],
    close: Sequence[float],
) -> None:
    """Validate OHLC series lengths and geometry."""
    if not (len(high) == len(low) == len(close)):
        raise ValueError("high, low and close must have equal length")

    if len(high) < 1:
        raise ValueError("OHLC series must not be empty")

    for i, (h, l, c) in enumerate(zip(high, low, close)):
        if h < l:
            raise ValueError(f"high must be >= low at index {i}")

        if not (l <= c <= h):
            raise ValueError(
                f"close must be between low and high at index {i}"
            )


def _validate_period(period: int, name: str = "period") -> int:
    """Validate rolling-window period."""
    if isinstance(period, bool) or not isinstance(period, int):
        raise TypeError(f"{name} must be an integer")

    if period <= 0:
        raise ValueError(f"{name} must be greater than zero")

    return period


# ---------------------------------------------------------------------------
# Directional Movement / ADX
# ---------------------------------------------------------------------------


def _true_range(
    high: Sequence[float],
    low: Sequence[float],
    close: Sequence[float],
) -> list[float]:
    """Calculate True Range for every observation."""
    tr: list[float] = []

    for i in range(len(high)):
        if i == 0:
            value = high[i] - low[i]
        else:
            value = max(
                high[i] - low[i],
                abs(high[i] - close[i - 1]),
                abs(low[i] - close[i - 1]),
            )

        tr.append(float(value))

    return tr


def _directional_movement(
    high: Sequence[float],
    low: Sequence[float],
) -> tuple[list[float], list[float]]:
    """Calculate +DM and -DM."""
    plus_dm: list[float] = [0.0]
    minus_dm: list[float] = [0.0]

    for i in range(1, len(high)):
        up_move = high[i] - high[i - 1]
        down_move = low[i - 1] - low[i]

        if up_move > down_move and up_move > 0:
            plus_dm.append(float(up_move))
        else:
            plus_dm.append(0.0)

        if down_move > up_move and down_move > 0:
            minus_dm.append(float(down_move))
        else:
            minus_dm.append(0.0)

    return plus_dm, minus_dm


def _rolling_mean(
    values: Sequence[float],
    period: int,
) -> list[float | None]:
    """Simple rolling mean with None until enough observations exist."""
    period = _validate_period(period)

    result: list[float | None] = [None] * len(values)

    if len(values) < period:
        return result

    for i in range(period - 1, len(values)):
        window = values[i - period + 1 : i + 1]
        result[i] = sum(window) / period

    return result


def adx_series(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number],
    period: int = 14,
) -> dict[str, list[float | None]]:
    """
    Calculate ADX, +DI and -DI.

    Returns:
        {
            "adx": [...],
            "plus_di": [...],
            "minus_di": [...]
        }

    Values are None until sufficient observations are available.
    """
    period = _validate_period(period)

    h = _to_float_series(high, "high")
    l = _to_float_series(low, "low")
    c = _to_float_series(close, "close")

    _validate_same_length(h, l, c)

    tr = _true_range(h, l, c)
    plus_dm, minus_dm = _directional_movement(h, l)

    atr = _rolling_mean(tr, period)
    plus_dm_avg = _rolling_mean(plus_dm, period)
    minus_dm_avg = _rolling_mean(minus_dm, period)

    plus_di: list[float | None] = [None] * len(h)
    minus_di: list[float | None] = [None] * len(h)
    dx: list[float | None] = [None] * len(h)

    for i in range(len(h)):
        if (
            atr[i] is None
            or plus_dm_avg[i] is None
            or minus_dm_avg[i] is None
            or atr[i] == 0
        ):
            continue

        pdi = 100.0 * plus_dm_avg[i] / atr[i]
        mdi = 100.0 * minus_dm_avg[i] / atr[i]

        plus_di[i] = pdi
        minus_di[i] = mdi

        denominator = pdi + mdi

        if denominator == 0:
            dx[i] = 0.0
        else:
            dx[i] = 100.0 * abs(pdi - mdi) / denominator

    adx: list[float | None] = [None] * len(h)

    valid_dx = [
        value if value is not None else float("nan")
        for value in dx
    ]

    # ADX requires a full period of DX observations.
    first_dx = period - 1

    if len(h) >= first_dx + period:
        for i in range(first_dx + period - 1, len(h)):
            window = valid_dx[i - period + 1 : i + 1]

            if any(math.isnan(value) for value in window):
                continue

            adx[i] = sum(window) / period

    return {
        "adx": adx,
        "plus_di": plus_di,
        "minus_di": minus_di,
    }


def adx(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number],
    period: int = 14,
) -> float | None:
    """Return the latest available ADX value."""
    series = adx_series(high, low, close, period)

    values = series["adx"]

    for value in reversed(values):
        if value is not None:
            return float(value)

    return None


# ---------------------------------------------------------------------------
# Supertrend
# ---------------------------------------------------------------------------


def supertrend_inputs(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number],
    period: int = 10,
    multiplier: float = 3.0,
) -> dict[str, list[float | None]]:
    """
    Calculate Supertrend components.

    Returns:
        {
            "atr": [...],
            "basic_upper": [...],
            "basic_lower": [...]
        }

    This function intentionally returns calculation inputs/components.
    It does not make a trading decision.
    """
    period = _validate_period(period)

    if not math.isfinite(float(multiplier)) or multiplier <= 0:
        raise ValueError("multiplier must be a finite number greater than zero")

    h = _to_float_series(high, "high")
    l = _to_float_series(low, "low")
    c = _to_float_series(close, "close")

    _validate_same_length(h, l, c)

    tr = _true_range(h, l, c)
    atr = _rolling_mean(tr, period)

    basic_upper: list[float | None] = [None] * len(h)
    basic_lower: list[float | None] = [None] * len(h)

    for i in range(len(h)):
        if atr[i] is None:
            continue

        midpoint = (h[i] + l[i]) / 2.0

        basic_upper[i] = midpoint + multiplier * atr[i]
        basic_lower[i] = midpoint - multiplier * atr[i]

    return {
        "atr": atr,
        "basic_upper": basic_upper,
        "basic_lower": basic_lower,
    }


def supertrend(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number],
    period: int = 10,
    multiplier: float = 3.0,
) -> dict[str, list[float | None]]:
    """
    Calculate the Supertrend line and direction.

    direction:
        1  = price is above the active Supertrend line
        -1 = price is below the active Supertrend line
        None = insufficient data
    """
    period = _validate_period(period)

    if not math.isfinite(float(multiplier)) or multiplier <= 0:
        raise ValueError("multiplier must be a finite number greater than zero")

    h = _to_float_series(high, "high")
    l = _to_float_series(low, "low")
    c = _to_float_series(close, "close")

    _validate_same_length(h, l, c)

    components = supertrend_inputs(
        h,
        l,
        c,
        period=period,
        multiplier=multiplier,
    )

    atr = components["atr"]
    basic_upper = components["basic_upper"]
    basic_lower = components["basic_lower"]

    final_upper: list[float | None] = [None] * len(h)
    final_lower: list[float | None] = [None] * len(h)
    line: list[float | None] = [None] * len(h)
    direction: list[int | None] = [None] * len(h)

    for i in range(len(h)):
        if (
            atr[i] is None
            or basic_upper[i] is None
            or basic_lower[i] is None
        ):
            continue

        if i == 0 or final_upper[i - 1] is None:
            final_upper[i] = basic_upper[i]
            final_lower[i] = basic_lower[i]
            continue

        previous_upper = final_upper[i - 1]
        previous_lower = final_lower[i - 1]
        previous_close = c[i - 1]

        final_upper[i] = (
            basic_upper[i]
            if basic_upper[i] < previous_upper
            or previous_close > previous_upper
            else previous_upper
        )

        final_lower[i] = (
            basic_lower[i]
            if basic_lower[i] > previous_lower
            or previous_close < previous_lower
            else previous_lower
        )

        previous_line = line[i - 1]
        previous_direction = direction[i - 1]

        if previous_line is None:
            if c[i] <= final_upper[i]:
                line[i] = final_upper[i]
                direction[i] = -1
            else:
                line[i] = final_lower[i]
                direction[i] = 1

        elif previous_direction == -1:
            if c[i] > final_upper[i]:
                line[i] = final_lower[i]
                direction[i] = 1
            else:
                line[i] = final_upper[i]
                direction[i] = -1

        else:
            if c[i] < final_lower[i]:
                line[i] = final_upper[i]
                direction[i] = -1
            else:
                line[i] = final_lower[i]
                direction[i] = 1

    return {
        "atr": atr,
        "final_upper": final_upper,
        "final_lower": final_lower,
        "supertrend": line,
        "direction": direction,
    }


# ---------------------------------------------------------------------------
# Ichimoku
# ---------------------------------------------------------------------------


def ichimoku(
    high: Iterable[Number],
    low: Iterable[Number],
    close: Iterable[Number],
    conversion_period: int = 9,
    base_period: int = 26,
    leading_span_b_period: int = 52,
) -> dict[str, list[float | None]]:
    """
    Calculate Ichimoku components.

    Components:
        conversion_line
        base_line
        leading_span_a
        leading_span_b

    The function keeps all returned arrays aligned with the input
    observation index. No implicit positional shifting is performed.
    """
    conversion_period = _validate_period(
        conversion_period,
        "conversion_period",
    )
    base_period = _validate_period(
        base_period,
        "base_period",
    )
    leading_span_b_period = _validate_period(
        leading_span_b_period,
        "leading_span_b_period",
    )

    h = _to_float_series(high, "high")
    l = _to_float_series(low, "low")
    c = _to_float_series(close, "close")

    _validate_same_length(h, l, c)

    n = len(h)

    conversion: list[float | None] = [None] * n
    base: list[float | None] = [None] * n
    span_a: list[float | None] = [None] * n
    span_b: list[float | None] = [None] * n

    for i in range(n):
        if i + 1 >= conversion_period:
            start = i - conversion_period + 1
            highest = max(h[start : i + 1])
            lowest = min(l[start : i + 1])
            conversion[i] = (highest + lowest) / 2.0

        if i + 1 >= base_period:
            start = i - base_period + 1
            highest = max(h[start : i + 1])
            lowest = min(l[start : i + 1])
            base[i] = (highest + lowest) / 2.0

        if conversion[i] is not None and base[i] is not None:
            span_a[i] = (conversion[i] + base[i]) / 2.0

        if i + 1 >= leading_span_b_period:
            start = i - leading_span_b_period + 1
            highest = max(h[start : i + 1])
            lowest = min(l[start : i + 1])
            span_b[i] = (highest + lowest) / 2.0

    return {
        "conversion_line": conversion,
        "base_line": base,
        "leading_span_a": span_a,
        "leading_span_b": span_b,
    }


__all__ = [
    "adx",
    "adx_series",
    "supertrend_inputs",
    "supertrend",
    "ichimoku",
]
