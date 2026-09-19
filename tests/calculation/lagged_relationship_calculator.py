from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from math import isfinite, sqrt
from typing import Iterable, Sequence


@dataclass(frozen=True)
class LaggedRelationshipResult:
    """
    Auditable lagged relationship result.

    Lag semantics:

        lag = 0
            Market[t] -> Company[t]

        lag = 1
            Market[t] -> Company[t+1]

        lag = 2
            Market[t] -> Company[t+2]

    A positive lag therefore represents a forward response
    of the company relative to the market observation.

    This is statistical association only and does not establish causation.
    """

    market: str
    company: str
    lag: int
    correlation: float | None
    sample_size: int
    aligned_timestamps: tuple[datetime, ...]
    market_values: tuple[float, ...]
    company_values: tuple[float, ...]
    calculation_method: str
    causation_claim: bool = False

    def validate(self) -> None:
        if not self.market:
            raise ValueError("market must be non-empty")

        if not self.company:
            raise ValueError("company must be non-empty")

        if not isinstance(self.lag, int):
            raise TypeError("lag must be an integer")

        if self.lag < 0:
            raise ValueError("lag must be non-negative")

        if self.sample_size < 0:
            raise ValueError("sample_size must be non-negative")

        if self.sample_size != len(self.aligned_timestamps):
            raise ValueError(
                "sample_size must equal aligned_timestamps length"
            )

        if len(self.market_values) != self.sample_size:
            raise ValueError(
                "market_values length must equal sample_size"
            )

        if len(self.company_values) != self.sample_size:
            raise ValueError(
                "company_values length must equal sample_size"
            )

        previous: datetime | None = None

        for timestamp in self.aligned_timestamps:
            if not isinstance(timestamp, datetime):
                raise TypeError(
                    "timestamps must be datetime objects"
                )

            if timestamp.tzinfo is None or timestamp.utcoffset() is None:
                raise ValueError(
                    "timestamp must be timezone-aware UTC timestamp"
                )

            normalized = timestamp.astimezone(timezone.utc)

            if normalized != timestamp:
                raise ValueError(
                    "timestamps must be normalized to UTC"
                )

            if previous is not None and timestamp <= previous:
                raise ValueError(
                    "aligned timestamps must be strictly increasing"
                )

            previous = timestamp

        for value in self.market_values:
            if not isfinite(float(value)):
                raise ValueError(
                    "market values must be finite"
                )

        for value in self.company_values:
            if not isfinite(float(value)):
                raise ValueError(
                    "company values must be finite"
                )

        if self.correlation is not None:
            if not isfinite(float(self.correlation)):
                raise ValueError(
                    "correlation must be finite"
                )

        if self.causation_claim:
            raise ValueError(
                "LaggedRelationshipResult must not claim causation"
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


def _validate_timestamped_observations(
    observations: Iterable[tuple[datetime, float]],
    *,
    name: str,
) -> dict[datetime, float]:
    """
    Validate timestamped observations.

    Duplicate timestamps are rejected.
    Missing observations are not filled.
    Observations are not silently discarded.
    """
    result: dict[datetime, float] = {}

    for timestamp, value in observations:
        normalized = _utc_timestamp(timestamp)

        numeric = float(value)

        if not isfinite(numeric):
            raise ValueError(
                f"{name} values must be finite"
            )

        if normalized in result:
            raise ValueError(
                f"duplicate timestamp in {name}: "
                f"{normalized.isoformat()}"
            )

        result[normalized] = numeric

    return result


def _pearson(
    x: Sequence[float],
    y: Sequence[float],
) -> float | None:
    """
    Calculate Pearson correlation.

    Returns None when:
    - fewer than two observations exist
    - either series has zero variance
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

    denominator = sqrt(
        variance_x * variance_y
    )

    if denominator == 0:
        return None

    return numerator / denominator


def _detect_timestamped_input(
    observations: object,
) -> bool:
    """
    Detect whether input is timestamped observations.

    Empty sequences are treated as numeric legacy input.
    """
    if not isinstance(observations, Sequence):
        return True

    if len(observations) == 0:
        return False

    first = observations[0]

    return (
        isinstance(first, tuple)
        and len(first) == 2
    )


def _build_timestamp_pairs(
    market_map: dict[datetime, float],
    company_map: dict[datetime, float],
    lag: int,
) -> tuple[
    tuple[datetime, ...],
    tuple[float, ...],
    tuple[float, ...],
]:
    """
    Build lagged pairs using timestamp identity.

    For lag=0:
        market[t] -> company[t]

    For lag>0:
        market[t] -> company[t+lag]

    IMPORTANT:
    The returned timestamp represents the company-side timestamp.

    Example:

        market:
            2026-01-01 -> 10

        company:
            2026-01-02 -> 20

        lag=1

    produces:

        aligned_timestamp = 2026-01-02
        market_value      = 10
        company_value     = 20
    """
    market_times = sorted(market_map)
    company_times = set(company_map)

    aligned_timestamps: list[datetime] = []
    market_values: list[float] = []
    company_values: list[float] = []

    if lag == 0:
        for timestamp in market_times:
            if timestamp not in company_times:
                continue

            aligned_timestamps.append(timestamp)
            market_values.append(market_map[timestamp])
            company_values.append(company_map[timestamp])

        return (
            tuple(aligned_timestamps),
            tuple(market_values),
            tuple(company_values),
        )

    # Positive lag uses observation-step semantics.
    #
    # Market observation at index i is paired with company
    # observation at index i + lag.
    #
    # This deliberately does NOT invent timestamps.
    company_sorted_times = sorted(company_map)

    company_index = {
        timestamp: index
        for index, timestamp
        in enumerate(company_sorted_times)
    }

    for market_index, market_timestamp in enumerate(market_times):
        target_index = market_index + lag

        if target_index >= len(company_sorted_times):
            break

        company_timestamp = company_sorted_times[target_index]

        # Preserve exact observation ordering while still using
        # real timestamps from the company series.
        if company_timestamp not in company_index:
            continue

        aligned_timestamps.append(company_timestamp)
        market_values.append(market_map[market_timestamp])
        company_values.append(company_map[company_timestamp])

    return (
        tuple(aligned_timestamps),
        tuple(market_values),
        tuple(company_values),
    )


def calculate_lagged_relationship(
    market_observations: Iterable[tuple[datetime, float]]
    | Sequence[float],
    company_observations: Iterable[tuple[datetime, float]]
    | Sequence[float],
    lag: int = 0,
    *,
    market: str = "",
    company: str = "",
) -> LaggedRelationshipResult:
    """
    Calculate a market/company relationship at a specified lag.

    Preferred timestamp-aware API:

        calculate_lagged_relationship(
            market_observations,
            company_observations,
            lag=1,
            market="GOLD",
            company="TITAN",
        )

    Semantics:

        lag=0:
            Market[t] -> Company[t]

        lag=1:
            Market[t] -> Company[t+1]

        lag=2:
            Market[t] -> Company[t+2]

    Positive lag means the market observation precedes the
    company observation by the specified observation step.

    This function does not claim causation.
    """
    if not isinstance(lag, int):
        raise TypeError("lag must be an integer")

    if lag < 0:
        raise ValueError(
            "lag must be non-negative"
        )

    market_is_timestamped = _detect_timestamped_input(
        market_observations
    )

    company_is_timestamped = _detect_timestamped_input(
        company_observations
    )

    if market_is_timestamped != company_is_timestamped:
        raise ValueError(
            "market and company observations must use the same format"
        )

    if market_is_timestamped:
        market_map = _validate_timestamped_observations(
            market_observations,  # type: ignore[arg-type]
            name="market",
        )

        company_map = _validate_timestamped_observations(
            company_observations,  # type: ignore[arg-type]
            name="company",
        )

        (
            aligned_timestamps,
            market_values,
            company_values,
        ) = _build_timestamp_pairs(
            market_map,
            company_map,
            lag,
        )

        result = LaggedRelationshipResult(
            market=market,
            company=company,
            lag=lag,
            correlation=_pearson(
                market_values,
                company_values,
            ),
            sample_size=len(aligned_timestamps),
            aligned_timestamps=aligned_timestamps,
            market_values=market_values,
            company_values=company_values,
            calculation_method=(
                "timestamped_observation_step_lag_pearson"
            ),
            causation_claim=False,
        )

        result.validate()

        return result

    market_values = tuple(
        float(value)
        for value in market_observations  # type: ignore[arg-type]
    )

    company_values = tuple(
        float(value)
        for value in company_observations  # type: ignore[arg-type]
    )

    for value in market_values:
        if not isfinite(value):
            raise ValueError(
                "market values must be finite"
            )

    for value in company_values:
        if not isfinite(value):
            raise ValueError(
                "company values must be finite"
            )

    if lag >= len(market_values):
        aligned_market = ()
        aligned_company = ()
    else:
        end = len(market_values) - lag

        aligned_market = market_values[:end]
        aligned_company = company_values[lag:]

        if len(aligned_market) != len(aligned_company):
            raise ValueError(
                "market and company series must have equal length"
            )

    result = LaggedRelationshipResult(
        market=market,
        company=company,
        lag=lag,
        correlation=_pearson(
            aligned_market,
            aligned_company,
        ),
        sample_size=len(aligned_market),
        aligned_timestamps=tuple(),
        market_values=tuple(aligned_market),
        company_values=tuple(aligned_company),
        calculation_method=(
            "positional_observation_step_lag_legacy"
        ),
        causation_claim=False,
    )

    # Legacy numeric results have no timestamps.
    # Validate structural fields manually instead of requiring
    # timestamp count == sample size.
    if result.sample_size < 0:
        raise ValueError(
            "sample_size must be non-negative"
        )

    if result.causation_claim:
        raise ValueError(
            "LaggedRelationshipResult must not claim causation"
        )

    return result


def calculate_lagged_correlation(
    market_values: Sequence[float],
    company_values: Sequence[float],
    lag: int = 0,
) -> float | None:
    """
    Backward-compatible numeric lagged correlation helper.
    """
    result = calculate_lagged_relationship(
        market_values,
        company_values,
        lag=lag,
    )

    return result.correlation


__all__ = [
    "LaggedRelationshipResult",
    "calculate_lagged_relationship",
    "calculate_lagged_correlation",
      ]
