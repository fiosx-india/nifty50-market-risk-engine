from __future__ import annotations

import math

import pytest

from indicators.volume_indicators import (
    accumulation_distribution,
    accumulation_distribution_series,
    obv,
    obv_series,
    price_volume_confirmation,
    relative_volume,
    volume_summary,
)


def test_relative_volume_uses_rolling_average():
    volume = [100, 100, 100, 200]

    result = relative_volume(volume, period=3)

    assert result[:2] == [None, None]
    assert result[2] == pytest.approx(1.0)
    assert result[3] == pytest.approx(1.5)


def test_relative_volume_zero_average_returns_none():
    volume = [0, 0, 0]

    result = relative_volume(volume, period=3)

    assert result == [None, None, None]


def test_relative_volume_rejects_negative_volume():
    with pytest.raises(ValueError):
        relative_volume([100, -10, 100])


def test_relative_volume_rejects_invalid_period():
    with pytest.raises(ValueError):
        relative_volume([100, 100], period=0)


def test_relative_volume_rejects_non_integer_period():
    with pytest.raises(TypeError):
        relative_volume([100, 100], period=2.5)


def test_obv_series_standard_calculation():
    close = [100, 101, 99, 99, 102]
    volume = [10, 20, 30, 40, 50]

    result = obv_series(close, volume)

    assert result == [
        0.0,
        20.0,
        -10.0,
        -10.0,
        40.0,
    ]


def test_obv_returns_latest_value():
    close = [100, 101, 99]
    volume = [10, 20, 30]

    assert obv(close, volume) == pytest.approx(-10.0)


def test_obv_uses_current_observation_volume():
    close = [100, 101]
    volume = [100, 50]

    result = obv_series(close, volume)

    assert result[-1] == pytest.approx(50.0)


def test_obv_unchanged_price_keeps_previous_value():
    close = [100, 100, 100]
    volume = [10, 20, 30]

    result = obv_series(close, volume)

    assert result == [0.0, 0.0, 0.0]


def test_obv_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        obv_series([100, 101], [10])


def test_obv_rejects_negative_volume():
    with pytest.raises(ValueError):
        obv_series([100, 101], [10, -20])


def test_accumulation_distribution_standard_calculation():
    high = [110]
    low = [90]
    close = [110]
    volume = [100]

    result = accumulation_distribution_series(
        high,
        low,
        close,
        volume,
    )

    assert result == [100.0]


def test_accumulation_distribution_middle_close_has_zero_flow():
    high = [110]
    low = [90]
    close = [100]
    volume = [100]

    result = accumulation_distribution_series(
        high,
        low,
        close,
        volume,
    )

    assert result == [0.0]


def test_accumulation_distribution_low_close_is_negative():
    high = [110]
    low = [90]
    close = [90]
    volume = [100]

    result = accumulation_distribution_series(
        high,
        low,
        close,
        volume,
    )

    assert result == [-100.0]


def test_accumulation_distribution_zero_range_is_zero():
    high = [100]
    low = [100]
    close = [100]
    volume = [100]

    result = accumulation_distribution_series(
        high,
        low,
        close,
        volume,
    )

    assert result == [0.0]


def test_accumulation_distribution_returns_latest_value():
    high = [110, 120]
    low = [90, 100]
    close = [110, 100]
    volume = [100, 200]

    result = accumulation_distribution(
        high,
        low,
        close,
        volume,
    )

    assert result == pytest.approx(0.0)


def test_accumulation_distribution_validates_ohlc():
    with pytest.raises(ValueError):
        accumulation_distribution_series(
            [90],
            [100],
            [95],
            [100],
        )


def test_accumulation_distribution_rejects_close_outside_range():
    with pytest.raises(ValueError):
        accumulation_distribution_series(
            [110],
            [90],
            [120],
            [100],
        )


def test_accumulation_distribution_rejects_negative_volume():
    with pytest.raises(ValueError):
        accumulation_distribution_series(
            [110],
            [90],
            [100],
            [-100],
        )


def test_price_volume_confirmation_requires_previous_price():
    close = [100, 101, 102]
    volume = [100, 100, 100]

    result = price_volume_confirmation(
        close,
        volume,
        period=2,
    )

    assert result[0] is None


def test_price_volume_confirmation_positive_for_price_rise():
    close = [100, 100, 110]
    volume = [100, 100, 200]

    result = price_volume_confirmation(
        close,
        volume,
        period=2,
    )

    assert result[1] == pytest.approx(0.0)
    assert result[2] == pytest.approx(1.3333333333)


def test_price_volume_confirmation_negative_for_price_fall():
    close = [100, 100, 90]
    volume = [100, 100, 200]

    result = price_volume_confirmation(
        close,
        volume,
        period=2,
    )

    assert result[2] == pytest.approx(-1.3333333333)


def test_price_volume_confirmation_zero_for_unchanged_price():
    close = [100, 100, 100]
    volume = [100, 100, 200]

    result = price_volume_confirmation(
        close,
        volume,
        period=2,
    )

    assert result[2] == pytest.approx(0.0)


def test_price_volume_confirmation_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        price_volume_confirmation(
            [100, 101],
            [100],
        )


def test_volume_summary_returns_expected_keys():
    high = [110, 111, 112]
    low = [90, 91, 92]
    close = [100, 105, 110]
    volume = [100, 150, 200]

    result = volume_summary(
        high,
        low,
        close,
        volume,
        period=2,
    )

    assert set(result) == {
        "relative_volume",
        "obv",
        "accumulation_distribution",
        "price_volume_confirmation",
    }


def test_volume_summary_contains_finite_values_when_available():
    high = [110, 111, 112]
    low = [90, 91, 92]
    close = [100, 105, 110]
    volume = [100, 150, 200]

    result = volume_summary(
        high,
        low,
        close,
        volume,
        period=2,
    )

    for key, value in result.items():
        if value is not None:
            assert math.isfinite(value), key


def test_volume_functions_reject_empty_input():
    with pytest.raises(ValueError):
        relative_volume([])

    with pytest.raises(ValueError):
        obv_series([], [])

    with pytest.raises(ValueError):
        accumulation_distribution_series([], [], [], [])


def test_volume_functions_reject_non_finite_values():
    with pytest.raises(ValueError):
        relative_volume([100, float("nan")])

    with pytest.raises(ValueError):
        obv_series([100, float("inf")], [100, 100])


def test_volume_inputs_are_not_modified():
    high = [110, 111]
    low = [90, 91]
    close = [100, 101]
    volume = [100, 200]

    original = (
        high.copy(),
        low.copy(),
        close.copy(),
        volume.copy(),
    )

    volume_summary(
        high,
        low,
        close,
        volume,
        period=2,
    )

    assert high == original[0]
    assert low == original[1]
    assert close == original[2]
    assert volume == original[3]
