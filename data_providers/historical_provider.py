"""Provider-neutral historical data facade."""
from .provider_contract import DataRequest, ProviderResult

class HistoricalDataProvider:
    def __init__(self, provider):
        if provider is None or not callable(getattr(provider, "fetch", None)):
            raise TypeError("provider must expose fetch(request)")
        self.provider = provider

    def fetch(self, symbol, start, end, interval="1d", market=""):
        request = DataRequest(symbol, start, end, interval, market)
        result = self.provider.fetch(request)
        if not isinstance(result, ProviderResult):
            raise TypeError("provider.fetch() must return ProviderResult")
        return result
