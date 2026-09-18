from __future__ import annotations

import math

import pytest

from indicators.chart_patterns import (
    higher_high,
    higher_high_series,
    higher_low,
    higher_low_series,
    lower_high,
    lower_high_series,
    lower_low,
    lower_low_series,
    range_levels,
    rolling_range_levels,
    breakout,
    breakdown,
    breakout_series,
    breakdown_series,
    structure_snapshot,
)


def test_higher_high():
    assert higher_high(100, 110) is True
    assert higher_high(110, 100) is False
    assert higher_high(100, 100) is False


def test_higher_low():
    assert higher_low(90, 95) is True
    assert higher_low(95, 90) is False
    assert higher_low(90, 90) is False


def test_lower_high():
    assert lower_high(110, 100) is True
    assert lower_high(100, 110) is False
    assert lower_high(100, 100) is False


def test_lower_low():
    assert lower_low(100, 90) is True
    assert lower_low(90, 100) is False
    assert lower_low(100, 100) is False


def test_higher_high_series():
    result = higher_high_series([100, 105, 103, 110])

    assert result == [False, True, False, True]


def test_higher_low_series():
    result = higher_low_series([90, 95, 92, 100])

    assert result == [False, True, False, True]


def test_lower_high_series():
    result = lower_high_series([110, 105, 108, 100])

    assert result == [False, True, False, True]


def test_lower_low_series():
    result = lower_low_series([100, 95, 98, 90])

    assert result == [False, True, False, True]


def test_range_levels():
    high = [110, 115, 112]
    low = [90, 92, 88]

    result = range_levels(high, low)

    assert result["high"] == pytest.approx(115.0)
    assert result["low"] == pytest.approx(88.0)
    assert result["midpoint"] == pytest.approx(101.5)
    assert result["range"] == pytest.approx(27.0)


def test_rolling_range_levels():
    high = [100, 110, 120, 115]
    low = [90, 95, 100, 105]

    result = rolling_range_levels(high, low, period=3)

    assert result[0] is None
    assert result[1] is None

    assert result[2] == {
        "high": 120.0,
        "low": 90.0,
        "midpoint": 105.0,
        "range": 30.0,
    }

    assert result[3] == {
        "high": 120.0,
        "low": 95.0,
        "midpoint": 107.5,
        "range": 25.0,
    }


def test_breakout_requires_strictly_above_resistance():
    assert breakout(101, 100) is True
    assert breakout(100, 100) is False
    assert breakout(99, 100) is False


def test_breakdown_requires_strictly_below_support():
    assert breakdown(99, 100) is True
    assert breakdown(100, 100) is False
    assert breakdown(101, 100) is False


def test_breakout_series():
    close = [99, 101, 100, 105]
    resistance = [100, 100, 100, 104]

    result = breakout_series(close, resistance)

    assert result == [False, True, False, True]


def test_breakdown_series():
    close = [101, 99, 100, 95]
    support = [100, 100, 100, 96]

    result = breakdown_series(close, support)

    assert result == [False, True, False, True]


def test_structure_snapshot():
    high = [100, 105, 103, 110]
    low = [90, 95, 92, 100]

    result = structure_snapshot(high, low)

    assert result["higher_high"] == [False, True, False, True]
    assert result["higher_low"] == [False, True, False, True]
    assert result["lower_high"] == [False, False, True, False]
    assert result["lower_low"] == [False, False, True, False]

    assert result["range_levels"]["high"] == pytest.approx(110.0)
    assert result["range_levels"]["low"] == pytest.approx(90.0)


def test_rejects_empty_series():
    with pytest.raises(ValueError):
        higher_high_series([])

    with pytest.raises(ValueError):
        higher_low_series([])

    with pytest.raises(ValueError):
        lower_high_series([])

    with pytest.raises(ValueError):
        lower_low_series([])

    with pytest.raises(ValueError):
        range_levels([], [])


def test_rejects_non_finite_scalar_values():
    with pytest.raises(ValueError):
        higher_high(float("nan"), 100)

    with pytest.raises(ValueError):
        lower_low(100, float("inf"))

    with pytest.raises(ValueError):
        breakout(float("nan"), 100)

    with pytest.raises(ValueError):
        breakdown(100, float("inf"))


def test_rejects_non_finite_series_values():
    with pytest.raises(ValueError):
        higher_high_series([100, float("nan")])

    with pytest.raises(ValueError):
        lower_low_series([100, float("inf")])


def test_rejects_mismatched_range_lengths():
    with pytest.raises(ValueError):
        range_levels(
            [100, 110],
            [90],
        )


def test_rejects_invalid_ohlc_relationship():
    with pytest.raises(ValueError):
        range_levels(
            [90, 100],
            [100, 95],
        )


def test_rejects_invalid_rolling_period():
    with pytest.raises(ValueError):
        rolling_range_levels(
            [100, 110],
            [90, 95],
            0,
        )


def test_rejects_non_integer_rolling_period():
    with pytest.raises(TypeError):
        rolling_range_levels(
            [100, 110],
            [90, 95],
            2.5,
        )


def test_breakout_series_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        breakout_series(
            [100, 101],
            [100],
        )


def test_breakdown_series_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        breakdown_series(
            [100, 101],
            [100],
        )


def test_structure_snapshot_does_not_modify_inputs():
    high = [100, 105, 110]
    low = [90, 95, 100]

    original_high = high.copy()
    original_low = low.copy()

    structure_snapshot(high, low)

    assert high == original_high
    assert low == original_low


def test_range_levels_returns_finite_values():
    result = range_levels(
        [100, 110, 105],
        [90, 95, 92],
    )

    for value in result.values():
        assert math.isfinite(value)


def test_rolling_range_has_no_lookahead():
    high = [100, 110, 120, 200]
    low = [90, 95, 100, 190]

    result = rolling_range_levels(
        high,
        low,
        period=3,
    )

    # Index 2 must use only observations 0, 1, 2.
    assert result[2]["high"] == pytest.approx(120.0)
    assert result[2]["low"] == pytest.approx(90.0)
