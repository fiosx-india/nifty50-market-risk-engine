from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any
import gzip
import json
import re
import time
import urllib.request

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

MARKET_EXCHANGE = {
    "NIFTY 50": "NSE",
    "NIFTY 50 COMPANY": "NSE",
    "CRUDE OIL": "MCX",
    "NATURAL GAS": "MCX",
    "GOLD": "MCX",
    "SILVER": "MCX",
    "COPPER": "MCX",
    "ALUMINIUM": "MCX",
    "ZINC": "MCX",
    "ELECTRICITY": None,
}

MCX_UNDERLYING = {
    "CRUDE OIL": ("CRUDEOIL", "CRUDE OIL"),
    "NATURAL GAS": ("NATURALGAS", "NATURAL GAS", "NATGAS", "NATGASMINI"),
    "GOLD": ("GOLD",),
    "SILVER": ("SILVER",),
    "COPPER": ("COPPER",),
    "ALUMINIUM": ("ALUMINIUM",),
    "ZINC": ("ZINC",),
}

INSTRUMENT_MASTER_URL = (
    "https://margincalculator.angelone.in/"
    "OpenAPI_File/files/OpenAPIScripMaster.json"
)
INSTRUMENT_MASTER_TTL = timedelta(hours=24)

# Network/API resilience. These are intentionally modest so the UI does not
# hang for a long time when Angel One is unavailable.
API_RETRIES = 3
API_RETRY_BACKOFF_SECONDS = 1.5
INSTRUMENT_MASTER_TIMEOUT_SECONDS = 20


def _normalize_market(value: str | None) -> str:
    return " ".join(str(value or "").strip().upper().split())


def _normalize_symbol(value: str | None) -> str:
    return str(value or "").strip()


def _interval_delta(interval: str) -> timedelta:
    return {
        "1m": timedelta(minutes=1),
        "3m": timedelta(minutes=3),
        "5m": timedelta(minutes=5),
        "10m": timedelta(minutes=10),
        "15m": timedelta(minutes=15),
        "30m": timedelta(minutes=30),
        "1H": timedelta(hours=1),
        "1D": timedelta(days=1),
    }[interval]


class AngelOneHistoricalProvider:

    name = "angel_one"
    version = "4.1.0"

    def __init__(
        self,
        api_key: str,
        client_code: str,
        pin: str,
        totp_secret: str,
    ):
        self.api_key = str(api_key).strip()
        self.client_code = str(client_code).strip()
        self.pin = str(pin).strip()
        self.totp_secret = str(totp_secret).strip()

        if not all((self.api_key, self.client_code, self.pin, self.totp_secret)):
            raise ValueError(
                "Angel One api_key, client_code, pin and totp_secret are required"
            )

        self.smart_api = SmartConnect(api_key=self.api_key)
        self._instrument_cache: dict[tuple[str, str], tuple[str, str, str]] = {}
        self._instrument_master: list[dict[str, Any]] = []
        self._instrument_master_loaded_at: datetime | None = None
        self.session: dict[str, Any] = {}
        self.feed_token: str | None = None

        self._login()

    # ------------------------------------------------------------------
    # SAFE ERROR / RETRY HELPERS
    # ------------------------------------------------------------------

    @staticmethod
    def _safe_error(exc: Exception) -> str:
        """Return an error without exposing request headers, tokens or secrets."""
        return type(exc).__name__

    @staticmethod
    def _response_message(response: Any, fallback: str) -> str:
        if not isinstance(response, dict):
            return fallback
        message = response.get("message")
        errorcode = response.get("errorcode")
        if message and errorcode:
            return f"{message} [{errorcode}]"
        if message:
            return str(message)
        return fallback

    def _call_with_retry(
        self,
        operation: str,
        fn,
        *,
        retries: int = API_RETRIES,
    ):
        last_exc: Exception | None = None

        for attempt in range(1, retries + 1):
            try:
                return fn()
            except Exception as exc:
                last_exc = exc
                if attempt >= retries:
                    raise RuntimeError(
                        f"Angel One {operation} request failed after "
                        f"{retries} attempts: {self._safe_error(exc)}"
                    ) from exc
                time.sleep(API_RETRY_BACKOFF_SECONDS * attempt)

        raise RuntimeError(
            f"Angel One {operation} request failed: "
            f"{self._safe_error(last_exc) if last_exc else 'UnknownError'}"
        )

    # ------------------------------------------------------------------
    # AUTHENTICATION
    # ------------------------------------------------------------------

    def _login(self) -> None:
        try:
            totp = pyotp.TOTP(self.totp_secret).now()
            response = self._call_with_retry(
                "authentication",
                lambda: self.smart_api.generateSession(
                    self.client_code,
                    self.pin,
                    totp,
                ),
            )
        except Exception as exc:
            if isinstance(exc, RuntimeError):
                raise
            raise RuntimeError(
                "Angel One authentication request failed: "
                f"{self._safe_error(exc)}"
            ) from exc

        if not isinstance(response, dict):
            raise RuntimeError("Angel One authentication returned an invalid response.")

        if response.get("status") is not True:
            raise RuntimeError(
                "Angel One login failed: "
                f"{self._response_message(response, 'Authentication failed')}"
            )

        self.session = response.get("data") or {}
        if not self.session:
            raise RuntimeError(
                "Angel One login succeeded but returned no session data."
            )

        try:
            self.feed_token = self.smart_api.getfeedToken()
        except Exception as exc:
            raise RuntimeError(
                "Angel One feed-token request failed: "
                f"{self._safe_error(exc)}"
            ) from exc

        if not self.session.get("jwtToken"):
            raise RuntimeError("Angel One login succeeded without jwtToken.")
        if not self.feed_token:
            raise RuntimeError("Angel One login succeeded without feedToken.")

    # ------------------------------------------------------------------
    # MARKET / EXCHANGE
    # ------------------------------------------------------------------

    @staticmethod
    def _exchange_for_market(market: str) -> str:
        normalized = _normalize_market(market)
        exchange = MARKET_EXCHANGE.get(normalized)

        if exchange:
            return exchange

        if normalized == "ELECTRICITY":
            raise ValueError(
                "Electricity is tracked by the application, but no Angel One "
                "instrument/token mapping is configured. No token will be fabricated."
            )

        raise ValueError(
            f"Angel One exchange is not configured for market '{market}'. "
            f"Supported markets: {', '.join(MARKET_EXCHANGE.keys())}"
        )

    # ------------------------------------------------------------------
    # INSTRUMENT MASTER
    # ------------------------------------------------------------------

    def _load_instrument_master(self, force: bool = False) -> list[dict[str, Any]]:
        now = datetime.utcnow()

        if (
            not force
            and self._instrument_master
            and self._instrument_master_loaded_at
            and now - self._instrument_master_loaded_at < INSTRUMENT_MASTER_TTL
        ):
            return self._instrument_master

        request = urllib.request.Request(
            INSTRUMENT_MASTER_URL,
            headers={"User-Agent": "NIFTY50-Market-Risk-Engine/4.1"},
        )

        try:
            with urllib.request.urlopen(
                request,
                timeout=INSTRUMENT_MASTER_TIMEOUT_SECONDS,
            ) as response:
                raw = response.read()
                encoding = response.headers.get("Content-Encoding", "").lower()
                if encoding == "gzip":
                    raw = gzip.decompress(raw)
                payload = json.loads(raw.decode("utf-8"))
        except Exception as exc:
            raise RuntimeError(
                "Unable to download Angel One instrument master: "
                f"{self._safe_error(exc)}"
            ) from exc

        if not isinstance(payload, list):
            raise RuntimeError("Angel One instrument master returned an invalid format.")

        cleaned = [row for row in payload if isinstance(row, dict)]
        if not cleaned:
            raise RuntimeError("Angel One instrument master is empty.")

        self._instrument_master = cleaned
        self._instrument_master_loaded_at = now
        return cleaned

    # ------------------------------------------------------------------
    # EXPIRY PARSING
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_expiry(value: Any) -> datetime | None:
        if value is None:
            return None
        text = str(value).strip()
        if not text:
            return None

        for fmt in ("%Y-%m-%d", "%d-%b-%Y", "%d%b%Y", "%d/%m/%Y", "%Y/%m/%d"):
            try:
                return datetime.strptime(text, fmt)
            except ValueError:
                continue
        return None

    @staticmethod
    def _expiry_from_trading_symbol(trading_symbol: str) -> datetime | None:
        text = str(trading_symbol or "").upper()
        match = re.search(
            r"(\d{2})(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(\d{2})FUT$",
            text,
        )
        if not match:
            return None

        try:
            return datetime(
                2000 + int(match.group(3)),
                datetime.strptime(match.group(2), "%b").month,
                int(match.group(1)),
            )
        except ValueError:
            return None

    # ------------------------------------------------------------------
    # INSTRUMENT RESOLUTION
    # ------------------------------------------------------------------

    def _resolve_instrument(
        self,
        symbol: str,
        market: str,
    ) -> tuple[str, str, str]:
        requested_symbol = _normalize_symbol(symbol)
        if not requested_symbol:
            raise ValueError("Angel One symbol cannot be empty.")

        normalized_market = _normalize_market(market)
        cache_key = (normalized_market, requested_symbol.upper())

        cached = self._instrument_cache.get(cache_key)
        if cached:
            return cached

        exchange = self._exchange_for_market(normalized_market)

        if normalized_market == "NIFTY 50":
            result = ("NSE", "99926000", "NIFTY")
            self._instrument_cache[cache_key] = result
            return result

        if normalized_market == "NIFTY 50 COMPANY":
            search_symbol = requested_symbol.upper()
            response = self._call_with_retry(
                "NSE symbol search",
                lambda: self.smart_api.searchScrip("NSE", search_symbol),
            )
            return self._select_equity_instrument(
                response, search_symbol, cache_key
            )

        if exchange == "MCX":
            return self._resolve_mcx_instrument(
                requested_symbol, normalized_market, cache_key
            )

        raise ValueError(f"Unsupported Angel One market '{market}'.")

    def _select_equity_instrument(
        self,
        response: Any,
        requested_symbol: str,
        cache_key: tuple[str, str],
    ) -> tuple[str, str, str]:
        if not isinstance(response, dict):
            raise RuntimeError("Angel One symbol search returned an invalid response.")

        if response.get("status") is not True:
            raise RuntimeError(
                "Angel One symbol search failed for "
                f"{requested_symbol}: "
                f"{self._response_message(response, 'Unknown error')}"
            )

        candidates = []
        for row in response.get("data") or []:
            if not isinstance(row, dict):
                continue
            trading_symbol = str(row.get("tradingsymbol") or "").strip()
            token = str(row.get("symboltoken") or "").strip()
            if trading_symbol and token:
                candidates.append(row)

        exact = [
            row for row in candidates
            if str(row.get("tradingsymbol", "")).upper()
            == f"{requested_symbol}-EQ"
        ]

        if not exact:
            raise RuntimeError(
                f"No NSE equity instrument found for {requested_symbol}."
            )

        chosen = exact[0]
        result = (
            "NSE",
            str(chosen["symboltoken"]),
            str(chosen["tradingsymbol"]),
        )
        self._instrument_cache[cache_key] = result
        return result

    # ------------------------------------------------------------------
    # MCX FUTURES RESOLUTION
    # ------------------------------------------------------------------

    def _resolve_mcx_instrument(
        self,
        requested_symbol: str,
        market: str,
        cache_key: tuple[str, str],
    ) -> tuple[str, str, str]:
        aliases = MCX_UNDERLYING.get(market)
        if not aliases:
            raise ValueError(f"No MCX underlying mapping exists for '{market}'.")

        master = self._load_instrument_master()
        futures: list[tuple[datetime, dict[str, Any]]] = []
        today = datetime.utcnow().date()

        for row in master:
            if not isinstance(row, dict):
                continue

            if str(row.get("exch_seg") or "").strip().lower() != "mcx_fo":
                continue

            trading_symbol = str(row.get("symbol") or "").strip()
            token = str(row.get("token") or "").strip()
            if not trading_symbol or not token:
                continue

            upper_symbol = trading_symbol.upper()
            if not upper_symbol.endswith("FUT"):
                continue

            if not any(upper_symbol.startswith(alias.upper()) for alias in aliases):
                continue

            expiry = self._parse_expiry(row.get("expiry"))
            if expiry is None:
                expiry = self._expiry_from_trading_symbol(trading_symbol)
            if expiry is None or expiry.date() < today:
                continue

            futures.append((expiry, row))

        if not futures:
            search_terms = [aliases[0], requested_symbol.upper()]
            search_response = None

            for search_term in search_terms:
                try:
                    response = self._call_with_retry(
                        "MCX symbol search",
                        lambda term=search_term: self.smart_api.searchScrip(
                            "MCX", term
                        ),
                        retries=2,
                    )
                except RuntimeError:
                    continue

                if (
                    isinstance(response, dict)
                    and response.get("status") is True
                    and response.get("data")
                ):
                    search_response = response
                    break

            for row in (search_response or {}).get("data") or []:
                if not isinstance(row, dict):
                    continue

                trading_symbol = str(row.get("tradingsymbol") or "").strip()
                token = str(row.get("symboltoken") or "").strip()
                if not trading_symbol or not token:
                    continue

                upper_symbol = trading_symbol.upper()
                if not upper_symbol.endswith("FUT"):
                    continue

                expiry = self._expiry_from_trading_symbol(trading_symbol)
                if expiry is None or expiry.date() < today:
                    continue

                futures.append(
                    (
                        expiry,
                        {
                            "token": token,
                            "symbol": trading_symbol,
                            "name": market,
                        },
                    )
                )

        if not futures:
            raise RuntimeError(
                f"Angel One has no active futures contract available for {market}."
            )

        futures.sort(key=lambda item: item[0])
        _, chosen = futures[0]

        token = str(
            chosen.get("token") or chosen.get("symboltoken") or ""
        ).strip()
        trading_symbol = str(
            chosen.get("symbol") or chosen.get("tradingsymbol") or ""
        ).strip()

        if not token or not trading_symbol:
            raise RuntimeError(
                f"Angel One returned an invalid active MCX contract for {market}."
            )

        result = ("MCX", token, trading_symbol)
        self._instrument_cache[cache_key] = result
        return result

    # ------------------------------------------------------------------
    # DATETIME
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_dt(value: Any) -> datetime:
        if isinstance(value, datetime):
            return value.replace(tzinfo=None) if value.tzinfo else value

        text = str(value).strip()
        if not text:
            raise ValueError("Date/time value cannot be empty.")

        text = text.replace("Z", "+00:00")
        try:
            dt = datetime.fromisoformat(text)
        except ValueError as exc:
            raise ValueError(f"Invalid date/time value: {value}") from exc

        return dt.replace(tzinfo=None) if dt.tzinfo else dt

    # ------------------------------------------------------------------
    # HISTORICAL DATA
    # ------------------------------------------------------------------

    def fetch(self, request: DataRequest) -> ProviderResult:
        if request.interval not in INTERVALS:
            raise ValueError(
                f"Angel One does not expose {request.interval} directly. "
                f"Supported native intervals: {', '.join(INTERVALS)}"
            )

        exchange, token, trading_symbol = self._resolve_instrument(
            request.symbol, request.market
        )

        interval, max_days = INTERVALS[request.interval]
        start = self._parse_dt(request.start)
        end = self._parse_dt(request.end)

        if end < start:
            raise ValueError("end must be greater than or equal to start")

        records: list[dict[str, Any]] = []
        cursor = start
        cursor_step = _interval_delta(request.interval)
        chunk_step = timedelta(days=max_days)

        while cursor <= end:
            chunk_end = min(cursor + chunk_step, end)
            params = {
                "exchange": exchange,
                "symboltoken": token,
                "interval": interval,
                "fromdate": cursor.strftime("%Y-%m-%d %H:%M"),
                "todate": chunk_end.strftime("%Y-%m-%d %H:%M"),
            }

            try:
                response = self._call_with_retry(
                    "historical data",
                    lambda: self.smart_api.getCandleData(params),
                )
            except RuntimeError as exc:
                raise RuntimeError(
                    f"Angel One historical data request failed for "
                    f"{request.symbol} ({request.interval}): {exc}"
                ) from exc

            if not isinstance(response, dict):
                raise RuntimeError(
                    "Angel One historical data returned an invalid response."
                )

            if response.get("status") is not True:
                raise RuntimeError(
                    "Angel One historical request failed for "
                    f"{request.symbol}: "
                    f"{self._response_message(response, 'Unknown error')}"
                )

            for row in response.get("data") or []:
                if not isinstance(row, (list, tuple)) or len(row) < 6:
                    continue
                try:
                    records.append(
                        {
                            "timestamp": row[0],
                            "open": float(row[1]),
                            "high": float(row[2]),
                            "low": float(row[3]),
                            "close": float(row[4]),
                            "volume": float(row[5]),
                        }
                    )
                except (TypeError, ValueError):
                    continue

            next_cursor = chunk_end + cursor_step
            if next_cursor <= cursor:
                break
            cursor = next_cursor

        deduped: list[dict[str, Any]] = []
        seen: set[str] = set()

        for record in records:
            timestamp = str(record.get("timestamp"))
            if timestamp in seen:
                continue
            seen.add(timestamp)
            deduped.append(record)

        deduped.sort(key=lambda item: str(item["timestamp"]))

        return ProviderResult(
            symbol=request.symbol,
            source=self.name,
            records=deduped,
        )

    # ------------------------------------------------------------------
    # LTP
    # ------------------------------------------------------------------

    def get_ltp(
        self,
        symbol: str,
        market: str = "NIFTY 50 Company",
    ) -> dict[str, Any]:
        exchange, token, trading_symbol = self._resolve_instrument(symbol, market)

        try:
            response = self._call_with_retry(
                "LTP",
                lambda: self.smart_api.getMarketData(
                    "LTP",
                    {"exchange": [token]},
                ),
            )
        except RuntimeError as exc:
            raise RuntimeError(
                f"Angel One LTP request failed for {symbol}: {exc}"
            ) from exc

        if not isinstance(response, dict):
            raise RuntimeError("Angel One LTP returned an invalid response.")

        if response.get("status") is not True:
            raise RuntimeError(
                "Angel One LTP request failed for "
                f"{symbol}: "
                f"{self._response_message(response, 'Unknown error')}"
            )

        fetched = (response.get("data") or {}).get("fetched") or []
        if not fetched:
            raise RuntimeError(f"Angel One returned no LTP for {symbol}.")

        result = dict(fetched[0])
        result.setdefault("symbol", trading_symbol)
        result.setdefault("exchange", exchange)
        result.setdefault("symbol_token", token)
        return result

    # ------------------------------------------------------------------
    # HEALTH
    # ------------------------------------------------------------------

    def health(self) -> dict[str, Any]:
        return {
            "provider": self.name,
            "version": self.version,
            "authenticated": bool(self.session.get("jwtToken")),
            "feed_token": bool(self.feed_token),
            "instrument_master_loaded": bool(self._instrument_master),
            "instrument_master_age_hours": (
                (
                    datetime.utcnow() - self._instrument_master_loaded_at
                ).total_seconds() / 3600
                if self._instrument_master_loaded_at
                else None
            ),
            "cached_instruments": len(self._instrument_cache),
        }
