"""
Tests for indicators.trend_indicators
"""

import math

import pytest

from indicators.trend_indicators import (
    adx,
    adx_series,
    ichimoku,
    supertrend,
    supertrend_inputs,
)


def sample_ohlc(count=80):
    close = [
        100.0 + i * 0.5 + (i % 5) * 0.1
        for i in range(count)
    ]

    high = [value + 2.0 for value in close]
    low = [value - 2.0 for value in close]

    return high, low, close


# ---------------------------------------------------------------------------
# ADX
# ---------------------------------------------------------------------------


def test_adx_series_returns_expected_keys():
    high, low, close = sample_ohlc()

    result = adx_series(
        high,
        low,
        close,
        period=14,
    )

    assert set(result) == {
        "adx",
        "plus_di",
        "minus_di",
    }


def test_adx_series_preserves_input_length():
    high, low, close = sample_ohlc(80)

    result = adx_series(
        high,
        low,
        close,
        period=14,
    )

    assert len(result["adx"]) == 80
    assert len(result["plus_di"]) == 80
    assert len(result["minus_di"]) == 80


def test_adx_requires_sufficient_history():
    high, low, close = sample_ohlc(10)

    result = adx_series(
        high,
        low,
        close,
        period=14,
    )

    assert all(value is None for value in result["adx"])


def test_adx_returns_latest_available_value():
    high, low, close = sample_ohlc(100)

    result = adx(
        high,
        low,
        close,
        period=14,
    )

    assert result is not None
    assert math.isfinite(result)
    assert 0.0 <= result <= 100.0


def test_adx_short_series_returns_none():
    high, low, close = sample_ohlc(10)

    result = adx(
        high,
        low,
        close,
        period=14,
    )

    assert result is None


def test_adx_validates_equal_lengths():
    high, low, close = sample_ohlc(30)

    with pytest.raises(ValueError):
        adx(
            high,
            low[:-1],
            close,
            period=14,
        )


def test_adx_rejects_invalid_ohlc_geometry():
    high, low, close = sample_ohlc(30)

    high[5] = 90.0
    low[5] = 100.0

    with pytest.raises(ValueError):
        adx_series(
            high,
            low,
            close,
            period=14,
        )


def test_adx_rejects_close_outside_range():
    high, low, close = sample_ohlc(30)

    close[5] = 200.0

    with pytest.raises(ValueError):
        adx_series(
            high,
            low,
            close,
            period=14,
        )


def test_adx_rejects_invalid_period():
    high, low, close = sample_ohlc(30)

    with pytest.raises(ValueError):
        adx(
            high,
            low,
            close,
            period=0,
        )


def test_adx_rejects_boolean_period():
    high, low, close = sample_ohlc(30)

    with pytest.raises(TypeError):
        adx(
            high,
            low,
            close,
            period=True,
        )


# ---------------------------------------------------------------------------
# Supertrend
# ---------------------------------------------------------------------------


def test_supertrend_inputs_returns_expected_keys():
    high, low, close = sample_ohlc()

    result = supertrend_inputs(
        high,
        low,
        close,
        period=10,
        multiplier=3.0,
    )

    assert set(result) == {
        "atr",
        "basic_upper",
        "basic_lower",
    }


def test_supertrend_inputs_preserves_length():
    high, low, close = sample_ohlc(60)

    result = supertrend_inputs(
        high,
        low,
        close,
        period=10,
        multiplier=3.0,
    )

    assert len(result["atr"]) == 60
    assert len(result["basic_upper"]) == 60
    assert len(result["basic_lower"]) == 60


def test_supertrend_requires_period_history_for_atr():
    high, low, close = sample_ohlc(5)

    result = supertrend_inputs(
        high,
        low,
        close,
        period=10,
    )

    assert all(value is None for value in result["atr"])
    assert all(value is None for value in result["basic_upper"])
    assert all(value is None for value in result["basic_lower"])


def test_supertrend_basic_bands_are_ordered():
    high, low, close = sample_ohlc(60)

    result = supertrend_inputs(
        high,
        low,
        close,
        period=10,
        multiplier=3.0,
    )

    for upper, lower in zip(
        result["basic_upper"],
        result["basic_lower"],
    ):
        if upper is None or lower is None:
            continue

        assert upper >= lower


def test_supertrend_returns_expected_keys():
    high, low, close = sample_ohlc(80)

    result = supertrend(
        high,
        low,
        close,
        period=10,
        multiplier=3.0,
    )

    assert set(result) == {
        "atr",
        "final_upper",
        "final_lower",
        "supertrend",
        "direction",
    }


def test_supertrend_preserves_length():
    high, low, close = sample_ohlc(80)

    result = supertrend(
        high,
        low,
        close,
        period=10,
        multiplier=3.0,
    )

    for key in result:
        assert len(result[key]) == 80


def test_supertrend_direction_is_valid():
    high, low, close = sample_ohlc(100)

    result = supertrend(
        high,
        low,
        close,
        period=10,
        multiplier=3.0,
    )

    directions = [
        value
        for value in result["direction"]
        if value is not None
    ]

    assert directions
    assert all(value in (-1, 1) for value in directions)


def test_supertrend_line_is_finite_when_available():
    high, low, close = sample_ohlc(100)

    result = supertrend(
        high,
        low,
        close,
        period=10,
        multiplier=3.0,
    )

    values = [
        value
        for value in result["supertrend"]
        if value is not None
    ]

    assert values
    assert all(math.isfinite(value) for value in values)


def test_supertrend_rejects_invalid_multiplier():
    high, low, close = sample_ohlc(50)

    with pytest.raises(ValueError):
        supertrend(
            high,
            low,
            close,
            period=10,
            multiplier=0,
        )


def test_supertrend_rejects_negative_multiplier():
    high, low, close = sample_ohlc(50)

    with pytest.raises(ValueError):
        supertrend(
            high,
            low,
            close,
            period=10,
            multiplier=-1,
        )


# ---------------------------------------------------------------------------
# Ichimoku
# ---------------------------------------------------------------------------


def test_ichimoku_returns_expected_keys():
    high, low, close = sample_ohlc(100)

    result = ichimoku(
        high,
        low,
        close,
    )

    assert set(result) == {
        "conversion_line",
        "base_line",
        "leading_span_a",
        "leading_span_b",
    }


def test_ichimoku_preserves_length():
    high, low, close = sample_ohlc(100)

    result = ichimoku(
        high,
        low,
        close,
    )

    for values in result.values():
        assert len(values) == 100


def test_ichimoku_conversion_line_uses_conversion_period():
    high, low, close = sample_ohlc(20)

    result = ichimoku(
        high,
        low,
        close,
        conversion_period=9,
        base_period=26,
        leading_span_b_period=52,
    )

    assert all(
        value is None
        for value in result["conversion_line"][:8]
    )

    assert result["conversion_line"][8] is not None


def test_ichimoku_base_line_requires_base_period():
    high, low, close = sample_ohlc(30)

    result = ichimoku(
        high,
        low,
        close,
        conversion_period=9,
        base_period=26,
        leading_span_b_period=52,
    )

    assert all(
        value is None
        for value in result["base_line"][:25]
    )

    assert result["base_line"][25] is not None


def test_ichimoku_span_b_requires_longer_period():
    high, low, close = sample_ohlc(60)

    result = ichimoku(
        high,
        low,
        close,
        conversion_period=9,
        base_period=26,
        leading_span_b_period=52,
    )

    assert all(
        value is None
        for value in result["leading_span_b"][:51]
    )

    assert result["leading_span_b"][51] is not None


def test_ichimoku_span_a_requires_both_lines():
    high, low, close = sample_ohlc(30)

    result = ichimoku(
        high,
        low,
        close,
        conversion_period=9,
        base_period=26,
        leading_span_b_period=52,
    )

    assert all(
        value is None
        for value in result["leading_span_a"][:25]
    )

    assert result["leading_span_a"][25] is not None


def test_ichimoku_values_are_finite():
    high, low, close = sample_ohlc(100)

    result = ichimoku(
        high,
        low,
        close,
    )

    for values in result.values():
        for value in values:
            if value is not None:
                assert math.isfinite(value)


def test_ichimoku_validates_equal_lengths():
    high, low, close = sample_ohlc(50)

    with pytest.raises(ValueError):
        ichimoku(
            high,
            low[:-1],
            close,
        )


def test_ichimoku_rejects_invalid_period():
    high, low, close = sample_ohlc(50)

    with pytest.raises(ValueError):
        ichimoku(
            high,
            low,
            close,
            conversion_period=0,
        )


def test_ichimoku_does_not_shift_output_length():
    high, low, close = sample_ohlc(120)

    result = ichimoku(
        high,
        low,
        close,
    )

    assert all(
        len(values) == len(close)
        for values in result.values()
    )
