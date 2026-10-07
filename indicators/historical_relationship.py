"""
Historical Relationship Analysis
================================

Timestamp-aware historical relationship utilities.

Responsibilities:
- Align historical return observations by timestamp.
- Calculate relationship statistics through an injected function.
- Preserve evidence about alignment and missing observations.
- Maintain backward compatibility for legacy numeric sequences.

This module does NOT:
- claim causation;
- make BUY / SELL decisions;
- assign confidence;
- predict future prices;
- silently pair timestamped observations by position.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from datetime import datetime, timezone
from math import isfinite
from typing import Any


def _is_timestamped(value: Any) -> bool:
    """Return True when the input looks like timestamped observations."""
    return (
        isinstance(value, Sequence)
        and not isinstance(value, (str, bytes))
        and bool(value)
        and isinstance(value[0], Mapping)
        and "timestamp" in value[0]
    )


def _utc_timestamp(timestamp: Any, name: str) -> datetime:
    """
    Validate and normalize a timestamp to UTC.

    Naive timestamps are rejected because they do not identify
    an unambiguous point in time.
    """
    if not isinstance(timestamp, datetime):
        raise TypeError(
            f"{name} timestamp must be a datetime"
        )

    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise ValueError(
            f"{name} timestamp must be timezone-aware UTC timestamp"
        )

    return timestamp.astimezone(timezone.utc)


def _finite_value(value: Any, name: str) -> float:
    """Convert a value to finite float."""
    try:
        numeric = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"{name} value must be numeric"
        ) from exc

    if not isfinite(numeric):
        raise ValueError(
            f"{name} value must be finite"
        )

    return numeric


def _validate_timestamped(
    records: Sequence[Mapping[str, Any]],
    name: str,
) -> dict[datetime, float]:
    """
    Validate timestamped observations.

    Requirements:
    - mapping records;
    - datetime timestamps;
    - timezone-aware timestamps;
    - UTC normalization;
    - finite values;
    - strictly increasing timestamps;
    - no duplicates;
    - either 'return' or 'value' field.
    """
    result: dict[datetime, float] = {}
    previous: datetime | None = None

    for record in records:
        if not isinstance(record, Mapping):
            raise TypeError(
                f"{name} records must be mappings"
            )

        if "timestamp" not in record:
            raise ValueError(
                f"{name} record requires 'timestamp'"
            )

        timestamp = _utc_timestamp(
            record["timestamp"],
            name,
        )

        value = record.get(
            "return",
            record.get("value"),
        )

        if value is None:
            raise ValueError(
                f"{name} record requires 'return' or 'value'"
            )

        numeric = _finite_value(
            value,
            name,
        )

        if timestamp in result:
            raise ValueError(
                f"{name} contains duplicate timestamps"
            )

        if previous is not None and timestamp <= previous:
            raise ValueError(
                f"{name} timestamps must be strictly increasing "
                "and unique"
            )

        result[timestamp] = numeric
        previous = timestamp

    return result


def _validate_numeric_sequence(
    values: Sequence[Any],
    name: str,
) -> list[float]:
    """Validate the legacy numeric representation."""
    result: list[float] = []

    for value in values:
        result.append(
            _finite_value(value, name)
        )

    return result


def relationship_snapshot(
    market_returns: Sequence[Any],
    company_returns: Sequence[Any],
    correlation_fn: Callable[
        [Sequence[float], Sequence[float]],
        Any,
    ],
) -> dict[str, Any]:
    """
    Build an auditable historical relationship snapshot.

    Timestamped inputs:
        - are aligned by exact UTC timestamp;
        - never use positional pairing;
        - explicitly report missing observations;
        - preserve the aligned timestamp set.

    Numeric inputs:
        - preserve the legacy positional API.

    The returned snapshot never makes a causation claim.
    """
    market_timestamped = _is_timestamped(
        market_returns
    )
    company_timestamped = _is_timestamped(
        company_returns
    )

    if market_timestamped != company_timestamped:
        raise TypeError(
            "market_returns and company_returns must both be "
            "timestamped or both be numeric"
        )

    # ------------------------------------------------------------------
    # Timestamp-aware path
    # ------------------------------------------------------------------
    if market_timestamped:
        market = _validate_timestamped(
            market_returns,
            "market_returns",
        )

        company = _validate_timestamped(
            company_returns,
            "company_returns",
        )

        market_timestamps = set(market)
        company_timestamps = set(company)

        aligned_timestamps = sorted(
            market_timestamps.intersection(
                company_timestamps
            )
        )

        missing_market = sorted(
            company_timestamps - market_timestamps
        )

        missing_company = sorted(
            market_timestamps - company_timestamps
        )

        aligned_market = [
            market[timestamp]
            for timestamp in aligned_timestamps
        ]

        aligned_company = [
            company[timestamp]
            for timestamp in aligned_timestamps
        ]

        correlation = (
            correlation_fn(
                aligned_market,
                aligned_company,
            )
            if aligned_timestamps
            else None
        )

        return {
            "sample_size": len(
                aligned_timestamps
            ),
            "correlation": correlation,
            "calculation_status": (
                "historical_observation"
            ),
            "causation_claim": False,
            "aligned_timestamps": tuple(
                aligned_timestamps
            ),
            "alignment_method": (
                "timestamp_intersection"
            ),
            "market_observation_count": len(
                market
            ),
            "company_observation_count": len(
                company
            ),
            "missing_market_observations": len(
                missing_market
            ),
            "missing_company_observations": len(
                missing_company
            ),
            "missing_market_timestamps": tuple(
                missing_market
            ),
            "missing_company_timestamps": tuple(
                missing_company
            ),
        }

    # ------------------------------------------------------------------
    # Legacy numeric path
    # ------------------------------------------------------------------
    market_values = _validate_numeric_sequence(
        market_returns,
        "market_returns",
    )

    company_values = _validate_numeric_sequence(
        company_returns,
        "company_returns",
    )

    sample_size = min(
        len(market_values),
        len(company_values),
    )

    correlation = correlation_fn(
        market_values,
        company_values,
    )

    return {
        "sample_size": sample_size,
        "correlation": correlation,
        "calculation_status": (
            "historical_observation"
        ),
        "causation_claim": False,
        "alignment_method": (
            "legacy_positional"
        ),
        "market_observation_count": len(
            market_values
        ),
        "company_observation_count": len(
            company_values
        ),
    }


__all__ = [
    "relationship_snapshot",
]
