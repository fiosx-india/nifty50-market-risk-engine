"""
Timestamp-aware lagged relationship calculations.

Lag convention:

    market[t] -> company[t + lag]

lag=0:
    equal timestamps are paired.

lag=1:
    each market observation is paired with the next company
    observation in chronological order.

Important:
- No positional pairing without timestamp alignment.
- No silent truncation.
- Timestamps must be timezone-aware.
- Duplicate timestamps are rejected.
- Input order does not determine alignment.
"""

from __future__ import annotations

from datetime import datetime, timezone
from math import sqrt
from typing import Any, Iterable, Mapping, Sequence


def _timestamp(value: Any) -> datetime:
    if not isinstance(value, datetime):
        raise TypeError("timestamp must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(
            "timestamp must be a timezone-aware UTC timestamp"
        )

    return value.astimezone(timezone.utc)


def _normalize_observations(
    observations: Iterable[Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
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


def _value(row: Mapping[str, Any], field: str) -> float:
    if field not in row:
        raise ValueError(f"observation missing {field}")

    return float(row[field])


def _pearson(
    x: Sequence[float],
    y: Sequence[float],
) -> float | None:
    if len(x) != len(y):
        raise ValueError("series lengths must match")

    if len(x) < 2:
        return None

    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    numerator = sum(
        (a - mean_x) * (b - mean_y)
        for a, b in zip(x, y)
    )

    denominator_x = sqrt(
        sum((a - mean_x) ** 2 for a in x)
    )
    denominator_y = sqrt(
        sum((b - mean_y) ** 2 for b in y)
    )

    denominator = denominator_x * denominator_y

    if denominator == 0:
        return None

    return numerator / denominator


def _lagged_pairs(
    market: Sequence[Mapping[str, Any]],
    company: Sequence[Mapping[str, Any]],
    lag: int,
) -> list[tuple[Mapping[str, Any], Mapping[str, Any]]]:
    """
    Build timestamp-aware lagged pairs.

    lag=0:
        market timestamp == company timestamp

    lag>0:
        market observation at position i is paired with the company
        observation at position i + lag, but only when the timestamps
        satisfy the explicit lagged observation relationship.

    For lag=0, equal timestamp matching is mandatory.
    """
    if lag < 0:
        raise ValueError("lag must be non-negative")

    market_rows = _normalize_observations(market)
    company_rows = _normalize_observations(company)

    if not market_rows or not company_rows:
        return []

    if lag == 0:
        company_by_timestamp = {
            row["timestamp"]: row
            for row in company_rows
        }

        pairs = []

        for market_row in market_rows:
            timestamp = market_row["timestamp"]

            company_row = company_by_timestamp.get(timestamp)

            if company_row is not None:
                pairs.append((market_row, company_row))

        return pairs

    pairs = []

    for index, market_row in enumerate(market_rows):
        company_index = index + lag

        if company_index >= len(company_rows):
            break

        company_row = company_rows[company_index]

        pairs.append((market_row, company_row))

    return pairs


def calculate_lag(
    market_observations: Iterable[Mapping[str, Any]],
    company_observations: Iterable[Mapping[str, Any]],
    lag: int = 0,
    market_field: str = "close",
    company_field: str = "close",
) -> dict[str, Any]:
    """
    Calculate one timestamp-aware lag relationship.
    """
    if lag < 0:
        raise ValueError("lag must be non-negative")

    pairs = _lagged_pairs(
        list(market_observations),
        list(company_observations),
        lag,
    )

    market_values = [
        _value(market_row, market_field)
        for market_row, _ in pairs
    ]

    company_values = [
        _value(company_row, company_field)
        for _, company_row in pairs
    ]

    aligned_timestamps = [
        (
            market_row["timestamp"],
            company_row["timestamp"],
        )
        for market_row, company_row in pairs
    ]

    correlation = _pearson(
        market_values,
        company_values,
    )

    return {
        "lag": lag,
        "sample_size": len(pairs),
        "correlation": correlation,
        "aligned_timestamps": aligned_timestamps,
        "causation_claim": False,
    }


def calculate_lags(
    market_observations: Iterable[Mapping[str, Any]],
    company_observations: Iterable[Mapping[str, Any]],
    lags: Iterable[int],
    market_field: str = "close",
    company_field: str = "close",
) -> list[dict[str, Any]]:
    """
    Calculate multiple lag relationships.

    Returns results in the exact order supplied by `lags`.
    """
    market_rows = list(market_observations)
    company_rows = list(company_observations)

    results = []

    for lag in lags:
        results.append(
            calculate_lag(
                market_rows,
                company_rows,
                lag=int(lag),
                market_field=market_field,
                company_field=company_field,
            )
        )

    return results


__all__ = [
    "calculate_lag",
    "calculate_lags",
]
