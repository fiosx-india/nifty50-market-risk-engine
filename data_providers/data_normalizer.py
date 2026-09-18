"""
Provider-neutral OHLCV normalization.

Responsibility:
    Raw provider records
        -> canonical timestamp + OHLCV fields

Rules:
- timestamp must be present
- timestamp may be a datetime or ISO-8601 string
- timestamp must contain timezone information
- timestamp is normalized to UTC
- naive timestamps are rejected
- OHLCV values are validated through OHLCVRecord
- records are returned in chronological order
- duplicate timestamps are rejected
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable, Mapping

from schemas.ohlcv import OHLCVRecord


_TIMESTAMP_KEYS = (
    "timestamp",
    "datetime",
    "date",
    "time",
)

_OPEN_KEYS = ("open", "Open", "OPEN")
_HIGH_KEYS = ("high", "High", "HIGH")
_LOW_KEYS = ("low", "Low", "LOW")
_CLOSE_KEYS = ("close", "Close", "CLOSE")
_VOLUME_KEYS = ("volume", "Volume", "VOLUME")


def _first_value(row: Mapping[str, Any], keys: tuple[str, ...]) -> Any:
    for key in keys:
        if key in row:
            return row[key]
    return None


def _timestamp(value: Any) -> datetime:
    """
    Convert an input timestamp into timezone-aware UTC datetime.

    Naive timestamps are deliberately rejected because their timezone
    cannot be determined safely at the normalization boundary.
    """
    if value is None:
        raise ValueError("missing timestamp")

    if isinstance(value, datetime):
        dt = value

    elif isinstance(value, str):
        text = value.strip()

        if not text:
            raise ValueError("empty timestamp")

        # ISO-8601 UTC suffix.
        if text.endswith("Z") or text.endswith("z"):
            text = text[:-1] + "+00:00"

        try:
            dt = datetime.fromisoformat(text)
        except ValueError as exc:
            raise ValueError("invalid timestamp") from exc

    else:
        raise TypeError(
            "timestamp must be a datetime or ISO-8601 string"
        )

    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    return dt.astimezone(timezone.utc)


def _number(
    row: Mapping[str, Any],
    keys: tuple[str, ...],
    field: str,
) -> Any:
    value = _first_value(row, keys)

    if value is None:
        raise ValueError(f"missing {field}")

    return value


def normalize_record(row: Mapping[str, Any]) -> OHLCVRecord:
    """
    Normalize one raw provider row into OHLCVRecord.
    """
    if not isinstance(row, Mapping):
        raise TypeError("each record must be a mapping")

    raw_timestamp = _first_value(row, _TIMESTAMP_KEYS)

    timestamp = _timestamp(raw_timestamp)

    open_ = _number(row, _OPEN_KEYS, "open")
    high = _number(row, _HIGH_KEYS, "high")
    low = _number(row, _LOW_KEYS, "low")
    close = _number(row, _CLOSE_KEYS, "close")
    volume = _number(row, _VOLUME_KEYS, "volume")

    return OHLCVRecord(
        timestamp=timestamp,
        open=open_,
        high=high,
        low=low,
        close=close,
        volume=volume,
    )


def normalize_records(
    rows: Iterable[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    """
    Normalize multiple provider records.

    The returned dictionaries use the canonical field names:

        timestamp
        open
        high
        low
        close
        volume

    Records are sorted chronologically.

    Duplicate timestamps are rejected rather than silently overwritten.
    """
    records = [
        normalize_record(row)
        for row in rows
    ]

    records.sort(key=lambda record: record.timestamp)

    for previous, current in zip(records, records[1:]):
        if previous.timestamp == current.timestamp:
            raise ValueError(
                f"duplicate timestamp: {current.timestamp.isoformat()}"
            )

    return [
        {
            "timestamp": record.timestamp,
            "open": record.open,
            "high": record.high,
            "low": record.low,
            "close": record.close,
            "volume": record.volume,
        }
        for record in records
    ]


__all__ = [
    "normalize_record",
    "normalize_records",
]
