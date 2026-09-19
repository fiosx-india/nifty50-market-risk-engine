from datetime import datetime, timedelta, timezone

import pytest

from calculation.lagged_relationship_calculator import (
    LaggedRelationshipResult,
    calculate_lagged_correlation,
    calculate_lagged_relationship,
)


UTC = timezone.utc


def ts(day: int, hour: int = 0) -> datetime:
    return datetime(
        2026,
        1,
        day,
        hour,
        0,
        0,
        tzinfo=UTC,
    )


def test_lag_zero_pairs_equal_timestamps():
    market = [
        (ts(1), 10.0),
        (ts(2), 20.0),
        (ts(3), 30.0),
    ]

    company = [
        (ts(1), 1.0),
        (ts(2), 2.0),
        (ts(3), 3.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=0,
        market="GOLD",
        company="TITAN",
    )

    assert result.lag == 0
    assert result.sample_size == 3

    assert result.aligned_timestamps == (
        ts(1),
        ts(2),
        ts(3),
    )

    assert result.market_values == (
        10.0,
        20.0,
        30.0,
    )

    assert result.company_values == (
        1.0,
        2.0,
        3.0,
    )

    assert result.correlation == pytest.approx(1.0)


def test_lag_one_market_leads_company_by_one_observation():
    market = [
        (ts(1), 10.0),
        (ts(2), 20.0),
        (ts(3), 30.0),
        (ts(4), 40.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(2), 200.0),
        (ts(3), 300.0),
        (ts(4), 400.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=1,
        market="GOLD",
        company="TITAN",
    )

    assert result.lag == 1
    assert result.sample_size == 3

    assert result.aligned_timestamps == (
        ts(2),
        ts(3),
        ts(4),
    )

    assert result.market_values == (
        10.0,
        20.0,
        30.0,
    )

    assert result.company_values == (
        200.0,
        300.0,
        400.0,
    )

    assert result.correlation == pytest.approx(1.0)


def test_lag_two_market_leads_company_by_two_observations():
    market = [
        (ts(1), 1.0),
        (ts(2), 2.0),
        (ts(3), 3.0),
        (ts(4), 4.0),
        (ts(5), 5.0),
    ]

    company = [
        (ts(1), 10.0),
        (ts(2), 20.0),
        (ts(3), 30.0),
        (ts(4), 40.0),
        (ts(5), 50.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=2,
    )

    assert result.sample_size == 3

    assert result.aligned_timestamps == (
        ts(3),
        ts(4),
        ts(5),
    )

    assert result.market_values == (
        1.0,
        2.0,
        3.0,
    )

    assert result.company_values == (
        30.0,
        40.0,
        50.0,
    )


def test_lag_does_not_use_future_company_data():
    market = [
        (ts(1), 10.0),
        (ts(2), 20.0),
        (ts(3), 30.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(2), 200.0),
        (ts(3), 300.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=1,
    )

    assert result.market_values == (
        10.0,
        20.0,
    )

    assert result.company_values == (
        200.0,
        300.0,
    )

    assert result.aligned_timestamps == (
        ts(2),
        ts(3),
    )


def test_lag_zero_requires_exact_timestamp_match():
    market = [
        (ts(1), 10.0),
        (ts(3), 30.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(2), 200.0),
        (ts(3), 300.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=0,
    )

    assert result.sample_size == 2

    assert result.aligned_timestamps == (
        ts(1),
        ts(3),
    )

    assert result.market_values == (
        10.0,
        30.0,
    )

    assert result.company_values == (
        100.0,
        300.0,
    )


def test_lag_one_uses_observation_steps_not_calendar_days():
    market = [
        (ts(1), 10.0),
        (ts(3), 30.0),
        (ts(5), 50.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(3), 300.0),
        (ts(5), 500.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=1,
    )

    assert result.sample_size == 2

    assert result.aligned_timestamps == (
        ts(3),
        ts(5),
    )

    assert result.market_values == (
        10.0,
        30.0,
    )

    assert result.company_values == (
        300.0,
        500.0,
    )


def test_lag_beyond_available_history_returns_empty_result():
    market = [
        (ts(1), 10.0),
        (ts(2), 20.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(2), 200.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=5,
    )

    assert result.sample_size == 0
    assert result.aligned_timestamps == ()
    assert result.market_values == ()
    assert result.company_values == ()
    assert result.correlation is None


def test_negative_lag_is_rejected():
    market = [
        (ts(1), 10.0),
        (ts(2), 20.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(2), 200.0),
    ]

    with pytest.raises(
        ValueError,
        match="lag must be non-negative",
    ):
        calculate_lagged_relationship(
            market,
            company,
            lag=-1,
        )


def test_non_integer_lag_is_rejected():
    market = [
        (ts(1), 10.0),
        (ts(2), 20.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(2), 200.0),
    ]

    with pytest.raises(
        TypeError,
        match="lag must be an integer",
    ):
        calculate_lagged_relationship(
            market,
            company,
            lag=1.5,
        )


def test_duplicate_market_timestamp_is_rejected():
    market = [
        (ts(1), 10.0),
        (ts(1), 20.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(2), 200.0),
    ]

    with pytest.raises(
        ValueError,
        match="duplicate timestamp",
    ):
        calculate_lagged_relationship(
            market,
            company,
            lag=0,
        )


def test_duplicate_company_timestamp_is_rejected():
    market = [
        (ts(1), 10.0),
        (ts(2), 20.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(1), 200.0),
    ]

    with pytest.raises(
        ValueError,
        match="duplicate timestamp",
    ):
        calculate_lagged_relationship(
            market,
            company,
            lag=0,
        )


def test_naive_timestamp_is_rejected():
    naive = datetime(2026, 1, 1)

    market = [
        (naive, 10.0),
    ]

    company = [
        (ts(1), 100.0),
    ]

    with pytest.raises(
        ValueError,
        match="timezone-aware UTC timestamp",
    ):
        calculate_lagged_relationship(
            market,
            company,
        )


def test_non_datetime_timestamp_is_rejected():
    market = [
        ("2026-01-01T00:00:00+00:00", 10.0),
    ]

    company = [
        (ts(1), 100.0),
    ]

    with pytest.raises(
        TypeError,
        match="timestamp must be a datetime",
    ):
        calculate_lagged_relationship(
            market,
            company,
        )


def test_timezone_offsets_are_normalized_to_utc():
    india_timestamp = datetime(
        2026,
        1,
        1,
        5,
        30,
        0,
        tzinfo=timezone(
            timedelta(hours=5, minutes=30)
        ),
    )

    market = [
        (india_timestamp, 10.0),
    ]

    company = [
        (ts(1), 100.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=0,
    )

    assert result.aligned_timestamps == (
        ts(1),
    )


def test_non_finite_market_value_is_rejected():
    market = [
        (ts(1), float("nan")),
    ]

    company = [
        (ts(1), 100.0),
    ]

    with pytest.raises(
        ValueError,
        match="market values must be finite",
    ):
        calculate_lagged_relationship(
            market,
            company,
        )


def test_non_finite_company_value_is_rejected():
    market = [
        (ts(1), 10.0),
    ]

    company = [
        (ts(1), float("inf")),
    ]

    with pytest.raises(
        ValueError,
        match="company values must be finite",
    ):
        calculate_lagged_relationship(
            market,
            company,
        )


def test_single_observation_has_no_correlation():
    market = [
        (ts(1), 10.0),
    ]

    company = [
        (ts(1), 100.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=0,
    )

    assert result.sample_size == 1
    assert result.correlation is None


def test_zero_variance_has_no_correlation():
    market = [
        (ts(1), 10.0),
        (ts(2), 10.0),
        (ts(3), 10.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(2), 200.0),
        (ts(3), 300.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=0,
    )

    assert result.sample_size == 3
    assert result.correlation is None


def test_negative_correlation_is_calculated():
    market = [
        (ts(1), 1.0),
        (ts(2), 2.0),
        (ts(3), 3.0),
    ]

    company = [
        (ts(1), 3.0),
        (ts(2), 2.0),
        (ts(3), 1.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=0,
    )

    assert result.correlation == pytest.approx(-1.0)


def test_result_does_not_claim_causation():
    result = calculate_lagged_relationship(
        [
            (ts(1), 1.0),
            (ts(2), 2.0),
            (ts(3), 3.0),
        ],
        [
            (ts(1), 10.0),
            (ts(2), 20.0),
            (ts(3), 30.0),
        ],
        lag=0,
        market="GOLD",
        company="TITAN",
    )

    assert result.causation_claim is False


def test_result_validation():
    result = LaggedRelationshipResult(
        market="GOLD",
        company="TITAN",
        lag=0,
        correlation=1.0,
        sample_size=2,
        aligned_timestamps=(
            ts(1),
            ts(2),
        ),
        market_values=(
            10.0,
            20.0,
        ),
        company_values=(
            100.0,
            200.0,
        ),
        calculation_method="test",
        causation_claim=False,
    )

    result.validate()


def test_result_rejects_causation_claim():
    result = LaggedRelationshipResult(
        market="GOLD",
        company="TITAN",
        lag=0,
        correlation=1.0,
        sample_size=0,
        aligned_timestamps=(),
        market_values=(),
        company_values=(),
        calculation_method="test",
        causation_claim=True,
    )

    with pytest.raises(
        ValueError,
        match="must not claim causation",
    ):
        result.validate()


def test_legacy_lagged_correlation():
    result = calculate_lagged_correlation(
        [1.0, 2.0, 3.0],
        [10.0, 20.0, 30.0],
        lag=0,
    )

    assert result == pytest.approx(1.0)


def test_legacy_lag_one():
    result = calculate_lagged_relationship(
        [1.0, 2.0, 3.0, 4.0],
        [10.0, 20.0, 30.0, 40.0],
        lag=1,
    )

    assert result.market_values == (
        1.0,
        2.0,
        3.0,
    )

    assert result.company_values == (
        20.0,
        30.0,
        40.0,
    )

    assert result.sample_size == 3


def test_legacy_lag_beyond_history():
    result = calculate_lagged_relationship(
        [1.0, 2.0],
        [10.0, 20.0],
        lag=5,
    )

    assert result.sample_size == 0
    assert result.correlation is None


def test_unsorted_input_is_processed_chronologically():
    market = [
        (ts(3), 30.0),
        (ts(1), 10.0),
        (ts(2), 20.0),
    ]

    company = [
        (ts(3), 300.0),
        (ts(1), 100.0),
        (ts(2), 200.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=0,
    )

    assert result.aligned_timestamps == (
        ts(1),
        ts(2),
        ts(3),
    )

    assert result.market_values == (
        10.0,
        20.0,
        30.0,
    )

    assert result.company_values == (
        100.0,
        200.0,
        300.0,
    )


def test_company_missing_observation_does_not_get_filled():
    market = [
        (ts(1), 10.0),
        (ts(2), 20.0),
        (ts(3), 30.0),
    ]

    company = [
        (ts(1), 100.0),
        (ts(3), 300.0),
    ]

    result = calculate_lagged_relationship(
        market,
        company,
        lag=0,
    )

    assert result.aligned_timestamps == (
        ts(1),
        ts(3),
    )

    assert result.sample_size == 2
