"""Foundation-layer smoke tests."""
def test_universe():
    from config.universe import NIFTY50_SYMBOLS, TRACKED_MARKETS, validate_universe
    assert len(NIFTY50_SYMBOLS) == 50
    assert len(TRACKED_MARKETS) == 9
    assert validate_universe() is True

def test_timeframes():
    from config.timeframes import TIMEFRAMES, validate_timeframes
    assert "1d" in TIMEFRAMES
    assert validate_timeframes() is True

def test_ohlcv_schema():
    from schemas.ohlcv import OHLCVRecord
    row = OHLCVRecord("2026-01-01", 100, 110, 95, 105, 1000)
    assert row.validate() is True
