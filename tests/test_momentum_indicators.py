"""
Tests for indicators.momentum_indicators
"""

import math

import pytest

from indicators.momentum_indicators import (
    stochastic,
    stochastic_series,
    williams_r,
    williams_r_series,
    cci,
    mfi,
)


def sample_ohlc(count=40):
    close = [
        100.0 + i * 0.5 + (i % 4) * 0.2
        for i in range(count)
    ]

    high = [value + 2.0 for value in close]
    low = [value - 2.0 for value in close]

    volume = [
        1000.0 + i * 10.0
        for i in range(count)
    ]

    return high, low, close, volume


# ---------------------------------------------------------------------------
# Stochastic
# ---------------------------------------------------------------------------


def test_stochastic_returns_value():
    high, low, close, _ = sample_ohlc()

    value = stochastic(
        high,
        low,
        close,
        period=14,
    )

    assert value is not None
    assert math.isfinite(value)
    assert 0.0 <= value <= 100.0


def test_stochastic_series_preserves_length():
    high, low, close, _ = sample_ohlc(50)

    result = stochastic_series(
        high,
        low,
        close,
        period=14,
    )

    assert len(result) == 50


def test_stochastic_requires_sufficient_history():
    high, low, close, _ = sample_ohlc(10)

    result = stochastic_series(
        high,
        low,
        close,
        period=14,
    )

    assert all(value is None for value in result)


def test_stochastic_uses_high_low_range():
    high = [100, 105, 110]
    low = [90, 95, 100]
    close = [95, 100, 110]

    result = stochastic_series(
        high,
        low,
        close,
        period=3,
    )

    assert result[-1] == pytest.approx(100.0)


def test_stochastic_is_bounded():
    high, low, close, _ = sample_ohlc(80)

    result = stochastic_series(
        high,
        low,
        close,
        period=14,
    )

    values = [
        value
        for value in result
        if value is not None
    ]

    assert values
    assert all(0.0 <= value <= 100.0 for value in values)


def test_stochastic_validates_lengths():
    high, low, close, _ = sample_ohlc(30)

    with pytest.raises(ValueError):
        stochastic(
            high,
            low[:-1],
            close,
            period=14,
        )


def test_stochastic_rejects_invalid_period():
    high, low, close, _ = sample_ohlc(30)

    with pytest.raises(ValueError):
        stochastic(
            high,
            low,
            close,
            period=0,
        )


# ---------------------------------------------------------------------------
# Williams %R
# ---------------------------------------------------------------------------


def test_williams_r_returns_value():
    high, low, close, _ = sample_ohlc()

    value = williams_r(
        high,
        low,
        close,
        period=14,
    )

    assert value is not None
    assert math.isfinite(value)
    assert -100.0 <= value <= 0.0


def test_williams_r_series_preserves_length():
    high, low, close, _ = sample_ohlc(50)

    result = williams_r_series(
        high,
        low,
        close,
        period=14,
    )

    assert len(result) == 50


def test_williams_r_requires_sufficient_history():
    high, low, close, _ = sample_ohlc(10)

    result = williams_r_series(
        high,
        low,
        close,
        period=14,
    )

    assert all(value is None for value in result)


def test_williams_r_at_high_is_zero():
    high = [100, 105, 110]
    low = [90, 95, 100]
    close = [95, 100, 110]

    result = williams_r_series(
        high,
        low,
        close,
        period=3,
    )

    assert result[-1] == pytest.approx(0.0)


def test_williams_r_is_bounded():
    high, low, close, _ = sample_ohlc(80)

    result = williams_r_series(
        high,
        low,
        close,
        period=14,
    )

    values = [
        value
        for value in result
        if value is not None
    ]

    assert values
    assert all(-100.0 <= value <= 0.0 for value in values)


# ---------------------------------------------------------------------------
# CCI
# ---------------------------------------------------------------------------


def test_cci_returns_value():
    high, low, close, _ = sample_ohlc()

    value = cci(
        high,
        low,
        close,
        period=14,
    )

    assert value is not None
    assert math.isfinite(value)


def test_cci_requires_sufficient_history():
    high, low, close, _ = sample_ohlc(10)

    value = cci(
        high,
        low,
        close,
        period=14,
    )

    assert value is None


# ---------------------------------------------------------------------------
# MFI
# ---------------------------------------------------------------------------


def test_mfi_returns_value():
    high, low, close, volume = sample_ohlc()

    value = mfi(
        high,
        low,
        close,
        volume,
        period=14,
    )

    assert value is not None
    assert math.isfinite(value)
    assert 0.0 <= value <= 100.0


def test_mfi_requires_sufficient_history():
    high, low, close, volume = sample_ohlc(10)

    value = mfi(
        high,
        low,
        close,
        volume,
        period=14,
    )

    assert value is None


def test_mfi_is_bounded():
    high, low, close, volume = sample_ohlc(80)

    value = mfi(
        high,
        low,
        close,
        volume,
        period=14,
    )

    assert value is not None
    assert 0.0 <= value <= 100.0


def test_momentum_functions_reject_invalid_ohlc():
    high, low, close, volume = sample_ohlc(30)

    high[5] = 90.0
    low[5] = 100.0

    with pytest.raises(ValueError):
        stochastic(
            high,
            low,
            close,
            period=14,
        )


def test_mfi_validates_volume_length():
    high, low, close, volume = sample_ohlc(30)

    with pytest.raises(ValueError):
        mfi(
            high,
            low,
            close,
            volume[:-1],
            period=14,
        )
