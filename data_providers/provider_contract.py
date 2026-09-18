"""Contracts for provider-neutral historical market data.

These contracts describe requests/results only. They intentionally contain no
vendor-specific symbols, API calls, trading decisions, or calculated outcomes.
"""

from dataclasses import dataclass
from typing import Any, Mapping, Protocol, Sequence


@dataclass(frozen=True)
class DataRequest:
    """Canonical request passed from the engine to a historical provider."""

    symbol: str
    start: str
    end: str
    interval: str = "1d"
    market: str = ""

    def __post_init__(self):
        if not isinstance(self.symbol, str) or not self.symbol.strip():
            raise ValueError("symbol must be a non-empty string")
        if self.start is None or self.end is None:
            raise ValueError("start and end are required")
        if not isinstance(self.interval, str) or not self.interval.strip():
            raise ValueError("interval must be a non-empty string")
        if not isinstance(self.market, str):
            raise TypeError("market must be a string")


@dataclass(frozen=True)
class ProviderResult:
    """Provider response before normalization.

    ``records`` must preserve the provider's observation membership. The
    normalizer is responsible for canonical timestamp/OHLCV validation.
    """

    symbol: str
    source: str
    records: Sequence[Mapping[str, Any]]
    status: str = "ok"
    error: str = ""

    def __post_init__(self):
        if not isinstance(self.symbol, str) or not self.symbol.strip():
            raise ValueError("symbol must be a non-empty string")
        if not isinstance(self.source, str) or not self.source.strip():
            raise ValueError("source must be a non-empty string")
        if self.records is None:
            raise ValueError("records must not be None")
        if not isinstance(self.status, str) or not self.status.strip():
            raise ValueError("status must be a non-empty string")
        if not isinstance(self.error, str):
            raise TypeError("error must be a string")


class HistoricalProvider(Protocol):
    """Structural interface implemented by a concrete data provider."""

    name: str

    def fetch(self, request: DataRequest) -> ProviderResult:
        """Fetch observations for the exact request without analytical changes."""
        ...
