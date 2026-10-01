
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import sys

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Project path
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Existing architecture: UI -> shared context/orchestration -> pure engines.
from context.market_context import MarketContext
from orchestration.central_brain import CentralBrain
from config.universe import NIFTY50_SYMBOLS, TRACKED_MARKETS
from data_providers.historical_provider import HistoricalDataProvider
from data_providers.angel_one_provider import AngelOneHistoricalProvider

from indicators.technical_indicators import (
    sma, ema, wma, roc, momentum, rsi, atr, bollinger, vwap,
)
from indicators.trend_indicators import adx, supertrend, ichimoku
from indicators.momentum_indicators import (
    stochastic, williams_r, cci, mfi,
)
from indicators.volume_indicators import (
    relative_volume, obv, accumulation_distribution,
    price_volume_confirmation,
)
from indicators.candlestick_patterns import detect_last as detect_candle
from indicators.chart_patterns import structure_snapshot
from indicators.market_structure import market_structure_snapshot


st.set_page_config(
    page_title="NIFTY 50 Market Risk Engine",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("📊 NIFTY 50 Market Risk Engine")
st.caption(
    "Evidence-first market research dashboard • existing engine architecture preserved"
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def normalize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize common CSV column spellings without changing engine modules."""
    aliases = {
        "date": "timestamp",
        "datetime": "timestamp",
        "time": "timestamp",
        "open": "open",
        "high": "high",
        "low": "low",
        "close": "close",
        "adj close": "close",
        "adj_close": "close",
        "volume": "volume",
    }
    rename = {}
    for col in df.columns:
        key = str(col).strip().lower()
        if key in aliases:
            rename[col] = aliases[key]
    out = df.rename(columns=rename).copy()

    required = ["open", "high", "low", "close", "volume"]
    missing = [c for c in required if c not in out.columns]
    if missing:
        raise ValueError(
            "CSV must contain Open, High, Low, Close and Volume columns. "
            f"Missing: {', '.join(missing)}"
        )

    if "timestamp" in out.columns:
        out["timestamp"] = pd.to_datetime(out["timestamp"], errors="coerce")
        out = out.dropna(subset=["timestamp"]).sort_values("timestamp")

    for col in required:
        out[col] = pd.to_numeric(out[col], errors="coerce")

    out = out.dropna(subset=required).reset_index(drop=True)
    if out.empty:
        raise ValueError("No valid OHLCV rows remain after cleaning.")

    if (out["high"] < out["low"]).any():
        raise ValueError("CSV contains rows where High < Low.")
    if ((out["close"] < out["low"]) | (out["close"] > out["high"])).any():
        raise ValueError("CSV contains Close values outside Low/High.")
    if (out["volume"] < 0).any():
        raise ValueError("CSV contains negative Volume.")

    return out


def latest(series):
    if isinstance(series, (list, tuple)) and series:
        return series[-1]
    return series


def fmt(value, digits=4):
    if value is None:
        return "—"
    try:
        if pd.isna(value):
            return "—"
        return f"{float(value):.{digits}f}"
    except Exception:
        return str(value)


def run_indicators(df: pd.DataFrame, period: int):
    o = df["open"].tolist()
    h = df["high"].tolist()
    l = df["low"].tolist()
    c = df["close"].tolist()
    v = df["volume"].tolist()

    result = {}
    # Each calculation is isolated so one optional indicator cannot break
    # the whole dashboard.
    calculations = {
        "SMA": lambda: latest(sma(c, period)),
        "EMA": lambda: latest(ema(c, period)),
        "WMA": lambda: latest(wma(c, period)),
        "RSI": lambda: latest(rsi(c, period)),
        "ROC": lambda: latest(roc(c, period)),
        "Momentum": lambda: latest(momentum(c, period)),
        "ATR": lambda: latest(atr(h, l, c, period)),
        "ADX": lambda: adx(h, l, c, period),
        "Williams %R": lambda: williams_r(h, l, c, period),
        "CCI": lambda: cci(h, l, c, period),
        "MFI": lambda: mfi(h, l, c, period),
        "Relative Volume": lambda: latest(relative_volume(v, period)),
        "OBV": lambda: obv(c, v),
        "A/D": lambda: accumulation_distribution(h, l, c, v),
        "Price/Volume": lambda: price_volume_confirmation(c, v, period),
        "VWAP": lambda: vwap(h, l, c, v),
    }

    for name, fn in calculations.items():
        try:
            result[name] = fn()
        except Exception as exc:
            result[name] = f"Error: {exc}"

    try:
        bb = bollinger(c, period)
        result["Bollinger"] = bb
    except Exception as exc:
        result["Bollinger"] = f"Error: {exc}"

    try:
        st_result = supertrend(h, l, c)
        result["Supertrend"] = st_result
    except Exception as exc:
        result["Supertrend"] = f"Error: {exc}"

    try:
        result["Ichimoku"] = ichimoku(h, l, c)
    except Exception as exc:
        result["Ichimoku"] = f"Error: {exc}"

    return result


def build_context(symbol: str, timeframe: str, df: pd.DataFrame | None):
    context = MarketContext(
        symbol=symbol,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
    context.market_observations["timeframe"] = timeframe
    if df is not None:
        context.market_observations["rows"] = len(df)
        context.market_observations["latest_close"] = float(df["close"].iloc[-1])
        context.market_observations["latest_volume"] = float(df["volume"].iloc[-1])
        context.market_observations["data_source"] = "uploaded_ohlcv"
    return CentralBrain().analyze(context)


# ---------------------------------------------------------------------------
# Angel One integration
# ---------------------------------------------------------------------------
ANGEL_NATIVE_INTERVAL = {
    "1m": "1m",
    "5m": "5m",
    "15m": "15m",
    "1H": "1H",
    "1D": "1D",
}


@st.cache_resource(ttl=1800, show_spinner=False)
def get_angel_provider(api_key: str, client_code: str, pin: str, totp_secret: str):
    return HistoricalDataProvider(
        AngelOneHistoricalProvider(
            api_key=api_key,
            client_code=client_code,
            pin=pin,
            totp_secret=totp_secret,
        )
    )


def get_angel_secrets():
    try:
        section = st.secrets["angel_one"]
        return (
            str(section["api_key"]),
            str(section["client_code"]),
            str(section["pin"]),
            str(section["totp_secret"]),
        )
    except Exception:
        return None


def fetch_from_angel(
    provider: HistoricalDataProvider,
    symbol: str,
    timeframe: str,
    start_date,
    end_date,
    market_kind: str,
):
    if timeframe not in ANGEL_NATIVE_INTERVAL:
        raise ValueError(
            "Angel One historical API currently supports 1m, 5m, 15m, 1H and 1D "
            "directly in this dashboard. Select one of these timeframes."
        )

    start = datetime.combine(start_date, datetime.min.time())
    end = datetime.combine(end_date, datetime.max.time())
    market = "NIFTY 50 Company" if market_kind == "NIFTY 50 Company" else "NIFTY 50"

    result = provider.fetch_normalized(
        symbol=symbol,
        start=start.isoformat(),
        end=end.isoformat(),
        interval=ANGEL_NATIVE_INTERVAL[timeframe],
        market=market,
    )
    frame = pd.DataFrame(result.records)
    if frame.empty:
        raise ValueError("Angel One returned no historical OHLCV rows for this range.")

    frame["timestamp"] = pd.to_datetime(frame["timestamp"], utc=True)
    for column in ["open", "high", "low", "close", "volume"]:
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame.dropna(subset=["open", "high", "low", "close", "volume"])
    return frame.reset_index(drop=True)


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("Market Universe")

    universe_type = st.radio(
        "Research target",
        ["NIFTY 50 Company", "Tracked Market"],
        index=0,
    )

    if universe_type == "NIFTY 50 Company":
        symbol = st.selectbox("Company", list(NIFTY50_SYMBOLS))
    else:
        symbol = st.selectbox("Market", list(TRACKED_MARKETS))

    timeframe = st.selectbox(
        "Timeframe",
        ["1m", "5m", "15m", "1H", "4H", "1D", "1W", "1M", "3M", "6M"],
        index=5,
    )

    period = st.number_input(
        "Indicator period",
        min_value=2,
        max_value=200,
        value=14,
        step=1,
    )

    st.divider()
    data_source = st.radio(
        "Data source",
        ["Angel One SmartAPI", "Historical OHLCV CSV"],
        index=0,
    )

    uploaded = None
    angel_start = st.date_input("Angel One start date", value=datetime.now().date() - pd.Timedelta(days=30))
    angel_end = st.date_input("Angel One end date", value=datetime.now().date())

    if data_source == "Historical OHLCV CSV":
        uploaded = st.file_uploader(
            "Historical OHLCV CSV",
            type=["csv"],
            help="Use columns such as Timestamp, Open, High, Low, Close, Volume.",
        )
    else:
        st.caption("Angel One credentials are read only from Streamlit Secrets.")
        fetch_angel = st.button("🔌 Fetch from Angel One", type="primary", use_container_width=True)

# ---------------------------------------------------------------------------
# Load data
# ---------------------------------------------------------------------------
df = None
angel_error = None

if data_source == "Angel One SmartAPI":
    secrets = get_angel_secrets()
    if fetch_angel:
        if secrets is None:
            angel_error = (
                "Angel One Secrets missing. Add [angel_one] with api_key, "
                "client_code, pin and totp_secret in Streamlit Cloud Secrets."
            )
        elif angel_end < angel_start:
            angel_error = "Angel One end date must be on or after the start date."
        else:
            try:
                provider = get_angel_provider(*secrets)
                market_kind = universe_type
                df = fetch_from_angel(
                    provider,
                    symbol,
                    timeframe,
                    angel_start,
                    angel_end,
                    market_kind,
                )
                angel_quote = provider.get_ltp(
                    symbol,
                    "NIFTY 50 Company" if market_kind == "NIFTY 50 Company" else "NIFTY 50",
                )
                st.session_state["angel_quote"] = angel_quote
                st.session_state["angel_connected"] = True
                st.session_state["ohlcv"] = df
                st.session_state["filename"] = "Angel One SmartAPI"
                st.session_state["data_source"] = "Angel One SmartAPI"
            except Exception as exc:
                angel_error = str(exc)
    elif st.session_state.get("data_source") == "Angel One SmartAPI" and "ohlcv" in st.session_state:
        df = st.session_state["ohlcv"]
        angel_quote = st.session_state.get("angel_quote")

else:
    if uploaded is not None:
        try:
            df = normalize_ohlcv(pd.read_csv(uploaded))
            st.session_state["ohlcv"] = df
            st.session_state["filename"] = uploaded.name
            st.session_state["data_source"] = "Historical OHLCV CSV"
        except Exception as exc:
            st.error(str(exc))
    elif st.session_state.get("data_source") == "Historical OHLCV CSV" and "ohlcv" in st.session_state:
        df = st.session_state["ohlcv"]

if angel_error:
    st.error(f"Angel One: {angel_error}")

# ---------------------------------------------------------------------------
# Top status cards
# ---------------------------------------------------------------------------
c1, c2, c3, c4 = st.columns(4)
c1.metric("Engine", "ONLINE")
c2.metric("Orchestrator", "CentralBrain")
c3.metric("Shared Context", "MarketContext")
c4.metric("Data", "ANGEL ONE" if df is not None and data_source == "Angel One SmartAPI" else ("CSV" if df is not None else "WAITING"))

# ---------------------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------------------
tab_overview, tab_technical, tab_structure, tab_context, tab_health = st.tabs(
    ["Overview", "Technical Intelligence", "Structure & Patterns",
     "Market Context", "Engine Health"]
)

with tab_overview:
    st.subheader(f"{symbol} • {timeframe}")

    if df is None:
        st.info(
            "Select Angel One SmartAPI in the sidebar, configure Streamlit Secrets, "
            "choose a date range and click Fetch from Angel One. CSV upload remains "
            "available as the provider-neutral fallback."
        )
    else:
        latest_close = float(df["close"].iloc[-1])
        previous_close = float(df["close"].iloc[-2]) if len(df) > 1 else None
        change = (
            (latest_close / previous_close - 1.0) * 100
            if previous_close not in (None, 0)
            else None
        )

        a, b, c, d = st.columns(4)
        a.metric("Latest Close", fmt(latest_close, 2))
        b.metric("Change", f"{fmt(change, 2)}%" if change is not None else "—")
        c.metric("Rows", f"{len(df):,}")
        d.metric("Latest Volume", fmt(df["volume"].iloc[-1], 0))
        if data_source == "Angel One SmartAPI" and angel_quote:
            st.metric("Angel One LTP", fmt(angel_quote.get("ltp"), 2))

        st.subheader("Price")
        chart_df = df[["close"]].copy()
        chart_df.index = (
            df["timestamp"] if "timestamp" in df.columns
            else range(len(df))
        )
        st.line_chart(chart_df, use_container_width=True)

        st.subheader("Recent OHLCV")
        st.dataframe(df.tail(20), use_container_width=True)

with tab_technical:
    if df is None:
        st.info("Upload OHLCV data first.")
    else:
        indicators = run_indicators(df, int(period))

        st.subheader("Core Indicators")
        cards = st.columns(4)
        names = ["SMA", "EMA", "RSI", "ATR"]
        for col, name in zip(cards, names):
            value = indicators.get(name)
            col.metric(name, fmt(value, 4))

        st.subheader("Momentum / Trend / Volume")
        rows = []
        for name in [
            "WMA", "ROC", "Momentum", "ADX", "Williams %R", "CCI",
            "MFI", "Relative Volume", "OBV", "A/D", "Price/Volume", "VWAP",
        ]:
            value = indicators.get(name)
            if isinstance(value, (dict, list, tuple)):
                display = str(value)
            else:
                display = fmt(value, 4) if not isinstance(value, str) else value
            rows.append({"Indicator": name, "Latest / Result": display})
        st.dataframe(pd.DataFrame(rows), use_container_width=True)

        st.subheader("Bollinger / Supertrend / Ichimoku")
        for name in ["Bollinger", "Supertrend", "Ichimoku"]:
            value = indicators.get(name)
            st.write(f"**{name}**")
            if isinstance(value, (dict, list, tuple)):
                st.json(value)
            else:
                st.write(value)

with tab_structure:
    if df is None:
        st.info("Upload OHLCV data first.")
    else:
        h = df["high"].tolist()
        l = df["low"].tolist()
        c = df["close"].tolist()
        o = df["open"].tolist()

        st.subheader("Market Structure")
        try:
            ms = market_structure_snapshot(h, l, c)
            st.json(ms)
        except Exception as exc:
            st.warning(f"Market structure unavailable: {exc}")

        st.subheader("Chart Structure")
        try:
            cs = structure_snapshot(h, l)
            st.json(cs)
        except Exception as exc:
            st.warning(f"Chart structure unavailable: {exc}")

        st.subheader("Latest Candlestick Pattern")
        try:
            candle = detect_candle({
                "open": o[-1],
                "high": h[-1],
                "low": l[-1],
                "close": c[-1],
            }, prior_closes=c[:-1])
            st.json(candle)
        except Exception as exc:
            st.warning(f"Candlestick detection unavailable: {exc}")

with tab_context:
    context = build_context(symbol, timeframe, df)

    st.subheader("Shared MarketContext")
    st.json(context.to_snapshot())

    st.subheader("Architecture")
    st.markdown(
        """
        **Data → Analysis modules → MarketContext → CentralBrain → UI**

        The UI does not create a second orchestration workflow and does not
        make an independent trading decision. Analysis modules contribute
        evidence; the shared context remains the common research object.
        """
    )

with tab_health:
    st.subheader("Engine Health")

    checks = [
        ("MarketContext", True),
        ("CentralBrain", True),
        ("Technical indicators", True),
        ("Trend indicators", True),
        ("Momentum indicators", True),
        ("Volatility indicators", True),
        ("Volume indicators", True),
        ("Candlestick patterns", True),
        ("Chart patterns", True),
        ("Market structure", True),
        ("Historical/relationship layers", True),
        ("Angel One SmartAPI provider", st.session_state.get("angel_connected", False)),
    ]

    health_df = pd.DataFrame(
        [
            {"Component": name, "Status": "READY" if ok else "NOT CONNECTED"}
            for name, ok in checks
        ]
    )
    st.dataframe(health_df, use_container_width=True)

    st.info(
        "Angel One is implemented as a concrete provider behind the existing "
        "HistoricalDataProvider boundary. Credentials stay in Streamlit Secrets; "
        "the UI does not contain API keys or independent market-analysis logic."
    )

st.divider()
st.caption(
    "Research/analysis software. Historical relationships and indicators are "
    "descriptive and depend on data quality; they do not guarantee future market outcomes."
)
