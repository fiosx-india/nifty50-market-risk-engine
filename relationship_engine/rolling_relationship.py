"""Timestamp-aware rolling relationship utilities.

This module provides rolling-window mechanics only. It does not calculate
correlation itself, infer causation, generate signals, or rank relationships.

Timestamped series are aligned by explicit timestamp intersection before
rolling windows are created. Missing timestamps remain gaps; observations are
never silently filled, sorted, or positionally truncated.
"""

from __future__ import annotations

from typing import Any, Mapping

from calculation.timestamp_alignment import (
    TimestampAlignmentError,
    align_timestamp_intersection,
)


def _is_timestamped(values: Any) -> bool:
    return bool(values) and isinstance(values[0], Mapping)


def rolling_windows(values, window):
    """Return rolling windows from a single sequence."""
    window = int(window)
    if window <= 0:
        raise ValueError("window must be positive")
    records = list(values)
    return [
        records[index - window:index]
        for index in range(window, len(records) + 1)
    ]


def _timestamped_windows(x, y, window):
    x_records = list(x)
    y_records = list(y)

    if not (_is_timestamped(x_records) and _is_timestamped(y_records)):
        raise TimestampAlignmentError(
            "timestamped rolling windows require both series to be timestamped"
        )

    aligned = align_timestamp_intersection(x_records, y_records)
    pairs = aligned["pairs"]
    timestamps = aligned["aligned_timestamps"]

    window = int(window)
    if window <= 0:
        raise ValueError("window must be positive")

    output = []
    for end in range(window, len(pairs) + 1):
        start = end - window
        output.append(
            {
                "timestamps": tuple(timestamps[start:end]),
                "pairs": tuple(pairs[start:end]),
                "timestamp_window": (
                    timestamps[start],
                    timestamps[end - 1],
                ),
                "sample_size": window,
            }
        )
    return output


def rolling_stat(x, y, window, stat_fn):
    """Apply stat_fn to rolling aligned observations.

    Numeric sequences retain the legacy positional behavior. Timestamped
    sequences are aligned by exact timestamp intersection first.
    """
    window = int(window)
    if window <= 0:
        raise ValueError("window must be positive")

    x_records = list(x)
    y_records = list(y)

    timestamped = _is_timestamped(x_records) or _is_timestamped(y_records)

    if timestamped:
        windows = _timestamped_windows(x_records, y_records, window)
        return [
            stat_fn(
                [pair[0] for pair in item["pairs"]],
                [pair[1] for pair in item["pairs"]],
            )
            for item in windows
        ]

    n = min(len(x_records), len(y_records))
    return [
        stat_fn(
            x_records[index - window:index],
            y_records[index - window:index],
        )
        for index in range(window, n + 1)
    ]


def rolling_stat_snapshots(x, y, window, stat_fn):
    """Return rolling results with auditable timestamp metadata."""
    window = int(window)
    if window <= 0:
        raise ValueError("window must be positive")

    x_records = list(x)
    y_records = list(y)

    if not (_is_timestamped(x_records) and _is_timestamped(y_records)):
        values = rolling_stat(x_records, y_records, window, stat_fn)
        return [
            {
                "value": value,
                "timestamp_window": None,
                "sample_size": min(window, len(x_records), len(y_records)),
                "calculation_method": getattr(stat_fn, "__name__", "stat_fn"),
                "causation_claim": False,
            }
            for value in values
        ]

    windows = _timestamped_windows(x_records, y_records, window)
    output = []

    for item in windows:
        x_values = [pair[0] for pair in item["pairs"]]
        y_values = [pair[1] for pair in item["pairs"]]
        output.append(
            {
                "value": stat_fn(x_values, y_values),
                "timestamp_window": item["timestamp_window"],
                "sample_size": item["sample_size"],
                "calculation_method": getattr(stat_fn, "__name__", "stat_fn"),
                "causation_claim": False,
            }
        )

    return output


__all__ = [
    "rolling_windows",
    "rolling_stat",
    "rolling_stat_snapshots",
]
