from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from historical.historical_relationship import relationship_snapshot


def utc(day: int, hour: int = 0) -> datetime:
    return datetime(
        2026,
        1,
        day,
        hour,
        tzinfo=timezone.utc,
    )


def correlation(market, company):
    if not market or not company:
        return None

    market_mean = sum(market) / len(market)
    company_mean = sum(company) / len(company)

    numerator = sum(
        (x - market_mean) * (y - company_mean)
        for x, y in zip(market, company)
    )

    market_variance = sum(
        (x - market_mean) ** 2
        for x in market
    )

    company_variance = sum(
        (y - company_mean) ** 2
        for y in company
    )

    denominator = (
        market_variance * company_variance
    ) ** 0.5

    if denominator == 0:
        return None

    return numerator / denominator


def test_timestamped_relationship_uses_timestamp_intersection():
    market = [
        {"timestamp": utc(1), "return": 0.01},
        {"timestamp": utc(2), "return": 0.02},
        {"timestamp": utc(3), "return": 0.03},
    ]

    company = [
        {"timestamp": utc(1), "return": 0.02},
        {"timestamp": utc(3), "return": 0.04},
        {"timestamp": utc(4), "return": 0.05},
    ]

    result = relationship_snapshot(
        market,
        company,
        correlation,
    )

    assert result["alignment_method"] == (
        "timestamp_intersection"
    )

    assert result["aligned_timestamps"] == (
        utc(1),
        utc(3),
    )

    assert result["sample_size"] == 2


def test_timestamped_relationship_does_not_use_positional_pairing():
    market = [
        {"timestamp": utc(1), "return": 0.10},
        {"timestamp": utc(2), "return": 0.20},
    ]

    company = [
        {"timestamp": utc(2), "return": 0.20},
        {"timestamp": utc(3), "return": 0.30},
    ]

    captured = {}

    def capture(market_values, company_values):
        captured["market"] = list(market_values)
        captured["company"] = list(company_values)
        return 0.0

    relationship_snapshot(
        market,
        company,
        capture,
    )

    assert captured["market"] == [0.20]
    assert captured["company"] == [0.20]


def test_timestamped_relationship_reports_missing_observations():
    market = [
        {"timestamp": utc(1), "return": 0.01},
        {"timestamp": utc(2), "return": 0.02},
    ]

    company = [
        {"timestamp": utc(2), "return": 0.03},
        {"timestamp": utc(3), "return": 0.04},
    ]

    result = relationship_snapshot(
        market,
        company,
        correlation,
    )

    assert result["missing_market_observations"] == 1
    assert result["missing_company_observations"] == 1

    assert result["missing_market_timestamps"] == (
        utc(3),
    )

    assert result["missing_company_timestamps"] == (
        utc(1),
    )


def test_timestamped_relationship_preserves_causation_false():
    result = relationship_snapshot(
        [
            {"timestamp": utc(1), "return": 0.01},
        ],
        [
            {"timestamp": utc(1), "return": 0.02},
        ],
        correlation,
    )

    assert result["causation_claim"] is False


def test_timestamped_relationship_normalizes_to_utc():
    india_tz = timezone(timedelta(hours=5, minutes=30))

    market = [
        {
            "timestamp": datetime(
                2026,
                1,
                1,
                5,
                30,
                tzinfo=india_tz,
            ),
            "return": 0.01,
        }
    ]

    company = [
        {
            "timestamp": utc(1),
            "return": 0.02,
        }
    ]

    result = relationship_snapshot(
        market,
        company,
        correlation,
    )

    assert result["aligned_timestamps"] == (
        utc(1),
    )


def test_timestamped_relationship_rejects_naive_timestamp():
    market = [
        {
            "timestamp": datetime(2026, 1, 1),
            "return": 0.01,
        }
    ]

    company = [
        {
            "timestamp": utc(1),
            "return": 0.02,
        }
    ]

    with pytest.raises(ValueError, match="timezone"):
        relationship_snapshot(
            market,
            company,
            correlation,
        )


def test_timestamped_relationship_rejects_duplicate_timestamp():
    market = [
        {"timestamp": utc(1), "return": 0.01},
        {"timestamp": utc(1), "return": 0.02},
    ]

    company = [
        {"timestamp": utc(1), "return": 0.03},
    ]

    with pytest.raises(ValueError, match="duplicate"):
        relationship_snapshot(
            market,
            company,
            correlation,
        )


def test_timestamped_relationship_rejects_unsorted_market():
    market = [
        {"timestamp": utc(2), "return": 0.02},
        {"timestamp": utc(1), "return": 0.01},
    ]

    company = [
        {"timestamp": utc(1), "return": 0.03},
        {"timestamp": utc(2), "return": 0.04},
    ]

    with pytest.raises(ValueError, match="strictly increasing"):
        relationship_snapshot(
            market,
            company,
            correlation,
        )


def test_timestamped_relationship_rejects_unsorted_company():
    market = [
        {"timestamp": utc(1), "return": 0.01},
        {"timestamp": utc(2), "return": 0.02},
    ]

    company = [
        {"timestamp": utc(2), "return": 0.03},
        {"timestamp": utc(1), "return": 0.04},
    ]

    with pytest.raises(ValueError, match="strictly increasing"):
        relationship_snapshot(
            market,
            company,
            correlation,
        )


def test_timestamped_relationship_requires_value_or_return():
    market = [
        {"timestamp": utc(1), "return": 0.01},
    ]

    company = [
        {"timestamp": utc(1)},
    ]

    with pytest.raises(ValueError, match="return"):
        relationship_snapshot(
            market,
            company,
            correlation,
        )


def test_timestamped_relationship_accepts_value_field():
    market = [
        {"timestamp": utc(1), "value": 0.01},
    ]

    company = [
        {"timestamp": utc(1), "value": 0.02},
    ]

    captured = {}

    def capture(market_values, company_values):
        captured["market"] = list(market_values)
        captured["company"] = list(company_values)
        return None

    relationship_snapshot(
        market,
        company,
        capture,
    )

    assert captured["market"] == [0.01]
    assert captured["company"] == [0.02]


def test_timestamped_relationship_rejects_non_finite_value():
    market = [
        {"timestamp": utc(1), "return": float("nan")},
    ]

    company = [
        {"timestamp": utc(1), "return": 0.02},
    ]

    with pytest.raises(ValueError, match="finite"):
        relationship_snapshot(
            market,
            company,
            correlation,
        )


def test_timestamped_relationship_rejects_mixed_input_types():
    market = [
        {"timestamp": utc(1), "return": 0.01},
    ]

    company = [0.02]

    with pytest.raises(TypeError):
        relationship_snapshot(
            market,
            company,
            correlation,
        )


def test_timestamped_relationship_with_no_overlap():
    market = [
        {"timestamp": utc(1), "return": 0.01},
    ]

    company = [
        {"timestamp": utc(2), "return": 0.02},
    ]

    called = False

    def correlation_fn(market_values, company_values):
        nonlocal called
        called = True
        return correlation(
            market_values,
            company_values,
        )

    result = relationship_snapshot(
        market,
        company,
        correlation_fn,
    )

    assert result["sample_size"] == 0
    assert result["correlation"] is None
    assert result["aligned_timestamps"] == ()
    assert called is False


def test_numeric_legacy_api_is_preserved():
    result = relationship_snapshot(
        [0.01, 0.02, 0.03],
        [0.02, 0.04, 0.06],
        correlation,
    )

    assert result["alignment_method"] == (
        "legacy_positional"
    )

    assert result["sample_size"] == 3
    assert result["causation_claim"] is False


def test_numeric_legacy_api_reports_observation_counts():
    result = relationship_snapshot(
        [0.01, 0.02],
        [0.03, 0.04, 0.05],
        correlation,
    )

    assert result["market_observation_count"] == 2
    assert result["company_observation_count"] == 3
    assert result["sample_size"] == 2


def test_numeric_api_rejects_non_finite_values():
    with pytest.raises(ValueError, match="finite"):
        relationship_snapshot(
            [0.01, float("inf")],
            [0.02, 0.03],
            correlation,
        )


def test_timestamped_alignment_is_chronological():
    market = [
        {"timestamp": utc(1), "return": 0.01},
        {"timestamp": utc(2), "return": 0.02},
        {"timestamp": utc(3), "return": 0.03},
    ]

    company = [
        {"timestamp": utc(1), "return": 0.02},
        {"timestamp": utc(2), "return": 0.03},
        {"timestamp": utc(3), "return": 0.04},
    ]

    result = relationship_snapshot(
        market,
        company,
        correlation,
    )

    assert result["aligned_timestamps"] == (
        utc(1),
        utc(2),
        utc(3),
    )
