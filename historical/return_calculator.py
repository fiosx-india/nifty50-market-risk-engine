"""Timestamp-aware historical return calculations.

This module preserves the legacy numeric-sequence API while adding the
canonical timestamped OHLCV contract.

Timestamped input:
    [{"timestamp": <UTC datetime>, "close": 100, ...}, ...]

Numeric input remains supported for backward compatibility:
    [100, 110, 121]

Timestamped histories:
- require timezone-aware UTC timestamps;
- reject duplicate timestamps;
- reject unsorted timestamps;
- reject zero prior close instead of silently dropping the observation;
- preserve the timestamp belonging to each calculated return;
- never fill missing timestamps.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping, Sequence

from calculation.timestamp_alignment import (
    TimestampAlignmentError,
    validate_timestamped_series,
)


def _is_timestamped(records: Sequence[Any]) -> bool:
    return bool(records) and isinstance(records[0], Mapping)


def _validate_timestamped_ohlcv(records: Sequence[Mapping[str, Any]]):
    """Validate timestamped OHLCV records and return them unchanged."""
    validated = validate_timestamped_series(records)

    for record in validated:
        if "close" not in record:
            raise ValueError("each OHLCV observation must contain close")

        try:
            close = float(record["close"])
        except (TypeError, ValueError) as exc:
            raise ValueError("close must be numeric") from exc

        if not (close == close and abs(close) != float("inf")):
            raise ValueError("close must be finite")

    return validated


def simple_returns(close):
    """Calculate simple returns.

    Timestamped OHLCV input returns timestamped observations:

        [
            {"timestamp": t1, "value": return_1},
            ...
        ]

    Legacy numeric input continues to return numeric values.
    """
    records = list(close)

    if not records:
        return []

    if _is_timestamped(records):
        validated = _validate_timestamped_ohlcv(records)
        output = []

        for previous, current in zip(validated, validated[1:]):
            previous_close = float(previous["close"])
            current_close = float(current["close"])

            if previous_close == 0:
                raise ValueError("zero prior close")

            output.append(
                {
                    "timestamp": current["timestamp"].astimezone(timezone.utc),
                    "value": round(current_close / previous_close - 1, 15),
                }
            )

        return output

    values = []
    for value in records:
        try:
            number = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError("close must be numeric") from exc

        if not (number == number and abs(number) != float("inf")):
            raise ValueError("close must be finite")
        values.append(number)

    output = []
    for previous, current in zip(values, values[1:]):
        if previous == 0:
            raise ValueError("zero prior close")
        output.append(round(current / previous - 1, 15))

    return output


def cumulative_return(close):
    """Calculate the cumulative return while preserving legacy behavior."""
    records = list(close)

    if not records:
        return None

    if _is_timestamped(records):
        validated = _validate_timestamped_ohlcv(records)
        if len(validated) < 2:
            return None

        first = float(validated[0]["close"])
        last = float(validated[-1]["close"])

        if first == 0:
            raise ValueError("zero initial close")

        return round(last / first - 1, 15)

    values = [float(value) for value in records]
    if len(values) < 2:
        return None
    if values[0] == 0:
        return None
    return round(values[-1] / values[0] - 1, 15)


__all__ = ["simple_returns", "cumulative_return"]
