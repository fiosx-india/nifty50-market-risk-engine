"""Contracts for historical market-data providers."""
from dataclasses import dataclass
from typing import Any, Mapping, Sequence, Protocol

@dataclass(frozen=True)
class DataRequest:
    symbol: str
    start: str
    end: str
    interval: str = "1d"
    market: str = ""

@dataclass(frozen=True)
class ProviderResult:
    symbol: str
    source: str
    records: Sequence[Mapping[str, Any]]
    status: str = "ok"
    error: str = ""

class HistoricalProvider(Protocol):
    name: str
    def fetch(self, request: DataRequest) -> ProviderResult: ...
