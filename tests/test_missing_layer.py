from datetime import datetime, timezone

import pytest

from data_providers.data_normalizer import normalize_record, normalize_records


def utc_timestamp():
    return datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )


def test_normalizer():
    x = normalize_records(
        [
            {
                "timestamp": "2026-01-01T00:00:00+00:00",
                "open": 100,
                "high": 110,
                "low": 95,
                "close": 105,
                "volume": 1000,
            }
        ]
    )

    assert len(x) == 1
    assert x[0]["timestamp"] == utc_timestamp()
    assert x[0]["open"] == 100.0
    assert x[0]["high"] == 110.0
    assert x[0]["low"] == 95.0
    assert x[0]["close"] == 105.0
    assert x[0]["volume"] == 1000.0


def test_normalizer_accepts_utc_z_suffix():
    result = normalize_records(
        [
            {
                "timestamp": "2026-01-01T00:00:00Z",
                "open": 100,
                "high": 110,
                "low": 95,
                "close": 105,
                "volume": 1000,
            }
        ]
    )

    assert result[0]["timestamp"] == utc_timestamp()


def test_normalizer_converts_offset_to_utc():
    result = normalize_records(
        [
            {
                "timestamp": "2026-01-01T05:30:00+05:30",
                "open": 100,
                "high": 110,
                "low": 95,
                "close": 105,
                "volume": 1000,
            }
        ]
    )

    assert result[0]["timestamp"] == utc_timestamp()


def test_normalizer_rejects_naive_string_timestamp():
    with pytest.raises(
        ValueError,
        match="timezone-aware UTC timestamp",
    ):
        normalize_records(
            [
                {
                    "timestamp": "2026-01-01",
                    "open": 100,
                    "high": 110,
                    "low": 95,
                    "close": 105,
                    "volume": 1000,
                }
            ]
        )


def test_normalizer_rejects_naive_datetime():
    naive = datetime(2026, 1, 1)

    with pytest.raises(
        ValueError,
        match="timezone-aware UTC timestamp",
    ):
        normalize_records(
            [
                {
                    "timestamp": naive,
                    "open": 100,
                    "high": 110,
                    "low": 95,
                    "close": 105,
                    "volume": 1000,
                }
            ]
        )


def test_normalizer_rejects_missing_timestamp():
    with pytest.raises(
        ValueError,
        match="missing timestamp",
    ):
        normalize_records(
            [
                {
                    "open": 100,
                    "high": 110,
                    "low": 95,
                    "close": 105,
                    "volume": 1000,
                }
            ]
        )


def test_normalizer_rejects_invalid_ohlcv():
    with pytest.raises(ValueError):
        normalize_records(
            [
                {
                    "timestamp": "2026-01-01T00:00:00+00:00",
                    "open": 100,
                    "high": 90,
                    "low": 95,
                    "close": 105,
                    "volume": 1000,
                }
            ]
        )


def test_normalizer_sorts_chronologically():
    result = normalize_records(
        [
            {
                "timestamp": "2026-01-01T00:10:00+00:00",
                "open": 102,
                "high": 112,
                "low": 97,
                "close": 107,
                "volume": 1200,
            },
            {
                "timestamp": "2026-01-01T00:00:00+00:00",
                "open": 100,
                "high": 110,
                "low": 95,
                "close": 105,
                "volume": 1000,
            },
        ]
    )

    assert result[0]["timestamp"] < result[1]["timestamp"]


def test_normalizer_rejects_duplicate_timestamps():
    row = {
        "timestamp": "2026-01-01T00:00:00+00:00",
        "open": 100,
        "high": 110,
        "low": 95,
        "close": 105,
        "volume": 1000,
    }

    with pytest.raises(
        ValueError,
        match="duplicate timestamp",
    ):
        normalize_records([row, row])


def test_normalize_record_returns_ohlcv_record():
    row = normalize_record(
        {
            "timestamp": "2026-01-01T00:00:00+00:00",
            "open": 100,
            "high": 110,
            "low": 95,
            "close": 105,
            "volume": 1000,
        }
    )

    assert row.timestamp == utc_timestamp()
    assert row.open == 100.0
    assert row.high == 110.0
    assert row.low == 95.0
    assert row.close == 105.0
    assert row.volume == 1000.0
