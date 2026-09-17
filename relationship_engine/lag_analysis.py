"""Timestamp-aware lag analysis for market/company relationships.

This module is a relationship-layer adapter. It does not calculate
correlation, causation, risk, or trading signals.

Canonical lag direction:
    market[t] -> company[t + lag]

Timestamped observations are validated and aligned explicitly. Numeric
sequences remain supported for backward compatibility.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Mapping

from calculation.timestamp_alignment import (
    TimestampAlignmentError,
    validate_timestamped_series,
)


def _is_timestamped(values: Any) -> bool:
    return bool(values) and isinstance(values[0], Mapping)


def _validate_timestamped_returns(values, name: str):
    records = validate_timestamped_series(values)

    for index, record in enumerate(records):
        if "value" not in record:
            raise TimestampAlignmentError(
                f"{name}[{index}] requires value"
            )
        try:
            value = float(record["value"])
        except (TypeError, ValueError) as exc:
            raise TimestampAlignmentError(
                f"{name}[{index}] value must be numeric"
            ) from exc
        if not (value == value and abs(value) != float("inf")):
            raise TimestampAlignmentError(
                f"{name}[{index}] value must be finite"
            )

    return records


def lag_pairs(market_returns, company_returns, lag):
    """Return market/company pairs for a non-negative observation lag.

    For timestamped observations, lag is defined in observation steps:
    ``market[i]`` is paired with ``company[i + lag]``.

    The returned timestamped pairs retain both timestamps so downstream
    calculations can audit exactly which observations were compared.

    No sorting, filling, or silent truncation is performed for timestamped
    inputs.
    """
    lag = int(lag)
    if lag < 0:
        raise ValueError("lag must be >= 0")

    market = list(market_returns)
    company = list(company_returns)

    timestamped = _is_timestamped(market) or _is_timestamped(company)

    if timestamped:
        if not (_is_timestamped(market) and _is_timestamped(company)):
            raise TimestampAlignmentError(
                "market and company observations must both be timestamped"
            )

        market = _validate_timestamped_returns(market, "market")
        company = _validate_timestamped_returns(company, "company")

        if len(market) <= lag or not company:
            return []

        pairs = []
        for index in range(min(len(market), len(company) - lag)):
            market_record = market[index]
            company_record = company[index + lag]

            market_timestamp = market_record["timestamp"].astimezone(timezone.utc)
            company_timestamp = company_record["timestamp"].astimezone(timezone.utc)

            # A positive lag must never pair an observation with a company
            # observation from the same or an earlier timestamp.
            if company_timestamp <= market_timestamp:
                continue

            pairs.append(
                {
                    "market_timestamp": market_timestamp,
                    "company_timestamp": company_timestamp,
                    "market_value": float(market_record["value"]),
                    "company_value": float(company_record["value"]),
                    "lag": lag,
                }
            )

        return pairs

    # Legacy numeric-sequence behavior.
    n = min(len(market), len(company))
    if n <= lag:
        return []

    market_values = list(map(float, market[-n:]))
    company_values = list(map(float, company[-n:]))

    return [
        (market_values[index], company_values[index + lag])
        for index in range(n - lag)
    ]


def lag_snapshot(market_returns, company_returns, lag):
    """Return an auditable lag-alignment snapshot."""
    pairs = lag_pairs(market_returns, company_returns, lag)

    if not pairs:
        return {
            "lag": int(lag),
            "sample_size": 0,
            "pairs": [],
            "timestamp_window": None,
            "status": "insufficient_data",
            "causation_claim": False,
        }

    if isinstance(pairs[0], Mapping):
        market_times = [item["market_timestamp"] for item in pairs]
        company_times = [item["company_timestamp"] for item in pairs]
        return {
            "lag": int(lag),
            "sample_size": len(pairs),
            "pairs": pairs,
            "timestamp_window": (
                min(market_times),
                max(company_times),
            ),
            "status": "calculated",
            "causation_claim": False,
        }

    return {
        "lag": int(lag),
        "sample_size": len(pairs),
        "pairs": pairs,
        "timestamp_window": None,
        "status": "calculated",
        "causation_claim": False,
    }


__all__ = ["lag_pairs", "lag_snapshot"]
