"""
Timestamp-aware event study calculations.

Architecture rules:
- Observations are aligned by explicit timestamps.
- Naive timestamps are rejected.
- All timestamps are normalized to UTC.
- Mismatched timestamp sets are NOT silently truncated.
- Event-study calculations must operate on an explicit common
  timestamp set.
- No causation claim is produced by this module.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Iterable, Mapping, Sequence


def _timestamp(value: Any) -> datetime:
    """Validate and normalize a timestamp to UTC."""
    if not isinstance(value, datetime):
        raise TypeError("timestamp must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    return value.astimezone(timezone.utc)


def _normalize(
    observations: Iterable[Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    """Normalize and chronologically sort timestamped observations."""
    rows = list(observations)

    normalized: list[Mapping[str, Any]] = []

    for row in rows:
        if not isinstance(row, Mapping):
            raise TypeError("observation must be a mapping")

        if "timestamp" not in row:
            raise ValueError("observation requires timestamp")

        timestamp = _timestamp(row["timestamp"])

        normalized.append(
            {
                **row,
                "timestamp": timestamp,
            }
        )

    normalized.sort(key=lambda row: row["timestamp"])

    timestamps = [row["timestamp"] for row in normalized]

    if len(timestamps) != len(set(timestamps)):
        raise ValueError("duplicate timestamps are not allowed")

    return normalized


def _timestamp_set(
    observations: Sequence[Mapping[str, Any]],
) -> set[datetime]:
    return {
        row["timestamp"]
        for row in observations
    }


def _validate_matching_timestamps(
    left: Sequence[Mapping[str, Any]],
    right: Sequence[Mapping[str, Any]],
) -> None:
    """
    Require exact timestamp-set equality.

    We deliberately do not silently intersect or truncate here.
    """
    left_timestamps = _timestamp_set(left)
    right_timestamps = _timestamp_set(right)

    if left_timestamps != right_timestamps:
        missing_from_right = sorted(
            left_timestamps - right_timestamps
        )
        missing_from_left = sorted(
            right_timestamps - left_timestamps
        )

        raise ValueError(
            "mismatched timestamp sets: "
            f"missing_from_right={missing_from_right}, "
            f"missing_from_left={missing_from_left}"
        )


def _value(
    row: Mapping[str, Any],
    field: str,
) -> float:
    if field not in row:
        raise ValueError(
            f"observation missing {field}"
        )

    return float(row[field])


def _mean(values: Sequence[float]) -> float | None:
    if not values:
        return None

    return sum(values) / len(values)


def _abnormal_return(
    company_return: float,
    benchmark_return: float,
) -> float:
    """
    Simple abnormal-return calculation.

    AR = company return - benchmark return
    """
    return company_return - benchmark_return


def calculate_abnormal_returns(
    company_observations: Iterable[Mapping[str, Any]],
    benchmark_observations: Iterable[Mapping[str, Any]],
    company_field: str = "return",
    benchmark_field: str = "return",
) -> dict[str, Any]:
    """
    Calculate timestamp-aligned abnormal returns.

    The two input series must have exactly the same timestamp set.
    """
    company = _normalize(company_observations)
    benchmark = _normalize(benchmark_observations)

    _validate_matching_timestamps(
        company,
        benchmark,
    )

    benchmark_by_timestamp = {
        row["timestamp"]: row
        for row in benchmark
    }

    aligned_timestamps: list[datetime] = []
    abnormal_returns: list[float] = []

    for company_row in company:
        timestamp = company_row["timestamp"]
        benchmark_row = benchmark_by_timestamp[timestamp]

        company_return = _value(
            company_row,
            company_field,
        )

        benchmark_return = _value(
            benchmark_row,
            benchmark_field,
        )

        abnormal_returns.append(
            _abnormal_return(
                company_return,
                benchmark_return,
            )
        )

        aligned_timestamps.append(timestamp)

    return {
        "abnormal_returns": abnormal_returns,
        "aligned_timestamps": aligned_timestamps,
        "sample_size": len(abnormal_returns),
        "mean_abnormal_return": _mean(abnormal_returns),
        "calculation_method": (
            "company_return - benchmark_return"
        ),
        "causation_claim": False,
    }


def event_study(
    company_observations: Iterable[Mapping[str, Any]],
    benchmark_observations: Iterable[Mapping[str, Any]],
    company_field: str = "return",
    benchmark_field: str = "return",
) -> dict[str, Any]:
    """
    Compatibility wrapper around calculate_abnormal_returns().
    """
    return calculate_abnormal_returns(
        company_observations=company_observations,
        benchmark_observations=benchmark_observations,
        company_field=company_field,
        benchmark_field=benchmark_field,
    )


__all__ = [
    "calculate_abnormal_returns",
    "event_study",
]
