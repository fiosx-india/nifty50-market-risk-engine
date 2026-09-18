"""Historical OHLCV data-quality checks.

This module validates data integrity only. It does not calculate market
relationships, risk, predictions, or trading signals.

The checks are deliberately provider-neutral and preserve gaps rather than
repairing them silently.
"""

from __future__ import annotations

from datetime import datetime, timezone
from math import isfinite
from typing import Any, Mapping, Sequence


def _validate_timestamp(value: Any) -> datetime:
    if not isinstance(value, datetime):
        raise ValueError("timestamp must be a datetime")
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("timestamp must be timezone-aware")
    return value.astimezone(timezone.utc)


def _finite_number(value: Any, field: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be numeric") from exc
    if not isfinite(number):
        raise ValueError(f"{field} must be finite")
    return number


def validate_ohlcv(records: Sequence[Mapping[str, Any]]):
    """Validate canonical timestamped OHLCV records.

    Returns a stable report rather than raising for row-level quality
    problems. Invalid timestamps/numbers are represented as errors too.
    """
    if not records:
        return {"valid": False, "errors": ("empty_data",)}

    errors = []
    previous = None
    seen = set()

    required = ("timestamp", "open", "high", "low", "close", "volume")

    for index, row in enumerate(records):
        prefix = f"row_{index}"

        if not isinstance(row, Mapping):
            errors.append(f"{prefix}:invalid_record")
            continue

        missing = [field for field in required if field not in row or row[field] is None]
        for field in missing:
            errors.append(f"{prefix}:missing_{field}")

        if missing:
            continue

        try:
            timestamp = _validate_timestamp(row["timestamp"])
        except ValueError as exc:
            errors.append(f"{prefix}:invalid_timestamp:{exc}")
            continue

        if timestamp in seen:
            errors.append(f"{prefix}:duplicate_timestamp")

        if previous is not None and timestamp <= previous:
            errors.append(f"{prefix}:non_increasing_timestamp")

        seen.add(timestamp)
        previous = timestamp

        try:
            open_value = _finite_number(row["open"], "open")
            high_value = _finite_number(row["high"], "high")
            low_value = _finite_number(row["low"], "low")
            close_value = _finite_number(row["close"], "close")
            volume_value = _finite_number(row["volume"], "volume")
        except ValueError as exc:
            errors.append(f"{prefix}:invalid_numeric:{exc}")
            continue

        if high_value < max(open_value, close_value):
            errors.append(f"{prefix}:invalid_high")

        if low_value > min(open_value, close_value):
            errors.append(f"{prefix}:invalid_low")

        if high_value < low_value:
            errors.append(f"{prefix}:invalid_range")

        if volume_value < 0:
            errors.append(f"{prefix}:negative_volume")

    return {
        "valid": not errors,
        "errors": tuple(errors),
    }


def coverage(records: Sequence[Mapping[str, Any]]):
    """Return basic time coverage without filling or inferring gaps."""
    if not records:
        return {
            "count": 0,
            "start": None,
            "end": None,
            "duration": None,
        }

    timestamps = []
    timestamp_errors = []

    for index, row in enumerate(records):
        try:
            timestamps.append(_validate_timestamp(row["timestamp"]))
        except (KeyError, ValueError, TypeError):
            timestamp_errors.append(index)

    if not timestamps:
        return {
            "count": len(records),
            "start": None,
            "end": None,
            "duration": None,
            "timestamp_errors": tuple(timestamp_errors),
        }

    start = min(timestamps)
    end = max(timestamps)

    return {
        "count": len(records),
        "start": start,
        "end": end,
        "duration": end - start,
        "timestamp_errors": tuple(timestamp_errors),
    }


def quality_summary(records: Sequence[Mapping[str, Any]]):
    """Combine integrity and coverage information into one quality report."""
    validation = validate_ohlcv(records)
    result = {
        **validation,
        "coverage": coverage(records),
    }

    if validation["valid"]:
        result["status"] = "valid"
    elif records:
        result["status"] = "invalid"
    else:
        result["status"] = "empty"

    return result


__all__ = [
    "validate_ohlcv",
    "coverage",
    "quality_summary",
]
