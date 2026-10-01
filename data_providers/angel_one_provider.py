from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import pyotp
from SmartApi import SmartConnect

from .provider_contract import DataRequest, ProviderResult


INTERVALS = {
    "1m": ("ONE_MINUTE", 30),
    "3m": ("THREE_MINUTE", 60),
    "5m": ("FIVE_MINUTE", 100),
    "10m": ("TEN_MINUTE", 100),
    "15m": ("FIFTEEN_MINUTE", 200),
    "30m": ("THIRTY_MINUTE", 200),
    "1H": ("ONE_HOUR", 400),
    "1D": ("ONE_DAY", 2000),
}


class AngelOneHistoricalProvider:
    """Concrete Angel One SmartAPI adapter behind the provider-neutral contract.

    This class owns authentication, instrument resolution, historical candles,
    and LTP retrieval. It does not calculate indicators or make decisions.
    """

    name = "angel_one"

    def __init__(self, api_key: str, client_code: str, pin: str, totp_secret: str):
        self.api_key = str(api_key).strip()
        self.client_code = str(client_code).strip()
        self.pin = str(pin).strip()
        self.totp_secret = str(totp_secret).strip()
        if not all((self.api_key, self.client_code, self.pin, self.totp_secret)):
            raise ValueError(
                "Angel One api_key, client_code, pin and totp_secret are required"
            )
        self.smart_api = SmartConnect(self.api_key)
        self._instrument_cache: dict[tuple[str, str], tuple[str, str]] = {}
        self._login()

    def _login(self) -> None:
        totp = pyotp.TOTP(self.totp_secret).now()
        response = self.smart_api.generateSession(self.client_code, self.pin, totp)
        if not response or response.get("status") is not True:
            message = (response or {}).get("message", "Angel One login failed")
            errorcode = (response or {}).get("errorcode", "")
            raise RuntimeError(
                f"Angel One login failed: {message} {errorcode}".strip()
            )

    def _resolve_instrument(self, symbol: str, market: str) -> tuple[str, str]:
        cache_key = (market, symbol)
        if cache_key in self._instrument_cache:
            return self._instrument_cache[cache_key]

        if market == "NIFTY 50":
            result = ("NSE", "99926000")
            self._instrument_cache[cache_key] = result
            return result

        if market == "NIFTY 50 Company":
            exchange = "NSE"
            search = symbol
        else:
            raise ValueError(
                "Angel One automatic instrument resolution currently supports "
                "NIFTY 50 companies and the NIFTY 50 index."
            )

        response = self.smart_api.searchScrip(exchange, search)
        if not response or response.get("status") is not True:
            raise RuntimeError(f"Angel One symbol search failed for {symbol}")

        candidates = response.get("data") or []
        exact = [
            item for item in candidates
            if item.get("tradingsymbol") == f"{symbol}-EQ"
        ]
        if not exact:
            exact = [
                item for item in candidates
                if str(item.get("tradingsymbol", "")).endswith("-EQ")
            ]
        if not exact:
            raise RuntimeError(f"No NSE equity instrument found for {symbol}")

        instrument = exact[0]
        result = (exchange, str(instrument["symboltoken"]))
        self._instrument_cache[cache_key] = result
        return result

    @staticmethod
    def _parse_dt(value: Any) -> datetime:
        if isinstance(value, datetime):
            return value.replace(tzinfo=None) if value.tzinfo else value
        text = str(value).strip().replace("Z", "+00:00")
        dt = datetime.fromisoformat(text)
        return dt.replace(tzinfo=None) if dt.tzinfo else dt

    def fetch(self, request: DataRequest) -> ProviderResult:
        if request.interval not in INTERVALS:
            raise ValueError(
                f"Angel One does not expose {request.interval} directly. "
                f"Supported native intervals: {', '.join(INTERVALS)}"
            )

        exchange, token = self._resolve_instrument(request.symbol, request.market)
        interval, max_days = INTERVALS[request.interval]
        start = self._parse_dt(request.start)
        end = self._parse_dt(request.end)
        if end < start:
            raise ValueError("end must be greater than or equal to start")

        records: list[dict[str, Any]] = []
        cursor = start
        step = timedelta(days=max_days)

        while cursor <= end:
            chunk_end = min(cursor + step, end)
            params = {
                "exchange": exchange,
                "symboltoken": token,
                "interval": interval,
                "fromdate": cursor.strftime("%Y-%m-%d %H:%M"),
                "todate": chunk_end.strftime("%Y-%m-%d %H:%M"),
            }
            response = self.smart_api.getCandleData(params)
            if not response or response.get("status") is not True:
                message = (response or {}).get(
                    "message", "Historical data request failed"
                )
                raise RuntimeError(
                    f"Angel One historical request failed: {message}"
                )

            for row in response.get("data") or []:
                if len(row) < 6:
                    continue
                records.append(
                    {
                        "timestamp": row[0],
                        "open": row[1],
                        "high": row[2],
                        "low": row[3],
                        "close": row[4],
                        "volume": row[5],
                    }
                )
            cursor = chunk_end + timedelta(minutes=1)

        return ProviderResult(
            symbol=request.symbol,
            source=self.name,
            records=records,
        )

    def get_ltp(
        self,
        symbol: str,
        market: str = "NIFTY 50 Company",
    ) -> dict[str, Any]:
        exchange, token = self._resolve_instrument(symbol, market)
        response = self.smart_api.getMarketData("LTP", {exchange: [token]})
        if not response or response.get("status") is not True:
            raise RuntimeError(f"Angel One LTP request failed for {symbol}")
        fetched = ((response.get("data") or {}).get("fetched") or [])
        if not fetched:
            raise RuntimeError(f"Angel One returned no LTP for {symbol}")
        return fetched[0]
