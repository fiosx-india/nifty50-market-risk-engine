"""Executable contract for timestamped historical calculations.

These tests deliberately specify the behaviour required before historical and
relationship calculations may consume provider-normalized observations.
"""

from datetime import datetime, timedelta, timezone

import pytest

from calculation.evidence_calculator import EvidenceRecord
from calculation.lagged_relationship_calculator import calculate_lags
from calculation.market_relationship_calculator import calculate
from historical.event_study import abnormal_returns
from historical.return_calculator import simple_returns

UTC = timezone.utc
BASE = datetime(2026, 1, 2, 9, 15, tzinfo=UTC)


def observation(minutes, value):
    """A canonical timestamped return observation used by alignment callers."""
    return {"timestamp": BASE + timedelta(minutes=minutes), "value": value}


def ohlcv(minutes, close):
    """A complete canonical OHLCV observation used by return callers."""
    return {
        "timestamp": BASE + timedelta(minutes=minutes),
        "open": close,
        "high": close,
        "low": close,
        "close": close,
        "volume": 100,
    }


def assert_pair_timestamps(result, expected):
    assert result["sample_size"] == len(expected)
    assert result["aligned_timestamps"] == expected


def test_ohlcv_observations_require_explicit_timezone_aware_timestamps():
    from data_providers.data_normalizer import normalize_records

    normalized = normalize_records([ohlcv(0, 100)])
    assert normalized[0]["timestamp"] == BASE

    with pytest.raises(ValueError, match="timezone-aware UTC timestamp"):
        normalize_records(
            [{**ohlcv(5, 101), "timestamp": BASE.replace(tzinfo=None)}]
        )


def test_identical_timestamps_align_all_observations():
    market = [observation(0, 1), observation(5, 2), observation(10, 3)]
    company = [observation(0, 10), observation(5, 20), observation(10, 30)]

    result = calculate(market, company)

    assert_pair_timestamps(
        result,
        [BASE, BASE + timedelta(minutes=5), BASE + timedelta(minutes=10)],
    )


def test_differently_ordered_inputs_align_by_timestamp_not_position():
    market = [observation(10, 3), observation(0, 1), observation(5, 2)]
    company = [observation(0, 10), observation(5, 20), observation(10, 30)]

    with pytest.raises(ValueError, match="chronologically ordered"):
        calculate(market, company)


@pytest.mark.parametrize(
    ("market", "company", "expected"),
    [
        (
            [observation(0, 1), observation(10, 3)],
            [observation(0, 10), observation(5, 20), observation(10, 30)],
            [BASE, BASE + timedelta(minutes=10)],
        ),
        (
            [observation(0, 1), observation(5, 2), observation(10, 3)],
            [observation(0, 10), observation(10, 30)],
            [BASE, BASE + timedelta(minutes=10)],
        ),
    ],
    ids=["missing_market_timestamp", "missing_company_timestamp"],
)
def test_missing_timestamps_are_not_silently_paired_or_filled(
    market, company, expected
):
    result = calculate(market, company)

    assert_pair_timestamps(result, expected)
    assert result["pairs"] == [(1.0, 10.0), (3.0, 30.0)]


def test_duplicate_timestamps_are_rejected_deterministically():
    market = [observation(0, 1), observation(0, 2)]

    with pytest.raises(ValueError, match="duplicate timestamp"):
        calculate(market, [observation(0, 10), observation(5, 20)])


@pytest.mark.parametrize(
    "market, company",
    [([], []), ([observation(0, 1)], [observation(0, 10)])],
)
def test_empty_and_single_observation_inputs_have_deterministic_results(
    market, company
):
    result = calculate(market, company)

    assert result["sample_size"] == len(market)
    assert result["status"] == "insufficient_data"


def test_naive_and_timezone_aware_timestamps_are_not_silently_compared():
    market = [observation(0, 1)]
    company = [{"timestamp": BASE.replace(tzinfo=None), "value": 10}]

    with pytest.raises(ValueError, match="timezone-aware UTC timestamp"):
        calculate(market, company)


def test_lag_zero_pairs_equal_timestamps():
    series = [observation(0, 1), observation(5, 2), observation(10, 3)]

    result = calculate_lags(
        series,
        [observation(0, 10), observation(5, 20), observation(10, 30)],
        [0],
    )[0]

    assert result["aligned_timestamps"] == [
        (BASE, BASE),
        (BASE + timedelta(minutes=5), BASE + timedelta(minutes=5)),
        (BASE + timedelta(minutes=10), BASE + timedelta(minutes=10)),
    ]


def test_positive_lag_pairs_market_t_with_company_t_plus_lag():
    market = [observation(0, 1), observation(5, 2), observation(10, 3)]
    company = [observation(0, 10), observation(5, 20), observation(10, 30)]

    result = calculate_lags(market, company, [1])[0]

    assert result["pairs"] == [(1.0, 20.0), (2.0, 30.0)]
    assert result["aligned_timestamps"] == [
        (BASE, BASE + timedelta(minutes=5)),
        (BASE + timedelta(minutes=5), BASE + timedelta(minutes=10)),
    ]


def test_lag_with_insufficient_history_fabricates_no_observations():
    result = calculate_lags(
        [observation(0, 1)],
        [observation(0, 10)],
        [1],
    )[0]

    assert result["pairs"] == []
    assert result["sample_size"] == 0
    assert result["status"] == "insufficient_data"


def test_positive_lag_never_pairs_a_company_observation_with_a_future_market_observation():
    market = [observation(0, 1), observation(5, 2), observation(10, 3)]
    company = [observation(0, 10), observation(5, 20), observation(10, 30)]

    result = calculate_lags(market, company, [1])[0]

    assert all(
        market_time < company_time
        for market_time, company_time in result["aligned_timestamps"]
    )


def test_correlation_uses_only_explicit_timestamp_intersection():
    market = [observation(0, 1), observation(5, 2), observation(10, 3)]
    company = [
        observation(0, 10),
        observation(10, 30),
        observation(15, 40),
    ]

    result = calculate(market, company)

    assert_pair_timestamps(
        result,
        [BASE, BASE + timedelta(minutes=10)],
    )
    assert result["pairs"] == [(1.0, 10.0), (3.0, 30.0)]


@pytest.mark.parametrize(
    "records, error",
    [
        (
            [ohlcv(0, 100), ohlcv(5, 0), ohlcv(10, 101)],
            "zero prior close",
        ),
        (
            [ohlcv(0, 100), ohlcv(0, 101)],
            "duplicate timestamp",
        ),
        (
            [ohlcv(5, 101), ohlcv(0, 100)],
            "chronologically ordered",
        ),
    ],
)
def test_returns_reject_invalid_timestamped_history_instead_of_dropping_observations(
    records, error
):
    with pytest.raises(ValueError, match=error):
        simple_returns(records)


def test_returns_remain_timestamped_and_preserve_missing_timestamp_gaps():
    result = simple_returns([ohlcv(0, 100), ohlcv(10, 110)])

    assert result == [
        {"timestamp": BASE + timedelta(minutes=10), "value": 0.1}
    ]


def test_event_study_rejects_mismatched_timestamp_sets_instead_of_truncating():
    with pytest.raises(ValueError, match="mismatched timestamp sets"):
        abnormal_returns(
            [observation(0, 1), observation(5, 2)],
            [observation(0, 10)],
        )


def test_evidence_record_retains_alignment_metadata():
    record = EvidenceRecord(
        symbol="COMPANY",
        market="MARKET",
        timeframe="5m",
        metric="correlation",
        value=None,
        sample_size=2,
        source="provider",
        methodology="timestamp_intersection",
        timestamp_window=(BASE, BASE + timedelta(minutes=10)),
        calculation_method="pearson",
        lag=1,
        data_quality={"missing_timestamps": 1},
        causation_claim=False,
    )

    assert record.timestamp_window == (BASE, BASE + timedelta(minutes=10))
    assert record.sample_size == 2
    assert record.calculation_method == "pearson"
    assert record.lag == 1
    assert record.data_quality == {"missing_timestamps": 1}
    assert record.causation_claim is False
