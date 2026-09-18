"""
Canonical OHLCV schema.

Historical market observations use explicit timezone-aware UTC timestamps.

Architecture contract:

Provider
    ↓
Normalizer
    ↓
OHLCVRecord
    ↓
Historical / Indicator / Relationship calculations

Rules:
- timestamp must be a datetime
- timestamp must be timezone-aware
- timestamp is normalized to UTC
- OHLC values must be finite
- high >= low
- open and close must lie within high/low
- volume must be finite and non-negative
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import math
from typing import Any


def _utc_timestamp(value: Any) -> datetime:
    """
    Validate and normalize a timestamp to timezone-aware UTC.

    Strings are intentionally not accepted here.

    String timestamps belong to the provider-normalization boundary.
    By the time data reaches OHLCVRecord, the timestamp must already be
    a canonical datetime object.
    """
    if value is None:
        raise ValueError("timestamp cannot be None")

    if not isinstance(value, datetime):
        raise TypeError("timestamp must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    return value.astimezone(timezone.utc)


def _finite_number(value: Any, field: str) -> float:
    """Convert a numeric field to float and reject non-finite values."""
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise TypeError(f"{field} must be numeric") from exc

    if not math.isfinite(number):
        raise ValueError(f"{field} must be finite")

    return number


@dataclass(frozen=True)
class OHLCVRecord:
    """
    Canonical single OHLCV observation.

    timestamp:
        timezone-aware datetime. Stored internally as UTC.

    open/high/low/close:
        finite numeric OHLC values.

    volume:
        finite non-negative numeric volume.
    """

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    def __post_init__(self) -> None:
        timestamp = _utc_timestamp(self.timestamp)

        open_ = _finite_number(self.open, "open")
        high = _finite_number(self.high, "high")
        low = _finite_number(self.low, "low")
        close = _finite_number(self.close, "close")
        volume = _finite_number(self.volume, "volume")

        if high < low:
            raise ValueError(
                "high must be greater than or equal to low"
            )

        if not (low <= open_ <= high):
            raise ValueError(
                "open must be within high/low range"
            )

        if not (low <= close <= high):
            raise ValueError(
                "close must be within high/low range"
            )

        if volume < 0:
            raise ValueError(
                "volume must be non-negative"
            )

        object.__setattr__(self, "timestamp", timestamp)
        object.__setattr__(self, "open", open_)
        object.__setattr__(self, "high", high)
        object.__setattr__(self, "low", low)
        object.__setattr__(self, "close", close)
        object.__setattr__(self, "volume", volume)


__all__ = [
    "OHLCVRecord",
]
