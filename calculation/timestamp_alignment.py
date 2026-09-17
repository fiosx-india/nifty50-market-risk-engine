"""Canonical timestamp validation and intersection utilities.

This module owns timestamp integrity and explicit timestamp-based alignment.
It does not calculate correlations, returns, risk, signals, or causation.

Contract:
- timestamps must be timezone-aware UTC ``datetime`` values;
- input observations must be strictly chronological;
- duplicate timestamps are rejected;
- missing timestamps are retained as gaps;
- alignment uses explicit timestamp intersection, never positional indexes;
- input observations are not silently sorted, filled, or truncated.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable, Mapping, Sequence


class TimestampAlignmentError(ValueError):
    """Raised when a series violates the canonical timestamp contract."""


def _validate_timestamp(value: Any) -> datetime:
    """Validate and return a canonical timezone-aware UTC timestamp."""
    if not isinstance(value, datetime):
        raise TimestampAlignmentError(
            "timestamp must be a timezone-aware UTC datetime"
        )

    if value.tzinfo is None or value.utcoffset() is None:
        raise TimestampAlignmentError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    utc_value = value.astimezone(timezone.utc)
    if utc_value.tzinfo != timezone.utc:
        raise TimestampAlignmentError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    return utc_value


def validate_timestamped_series(
    observations: Sequence[Mapping[str, Any]] | Iterable[Mapping[str, Any]],
) -> tuple[Mapping[str, Any], ...]:
    """Validate a timestamped observation series without reordering it.

    Returns the original observations as a tuple. The function deliberately
    does not sort, fill gaps, deduplicate, or drop observations.
    """
    records = tuple(observations)

    previous: datetime | None = None
    seen: set[datetime] = set()

    for record in records:
        if not isinstance(record, Mapping):
            raise TimestampAlignmentError(
                "each observation must be a mapping containing timestamp"
            )

        if "timestamp" not in record:
            raise TimestampAlignmentError(
                "each observation must contain timestamp"
            )

        timestamp = _validate_timestamp(record["timestamp"])

        if timestamp in seen:
            raise TimestampAlignmentError(
                f"duplicate timestamp: {timestamp.isoformat()}"
            )

        if previous is not None and timestamp <= previous:
            raise TimestampAlignmentError(
                "timestamps must be chronologically ordered"
            )

        seen.add(timestamp)
        previous = timestamp

    return records


def align_timestamp_intersection(
    left: Sequence[Mapping[str, Any]] | Iterable[Mapping[str, Any]],
    right: Sequence[Mapping[str, Any]] | Iterable[Mapping[str, Any]],
    *,
    left_value_key: str = "value",
    right_value_key: str = "value",
) -> dict[str, Any]:
    """Align two timestamped value series by exact timestamp intersection.

    The result preserves chronological order and contains only timestamps
    explicitly present in both inputs.

    No positional pairing, padding, forward-filling, interpolation, or
    silent truncation is performed.
    """
    left_records = validate_timestamped_series(left)
    right_records = validate_timestamped_series(right)

    left_map: dict[datetime, Mapping[str, Any]] = {
        _validate_timestamp(record["timestamp"]): record
        for record in left_records
    }
    right_map: dict[datetime, Mapping[str, Any]] = {
        _validate_timestamp(record["timestamp"]): record
        for record in right_records
    }

    timestamps = sorted(left_map.keys() & right_map.keys())

    pairs: list[tuple[float, float]] = []
    aligned_timestamps: list[datetime] = []

    for timestamp in timestamps:
        left_record = left_map[timestamp]
        right_record = right_map[timestamp]

        if left_value_key not in left_record:
            raise TimestampAlignmentError(
                f"missing value field: {left_value_key}"
            )
        if right_value_key not in right_record:
            raise TimestampAlignmentError(
                f"missing value field: {right_value_key}"
            )

        pairs.append(
            (float(left_record[left_value_key]), float(right_record[right_value_key]))
        )
        aligned_timestamps.append(timestamp)

    return {
        "pairs": pairs,
        "aligned_timestamps": aligned_timestamps,
        "sample_size": len(pairs),
        "left_count": len(left_records),
        "right_count": len(right_records),
        "status": "calculated" if len(pairs) >= 2 else "insufficient_data",
    }


__all__ = [
    "TimestampAlignmentError",
    "validate_timestamped_series",
    "align_timestamp_intersection",
]
