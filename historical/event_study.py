"""Timestamp-aware abnormal-return event study.

This module preserves the legacy numeric-sequence API while adding the
canonical timestamp-aware alignment contract.

For timestamped observations, asset and benchmark returns are aligned by
exact UTC timestamp intersection. Missing observations are retained as gaps;
they are never filled, positionally paired, silently truncated, or sorted by
this module. Correlation/causation conclusions are outside this module.
"""

from __future__ import annotations

from statistics import mean
from typing import Any, Mapping

from calculation.timestamp_alignment import (
    TimestampAlignmentError,
    align_timestamp_intersection,
)


def _is_timestamped(values: Any) -> bool:
    return bool(values) and isinstance(values[0], Mapping)


def _validate_return_records(records, name: str):
    """Validate timestamped return records and return a concrete list."""
    items = list(records)
    if not items:
        return []

    # Reuse the canonical timestamp/alignment validation by pairing later.
    for index, item in enumerate(items):
        if not isinstance(item, Mapping):
            raise TimestampAlignmentError(
                f"{name}[{index}] must be a timestamped return observation"
            )
        if "timestamp" not in item or "value" not in item:
            raise TimestampAlignmentError(
                f"{name}[{index}] requires timestamp and value"
            )
        try:
            value = float(item["value"])
        except (TypeError, ValueError) as exc:
            raise TimestampAlignmentError(
                f"{name}[{index}] value must be numeric"
            ) from exc
        if not (value == value and abs(value) != float("inf")):
            raise TimestampAlignmentError(
                f"{name}[{index}] value must be finite"
            )
    return items


def abnormal_returns(asset_returns, benchmark_returns):
    """Calculate asset minus benchmark return.

    Legacy numeric inputs return ``list[float]``.

    Timestamped inputs return observations containing:
    ``timestamp``, ``value``, and the aligned asset/benchmark returns.
    Alignment is an exact timestamp intersection.
    """
    asset = list(asset_returns)
    benchmark = list(benchmark_returns)

    timestamped = _is_timestamped(asset) or _is_timestamped(benchmark)
    if timestamped:
        if not (_is_timestamped(asset) and _is_timestamped(benchmark)):
            raise TimestampAlignmentError(
                "asset and benchmark observations must both be timestamped"
            )

        asset = _validate_return_records(asset, "asset")
        benchmark = _validate_return_records(benchmark, "benchmark")
        aligned = align_timestamp_intersection(asset, benchmark)

        output = []
        for timestamp, (asset_value, benchmark_value) in zip(
            aligned["aligned_timestamps"], aligned["pairs"]
        ):
            output.append(
                {
                    "timestamp": timestamp,
                    "value": asset_value - benchmark_value,
                    "asset_return": asset_value,
                    "benchmark_return": benchmark_value,
                }
            )
        return output

    n = min(len(asset), len(benchmark))
    return [
        float(asset[i]) - float(benchmark[i])
        for i in range(n)
    ]


def cumulative_abnormal_return(asset_returns, benchmark_returns):
    """Calculate cumulative abnormal return.

    For timestamped inputs, returns the sum of abnormal returns over the
    explicit timestamp intersection. ``None`` is returned when no aligned
    observations exist.
    """
    abnormal = abnormal_returns(asset_returns, benchmark_returns)

    if not abnormal:
        return None

    if _is_timestamped(abnormal):
        return sum(float(item["value"]) for item in abnormal)

    return sum(abnormal)


def abnormal_return_snapshot(asset_returns, benchmark_returns):
    """Return an auditable timestamp-aware event-study snapshot.

    This helper is additive and does not alter the legacy functions above.
    """
    abnormal = abnormal_returns(asset_returns, benchmark_returns)

    if _is_timestamped(abnormal):
        timestamps = [item["timestamp"] for item in abnormal]
        values = [float(item["value"]) for item in abnormal]
        return {
            "sample_size": len(values),
            "timestamp_window": (
                (timestamps[0], timestamps[-1]) if timestamps else None
            ),
            "mean_abnormal_return": mean(values) if values else None,
            "cumulative_abnormal_return": sum(values) if values else None,
            "calculation_status": (
                "calculated" if values else "insufficient_data"
            ),
            "causation_claim": False,
        }

    values = [float(item) for item in abnormal]
    return {
        "sample_size": len(values),
        "timestamp_window": None,
        "mean_abnormal_return": mean(values) if values else None,
        "cumulative_abnormal_return": sum(values) if values else None,
        "calculation_status": "calculated" if values else "insufficient_data",
        "causation_claim": False,
    }


__all__ = [
    "abnormal_returns",
    "cumulative_abnormal_return",
    "abnormal_return_snapshot",
]
