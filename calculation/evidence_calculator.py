"""Auditable evidence records for the shared Market Context.

This module stores calculated observations and their provenance. It does not
calculate correlations, infer causation, generate signals, or rank outcomes.

The evidence envelope is intentionally provider-neutral so downstream
relationship, historical, global-effect, news/event, and orchestration layers
can consume one consistent record.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class EvidenceRecord:
    """Immutable, auditable analytical evidence."""

    symbol: str
    market: str
    timeframe: str
    metric: str
    value: Any
    sample_size: int
    source: str
    methodology: str

    # Timestamp/provenance fields.
    timestamp_window: Any = None
    calculation_method: str = "unspecified"
    lag: int | None = None
    data_quality: str = "unknown"
    data_freshness: str = "unknown"

    # Analytical status / limitations.
    causation_claim: bool = False
    status: str = "observed"
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not isinstance(self.symbol, str) or not self.symbol.strip():
            raise ValueError("symbol must be a non-empty string")

        if not isinstance(self.market, str) or not self.market.strip():
            raise ValueError("market must be a non-empty string")

        if not isinstance(self.timeframe, str) or not self.timeframe.strip():
            raise ValueError("timeframe must be a non-empty string")

        if not isinstance(self.metric, str) or not self.metric.strip():
            raise ValueError("metric must be a non-empty string")

        if not isinstance(self.sample_size, int):
            raise ValueError("sample_size must be an integer")

        if self.sample_size < 0:
            raise ValueError("sample_size must be >= 0")

        if self.lag is not None:
            if not isinstance(self.lag, int):
                raise ValueError("lag must be an integer or None")
            if self.lag < 0:
                raise ValueError("lag must be >= 0")

        if not isinstance(self.causation_claim, bool):
            raise ValueError("causation_claim must be boolean")

        if not isinstance(self.limitations, tuple):
            raise ValueError("limitations must be a tuple")

    def as_dict(self) -> dict[str, Any]:
        """Return a serializable evidence envelope."""
        return {
            "symbol": self.symbol,
            "market": self.market,
            "timeframe": self.timeframe,
            "metric": self.metric,
            "value": self.value,
            "sample_size": self.sample_size,
            "source": self.source,
            "methodology": self.methodology,
            "timestamp_window": self.timestamp_window,
            "calculation_method": self.calculation_method,
            "lag": self.lag,
            "data_quality": self.data_quality,
            "data_freshness": self.data_freshness,
            "causation_claim": self.causation_claim,
            "status": self.status,
            "limitations": self.limitations,
        }


def build_evidence(
    *,
    symbol: str,
    market: str,
    timeframe: str,
    metric: str,
    value: Any,
    sample_size: int,
    source: str,
    methodology: str,
    timestamp_window: Any = None,
    calculation_method: str = "unspecified",
    lag: int | None = None,
    data_quality: str = "unknown",
    data_freshness: str = "unknown",
    causation_claim: bool = False,
    status: str = "observed",
    limitations: tuple[str, ...] = (),
) -> EvidenceRecord:
    """Construct a validated immutable evidence record."""
    return EvidenceRecord(
        symbol=symbol,
        market=market,
        timeframe=timeframe,
        metric=metric,
        value=value,
        sample_size=sample_size,
        source=source,
        methodology=methodology,
        timestamp_window=timestamp_window,
        calculation_method=calculation_method,
        lag=lag,
        data_quality=data_quality,
        data_freshness=data_freshness,
        causation_claim=causation_claim,
        status=status,
        limitations=limitations,
    )


__all__ = ["EvidenceRecord", "build_evidence"]
