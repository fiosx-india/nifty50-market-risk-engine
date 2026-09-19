from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from math import isfinite, sqrt
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class RelationshipResult:
    """
    Auditable relationship-calculation result.

    Correlation describes statistical association only.
    It does not establish causation.
    """

    market: str
    company: str
    correlation: float | None
    sample_size: int
    aligned_timestamps: tuple[datetime, ...]
    company_mean_return: float | None
    market_mean_return: float | None
    excess_mean_return: float | None
    calculation_method: str
    causation_claim: bool = False

    def validate(self) -> None:
        if not self.market:
            raise ValueError("market must be non-empty")

        if not self.company:
            raise ValueError("company must be non-empty")

        if self.sample_size < 0:
            raise ValueError("sample_size must be non-negative")

        if self.sample_size != len(self.aligned_timestamps):
            raise ValueError(
                "sample_size must equal aligned_timestamps length"
            )

        for ts in self.aligned_timestamps:
            if not isinstance(ts, datetime):
                raise TypeError("timestamps must be datetime objects")

            if ts.tzinfo is None or ts.utcoffset() is None:
                raise ValueError(
                    "timestamp must be timezone-aware UTC timestamp"
                )

            if ts.astimezone(timezone.utc) != ts:
                raise ValueError("timestamps must be normalized to UTC")

        for value in (
            self.correlation,
            self.company_mean_return,
            self.market_mean_return,
            self.excess_mean_return,
        ):
            if value is not None and not isfinite(float(value)):
                raise ValueError("result values must be finite")

        if self.causation_claim:
            raise ValueError(
                "RelationshipResult must not claim causation"
            )


def _utc_timestamp(value: datetime) -> datetime:
    """
    Normalize a timezone-aware datetime to UTC.
    """
    if not isinstance(value, datetime):
        raise TypeError("timestamp must be a datetime")

    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(
            "timestamp must be timezone-aware UTC timestamp"
        )

    return value.astimezone(timezone.utc)


def _validate_timestamped_values(
    observations: Iterable[tuple[datetime, float]],
    *,
    name: str,
) -> dict[datetime, float]:
    """
    Validate timestamped numeric observations.

    No silent sorting, truncation, filling, or duplicate replacement.
    """
    result: dict[datetime, float] = {}

    for timestamp, value in observations:
        ts = _utc_timestamp(timestamp)

        numeric = float(value)

        if not isfinite(numeric):
            raise ValueError(f"{name} values must be finite")

        if ts in result:
            raise ValueError(
                f"duplicate timestamp in {name}: {ts.isoformat()}"
            )

        result[ts] = numeric

    return result


def _validate_numeric_series(
    values: Sequence[float],
    *,
    name: str,
) -> tuple[float, ...]:
    result = tuple(float(value) for value in values)

    for value in result:
        if not isfinite(value):
            raise ValueError(f"{name} values must be finite")

    return result


def _pearson(
    x: Sequence[float],
    y: Sequence[float],
) -> float | None:
    """
    Calculate Pearson correlation.

    Returns None when fewer than two observations are available
    or either series has zero variance.
    """
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

    variance_x = sum(
        (a - mean_x) ** 2
        for a in x
    )

    variance_y = sum(
        (b - mean_y) ** 2
        for b in y
    )

    denominator = sqrt(variance_x * variance_y)

    if denominator == 0:
        return None

    return numerator / denominator


def _timestamp_alignment(
    company_observations: Mapping[datetime, float],
    market_observations: Mapping[datetime, float],
) -> tuple[
    tuple[datetime, ...],
    tuple[float, ...],
    tuple[float, ...],
]:
    """
    Align observations strictly by identical timestamps.

    Missing timestamps are not fabricated and unmatched observations
    are not positionally paired.
    """
    company_map = {
        _utc_timestamp(timestamp): float(value)
        for timestamp, value in company_observations.items()
    }

    market_map = {
        _utc_timestamp(timestamp): float(value)
        for timestamp, value in market_observations.items()
    }

    common = sorted(
        set(company_map).intersection(market_map)
    )

    company_values = tuple(
        company_map[timestamp]
        for timestamp in common
    )

    market_values = tuple(
        market_map[timestamp]
        for timestamp in common
    )

    return (
        tuple(common),
        company_values,
        market_values,
    )


def calculate_market_relationship(
    company_observations: Iterable[tuple[datetime, float]]
    | Sequence[float],
    market_observations: Iterable[tuple[datetime, float]]
    | Sequence[float],
    *,
    company: str = "",
    market: str = "",
    benchmark_observations: Iterable[tuple[datetime, float]] | None = None,
) -> RelationshipResult:
    """
    Calculate the relationship between company and market observations.

    Preferred API:
        timestamped observations

    Example:
        calculate_market_relationship(
            company_observations=[
                (datetime(..., tzinfo=timezone.utc), 0.01),
                ...
            ],
            market_observations=[
                (datetime(..., tzinfo=timezone.utc), 0.02),
                ...
            ],
            company="TITAN",
            market="GOLD",
        )

    Legacy API:
        numeric sequences remain supported for backward compatibility.
    """

    company_is_timestamped = (
        not isinstance(company_observations, Sequence)
        or (
            len(company_observations) > 0
            and isinstance(company_observations[0], tuple)
        )
    )

    market_is_timestamped = (
        not isinstance(market_observations, Sequence)
        or (
            len(market_observations) > 0
            and isinstance(market_observations[0], tuple)
        )
    )

    if company_is_timestamped != market_is_timestamped:
        raise ValueError(
            "company and market observations must use the same format"
        )

    if company_is_timestamped:
        company_map = _validate_timestamped_values(
            company_observations,  # type: ignore[arg-type]
            name="company",
        )

        market_map = _validate_timestamped_values(
            market_observations,  # type: ignore[arg-type]
            name="market",
        )

        timestamps, company_values, market_values = (
            _timestamp_alignment(
                company_map,
                market_map,
            )
        )

        company_mean = (
            sum(company_values) / len(company_values)
            if company_values
            else None
        )

        market_mean = (
            sum(market_values) / len(market_values)
            if market_values
            else None
        )

        excess_mean = (
            company_mean - market_mean
            if company_mean is not None
            and market_mean is not None
            else None
        )

        result = RelationshipResult(
            market=market,
            company=company,
            correlation=_pearson(
                company_values,
                market_values,
            ),
            sample_size=len(timestamps),
            aligned_timestamps=timestamps,
            company_mean_return=company_mean,
            market_mean_return=market_mean,
            excess_mean_return=excess_mean,
            calculation_method=(
                "timestamp_intersection_pearson"
            ),
            causation_claim=False,
        )

        result.validate()
        return result

    company_values = _validate_numeric_series(
        company_observations,  # type: ignore[arg-type]
        name="company",
    )

    market_values = _validate_numeric_series(
        market_observations,  # type: ignore[arg-type]
        name="market",
    )

    if len(company_values) != len(market_values):
        raise ValueError(
            "company and market series must have equal length"
        )

    company_mean = (
        sum(company_values) / len(company_values)
        if company_values
        else None
    )

    market_mean = (
        sum(market_values) / len(market_values)
        if market_values
        else None
    )

    excess_mean = (
        company_mean - market_mean
        if company_mean is not None
        and market_mean is not None
        else None
    )

    result = RelationshipResult(
        market=market,
        company=company,
        correlation=_pearson(
            company_values,
            market_values,
        ),
        sample_size=len(company_values),
        aligned_timestamps=tuple(),
        company_mean_return=company_mean,
        market_mean_return=market_mean,
        excess_mean_return=excess_mean,
        calculation_method="positional_pearson_legacy",
        causation_claim=False,
    )

    result.validate()
    return result


def calculate_correlation(
    company_values: Sequence[float],
    market_values: Sequence[float],
) -> float | None:
    """
    Backward-compatible numeric correlation helper.
    """
    company = _validate_numeric_series(
        company_values,
        name="company",
    )

    market = _validate_numeric_series(
        market_values,
        name="market",
    )

    if len(company) != len(market):
        raise ValueError(
            "company and market series must have equal length"
        )

    return _pearson(company, market)


def calculate_timestamped_correlation(
    company_observations: Iterable[tuple[datetime, float]],
    market_observations: Iterable[tuple[datetime, float]],
) -> RelationshipResult:
    """
    Convenience API for timestamp-aware relationship calculation.
    """
    return calculate_market_relationship(
        company_observations,
        market_observations,
    )


__all__ = [
    "RelationshipResult",
    "calculate_market_relationship",
    "calculate_correlation",
    "calculate_timestamped_correlation",
]
