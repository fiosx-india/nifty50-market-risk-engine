from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Iterable, Sequence


@dataclass(frozen=True)
class EvidenceRecord:
    """
    Auditable evidence produced by a calculation.

    This object records what was calculated, on which observations,
    using which method and lag.

    It does not make a trading decision and does not claim causation.
    """

    evidence_id: str
    symbol: str
    market: str
    timestamp_window: tuple[datetime, datetime] | None
    sample_size: int
    calculation_method: str
    lag: int
    metric: str
    value: float | None
    data_quality: str
    causation_claim: bool = False

    def validate(self) -> None:
        if not self.evidence_id:
            raise ValueError("evidence_id must be non-empty")

        if not self.symbol:
            raise ValueError("symbol must be non-empty")

        if not self.market:
            raise ValueError("market must be non-empty")

        if self.sample_size < 0:
            raise ValueError("sample_size must be non-negative")

        if not self.calculation_method:
            raise ValueError(
                "calculation_method must be non-empty"
            )

        if self.lag < 0:
            raise ValueError(
                "lag must be non-negative"
            )

        if not self.metric:
            raise ValueError("metric must be non-empty")

        if not self.data_quality:
            raise ValueError(
                "data_quality must be non-empty"
            )

        if self.timestamp_window is not None:
            if len(self.timestamp_window) != 2:
                raise ValueError(
                    "timestamp_window must contain two timestamps"
                )

            start, end = self.timestamp_window

            _validate_utc_timestamp(start)
            _validate_utc_timestamp(end)

            if end < start:
                raise ValueError(
                    "timestamp_window end must not precede start"
                )

        if self.causation_claim:
            raise ValueError(
                "EvidenceRecord must not claim causation"
            )


def _validate_utc_timestamp(
    timestamp: datetime,
) -> None:
    if not isinstance(timestamp, datetime):
        raise TypeError(
            "timestamp must be a datetime"
        )

    if timestamp.tzinfo is None or timestamp.utcoffset() is None:
        raise ValueError(
            "timestamp must be timezone-aware UTC timestamp"
        )

    if timestamp.astimezone(timezone.utc) != timestamp:
        raise ValueError(
            "timestamp must be normalized to UTC"
        )


def _normalize_timestamps(
    timestamps: Iterable[datetime],
) -> tuple[datetime, ...]:
    result: list[datetime] = []

    for timestamp in timestamps:
        _validate_utc_timestamp(timestamp)
        result.append(timestamp)

    return tuple(result)


def _build_timestamp_window(
    timestamps: Sequence[datetime],
) -> tuple[datetime, datetime] | None:
    if not timestamps:
        return None

    ordered = sorted(timestamps)

    return (
        ordered[0],
        ordered[-1],
    )


def _quality_from_sample_size(
    sample_size: int,
) -> str:
    """
    Descriptive quality classification only.

    This is not a confidence score and must not be interpreted
    as prediction accuracy.
    """
    if sample_size == 0:
        return "no_data"

    if sample_size < 2:
        return "insufficient"

    if sample_size < 30:
        return "limited"

    if sample_size < 100:
        return "moderate"

    return "adequate"


def build_evidence_record(
    *,
    evidence_id: str,
    symbol: str,
    market: str,
    timestamps: Iterable[datetime],
    sample_size: int,
    calculation_method: str,
    lag: int,
    metric: str,
    value: float | None,
    data_quality: str | None = None,
) -> EvidenceRecord:
    """
    Build a validated EvidenceRecord.

    No business decision is made here.
    """

    normalized_timestamps = _normalize_timestamps(
        timestamps
    )

    if sample_size < 0:
        raise ValueError(
            "sample_size must be non-negative"
        )

    if sample_size != len(normalized_timestamps):
        raise ValueError(
            "sample_size must equal timestamp count"
        )

    quality = (
        data_quality
        if data_quality is not None
        else _quality_from_sample_size(sample_size)
    )

    record = EvidenceRecord(
        evidence_id=evidence_id,
        symbol=symbol,
        market=market,
        timestamp_window=_build_timestamp_window(
            normalized_timestamps
        ),
        sample_size=sample_size,
        calculation_method=calculation_method,
        lag=lag,
        metric=metric,
        value=value,
        data_quality=quality,
        causation_claim=False,
    )

    record.validate()

    return record


def evidence_from_relationship(
    *,
    evidence_id: str,
    symbol: str,
    market: str,
    aligned_timestamps: Iterable[datetime],
    correlation: float | None,
    sample_size: int,
    calculation_method: str,
    lag: int = 0,
    data_quality: str | None = None,
) -> EvidenceRecord:
    """
    Convert a relationship calculation into auditable evidence.
    """

    return build_evidence_record(
        evidence_id=evidence_id,
        symbol=symbol,
        market=market,
        timestamps=aligned_timestamps,
        sample_size=sample_size,
        calculation_method=calculation_method,
        lag=lag,
        metric="correlation",
        value=correlation,
        data_quality=data_quality,
    )


def evidence_from_lagged_relationship(
    *,
    evidence_id: str,
    symbol: str,
    market: str,
    aligned_timestamps: Iterable[datetime],
    correlation: float | None,
    sample_size: int,
    calculation_method: str,
    lag: int,
    data_quality: str | None = None,
) -> EvidenceRecord:
    """
    Convert lagged relationship output into auditable evidence.
    """

    if lag < 0:
        raise ValueError(
            "lag must be non-negative"
        )

    return build_evidence_record(
        evidence_id=evidence_id,
        symbol=symbol,
        market=market,
        timestamps=aligned_timestamps,
        sample_size=sample_size,
        calculation_method=calculation_method,
        lag=lag,
        metric="lagged_correlation",
        value=correlation,
        data_quality=data_quality,
    )


def build_evidence_from_result(
    result: object,
    *,
    evidence_id: str,
    symbol: str,
    market: str,
    metric: str = "correlation",
    data_quality: str | None = None,
) -> EvidenceRecord:
    """
    Generic adapter for relationship-like calculation results.

    Required attributes:
        aligned_timestamps
        sample_size
        calculation_method
        lag
        correlation

    This function does not infer business meaning.
    """

    required = (
        "aligned_timestamps",
        "sample_size",
        "calculation_method",
        "lag",
        "correlation",
    )

    missing = [
        name
        for name in required
        if not hasattr(result, name)
    ]

    if missing:
        raise AttributeError(
            "result missing required attributes: "
            + ", ".join(missing)
        )

    return build_evidence_record(
        evidence_id=evidence_id,
        symbol=symbol,
        market=market,
        timestamps=getattr(
            result,
            "aligned_timestamps",
        ),
        sample_size=getattr(
            result,
            "sample_size",
        ),
        calculation_method=getattr(
            result,
            "calculation_method",
        ),
        lag=getattr(
            result,
            "lag",
        ),
        metric=metric,
        value=getattr(
            result,
            "correlation",
        ),
        data_quality=data_quality,
    )


__all__ = [
    "EvidenceRecord",
    "build_evidence_record",
    "evidence_from_relationship",
    "evidence_from_lagged_relationship",
    "build_evidence_from_result",
]
