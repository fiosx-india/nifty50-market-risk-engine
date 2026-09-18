"""Provider-neutral historical data facade.

This module owns the boundary around a concrete provider. It does not implement
vendor-specific API calls and does not invent symbols. Raw provider output can
be requested with ``fetch``; timestamp-aware normalization is explicitly
available through ``fetch_normalized``.
"""

from .data_normalizer import normalize_records
from .provider_contract import DataRequest, ProviderResult


class HistoricalDataProvider:
    """Small facade that validates provider boundaries.

    The supplied provider must expose ``fetch(request)`` and return a
    ``ProviderResult``. The raw ``fetch`` API is preserved for compatibility.
    """

    def __init__(self, provider):
        if provider is None or not callable(getattr(provider, "fetch", None)):
            raise TypeError("provider must expose fetch(request)")
        self.provider = provider

    @staticmethod
    def _validate_request(symbol, start, end, interval, market):
        if not isinstance(symbol, str) or not symbol.strip():
            raise ValueError("symbol must be a non-empty string")
        if start is None or end is None:
            raise ValueError("start and end are required")
        if not isinstance(interval, str) or not interval.strip():
            raise ValueError("interval must be a non-empty string")
        if market is not None and not isinstance(market, str):
            raise TypeError("market must be a string")

    @staticmethod
    def _validate_result(result):
        if not isinstance(result, ProviderResult):
            raise TypeError("provider.fetch() must return ProviderResult")
        if not isinstance(result.symbol, str) or not result.symbol.strip():
            raise ValueError("ProviderResult.symbol must be a non-empty string")
        if not isinstance(result.source, str) or not result.source.strip():
            raise ValueError("ProviderResult.source must be a non-empty string")
        if result.records is None:
            raise ValueError("ProviderResult.records must not be None")
        return result

    def fetch(self, symbol, start, end, interval="1d", market=""):
        """Fetch raw provider records without sorting, filling, or truncating."""
        self._validate_request(symbol, start, end, interval, market)
        request = DataRequest(symbol, start, end, interval, market or "")
        result = self.provider.fetch(request)
        return self._validate_result(result)

    def fetch_normalized(self, symbol, start, end, interval="1d", market=""):
        """Fetch and normalize records using the canonical timestamp-aware layer."""
        result = self.fetch(symbol, start, end, interval, market)
        normalized = normalize_records(result.records)
        return ProviderResult(
            symbol=result.symbol,
            source=result.source,
            records=normalized,
            status=result.status,
            error=result.error,
        )
