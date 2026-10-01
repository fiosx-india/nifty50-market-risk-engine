from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any

import pyotp
from SmartApi import SmartConnect

from .provider_contract import DataRequest, ProviderResult


# ---------------------------------------------------------------------------
# ANGEL ONE HISTORICAL API LIMITS
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# CANONICAL MARKET -> EXCHANGE
# ---------------------------------------------------------------------------

MARKET_EXCHANGE = {
    "NIFTY 50": "NSE",
    "NIFTY 50 COMPANY": "NSE",

    # Tracked commodity / energy markets.
    "CRUDE OIL": "MCX",
    "NATURAL GAS": "MCX",
    "GOLD": "MCX",
    "SILVER": "MCX",
    "COPPER": "MCX",
    "ALUMINIUM": "MCX",
    "ZINC": "MCX",
    "ELECTRICITY": "MCX",
}


# ---------------------------------------------------------------------------
# NORMALIZATION HELPERS
# ---------------------------------------------------------------------------

def _normalize_market(value: str | None) -> str:
    return " ".join(str(value or "").strip().upper().split())


def _normalize_symbol(value: str | None) -> str:
    return str(value or "").strip()


def _interval_delta(interval: str) -> timedelta:
    """
    Return the smallest safe cursor step for the requested Angel interval.
    """

    mapping = {
        "1m": timedelta(minutes=1),
        "3m": timedelta(minutes=3),
        "5m": timedelta(minutes=5),
        "10m": timedelta(minutes=10),
        "15m": timedelta(minutes=15),
        "30m": timedelta(minutes=30),
        "1H": timedelta(hours=1),
        "1D": timedelta(days=1),
    }

    return mapping[interval]


# ---------------------------------------------------------------------------
# PROVIDER
# ---------------------------------------------------------------------------

class AngelOneHistoricalProvider:
    """
    Concrete Angel One SmartAPI adapter behind the provider-neutral contract.

    Responsibilities:
        - Angel One authentication
        - market/exchange resolution
        - instrument resolution
        - historical OHLCV candles
        - LTP retrieval

    This class does NOT:
        - calculate indicators
        - generate signals
        - make trading decisions
        - perform business intelligence

    Architecture remains:

        App
          ↓
        HistoricalDataProvider
          ↓
        AngelOneHistoricalProvider
          ↓
        Angel One SmartAPI
    """

    name = "angel_one"
    version = "3.0.0"

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

        if not all(
            (
                self.api_key,
                self.client_code,
                self.pin,
                self.totp_secret,
            )
        ):
            raise ValueError(
                "Angel One api_key, client_code, pin and totp_secret are required"
            )

        self.smart_api = SmartConnect(api_key=self.api_key)

        # (market, symbol) -> (exchange, token, trading_symbol)
        self._instrument_cache: dict[
            tuple[str, str],
            tuple[str, str, str],
        ] = {}

        self.session: dict[str, Any] = {}
        self.feed_token: str | None = None

        self._login()

    # ------------------------------------------------------------------
    # AUTHENTICATION
    # ------------------------------------------------------------------

    def _login(self) -> None:
        """
        Authenticate once during provider initialization.

        Credentials are never logged.
        """

        try:
            totp = pyotp.TOTP(self.totp_secret).now()

            response = self.smart_api.generateSession(
                self.client_code,
                self.pin,
                totp,
            )

        except Exception as exc:
            raise RuntimeError(
                f"Angel One authentication request failed: "
                f"{type(exc).__name__}"
            ) from exc

        if not isinstance(response, dict):
            raise RuntimeError(
                "Angel One authentication returned an invalid response."
            )

        if response.get("status") is not True:
            message = str(
                response.get(
                    "message",
                    "Angel One login failed",
                )
            )

            errorcode = str(
                response.get(
                    "errorcode",
                    "",
                )
            )

            suffix = f" [{errorcode}]" if errorcode else ""

            raise RuntimeError(
                f"Angel One login failed: {message}{suffix}"
            )

        self.session = response.get("data") or {}

        if not self.session:
            raise RuntimeError(
                "Angel One login succeeded but returned no session data."
            )

        self.feed_token = self.smart_api.getfeedToken()

        if not self.session.get("jwtToken"):
            raise RuntimeError(
                "Angel One login succeeded without jwtToken."
            )

        if not self.feed_token:
            raise RuntimeError(
                "Angel One login succeeded without feedToken."
            )

    # ------------------------------------------------------------------
    # MARKET / EXCHANGE RESOLUTION
    # ------------------------------------------------------------------

    @staticmethod
    def _exchange_for_market(market: str) -> str:
        normalized = _normalize_market(market)

        exchange = MARKET_EXCHANGE.get(normalized)

        if exchange:
            return exchange

        raise ValueError(
            "Angel One exchange is not configured for market "
            f"'{market}'. Supported markets: "
            f"{', '.join(MARKET_EXCHANGE.keys())}"
        )

    # ------------------------------------------------------------------
    # INSTRUMENT RESOLUTION
    # ------------------------------------------------------------------

    def _resolve_instrument(
        self,
        symbol: str,
        market: str,
    ) -> tuple[str, str, str]:
        """
        Resolve:

            (exchange, symbol token, trading symbol)

        using Angel One's authenticated Search Scrip API.

        No vendor token is invented for commodities.
        """

        requested_symbol = _normalize_symbol(symbol)

        if not requested_symbol:
            raise ValueError(
                "Angel One symbol cannot be empty."
            )

        normalized_market = _normalize_market(market)

        cache_key = (
            normalized_market,
            requested_symbol.upper(),
        )

        cached = self._instrument_cache.get(cache_key)

        if cached:
            return cached

        exchange = self._exchange_for_market(
            normalized_market
        )

        # --------------------------------------------------------------
        # NIFTY 50 INDEX
        # --------------------------------------------------------------

        if normalized_market == "NIFTY 50":
            result = (
                "NSE",
                "99926000",
                "NIFTY",
            )

            self._instrument_cache[cache_key] = result

            return result

        # --------------------------------------------------------------
        # NIFTY 50 EQUITY / OTHER NSE EQUITIES
        # --------------------------------------------------------------

        if normalized_market == "NIFTY 50 COMPANY":
            search_symbol = requested_symbol.upper()

            response = self.smart_api.searchScrip(
                exchange,
                search_symbol,
            )

            return self._select_instrument(
                response=response,
                requested_symbol=search_symbol,
                exchange=exchange,
                market=normalized_market,
                cache_key=cache_key,
                equity_only=True,
            )

        # --------------------------------------------------------------
        # MCX / TRACKED MARKETS
        # --------------------------------------------------------------

        if exchange == "MCX":
            search_symbol = requested_symbol.upper()

            response = self.smart_api.searchScrip(
                "MCX",
                search_symbol,
            )

            return self._select_instrument(
                response=response,
                requested_symbol=search_symbol,
                exchange="MCX",
                market=normalized_market,
                cache_key=cache_key,
                equity_only=False,
            )

        raise ValueError(
            f"Unsupported Angel One market '{market}'."
        )

    # ------------------------------------------------------------------
    # INSTRUMENT SELECTION
    # ------------------------------------------------------------------

    def _select_instrument(
        self,
        response: Any,
        requested_symbol: str,
        exchange: str,
        market: str,
        cache_key: tuple[str, str],
        equity_only: bool,
    ) -> tuple[str, str, str]:
        """
        Select the best usable instrument returned by Angel One.

        For NSE companies:
            exact SYMBOL-EQ is preferred.

        For MCX:
            exact trading symbol is preferred;
            otherwise matching candidates are considered.

        No token is fabricated.
        """

        if not isinstance(response, dict):
            raise RuntimeError(
                f"Angel One symbol search returned an invalid response "
                f"for {requested_symbol}."
            )

        if response.get("status") is not True:
            message = str(
                response.get(
                    "message",
                    "Angel One symbol search failed",
                )
            )

            raise RuntimeError(
                f"Angel One symbol search failed for "
                f"{requested_symbol}: {message}"
            )

        rows = response.get("data") or []

        candidates: list[dict[str, Any]] = []

        for row in rows:
            if not isinstance(row, dict):
                continue

            trading_symbol = str(
                row.get("tradingsymbol") or ""
            ).strip()

            token = str(
                row.get("symboltoken") or ""
            ).strip()

            if not trading_symbol or not token:
                continue

            candidates.append(row)

        if not candidates:
            raise RuntimeError(
                f"No Angel One instrument found for "
                f"{requested_symbol} on {exchange}."
            )

        requested_upper = requested_symbol.upper()

        # --------------------------------------------------------------
        # NSE EQUITY
        # --------------------------------------------------------------

        if equity_only:

            exact_equity = [
                row
                for row in candidates
                if str(
                    row.get("tradingsymbol", "")
                ).upper()
                == f"{requested_upper}-EQ"
            ]

            if exact_equity:
                chosen = exact_equity[0]

            else:
                equity_candidates = [
                    row
                    for row in candidates
                    if str(
                        row.get("tradingsymbol", "")
                    ).upper().endswith("-EQ")
                ]

                if not equity_candidates:
                    raise RuntimeError(
                        f"No NSE equity instrument found for "
                        f"{requested_symbol}."
                    )

                chosen = equity_candidates[0]

        # --------------------------------------------------------------
        # MCX
        # --------------------------------------------------------------

        else:

            exact = [
                row
                for row in candidates
                if str(
                    row.get("tradingsymbol", "")
                ).upper()
                == requested_upper
            ]

            if exact:
                chosen = exact[0]

            else:
                matching = [
                    row
                    for row in candidates
                    if requested_upper
                    in str(
                        row.get("tradingsymbol", "")
                    ).upper()
                ]

                if not matching:
                    raise RuntimeError(
                        f"Angel One returned instruments for "
                        f"{requested_symbol}, but none matched the "
                        f"requested market instrument."
                    )

                # Prefer instruments that start with the requested
                # underlying symbol.
                starts_with = [
                    row
                    for row in matching
                    if str(
                        row.get("tradingsymbol", "")
                    ).upper().startswith(requested_upper)
                ]

                chosen = (
                    starts_with[0]
                    if starts_with
                    else matching[0]
                )

        trading_symbol = str(
            chosen["tradingsymbol"]
        ).strip()

        token = str(
            chosen["symboltoken"]
        ).strip()

        result = (
            exchange,
            token,
            trading_symbol,
        )

        self._instrument_cache[cache_key] = result

        return result

    # ------------------------------------------------------------------
    # DATETIME
    # ------------------------------------------------------------------

    @staticmethod
    def _parse_dt(value: Any) -> datetime:
        if isinstance(value, datetime):
            if value.tzinfo:
                return value.replace(
                    tzinfo=None
                )

            return value

        text = str(value).strip()

        if not text:
            raise ValueError(
                "Date/time value cannot be empty."
            )

        text = text.replace(
            "Z",
            "+00:00",
        )

        try:
            dt = datetime.fromisoformat(text)

        except ValueError as exc:
            raise ValueError(
                f"Invalid date/time value: {value}"
            ) from exc

        if dt.tzinfo:
            return dt.replace(
                tzinfo=None
            )

        return dt

    # ------------------------------------------------------------------
    # HISTORICAL DATA
    # ------------------------------------------------------------------

    def fetch(
        self,
        request: DataRequest,
    ) -> ProviderResult:

        if request.interval not in INTERVALS:
            raise ValueError(
                f"Angel One does not expose "
                f"{request.interval} directly. "
                f"Supported native intervals: "
                f"{', '.join(INTERVALS)}"
            )

        exchange, token, trading_symbol = (
            self._resolve_instrument(
                request.symbol,
                request.market,
            )
        )

        interval, max_days = INTERVALS[
            request.interval
        ]

        start = self._parse_dt(
            request.start
        )

        end = self._parse_dt(
            request.end
        )

        if end < start:
            raise ValueError(
                "end must be greater than or equal to start"
            )

        records: list[dict[str, Any]] = []

        cursor = start

        cursor_step = _interval_delta(
            request.interval
        )

        chunk_step = timedelta(
            days=max_days
        )

        while cursor <= end:

            chunk_end = min(
                cursor + chunk_step,
                end,
            )

            params = {
                "exchange": exchange,
                "symboltoken": token,
                "interval": interval,
                "fromdate": cursor.strftime(
                    "%Y-%m-%d %H:%M"
                ),
                "todate": chunk_end.strftime(
                    "%Y-%m-%d %H:%M"
                ),
            }

            try:
                response = self.smart_api.getCandleData(
                    params
                )

            except Exception as exc:
                raise RuntimeError(
                    "Angel One historical data request "
                    f"failed for {request.symbol}: "
                    f"{type(exc).__name__}"
                ) from exc

            if not isinstance(response, dict):
                raise RuntimeError(
                    "Angel One historical data returned "
                    "an invalid response."
                )

            if response.get("status") is not True:
                message = str(
                    response.get(
                        "message",
                        "Historical data request failed",
                    )
                )

                raise RuntimeError(
                    f"Angel One historical request failed "
                    f"for {request.symbol}: {message}"
                )

            rows = response.get(
                "data"
            ) or []

            for row in rows:

                if not isinstance(
                    row,
                    (list, tuple),
                ):
                    continue

                if len(row) < 6:
                    continue

                try:
                    record = {
                        "timestamp": row[0],
                        "open": float(row[1]),
                        "high": float(row[2]),
                        "low": float(row[3]),
                        "close": float(row[4]),
                        "volume": float(row[5]),
                    }

                except (
                    TypeError,
                    ValueError,
                ):
                    continue

                records.append(record)

            # Move by one complete candle interval so that the next
            # request does not repeatedly request the same candle.
            next_cursor = (
                chunk_end + cursor_step
            )

            if next_cursor <= cursor:
                break

            cursor = next_cursor

        # --------------------------------------------------------------
        # DEDUPLICATION
        # --------------------------------------------------------------

        deduped: list[dict[str, Any]] = []
        seen: set[str] = set()

        for record in records:

            timestamp = str(
                record.get("timestamp")
            )

            if timestamp in seen:
                continue

            seen.add(timestamp)
            deduped.append(record)

        deduped.sort(
            key=lambda item: str(
                item["timestamp"]
            )
        )

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

        exchange, token, trading_symbol = (
            self._resolve_instrument(
                symbol,
                market,
            )
        )

        try:
            response = self.smart_api.getMarketData(
                "LTP",
                {
                    exchange: [token]
                },
            )

        except Exception as exc:
            raise RuntimeError(
                f"Angel One LTP request failed for "
                f"{symbol}: {type(exc).__name__}"
            ) from exc

        if not isinstance(response, dict):
            raise RuntimeError(
                "Angel One LTP returned an invalid response."
            )

        if response.get("status") is not True:
            message = str(
                response.get(
                    "message",
                    "Angel One LTP request failed",
                )
            )

            raise RuntimeError(
                f"Angel One LTP request failed for "
                f"{symbol}: {message}"
            )

        fetched = (
            (response.get("data") or {})
            .get("fetched")
            or []
        )

        if not fetched:
            raise RuntimeError(
                f"Angel One returned no LTP for "
                f"{symbol}."
            )

        result = dict(
            fetched[0]
        )

        # Preserve canonical identity for downstream layers.
        result.setdefault(
            "symbol",
            trading_symbol,
        )

        result.setdefault(
            "exchange",
            exchange,
        )

        result.setdefault(
            "symbol_token",
            token,
        )

        return result

    # ------------------------------------------------------------------
    # HEALTH
    # ------------------------------------------------------------------

    def health(self) -> dict[str, Any]:
        return {
            "provider": self.name,
            "version": self.version,
            "authenticated": bool(
                self.session.get("jwtToken")
            ),
            "feed_token": bool(
                self.feed_token
            ),
            "cached_instruments": len(
                self._instrument_cache
            ),
        }
