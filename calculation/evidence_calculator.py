"""Auditable evidence records; no trading decision."""
from dataclasses import dataclass, asdict
from typing import Any

@dataclass(frozen=True)
class EvidenceRecord:
    symbol: str
    market: str
    timeframe: str
    metric: str
    value: Any
    sample_size: int
    source: str
    methodology: str
    data_freshness: str = "unknown"
    causation_claim: bool = False

def build_evidence(symbol, market, timeframe, metric, value, sample_size,
                   source, methodology, data_freshness="unknown"):
    return asdict(EvidenceRecord(
        symbol, market, timeframe, metric, value, int(sample_size),
        source, methodology, data_freshness
    ))
