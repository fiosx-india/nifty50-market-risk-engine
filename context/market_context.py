"""Shared evidence context for the research engine.

CentralBrain remains the only orchestration layer. MarketContext stores
timestamped evidence and conflicts; it does not calculate relationships,
generate predictions, or make trading decisions.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Mapping


@dataclass(frozen=True)
class EvidenceEnvelope:
    """Common auditable envelope for evidence entering MarketContext."""

    evidence_id: str
    evidence_type: str
    symbol: str = ""
    market: str = ""
    timeframe: str = ""
    timestamp_window: tuple[Any, Any] | None = None
    as_of: datetime | None = None
    source: str = ""
    metric: str = ""
    value: Any = None
    unit: str = ""
    calculation_method: str = ""
    lag: int | None = None
    sample_size: int | None = None
    aligned_count: int | None = None
    missing_count: int | None = None
    data_quality: str = ""
    data_freshness: str = ""
    status: str = ""
    limitations: tuple[str, ...] = ()
    causation_claim: bool = False
    provenance: Mapping[str, Any] = field(default_factory=dict)

    def validate(self) -> bool:
        if not self.evidence_id.strip():
            raise ValueError("evidence_id must not be empty")
        if not self.evidence_type.strip():
            raise ValueError("evidence_type must not be empty")
        if self.lag is not None and self.lag < 0:
            raise ValueError("lag cannot be negative")
        if self.sample_size is not None and self.sample_size < 0:
            raise ValueError("sample_size cannot be negative")
        if self.aligned_count is not None and self.aligned_count < 0:
            raise ValueError("aligned_count cannot be negative")
        if self.missing_count is not None and self.missing_count < 0:
            raise ValueError("missing_count cannot be negative")
        return True


@dataclass
class MarketContext:
    """Shared mutable evidence context owned by the orchestration layer."""

    symbol: str
    timestamp: str | datetime
    market_observations: dict = field(default_factory=dict)
    company_observations: dict = field(default_factory=dict)
    technical_evidence: dict = field(default_factory=dict)
    pattern_evidence: dict = field(default_factory=dict)
    global_evidence: dict = field(default_factory=dict)
    relationship_evidence: list = field(default_factory=list)
    news_evidence: list = field(default_factory=list)
    conflicts: list = field(default_factory=list)

    def add_evidence(self, evidence: EvidenceEnvelope):
        evidence.validate()
        self.relationship_evidence.append(evidence)
        return evidence

    def add_relationship_evidence(self, evidence):
        """Backward-compatible relationship evidence writer."""
        if isinstance(evidence, EvidenceEnvelope):
            return self.add_evidence(evidence)
        self.relationship_evidence.append(dict(evidence))
        return evidence

    def add_news_evidence(self, evidence):
        if isinstance(evidence, EvidenceEnvelope):
            evidence.validate()
            self.news_evidence.append(evidence)
        else:
            self.news_evidence.append(dict(evidence))
        return evidence

    def add_conflict(self, evidence):
        if isinstance(evidence, EvidenceEnvelope):
            evidence.validate()
            self.conflicts.append(evidence)
        else:
            self.conflicts.append(dict(evidence))
        return evidence

    def add_technical_evidence(self, evidence):
        self.technical_evidence[str(len(self.technical_evidence))] = evidence
        return evidence

    def add_pattern_evidence(self, evidence):
        self.pattern_evidence[str(len(self.pattern_evidence))] = evidence
        return evidence

    def add_global_evidence(self, evidence):
        self.global_evidence[str(len(self.global_evidence))] = evidence
        return evidence

    def to_snapshot(self) -> dict[str, Any]:
        """Return a serializable snapshot without calculating new results."""
        return {
            "symbol": self.symbol,
            "timestamp": self.timestamp,
            "market_observations": dict(self.market_observations),
            "company_observations": dict(self.company_observations),
            "technical_evidence": dict(self.technical_evidence),
            "pattern_evidence": dict(self.pattern_evidence),
            "global_evidence": dict(self.global_evidence),
            "relationship_evidence": list(self.relationship_evidence),
            "news_evidence": list(self.news_evidence),
            "conflicts": list(self.conflicts),
        }


__all__ = ["EvidenceEnvelope", "MarketContext"]
