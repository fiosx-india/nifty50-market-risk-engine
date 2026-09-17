"""Canonical analysis timeframes.

Timeframes are configuration only. No direction, score, probability, or forecast
is encoded here.
"""

TIMEFRAMES = (
    "1m", "5m", "15m", "30m", "1h", "4h",
    "1d", "1w", "1M", "3M", "6M", "1Y",
)

HISTORICAL_WINDOWS = (
    "intraday",
    "1D",
    "1W",
    "1M",
    "3M",
    "6M",
    "1Y",
)

def validate_timeframes():
    if not TIMEFRAMES:
        raise ValueError("TIMEFRAMES must not be empty")
    if not HISTORICAL_WINDOWS:
        raise ValueError("HISTORICAL_WINDOWS must not be empty")
    return True
