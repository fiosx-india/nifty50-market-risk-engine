from datetime import datetime, timedelta, timezone

import pytest

from calculation.market_relationship_calculator import (
    RelationshipResult,
    calculate_correlation,
    calculate_market_relationship,
    calculate_timestamped_correlation,
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


def test_timestamped_relationship_aligns_by_timestamp():
    company = [
        (ts(1), 0.01),
        (ts(2), 0.02),
        (ts(3), 0.03),
    ]

    market = [
        (ts(1), 0.10),
        (ts(2), 0.20),
        (ts(3), 0.30),
    ]

    result = calculate_market_relationship(
        company,
        market,
        company="TITAN",
        market="GOLD",
    )

    assert result.sample_size == 3
    assert result.aligned_timestamps == (
        ts(1),
        ts(2),
        ts(3),
    )
    assert result.correlation == pytest.approx(1.0)
    assert result.company_mean_return == pytest.approx(0.02)
    assert result.market_mean_return == pytest.approx(0.20)
    assert result.excess_mean_return == pytest.approx(-0.18)
    assert result.causation_claim is False


def test_timestamp_alignment_does_not_use_position():
    company = [
        (ts(1), 1.0),
        (ts(2), 2.0),
        (ts(3), 3.0),
    ]

    market = [
        (ts(1), 10.0),
        (ts(3), 30.0),
        (ts(4), 40.0),
    ]

    result = calculate_market_relationship(
        company,
        market,
        company="ABC",
        market="GOLD",
    )

    assert result.aligned_timestamps == (
        ts(1),
        ts(3),
    )

    assert result.sample_size == 2


def test_unmatched_timestamps_are_not_fabricated():
    company = [
        (ts(1), 1.0),
        (ts(2), 2.0),
    ]

    market = [
        (ts(3), 3.0),
        (ts(4), 4.0),
    ]

    result = calculate_market_relationship(
        company,
        market,
        company="ABC",
        market="GOLD",
    )

    assert result.sample_size == 0
    assert result.aligned_timestamps == ()
    assert result.correlation is None
    assert result.company_mean_return is None
    assert result.market_mean_return is None
    assert result.excess_mean_return is None


def test_duplicate_company_timestamp_is_rejected():
    company = [
        (ts(1), 0.01),
        (ts(1), 0.02),
    ]

    market = [
        (ts(1), 0.10),
        (ts(2), 0.20),
    ]

    with pytest.raises(ValueError, match="duplicate timestamp"):
        calculate_market_relationship(company, market)


def test_duplicate_market_timestamp_is_rejected():
    company = [
        (ts(1), 0.01),
        (ts(2), 0.02),
    ]

    market = [
        (ts(1), 0.10),
        (ts(1), 0.20),
    ]

    with pytest.raises(ValueError, match="duplicate timestamp"):
        calculate_market_relationship(company, market)


def test_naive_timestamp_is_rejected():
    naive = datetime(2026, 1, 1)

    company = [
        (naive, 0.01),
    ]

    market = [
        (ts(1), 0.10),
    ]

    with pytest.raises(
        ValueError,
        match="timezone-aware UTC timestamp",
    ):
        calculate_market_relationship(company, market)


def test_non_datetime_timestamp_is_rejected():
    company = [
        ("2026-01-01T00:00:00+00:00", 0.01),
    ]

    market = [
        (ts(1), 0.10),
    ]

    with pytest.raises(TypeError, match="timestamp must be a datetime"):
        calculate_market_relationship(company, market)


def test_non_utc_timestamp_is_normalized_to_utc():
    india_timestamp = datetime(
        2026,
        1,
        1,
        5,
        30,
        0,
        tzinfo=timezone(timedelta(hours=5, minutes=30)),
    )

    company = [
        (india_timestamp, 0.01),
    ]

    market = [
        (ts(1), 0.10),
    ]

    result = calculate_market_relationship(
        company,
        market,
        company="ABC",
        market="GOLD",
    )

    assert result.aligned_timestamps == (ts(1),)


def test_non_finite_company_value_is_rejected():
    company = [
        (ts(1), float("nan")),
    ]

    market = [
        (ts(1), 0.10),
    ]

    with pytest.raises(ValueError, match="finite"):
        calculate_market_relationship(company, market)


def test_non_finite_market_value_is_rejected():
    company = [
        (ts(1), 0.01),
    ]

    market = [
        (ts(1), float("inf")),
    ]

    with pytest.raises(ValueError, match="finite"):
        calculate_market_relationship(company, market)


def test_single_observation_has_no_correlation():
    company = [
        (ts(1), 0.01),
    ]

    market = [
        (ts(1), 0.10),
    ]

    result = calculate_market_relationship(
        company,
        market,
    )

    assert result.sample_size == 1
    assert result.correlation is None


def test_zero_variance_has_no_correlation():
    company = [
        (ts(1), 0.01),
        (ts(2), 0.01),
        (ts(3), 0.01),
    ]

    market = [
        (ts(1), 0.10),
        (ts(2), 0.20),
        (ts(3), 0.30),
    ]

    result = calculate_market_relationship(
        company,
        market,
    )

    assert result.sample_size == 3
    assert result.correlation is None


def test_negative_correlation():
    company = [
        (ts(1), 1.0),
        (ts(2), 2.0),
        (ts(3), 3.0),
    ]

    market = [
        (ts(1), 3.0),
        (ts(2), 2.0),
        (ts(3), 1.0),
    ]

    result = calculate_market_relationship(
        company,
        market,
    )

    assert result.correlation == pytest.approx(-1.0)


def test_timestamped_convenience_function():
    company = [
        (ts(1), 1.0),
        (ts(2), 2.0),
        (ts(3), 3.0),
    ]

    market = [
        (ts(1), 2.0),
        (ts(2), 4.0),
        (ts(3), 6.0),
    ]

    result = calculate_timestamped_correlation(
        company,
        market,
    )

    assert result.correlation == pytest.approx(1.0)
    assert result.sample_size == 3


def test_legacy_numeric_correlation():
    result = calculate_correlation(
        [1.0, 2.0, 3.0],
        [2.0, 4.0, 6.0],
    )

    assert result == pytest.approx(1.0)


def test_legacy_numeric_length_mismatch_is_rejected():
    with pytest.raises(
        ValueError,
        match="equal length",
    ):
        calculate_correlation(
            [1.0, 2.0, 3.0],
            [1.0, 2.0],
        )


def test_legacy_numeric_relationship():
    result = calculate_market_relationship(
        [1.0, 2.0, 3.0],
        [2.0, 4.0, 6.0],
        company="ABC",
        market="GOLD",
    )

    assert result.correlation == pytest.approx(1.0)
    assert result.sample_size == 3
    assert result.company_mean_return == pytest.approx(2.0)
    assert result.market_mean_return == pytest.approx(4.0)
    assert result.excess_mean_return == pytest.approx(-2.0)
    assert result.aligned_timestamps == ()
    assert result.causation_claim is False


def test_mixed_timestamp_and_numeric_formats_are_rejected():
    company = [
        (ts(1), 0.01),
        (ts(2), 0.02),
    ]

    market = [
        0.10,
        0.20,
    ]

    with pytest.raises(
        ValueError,
        match="same format",
    ):
        calculate_market_relationship(
            company,
            market,
        )


def test_relationship_result_validation():
    result = RelationshipResult(
        market="GOLD",
        company="TITAN",
        correlation=0.5,
        sample_size=2,
        aligned_timestamps=(
            ts(1),
            ts(2),
        ),
        company_mean_return=0.01,
        market_mean_return=0.02,
        excess_mean_return=-0.01,
        calculation_method="timestamp_intersection_pearson",
        causation_claim=False,
    )

    result.validate()


def test_relationship_result_rejects_causation_claim():
    result = RelationshipResult(
        market="GOLD",
        company="TITAN",
        correlation=0.5,
        sample_size=0,
        aligned_timestamps=(),
        company_mean_return=None,
        market_mean_return=None,
        excess_mean_return=None,
        calculation_method="test",
        causation_claim=True,
    )

    with pytest.raises(
        ValueError,
        match="must not claim causation",
    ):
        result.validate()


def test_relationship_result_sample_size_must_match_timestamps():
    result = RelationshipResult(
        market="GOLD",
        company="TITAN",
        correlation=0.5,
        sample_size=3,
        aligned_timestamps=(ts(1), ts(2)),
        company_mean_return=0.01,
        market_mean_return=0.02,
        excess_mean_return=-0.01,
        calculation_method="test",
        causation_claim=False,
    )

    with pytest.raises(
        ValueError,
        match="sample_size must equal",
    ):
        result.validate()


def test_relationship_result_rejects_naive_timestamp():
    result = RelationshipResult(
        market="GOLD",
        company="TITAN",
        correlation=None,
        sample_size=1,
        aligned_timestamps=(
            datetime(2026, 1, 1),
        ),
        company_mean_return=0.01,
        market_mean_return=0.02,
        excess_mean_return=-0.01,
        calculation_method="test",
        causation_claim=False,
    )

    with pytest.raises(
        ValueError,
        match="timezone-aware UTC timestamp",
    ):
        result.validate()


def test_alignment_is_chronological():
    company = [
        (ts(3), 3.0),
        (ts(1), 1.0),
        (ts(2), 2.0),
    ]

    market = [
        (ts(2), 20.0),
        (ts(3), 30.0),
        (ts(1), 10.0),
    ]

    result = calculate_market_relationship(
        company,
        market,
    )

    assert result.aligned_timestamps == (
        ts(1),
        ts(2),
        ts(3),
    )


def test_result_is_descriptive_not_causal():
    result = calculate_market_relationship(
        [
            (ts(1), 0.01),
            (ts(2), 0.02),
            (ts(3), 0.03),
        ],
        [
            (ts(1), 0.02),
            (ts(2), 0.04),
            (ts(3), 0.06),
        ],
        company="TITAN",
        market="GOLD",
    )

    assert result.causation_claim is False
