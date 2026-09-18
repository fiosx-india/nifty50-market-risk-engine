from datetime import datetime, timezone

import pytest

from config.universe import NIFTY50_SYMBOLS, TRACKED_MARKETS
from config.timeframes import TIMEFRAMES
from schemas.ohlcv import OHLCVRecord


def test_universe_has_50_nifty_symbols():
    assert len(NIFTY50_SYMBOLS) == 50
    assert len(set(NIFTY50_SYMBOLS)) == 50


def test_tracked_markets():
    assert TRACKED_MARKETS == (
        "NIFTY 50",
        "Crude Oil",
        "Gold",
        "Silver",
        "Natural Gas",
        "Copper",
        "Aluminium",
        "Zinc",
        "Electricity",
    )


def test_timeframes_are_configured():
    assert "1m" in TIMEFRAMES
    assert "5m" in TIMEFRAMES
    assert "15m" in TIMEFRAMES
    assert "1h" in TIMEFRAMES
    assert "4h" in TIMEFRAMES
    assert "1d" in TIMEFRAMES


def test_ohlcv_schema():
    timestamp = datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )

    row = OHLCVRecord(
        timestamp,
        100,
        110,
        95,
        105,
        1000,
    )

    assert row.timestamp == timestamp
    assert row.open == 100.0
    assert row.high == 110.0
    assert row.low == 95.0
    assert row.close == 105.0
    assert row.volume == 1000.0


def test_ohlcv_timestamp_is_normalized_to_utc():
    from datetime import timedelta

    timestamp = datetime(
        2026,
        1,
        1,
        5,
        tzinfo=timezone(timedelta(hours=5)),
    )

    row = OHLCVRecord(
        timestamp,
        100,
        110,
        95,
        105,
        1000,
    )

    assert row.timestamp == datetime(
        2026,
        1,
        1,
        0,
        tzinfo=timezone.utc,
    )


def test_ohlcv_rejects_naive_timestamp():
    timestamp = datetime(
        2026,
        1,
        1,
    )

    with pytest.raises(
        ValueError,
        match="timezone-aware UTC timestamp",
    ):
        OHLCVRecord(
            timestamp,
            100,
            110,
            95,
            105,
            1000,
        )


def test_ohlcv_rejects_string_timestamp():
    with pytest.raises(
        TypeError,
        match="timestamp must be a datetime",
    ):
        OHLCVRecord(
            "2026-01-01",
            100,
            110,
            95,
            105,
            1000,
        )


def test_ohlcv_rejects_invalid_range():
    timestamp = datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )

    with pytest.raises(ValueError):
        OHLCVRecord(
            timestamp,
            100,
            90,
            95,
            98,
            1000,
        )


def test_ohlcv_rejects_open_outside_range():
    timestamp = datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )

    with pytest.raises(ValueError):
        OHLCVRecord(
            timestamp,
            120,
            110,
            95,
            105,
            1000,
        )


def test_ohlcv_rejects_close_outside_range():
    timestamp = datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )

    with pytest.raises(ValueError):
        OHLCVRecord(
            timestamp,
            100,
            110,
            95,
            120,
            1000,
        )


def test_ohlcv_rejects_negative_volume():
    timestamp = datetime(
        2026,
        1,
        1,
        tzinfo=timezone.utc,
    )

    with pytest.raises(ValueError):
        OHLCVRecord(
            timestamp,
            100,
            110,
            95,
            105,
            -1,
        )
