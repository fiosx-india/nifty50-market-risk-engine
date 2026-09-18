"""Historical relationship snapshot utilities.

Records historical relationship observations without making causation or
trading decisions. Timestamped observations are aligned by common timestamps.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from datetime import datetime
from math import isfinite
from typing import Any


def _is_timestamped(value: Any) -> bool:
    return (
        isinstance(value, Sequence)
        and not isinstance(value, (str, bytes))
        and bool(value)
        and isinstance(value[0], dict)
        and "timestamp" in value[0]
    )


def _validate_timestamped(
    records: Sequence[dict[str, Any]], name: str
) -> dict[datetime, float]:
    result: dict[datetime, float] = {}
    previous: datetime | None = None

    for record in records:
        if not isinstance(record, dict):
            raise TypeError(f"{name} records must be mappings")

        timestamp = record.get("timestamp")
        if not isinstance(timestamp, datetime):
            raise TypeError(f"{name} timestamp must be a datetime")
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise ValueError(f"{name} timestamp must be timezone-aware")

        value = record.get("return", record.get("value"))
        if value is None:
            raise ValueError(f"{name} record requires 'return' or 'value'")

        numeric = float(value)
        if not isfinite(numeric):
            raise ValueError(f"{name} value must be finite")

        if previous is not None and timestamp <= previous:
            raise ValueError(
                f"{name} timestamps must be strictly increasing and unique"
            )

        result[timestamp] = numeric
        previous = timestamp

    return result


def relationship_snapshot(
    market_returns: Sequence[Any],
    company_returns: Sequence[Any],
    correlation_fn: Callable[[Sequence[float], Sequence[float]], Any],
) -> dict[str, Any]:
    """Build an auditable historical relationship snapshot.

    Numeric sequences preserve the original positional API. Timestamped
    records use timestamp intersection and do not silently pair observations
    by position.
    """
    market_timestamped = _is_timestamped(market_returns)
    company_timestamped = _is_timestamped(company_returns)

    if market_timestamped != company_timestamped:
        raise TypeError(
            "market_returns and company_returns must both be timestamped "
            "or both be numeric"
        )

    if market_timestamped:
        market = _validate_timestamped(market_returns, "market_returns")
        company = _validate_timestamped(company_returns, "company_returns")

        timestamps = sorted(set(market).intersection(company))
        aligned_market = [market[timestamp] for timestamp in timestamps]
        aligned_company = [company[timestamp] for timestamp in timestamps]

        correlation = (
            correlation_fn(aligned_market, aligned_company)
            if timestamps
            else None
        )

        return {
            "sample_size": len(timestamps),
            "correlation": correlation,
            "calculation_status": "historical_observation",
            "causation_claim": False,
            "aligned_timestamps": tuple(timestamps),
            "alignment_method": "timestamp_intersection",
            "market_observation_count": len(market),
            "company_observation_count": len(company),
            "missing_market_observations": len(set(company) - set(market)),
            "missing_company_observations": len(set(market) - set(company)),
        }

    market_values = [float(value) for value in market_returns]
    company_values = [float(value) for value in company_returns]

    return {
        "sample_size": min(len(market_values), len(company_values)),
        "correlation": correlation_fn(market_values, company_values),
        "calculation_status": "historical_observation",
        "causation_claim": False,
        "alignment_method": "legacy_positional",
    }
