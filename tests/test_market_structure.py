from __future__ import annotations

import math

import pytest

from indicators.market_structure import (
    bos,
    liquidity_zones,
    market_structure_snapshot,
    structure_state,
    swing_points,
)


def test_swing_points_detects_local_high_and_low():
    high = [100, 105, 110, 104, 102]
    low = [90, 95, 100, 94, 92]

    result = swing_points(
        high,
        low,
        left=1,
        right=1,
    )

    assert result["swing_high"] == [
        False,
        False,
        True,
        False,
        False,
    ]

    assert result["swing_low"] == [
        False,
        False,
        False,
        False,
        False,
    ]


def test_swing_points_detects_local_low():
    high = [110, 105, 108, 112, 115]
    low = [100, 95, 102, 104, 108]

    result = swing_points(
        high,
        low,
        left=1,
        right=1,
    )

    assert result["swing_high"] == [
        False,
        False,
        False,
        False,
        False,
    ]

    assert result["swing_low"] == [
        False,
        True,
        False,
        False,
        False,
    ]


def test_swing_points_requires_complete_window():
    high = [100, 110, 100]
    low = [90, 100, 90]

    result = swing_points(
        high,
        low,
        left=1,
        right=1,
    )

    assert result["swing_high"][0] is False
    assert result["swing_high"][-1] is False
    assert result["swing_low"][0] is False
    assert result["swing_low"][-1] is False


def test_swing_points_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        swing_points(
            [100, 105],
            [90],
        )


def test_swing_points_rejects_invalid_period():
    with pytest.raises(ValueError):
        swing_points(
            [100, 105, 110],
            [90, 95, 100],
            left=0,
            right=1,
        )


def test_structure_state_detects_higher_high_and_higher_low():
    high = [100, 105, 110]
    low = [90, 95, 100]

    result = structure_state(high, low)

    assert result == [
        "NEUTRAL",
        "HH_HL",
        "HH_HL",
    ]


def test_structure_state_detects_lower_high_and_lower_low():
    high = [110, 105, 100]
    low = [100, 95, 90]

    result = structure_state(high, low)

    assert result == [
        "NEUTRAL",
        "LH_LL",
        "LH_LL",
    ]


def test_structure_state_detects_single_component_changes():
    high = [100, 110, 105]
    low = [90, 95, 95]

    result = structure_state(high, low)

    assert result == [
        "NEUTRAL",
        "HH_HL",
        "LH",
    ]


def test_structure_state_detects_neutral():
    high = [100, 100]
    low = [90, 90]

    result = structure_state(high, low)

    assert result == [
        "NEUTRAL",
        "NEUTRAL",
    ]


def test_bos_detects_bullish_break():
    close = [100, 105, 111]
    swing_high = [False, True, False]
    swing_low = [False, False, False]

    result = bos(
        close,
        swing_high,
        swing_low,
    )

    assert result["bullish_bos"] == [
        False,
        False,
        True,
    ]


def test_bos_detects_bearish_break():
    close = [100, 95, 89]
    swing_high = [False, False, False]
    swing_low = [False, True, False]

    result = bos(
        close,
        swing_high,
        swing_low,
    )

    assert result["bearish_bos"] == [
        False,
        False,
        True,
    ]


def test_bos_does_not_use_current_swing_as_future_information():
    close = [100, 111]
    swing_high = [False, True]
    swing_low = [False, False]

    result = bos(
        close,
        swing_high,
        swing_low,
    )

    assert result["bullish_bos"] == [
        False,
        False,
    ]


def test_bos_requires_equal_lengths():
    with pytest.raises(ValueError):
        bos(
            [100, 105],
            [False],
            [False, False],
        )


def test_liquidity_zones_groups_nearby_highs():
    high = [100.0, 100.05, 110.0]
    low = [90.0, 90.02, 80.0]

    result = liquidity_zones(
        high,
        low,
        tolerance=0.001,
    )

    assert len(result["high_zones"]) == 2
    assert result["high_zones"][0]["count"] == pytest.approx(2.0)


def test_liquidity_zones_groups_nearby_lows():
    high = [110.0, 120.0, 130.0]
    low = [90.0, 90.05, 80.0]

    result = liquidity_zones(
        high,
        low,
        tolerance=0.001,
    )

    assert len(result["low_zones"]) == 2
    assert result["low_zones"][0]["count"] == pytest.approx(2.0)


def test_liquidity_zones_rejects_negative_tolerance():
    with pytest.raises(ValueError):
        liquidity_zones(
            [100],
            [90],
            tolerance=-0.01,
        )


def test_liquidity_zones_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        liquidity_zones(
            [100, 110],
            [90],
        )


def test_market_structure_snapshot_without_close():
    high = [100, 105, 110]
    low = [90, 95, 100]

    result = market_structure_snapshot(
        high,
        low,
    )

    assert "swing_points" in result
    assert "structure_state" in result
    assert "liquidity_zones" in result
    assert "bos" not in result


def test_market_structure_snapshot_with_close():
    high = [100, 105, 110, 104, 102]
    low = [90, 95, 100, 94, 92]
    close = [95, 103, 109, 103, 101]

    result = market_structure_snapshot(
        high,
        low,
        close,
    )

    assert "swing_points" in result
    assert "structure_state" in result
    assert "liquidity_zones" in result
    assert "bos" in result


def test_snapshot_rejects_close_length_mismatch():
    with pytest.raises(ValueError):
        market_structure_snapshot(
            [100, 105],
            [90, 95],
            [95],
        )


def test_market_structure_rejects_non_finite_values():
    with pytest.raises(ValueError):
        swing_points(
            [100, float("nan"), 110],
            [90, 95, 100],
        )

    with pytest.raises(ValueError):
        structure_state(
            [100, 105],
            [90, float("inf")],
        )


def test_market_structure_does_not_modify_inputs():
    high = [100, 105, 110]
    low = [90, 95, 100]

    original_high = high.copy()
    original_low = low.copy()

    market_structure_snapshot(
        high,
        low,
    )

    assert high == original_high
    assert low == original_low


def test_liquidity_zone_prices_are_finite():
    result = liquidity_zones(
        [100, 105, 110],
        [90, 95, 100],
    )

    for zone in result["high_zones"]:
        assert math.isfinite(zone["price"])

    for zone in result["low_zones"]:
        assert math.isfinite(zone["price"])
