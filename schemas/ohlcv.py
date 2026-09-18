"""Provider-neutral timestamp-aware OHLCV record schema.

This schema represents observed market data only. It does not contain
relationships, predictions, trading decisions, or hard-coded market results.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
import math


def _finite_number(value, field):
    if value is None:
        raise ValueError(f"{field} cannot be None")
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be numeric") from exc
    if not math.isfinite(number):
        raise ValueError(f"{field} must be finite")
    return number


def _utc_timestamp(value):
    if value is None:
        raise ValueError("timestamp cannot be None")

    if not isinstance(value, datetime):
        raise TypeError("timestamp must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("timestamp must be timezone-aware")

    return value.astimezone(timezone.utc)


@dataclass(frozen=True)
class OHLCVRecord:
    """One canonical, timezone-aware market observation."""

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    def __post_init__(self):
        timestamp = _utc_timestamp(self.timestamp)
        open_ = _finite_number(self.open, "open")
        high = _finite_number(self.high, "high")
        low = _finite_number(self.low, "low")
        close = _finite_number(self.close, "close")
        volume = _finite_number(self.volume, "volume")

        if high < max(open_, close):
            raise ValueError("high is below open/close")
        if low > min(open_, close):
            raise ValueError("low is above open/close")
        if high < low:
            raise ValueError("high is below low")
        if volume < 0:
            raise ValueError("volume cannot be negative")

        object.__setattr__(self, "timestamp", timestamp)
        object.__setattr__(self, "open", open_)
        object.__setattr__(self, "high", high)
        object.__setattr__(self, "low", low)
        object.__setattr__(self, "close", close)
        object.__setattr__(self, "volume", volume)

    def validate(self):
        """Validate and return True for compatibility with the existing API."""
        _utc_timestamp(self.timestamp)
        _finite_number(self.open, "open")
        _finite_number(self.high, "high")
        _finite_number(self.low, "low")
        _finite_number(self.close, "close")
        _finite_number(self.volume, "volume")

        if self.high < max(self.open, self.close):
            raise ValueError("high is below open/close")
        if self.low > min(self.open, self.close):
            raise ValueError("low is above open/close")
        if self.high < self.low:
            raise ValueError("high is below low")
        if self.volume < 0:
            raise ValueError("volume cannot be negative")
        return True
