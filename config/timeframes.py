"""Canonical analysis timeframes.

Configuration only. This module contains no direction, score, probability,
forecast, or market relationship result.
"""

TIMEFRAMES = (
    "1m",
    "5m",
    "15m",
    "30m",
    "1h",
    "4h",
    "1d",
    "1w",
    "1M",
    "3M",
    "6M",
    "1Y",
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

# Minimum structural lookback labels used by callers. These are configuration
# names only; actual observation counts are determined by the data layer.
TIMEFRAME_GROUPS = {
    "intraday": ("1m", "5m", "15m", "30m", "1h", "4h"),
    "daily": ("1d",),
    "weekly": ("1w",),
    "monthly": ("1M", "3M", "6M", "1Y"),
}


def validate_timeframes():
    """Validate the canonical timeframe configuration."""
    if not TIMEFRAMES:
        raise ValueError("TIMEFRAMES must not be empty")

    if len(set(TIMEFRAMES)) != len(TIMEFRAMES):
        raise ValueError("Duplicate timeframe in TIMEFRAMES")

    if any(not isinstance(value, str) or not value.strip() for value in TIMEFRAMES):
        raise ValueError("TIMEFRAMES contains an empty or invalid value")

    if not HISTORICAL_WINDOWS:
        raise ValueError("HISTORICAL_WINDOWS must not be empty")

    if len(set(HISTORICAL_WINDOWS)) != len(HISTORICAL_WINDOWS):
        raise ValueError("Duplicate historical window")

    if any(
        not isinstance(value, str) or not value.strip()
        for value in HISTORICAL_WINDOWS
    ):
        raise ValueError("HISTORICAL_WINDOWS contains an empty or invalid value")

    configured = set(TIMEFRAMES)
    for group, values in TIMEFRAME_GROUPS.items():
        if not values:
            raise ValueError(f"Timeframe group '{group}' must not be empty")
        if any(value not in configured for value in values):
            raise ValueError(f"Timeframe group '{group}' contains unknown timeframe")

    return True


def is_valid_timeframe(timeframe):
    """Return True when the value is a canonical analysis timeframe."""
    return isinstance(timeframe, str) and timeframe in TIMEFRAMES


def get_timeframes():
    """Return the canonical analysis timeframes."""
    return TIMEFRAMES


def get_historical_windows():
    """Return the configured historical window labels."""
    return HISTORICAL_WINDOWS


def get_timeframe_group(group):
    """Return one configured timeframe group."""
    if group not in TIMEFRAME_GROUPS:
        raise KeyError(f"Unknown timeframe group: {group}")
    return TIMEFRAME_GROUPS[group]
