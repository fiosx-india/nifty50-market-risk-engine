from __future__ import annotations

from datetime import datetime, timezone

import pytest

from historical.return_calculator import (
    simple_returns,
    cumulative_return,
)


def utc(day: int, hour: int = 0) -> datetime:
    return datetime(
        2026,
        1,
        day,
        hour,
        tzinfo=timezone.utc,
    )


def test_simple_returns_numeric_sequence():
    result = simple_returns([100, 110, 121])

    assert result == [
        pytest.approx(0.10),
        pytest.approx(0.10),
    ]


def test_simple_returns_preserves_timestamp_of_current_observation():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": 110,
        },
        {
            "timestamp": utc(3),
            "close": 121,
        },
    ]

    result = simple_returns(records)

    assert len(result) == 2

    assert result[0]["timestamp"] == utc(2)
    assert result[1]["timestamp"] == utc(3)

    assert result[0]["value"] == pytest.approx(0.10)
    assert result[1]["value"] == pytest.approx(0.10)


def test_simple_returns_requires_timezone_aware_timestamp():
    records = [
        {
            "timestamp": datetime(2026, 1, 1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": 110,
        },
    ]

    with pytest.raises(ValueError, match="timezone"):
        simple_returns(records)


def test_simple_returns_accepts_utc_timestamp():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": 105,
        },
    ]

    result = simple_returns(records)

    assert result[0]["timestamp"].tzinfo == timezone.utc
    assert result[0]["value"] == pytest.approx(0.05)


def test_simple_returns_rejects_duplicate_timestamps():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(1),
            "close": 105,
        },
    ]

    with pytest.raises(ValueError):
        simple_returns(records)


def test_simple_returns_rejects_unsorted_timestamps():
    records = [
        {
            "timestamp": utc(2),
            "close": 110,
        },
        {
            "timestamp": utc(1),
            "close": 100,
        },
    ]

    with pytest.raises(ValueError):
        simple_returns(records)


def test_simple_returns_rejects_zero_prior_close():
    records = [
        {
            "timestamp": utc(1),
            "close": 0,
        },
        {
            "timestamp": utc(2),
            "close": 100,
        },
    ]

    with pytest.raises(ValueError, match="zero prior close"):
        simple_returns(records)


def test_simple_returns_does_not_silently_drop_zero_prior_close():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": 0,
        },
        {
            "timestamp": utc(3),
            "close": 110,
        },
    ]

    with pytest.raises(ValueError, match="zero prior close"):
        simple_returns(records)


def test_simple_returns_requires_close():
    records = [
        {
            "timestamp": utc(1),
        },
        {
            "timestamp": utc(2),
            "close": 100,
        },
    ]

    with pytest.raises(ValueError, match="close"):
        simple_returns(records)


def test_simple_returns_rejects_non_numeric_close():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": "invalid",
        },
    ]

    with pytest.raises(ValueError, match="close"):
        simple_returns(records)


def test_simple_returns_rejects_nan_close():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": float("nan"),
        },
    ]

    with pytest.raises(ValueError, match="finite"):
        simple_returns(records)


def test_simple_returns_rejects_infinite_close():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": float("inf"),
        },
    ]

    with pytest.raises(ValueError, match="finite"):
        simple_returns(records)


def test_simple_returns_empty_input():
    assert simple_returns([]) == []


def test_cumulative_return_numeric_sequence():
    result = cumulative_return([100, 110, 121])

    assert result == pytest.approx(0.21)


def test_cumulative_return_timestamped_sequence():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": 110,
        },
        {
            "timestamp": utc(3),
            "close": 121,
        },
    ]

    result = cumulative_return(records)

    assert result == pytest.approx(0.21)


def test_cumulative_return_uses_first_and_last_observation():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": 150,
        },
        {
            "timestamp": utc(3),
            "close": 125,
        },
    ]

    result = cumulative_return(records)

    assert result == pytest.approx(0.25)


def test_cumulative_return_rejects_zero_initial_close():
    records = [
        {
            "timestamp": utc(1),
            "close": 0,
        },
        {
            "timestamp": utc(2),
            "close": 100,
        },
    ]

    with pytest.raises(ValueError, match="zero initial close"):
        cumulative_return(records)


def test_cumulative_return_requires_timestamp_contract():
    records = [
        {
            "timestamp": datetime(2026, 1, 1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": 110,
        },
    ]

    with pytest.raises(ValueError, match="timezone"):
        cumulative_return(records)


def test_cumulative_return_rejects_duplicate_timestamps():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(1),
            "close": 110,
        },
    ]

    with pytest.raises(ValueError):
        cumulative_return(records)


def test_cumulative_return_rejects_unsorted_timestamps():
    records = [
        {
            "timestamp": utc(2),
            "close": 110,
        },
        {
            "timestamp": utc(1),
            "close": 100,
        },
    ]

    with pytest.raises(ValueError):
        cumulative_return(records)


def test_timestamped_returns_do_not_fill_missing_dates():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(3),
            "close": 110,
        },
    ]

    result = simple_returns(records)

    assert len(result) == 1
    assert result[0]["timestamp"] == utc(3)
    assert result[0]["value"] == pytest.approx(0.10)


def test_returns_preserve_chronological_order():
    records = [
        {
            "timestamp": utc(1),
            "close": 100,
        },
        {
            "timestamp": utc(2),
            "close": 105,
        },
        {
            "timestamp": utc(3),
            "close": 102,
        },
    ]

    result = simple_returns(records)

    timestamps = [item["timestamp"] for item in result]

    assert timestamps == [
        utc(2),
        utc(3),
    ]


def test_numeric_and_timestamped_returns_match():
    prices = [100, 110, 99]

    numeric_result = simple_returns(prices)

    timestamped_result = simple_returns(
        [
            {
                "timestamp": utc(1),
                "close": 100,
            },
            {
                "timestamp": utc(2),
                "close": 110,
            },
            {
                "timestamp": utc(3),
                "close": 99,
            },
        ]
    )

    assert [
        item["value"]
        for item in timestamped_result
    ] == pytest.approx(numeric_result)


def test_single_observation_cumulative_return_is_none():
    assert cumulative_return([100]) is None

    assert cumulative_return(
        [
            {
                "timestamp": utc(1),
                "close": 100,
            }
        ]
    ) is None


def test_empty_cumulative_return_is_none():
    assert cumulative_return([]) is None
