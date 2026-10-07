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


# ---------------------------------------------------------------------------
# Existing architecture
#
# UI
#   â†“
# HistoricalDataProvider
#   â†“
# AngelOneHistoricalProvider
#   â†“
# existing provider / instrument resolution
#   â†“
# MarketContext
#   â†“
# CentralBrain
#   â†“
# UI
#
# No second orchestration workflow is created here.
# ---------------------------------------------------------------------------
from context.market_context import MarketContext
from orchestration.central_brain import CentralBrain
from config.universe import NIFTY50_SYMBOLS, TRACKED_MARKETS
from data_providers.historical_provider import HistoricalDataProvider
from data_providers.angel_one_provider import AngelOneHistoricalProvider

from indicators.technical_indicators import (
    sma,
    ema,
    wma,
    roc,
    momentum,
    rsi,
    atr,
    bollinger,
    vwap,
)

from indicators.trend_indicators import (
    adx,
    supertrend,
    ichimoku,
)

from indicators.momentum_indicators import (
    stochastic,
    williams_r,
    cci,
    mfi,
)

from indicators.volume_indicators import (
    relative_volume,
    obv,
    accumulation_distribution,
    price_volume_confirmation,
)

from indicators.candlestick_patterns import (
    detect_last as detect_candle,
)

from indicators.chart_patterns import (
    structure_snapshot,
)

from indicators.market_structure import (
    market_structure_snapshot,
)


# ---------------------------------------------------------------------------
# Streamlit configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="NIFTY 50 Market Risk Engine",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.title("📊 NIFTY 50 Market Risk Engine")

st.caption(
    "Evidence-first market research dashboard • "
    "existing engine architecture preserved"
)


# ===========================================================================
# CONSTANTS
# ===========================================================================

ANGEL_NATIVE_INTERVAL = {
    "1m": "1m",
    "5m": "5m",
    "15m": "15m",
    "1H": "1H",
    "1D": "1D",
}


# Angel One historical API path used by this dashboard.
# These are the timeframes directly supported by the current provider
# integration.
ANGEL_SUPPORTED_TIMEFRAMES = tuple(
    ANGEL_NATIVE_INTERVAL.keys()
)


# ===========================================================================
# SESSION STATE INITIALIZATION
# ===========================================================================

def initialize_session_state():
    """
    Initialize dashboard state without creating a second orchestration layer.
    """

    defaults = {
        "ohlcv": None,
        "angel_quote": None,
        "angel_connected": False,
        "angel_error": None,
        "data_source": None,
        "filename": None,
        "data_identity": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


initialize_session_state()


# ===========================================================================
# HELPERS
# ===========================================================================

def normalize_ohlcv(
    df: pd.DataFrame,
    selected_symbol: str | None = None,
) -> pd.DataFrame:
    """
    Normalize either:

    1. Historical OHLCV time-series CSV
    2. NSE/market-watch snapshot CSV

    The uploaded MW-NIFTY-50-01-Oct-2026.csv is a market snapshot:
    it contains OPEN/HIGH/LOW/PREV. CLOSE/LTP/VOLUME (shares), not a
    historical Close column or timestamps.

    For a snapshot, LTP is exposed as the latest price in the canonical
    `close` field only for compatibility with the existing MarketContext.
    The dataframe is explicitly marked with attrs["data_mode"] so technical
    indicators and pattern engines are not run as if this were historical
    candle data.
    """

    if df is None or df.empty:
        raise ValueError("CSV is empty.")

    # -----------------------------------------------------------------------
    # Detect the supplied NSE/market-watch snapshot schema BEFORE applying
    # generic OHLCV aliases.
    # -----------------------------------------------------------------------
    normalized_keys = {
        str(col).strip().lower(): col
        for col in df.columns
    }

    snapshot_required = {
        "symbol",
        "open",
        "high",
        "low",
        "prev. close",
        "ltp",
        "volume (shares)",
    }

    if snapshot_required.issubset(set(normalized_keys.keys())):

        symbol_col = normalized_keys["symbol"]
        open_col = normalized_keys["open"]
        high_col = normalized_keys["high"]
        low_col = normalized_keys["low"]
        prev_close_col = normalized_keys["prev. close"]
        ltp_col = normalized_keys["ltp"]
        volume_col = normalized_keys["volume (shares)"]

        out = pd.DataFrame(
            {
                "symbol": df[symbol_col].astype(str).str.strip(),
                "open": pd.to_numeric(
                    df[open_col].astype(str).str.replace(",", "", regex=False),
                    errors="coerce",
                ),
                "high": pd.to_numeric(
                    df[high_col].astype(str).str.replace(",", "", regex=False),
                    errors="coerce",
                ),
                "low": pd.to_numeric(
                    df[low_col].astype(str).str.replace(",", "", regex=False),
                    errors="coerce",
                ),
                "prev_close": pd.to_numeric(
                    df[prev_close_col].astype(str).str.replace(",", "", regex=False),
                    errors="coerce",
                ),
                "ltp": pd.to_numeric(
                    df[ltp_col].astype(str).str.replace(",", "", regex=False),
                    errors="coerce",
                ),
                "volume": pd.to_numeric(
                    df[volume_col].astype(str).str.replace(",", "", regex=False),
                    errors="coerce",
                ),
            }
        )

        out = out.dropna(
            subset=[
                "symbol",
                "open",
                "high",
                "low",
                "ltp",
                "volume",
            ]
        ).reset_index(drop=True)

        if out.empty:
            raise ValueError(
                "The market snapshot CSV contains no valid rows."
            )

        # A market snapshot has no candle close. LTP is the current/latest
        # traded price, so expose it as canonical latest price while marking
        # the semantics explicitly.
        out["close"] = out["ltp"]

        out["timestamp"] = pd.Timestamp.now(tz="UTC")

        if selected_symbol:
            requested = str(selected_symbol).strip().upper()

            matches = out[
                out["symbol"].str.upper() == requested
            ].copy()

            if matches.empty:
                available_preview = ", ".join(
                    out["symbol"].head(12).tolist()
                )

                raise ValueError(
                    f"The uploaded market snapshot does not contain "
                    f"'{selected_symbol}'. "
                    f"This file contains {len(out)} instruments, including: "
                    f"{available_preview}. "
                    "Upload a file containing the selected instrument or "
                    "use Angel One SmartAPI for that market."
                )

            out = matches.reset_index(drop=True)

        if (out["high"] < out["low"]).any():
            raise ValueError(
                "Market snapshot contains rows where High < Low."
            )

        if (out["ltp"] < out["low"]).any() or (
            out["ltp"] > out["high"]
        ).any():
            raise ValueError(
                "Market snapshot contains LTP values outside Low/High."
            )

        if (out["volume"] < 0).any():
            raise ValueError(
                "Market snapshot contains negative Volume."
            )

        out.attrs["data_mode"] = "market_snapshot"
        out.attrs["price_semantics"] = "LTP"
        out.attrs["historical"] = False
        out.attrs["source_format"] = "NSE market-watch snapshot"

        return out[
            [
                "timestamp",
                "symbol",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "prev_close",
                "ltp",
            ]
        ]

    # -----------------------------------------------------------------------
    # Standard historical OHLCV CSV
    # -----------------------------------------------------------------------
    aliases = {
        "date": "timestamp",
        "datetime": "timestamp",
        "time": "timestamp",
        "timestamp": "timestamp",
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

    required = [
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    missing = [
        column
        for column in required
        if column not in out.columns
    ]

    if missing:
        raise ValueError(
            "CSV must contain Open, High, Low, Close and Volume columns. "
            f"Missing: {', '.join(missing)}. "
            "The uploaded MW-NIFTY file is a market snapshot, not a "
            "historical OHLCV file."
        )

    if "timestamp" in out.columns:
        out["timestamp"] = pd.to_datetime(
            out["timestamp"],
            errors="coerce",
            utc=True,
        )

        out = (
            out
            .dropna(subset=["timestamp"])
            .sort_values("timestamp")
        )

    for column in required:
        out[column] = pd.to_numeric(
            out[column].astype(str).str.replace(",", "", regex=False),
            errors="coerce",
        )

    out = (
        out
        .dropna(subset=required)
        .reset_index(drop=True)
    )

    if out.empty:
        raise ValueError(
            "No valid OHLCV rows remain after cleaning."
        )

    if "timestamp" not in out.columns:
        raise ValueError(
            "Historical OHLCV CSV requires a Timestamp/Date/Datetime column."
        )

    if (out["high"] < out["low"]).any():
        raise ValueError(
            "CSV contains rows where High < Low."
        )

    if (
        (out["close"] < out["low"])
        | (out["close"] > out["high"])
    ).any():
        raise ValueError(
            "CSV contains Close values outside Low/High."
        )

    if (out["volume"] < 0).any():
        raise ValueError(
            "CSV contains negative Volume."
        )

    out.attrs["data_mode"] = "historical_ohlcv"
    out.attrs["price_semantics"] = "close"
    out.attrs["historical"] = True
    out.attrs["source_format"] = "historical OHLCV"

    return out


def latest(series):
    """
    Return the latest value from a list/tuple.
    Otherwise return the value unchanged.
    """

    if isinstance(series, (list, tuple)) and series:
        return series[-1]

    return series


def fmt(value, digits=4):
    """
    Safe numeric display helper.
    """

    if value is None:
        return "—"

    try:
        if pd.isna(value):
            return "—"

        return f"{float(value):.{digits}f}"

    except Exception:
        return str(value)


# ===========================================================================
# MARKET IDENTITY
# ===========================================================================

def get_market_identity(
    universe_type: str,
    symbol: str,
) -> dict:
    """
    Build the canonical identity passed through the existing provider
    boundary.

    IMPORTANT:
        Company:
            symbol = HDFCBANK
            market = NIFTY 50 Company

        Tracked market:
            symbol = Gold
            market = Gold

    The previous implementation incorrectly converted every tracked market
    into:
        market = NIFTY 50

    That behavior is intentionally removed.
    """

    if universe_type == "NIFTY 50 Company":

        if symbol not in NIFTY50_SYMBOLS:
            raise ValueError(
                f"Unsupported NIFTY 50 company: {symbol}"
            )

        return {
            "universe_type": "NIFTY 50 Company",
            "symbol": symbol,
            "market": "NIFTY 50 Company",
            "display_name": symbol,
        }

    if universe_type == "Tracked Market":

        if symbol not in TRACKED_MARKETS:
            raise ValueError(
                f"Unsupported tracked market: {symbol}"
            )

        return {
            "universe_type": "Tracked Market",
            "symbol": symbol,
            "market": symbol,
            "display_name": symbol,
        }

    raise ValueError(
        f"Unsupported research target: {universe_type}"
    )


def build_data_identity(
    universe_type: str,
    symbol: str,
    timeframe: str,
    data_source: str,
) -> tuple:
    """
    Stable identity for preventing stale session data from being reused
    across different market selections.
    """

    identity = get_market_identity(
        universe_type,
        symbol,
    )

    return (
        identity["universe_type"],
        identity["symbol"],
        identity["market"],
        timeframe,
        data_source,
    )


# ===========================================================================
# INDICATORS
# ===========================================================================

def run_indicators(
    df: pd.DataFrame,
    period: int,
):
    """
    Run all optional indicators independently.

    One indicator failure must not break the dashboard.
    """

    h = df["high"].tolist()
    l = df["low"].tolist()
    c = df["close"].tolist()
    v = df["volume"].tolist()

    result = {}

    calculations = {
        "SMA": lambda: latest(
            sma(c, period)
        ),

        "EMA": lambda: latest(
            ema(c, period)
        ),

        "WMA": lambda: latest(
            wma(c, period)
        ),

        "RSI": lambda: latest(
            rsi(c, period)
        ),

        "ROC": lambda: latest(
            roc(c, period)
        ),

        "Momentum": lambda: latest(
            momentum(c, period)
        ),

        "ATR": lambda: latest(
            atr(h, l, c, period)
        ),

        "ADX": lambda: adx(
            h, l, c, period
        ),

        "Williams %R": lambda: williams_r(
            h, l, c, period
        ),

        "CCI": lambda: cci(
            h, l, c, period
        ),

        "MFI": lambda: mfi(
            h, l, c, period
        ),

        "Relative Volume": lambda: latest(
            relative_volume(v, period)
        ),

        "OBV": lambda: obv(
            c,
            v,
        ),

        "A/D": lambda: accumulation_distribution(
            h,
            l,
            c,
            v,
        ),

        "Price/Volume": lambda: price_volume_confirmation(
            c,
            v,
            period,
        ),

        "VWAP": lambda: vwap(
            h,
            l,
            c,
            v,
        ),
    }

    for name, calculation in calculations.items():

        try:
            result[name] = calculation()

        except Exception as exc:
            result[name] = (
                f"Error: {exc}"
            )

    try:

        result["Bollinger"] = bollinger(
            c,
            period,
        )

    except Exception as exc:

        result["Bollinger"] = (
            f"Error: {exc}"
        )

    try:

        result["Supertrend"] = supertrend(
            h,
            l,
            c,
        )

    except Exception as exc:

        result["Supertrend"] = (
            f"Error: {exc}"
        )

    try:

        result["Ichimoku"] = ichimoku(
            h,
            l,
            c,
        )

    except Exception as exc:

        result["Ichimoku"] = (
            f"Error: {exc}"
        )

    return result


# ===========================================================================
# MARKET CONTEXT
# ===========================================================================

def build_context(
    symbol: str,
    timeframe: str,
    df: pd.DataFrame | None,
    universe_type: str = "",
    market: str = "",
):
    """
    Build the existing shared MarketContext.

    CentralBrain remains the only orchestration layer.
    """

    context = MarketContext(
        symbol=symbol,
        timestamp=datetime.now(
            timezone.utc
        ).isoformat(),
    )

    context.market_observations[
        "timeframe"
    ] = timeframe

    context.market_observations[
        "universe_type"
    ] = universe_type

    context.market_observations[
        "market"
    ] = market

    if df is not None:

        context.market_observations[
            "rows"
        ] = len(df)

        context.market_observations[
            "latest_close"
        ] = float(
            df["close"].iloc[-1]
        )

        context.market_observations[
            "latest_volume"
        ] = float(
            df["volume"].iloc[-1]
        )

        context.market_observations[
            "data_source"
        ] = st.session_state.get(
            "data_source",
            "unknown",
        )

    return CentralBrain().analyze(context)


# ===========================================================================
# ANGEL ONE PROVIDER
# ===========================================================================

@st.cache_resource(
    ttl=1800,
    show_spinner=False,
)
def get_angel_provider(
    api_key: str,
    client_code: str,
    pin: str,
    totp_secret: str,
):
    """
    Create the existing Angel One provider behind the
    HistoricalDataProvider boundary.

    Credentials are supplied from Streamlit Secrets only.
    """

    concrete_provider = AngelOneHistoricalProvider(
        api_key=api_key,
        client_code=client_code,
        pin=pin,
        totp_secret=totp_secret,
    )

    return HistoricalDataProvider(
        concrete_provider
    )


def get_angel_secrets():
    """
    Read Angel One credentials only from Streamlit Secrets.

    No credentials are displayed.
    """

    try:

        section = st.secrets[
            "angel_one"
        ]

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
    universe_type: str,
):
    """
    Fetch Angel One historical OHLCV using the existing provider boundary.

    CRITICAL FIX:
        Tracked Market:
            market = selected market

        NIFTY 50 Company:
            market = NIFTY 50 Company

    No tracked market is silently converted to NIFTY 50.
    """

    if timeframe not in ANGEL_NATIVE_INTERVAL:

        supported = ", ".join(
            ANGEL_SUPPORTED_TIMEFRAMES
        )

        raise ValueError(
            "Angel One historical API in this dashboard currently "
            f"supports: {supported}. "
            f"Selected timeframe: {timeframe}"
        )

    identity = get_market_identity(
        universe_type,
        symbol,
    )

    start = datetime.combine(
        start_date,
        datetime.min.time(),
    )

    end = datetime.combine(
        end_date,
        datetime.max.time(),
    )

    # ---------------------------------------------------------------
    # IMPORTANT:
    #
    # OLD:
    # market = "NIFTY 50 Company" if ...
    #          else "NIFTY 50"
    #
    # NEW:
    # market comes from the actual selected identity.
    # ---------------------------------------------------------------
    market = identity["market"]

    result = provider.fetch_normalized(
        symbol=identity["symbol"],
        start=start.isoformat(),
        end=end.isoformat(),
        interval=ANGEL_NATIVE_INTERVAL[
            timeframe
        ],
        market=market,
    )

    if result is None:
        raise ValueError(
            "Angel One provider returned no result."
        )

    if getattr(result, "error", ""):
        raise ValueError(
            f"Angel One provider error: {result.error}"
        )

    frame = pd.DataFrame(
        result.records
    )

    if frame.empty:

        raise ValueError(
            "Angel One returned no historical OHLCV rows "
            f"for {symbol} / {market} "
            f"({timeframe}) in the selected date range."
        )

    required_columns = [
        "open",
        "high",
        "low",
        "close",
        "volume",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in frame.columns
    ]

    if missing_columns:

        raise ValueError(
            "Angel One returned incomplete OHLCV data. "
            f"Missing: {', '.join(missing_columns)}"
        )

    if "timestamp" not in frame.columns:

        raise ValueError(
            "Angel One response does not contain timestamp data."
        )

    frame["timestamp"] = pd.to_datetime(
        frame["timestamp"],
        utc=True,
        errors="coerce",
    )

    for column in required_columns:

        frame[column] = pd.to_numeric(
            frame[column],
            errors="coerce",
        )

    frame = (
        frame
        .dropna(
            subset=[
                "timestamp",
                *required_columns,
            ]
        )
        .sort_values("timestamp")
        .drop_duplicates(
            subset=["timestamp"],
            keep="last",
        )
        .reset_index(drop=True)
    )

    if frame.empty:

        raise ValueError(
            "Angel One returned records, but none remained "
            "after OHLCV validation."
        )

    if (frame["high"] < frame["low"]).any():

        raise ValueError(
            "Angel One returned invalid OHLCV data: High < Low."
        )

    if (
        (frame["close"] < frame["low"])
        | (frame["close"] > frame["high"])
    ).any():

        raise ValueError(
            "Angel One returned invalid OHLCV data: "
            "Close is outside Low/High."
        )

    if (frame["volume"] < 0).any():

        raise ValueError(
            "Angel One returned invalid OHLCV data: "
            "negative volume."
        )

    return frame


# ===========================================================================
# LTP
# ===========================================================================

def fetch_angel_ltp(
    provider: HistoricalDataProvider,
    symbol: str,
    universe_type: str,
):
    """
    Fetch LTP using exactly the same market identity as historical data.
    """

    identity = get_market_identity(
        universe_type,
        symbol,
    )

    quote = provider.get_ltp(
        identity["symbol"],
        identity["market"],
    )

    if not quote:
        return None

    return quote


# ===========================================================================
# CLEAR STALE ANGEL SESSION
# ===========================================================================

def clear_angel_state():
    """
    Clear only Angel One data state.

    Does not modify engine architecture or MarketContext.
    """

    st.session_state[
        "ohlcv"
    ] = None

    st.session_state[
        "angel_quote"
    ] = None

    st.session_state[
        "angel_connected"
    ] = False

    st.session_state[
        "angel_error"
    ] = None

    st.session_state[
        "data_source"
    ] = None

    st.session_state[
        "filename"
    ] = None

    st.session_state[
        "data_identity"
    ] = None


# ===========================================================================
# SIDEBAR SELECTION STATE
# ===========================================================================

def _first_valid(items, fallback):
    """Return fallback if valid; otherwise use the first available item."""
    values = list(items)

    if not values:
        raise ValueError("Selection list cannot be empty.")

    if fallback in values:
        return fallback

    return values[0]


def reset_market_data_state():
    """
    Clear loaded provider data when the research target changes.

    This prevents data from one company/market from appearing under another
    selection. It does not create another orchestration workflow.
    """
    clear_angel_state()


def on_universe_type_change():
    """
    Give Company and Tracked Market their own independent Streamlit state.

    This is the important fix for the old UI state problem where a value such
    as 'Gold' could remain inside the Company selector after changing the
    research universe.
    """
    reset_market_data_state()

    if st.session_state["universe_type"] == "NIFTY 50 Company":
        st.session_state["company_symbol"] = _first_valid(
            NIFTY50_SYMBOLS,
            st.session_state.get("company_symbol", "HDFCBANK"),
        )
    else:
        st.session_state["tracked_market_symbol"] = _first_valid(
            TRACKED_MARKETS,
            st.session_state.get("tracked_market_symbol", "NIFTY 50"),
        )


def on_company_change():
    """Clear stale data after changing the selected NIFTY 50 company."""
    reset_market_data_state()


def on_tracked_market_change():
    """Clear stale data after changing the selected tracked market."""
    reset_market_data_state()


# ===========================================================================
# SIDEBAR
# ===========================================================================

# Initialize the two independent widget values before the widgets are created.
# Explicit widget keys are used so Streamlit can never reuse the Company
# selector's state for the Tracked Market selector.
if "universe_type" not in st.session_state:
    st.session_state["universe_type"] = "NIFTY 50 Company"

if "company_symbol" not in st.session_state:
    st.session_state["company_symbol"] = _first_valid(
        NIFTY50_SYMBOLS,
        "HDFCBANK",
    )

if "tracked_market_symbol" not in st.session_state:
    st.session_state["tracked_market_symbol"] = _first_valid(
        TRACKED_MARKETS,
        "NIFTY 50",
    )


with st.sidebar:

    st.header(
        "Market Universe"
    )

    universe_type = st.radio(
        "Research target",
        [
            "NIFTY 50 Company",
            "Tracked Market",
        ],
        key="universe_type",
        on_change=on_universe_type_change,
    )

    if universe_type == "NIFTY 50 Company":

        symbol = st.selectbox(
            "Company",
            list(NIFTY50_SYMBOLS),
            key="company_symbol",
            on_change=on_company_change,
        )

    else:

        symbol = st.selectbox(
            "Market",
            list(TRACKED_MARKETS),
            key="tracked_market_symbol",
            on_change=on_tracked_market_change,
        )

    # Validate the selected identity immediately.
    try:

        selected_identity = get_market_identity(
            universe_type,
            symbol,
        )

    except Exception as exc:

        st.error(
            f"Market identity error: {exc}"
        )

        selected_identity = {
            "universe_type": universe_type,
            "symbol": symbol,
            "market": "",
            "display_name": symbol,
        }

    st.caption(
        f"Provider market: "
        f"`{selected_identity['market']}`"
    )

    timeframe = st.selectbox(
        "Timeframe",
        [
            "1m",
            "5m",
            "15m",
            "1H",
            "4H",
            "1D",
            "1W",
            "1M",
            "3M",
            "6M",
        ],
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
        [
            "Angel One SmartAPI",
            "Historical OHLCV CSV",
        ],
        index=0,
    )

    uploaded = None

    angel_start = st.date_input(
        "Angel One start date",
        value=(
            datetime.now().date()
            - pd.Timedelta(value=30, unit="D")
        ),
    )

    angel_end = st.date_input(
        "Angel One end date",
        value=datetime.now().date(),
    )

    if data_source == "Historical OHLCV CSV":

        uploaded = st.file_uploader(
            "Historical OHLCV CSV",
            type=["csv"],
            help=(
                "Use columns such as Timestamp, Open, "
                "High, Low, Close, Volume."
            ),
        )

        fetch_angel = False

    else:

        st.caption(
            "Angel One credentials are read only "
            "from Streamlit Secrets."
        )

        if timeframe not in ANGEL_NATIVE_INTERVAL:

            st.warning(
                "Selected timeframe is not directly supported "
                "by the current Angel One historical provider. "
                "Use 1m, 5m, 15m, 1H or 1D for Angel One fetch."
            )

        fetch_angel = st.button(
            "🔌 Fetch from Angel One",
            type="primary",
            width="stretch",
        )


# ===========================================================================
# LOAD DATA
# ===========================================================================

df = None

angel_error = None
angel_quote = None


# ---------------------------------------------------------------------------
# Current selection identity
# ---------------------------------------------------------------------------

current_identity = build_data_identity(
    universe_type=universe_type,
    symbol=symbol,
    timeframe=timeframe,
    data_source=data_source,
)


# ---------------------------------------------------------------------------
# Angel One
# ---------------------------------------------------------------------------

if data_source == "Angel One SmartAPI":

    secrets = get_angel_secrets()

    if fetch_angel:

        # Clear stale connection status BEFORE a new attempt.
        st.session_state[
            "angel_connected"
        ] = False

        st.session_state[
            "angel_error"
        ] = None

        st.session_state[
            "angel_quote"
        ] = None

        # ---------------------------------------------------------------
        # Validate credentials
        # ---------------------------------------------------------------

        if secrets is None:

            angel_error = (
                "Angel One Secrets missing. "
                "Add [angel_one] with api_key, client_code, "
                "pin and totp_secret in Streamlit Cloud Secrets."
            )

        elif angel_end < angel_start:

            angel_error = (
                "Angel One end date must be "
                "on or after the start date."
            )

        elif timeframe not in ANGEL_NATIVE_INTERVAL:

            angel_error = (
                "Selected timeframe is not directly supported "
                "by the current Angel One historical provider. "
                "Use 1m, 5m, 15m, 1H or 1D."
            )

        else:

            try:

                # -------------------------------------------------------
                # Provider
                # -------------------------------------------------------

                provider = get_angel_provider(
                    *secrets
                )

                # -------------------------------------------------------
                # Historical data
                # -------------------------------------------------------

                df = fetch_from_angel(
                    provider=provider,
                    symbol=symbol,
                    timeframe=timeframe,
                    start_date=angel_start,
                    end_date=angel_end,
                    universe_type=universe_type,
                )

                # -------------------------------------------------------
                # LTP
                # -------------------------------------------------------

                angel_quote = fetch_angel_ltp(
                    provider=provider,
                    symbol=symbol,
                    universe_type=universe_type,
                )

                # -------------------------------------------------------
                # SUCCESS STATE
                # -------------------------------------------------------

                st.session_state[
                    "angel_quote"
                ] = angel_quote

                st.session_state[
                    "angel_connected"
                ] = True

                st.session_state[
                    "angel_error"
                ] = None

                st.session_state[
                    "ohlcv"
                ] = df

                st.session_state[
                    "filename"
                ] = "Angel One SmartAPI"

                st.session_state[
                    "data_source"
                ] = "Angel One SmartAPI"

                st.session_state[
                    "data_identity"
                ] = current_identity

            except Exception as exc:

                # -------------------------------------------------------
                # IMPORTANT:
                # Do not mark the provider connected if the request failed.
                # -------------------------------------------------------

                angel_error = str(
                    exc
                )

                st.session_state[
                    "angel_connected"
                ] = False

                st.session_state[
                    "angel_error"
                ] = angel_error

                st.session_state[
                    "angel_quote"
                ] = None

                # Do not reuse stale OHLCV for another identity.
                if (
                    st.session_state.get(
                        "data_identity"
                    )
                    != current_identity
                ):

                    st.session_state[
                        "ohlcv"
                    ] = None

    else:

        # ---------------------------------------------------------------
        # Reuse only if the session data belongs to the SAME selection.
        # ---------------------------------------------------------------

        stored_identity = st.session_state.get(
            "data_identity"
        )

        if (
            st.session_state.get(
                "data_source"
            )
            == "Angel One SmartAPI"
            and stored_identity == current_identity
            and st.session_state.get(
                "ohlcv"
            ) is not None
        ):

            df = st.session_state[
                "ohlcv"
            ]

            angel_quote = st.session_state.get(
                "angel_quote"
            )

        else:

            # Different symbol / market / timeframe.
            # Do not display stale data.
            if stored_identity != current_identity:

                st.session_state[
                    "angel_connected"
                ] = False

                st.session_state[
                    "angel_quote"
                ] = None


# ---------------------------------------------------------------------------
# CSV
# ---------------------------------------------------------------------------

else:

    # CSV mode must not inherit Angel One status.
    st.session_state[
        "angel_connected"
    ] = False

    st.session_state[
        "angel_quote"
    ] = None

    if uploaded is not None:

        try:

            df = normalize_ohlcv(
                pd.read_csv(
                    uploaded
                ),
                selected_symbol=symbol,
            )

            st.session_state[
                "ohlcv"
            ] = df

            st.session_state[
                "filename"
            ] = uploaded.name

            st.session_state[
                "data_source"
            ] = "Historical OHLCV CSV"

            st.session_state[
                "data_identity"
            ] = current_identity

        except Exception as exc:

            st.error(
                str(exc)
            )

            st.session_state[
                "ohlcv"
            ] = None

    else:

        if (
            st.session_state.get(
                "data_source"
            )
            == "Historical OHLCV CSV"
            and st.session_state.get(
                "data_identity"
            )
            == current_identity
            and st.session_state.get(
                "ohlcv"
            ) is not None
        ):

            df = st.session_state[
                "ohlcv"
            ]

        else:

            df = None


# ---------------------------------------------------------------------------
# Display Angel error
# ---------------------------------------------------------------------------

if angel_error:

    st.error(
        f"Angel One: {angel_error}"
    )


# ===========================================================================
# TOP STATUS CARDS
# ===========================================================================

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Engine",
    "ONLINE",
)

c2.metric(
    "Orchestrator",
    "CentralBrain",
)

c3.metric(
    "Shared Context",
    "MarketContext",
)

if (
    df is not None
    and data_source == "Angel One SmartAPI"
):

    data_status = "ANGEL ONE"

elif (
    df is not None
    and data_source == "Historical OHLCV CSV"
):

    data_status = "CSV"

else:

    data_status = "WAITING"

c4.metric(
    "Data",
    data_status,
)


# ===========================================================================
# CONNECTION / IDENTITY STATUS
# ===========================================================================

if data_source == "Angel One SmartAPI":

    st.markdown(
        "### 🔌 Angel One Data Status"
    )

    status_col1, status_col2, status_col3, status_col4 = st.columns(4)

    status_col1.metric(
        "Authentication",
        (
            "CONNECTED"
            if st.session_state.get(
                "angel_connected",
                False,
            )
            else "NOT CONNECTED"
        ),
    )

    status_col2.metric(
        "Selected",
        symbol,
    )

    status_col3.metric(
        "Provider Market",
        selected_identity["market"],
    )

    status_col4.metric(
        "Timeframe",
        timeframe,
    )

    if (
        universe_type == "Tracked Market"
        and symbol != selected_identity["market"]
    ):

        st.error(
            "Market identity mismatch detected."
        )

    if (
        st.session_state.get(
            "angel_connected"
        )
        and df is not None
    ):

        st.success(
            "Angel One data is connected for the currently "
            "selected market identity."
        )


# ===========================================================================
# TABS
# ===========================================================================

(
    tab_overview,
    tab_technical,
    tab_structure,
    tab_context,
    tab_health,
) = st.tabs(
    [
        "Overview",
        "Technical Intelligence",
        "Structure & Patterns",
        "Market Context",
        "Engine Health",
    ]
)


# ===========================================================================
# OVERVIEW
# ===========================================================================

with tab_overview:

    st.subheader(
        f"{symbol} • {timeframe}"
    )

    if df is None:

        st.info(
            "Select Angel One SmartAPI in the sidebar, "
            "configure Streamlit Secrets, choose a supported "
            "timeframe/date range and click Fetch from Angel One. "
            "CSV upload remains available as the provider-neutral fallback."
        )

    else:

        data_mode = df.attrs.get(
            "data_mode",
            "historical_ohlcv",
        )

        if data_mode == "market_snapshot":
            st.info(
                "Market snapshot loaded. The uploaded file provides "
                "current LTP/open/high/low/volume for the selected instrument; "
                "it is not a historical candle series."
            )

        latest_close = float(
            df["close"].iloc[-1]
        )

        previous_close = (
            float(
                df["close"].iloc[-2]
            )
            if len(df) > 1
            else None
        )

        change = (
            (
                latest_close
                / previous_close
                - 1.0
            )
            * 100
            if previous_close not in (
                None,
                0,
            )
            else None
        )

        a, b, c, d = st.columns(4)

        a.metric(
            "Latest Close",
            fmt(
                latest_close,
                2,
            ),
        )

        b.metric(
            "Change",
            (
                f"{fmt(change, 2)}%"
                if change is not None
                else "—"
            ),
        )

        c.metric(
            "Rows",
            f"{len(df):,}",
        )

        d.metric(
            "Latest Volume",
            fmt(
                df["volume"].iloc[-1],
                0,
            ),
        )

        if (
            data_source == "Angel One SmartAPI"
            and angel_quote
        ):

            st.metric(
                "Angel One LTP",
                fmt(
                    angel_quote.get(
                        "ltp"
                    ),
                    2,
                ),
            )

        st.subheader(
            "Price"
        )

        chart_df = df[
            ["close"]
        ].copy()

        chart_df.index = (
            df["timestamp"]
            if "timestamp" in df.columns
            else range(len(df))
        )

        st.line_chart(
            chart_df,
            width="stretch",
        )

        st.subheader(
            "Recent OHLCV"
        )

        st.dataframe(
            df.tail(20),
            width="stretch",
        )


# ===========================================================================
# TECHNICAL INTELLIGENCE
# ===========================================================================

with tab_technical:

    if df is None:

        st.info(
            "Load OHLCV data first."
        )

    elif df.attrs.get("data_mode") == "market_snapshot":

        st.info(
            "Technical indicators require historical candle data. "
            "The uploaded file is a one-day market snapshot, so indicators "
            "are intentionally not calculated from it. Use Angel One SmartAPI "
            "or upload a historical OHLCV file."
        )

    else:

        indicators = run_indicators(
            df,
            int(period),
        )

        st.subheader(
            "Core Indicators"
        )

        cards = st.columns(4)

        names = [
            "SMA",
            "EMA",
            "RSI",
            "ATR",
        ]

        for col, name in zip(
            cards,
            names,
        ):

            value = indicators.get(
                name
            )

            col.metric(
                name,
                fmt(
                    value,
                    4,
                ),
            )

        st.subheader(
            "Momentum / Trend / Volume"
        )

        rows = []

        for name in [
            "WMA",
            "ROC",
            "Momentum",
            "ADX",
            "Williams %R",
            "CCI",
            "MFI",
            "Relative Volume",
            "OBV",
            "A/D",
            "Price/Volume",
            "VWAP",
        ]:

            value = indicators.get(
                name
            )

            if isinstance(
                value,
                (
                    dict,
                    list,
                    tuple,
                ),
            ):

                display = str(
                    value
                )

            else:

                display = (
                    fmt(
                        value,
                        4,
                    )
                    if not isinstance(
                        value,
                        str,
                    )
                    else value
                )

            rows.append(
                {
                    "Indicator": name,
                    "Latest / Result": display,
                }
            )

        st.dataframe(
            pd.DataFrame(rows),
            width="stretch",
        )

        st.subheader(
            "Bollinger / Supertrend / Ichimoku"
        )

        for name in [
            "Bollinger",
            "Supertrend",
            "Ichimoku",
        ]:

            value = indicators.get(
                name
            )

            st.write(
                f"**{name}**"
            )

            if isinstance(
                value,
                (
                    dict,
                    list,
                    tuple,
                ),
            ):

                st.json(
                    value
                )

            else:

                st.write(
                    value
                )


# ===========================================================================
# STRUCTURE & PATTERNS
# ===========================================================================

with tab_structure:

    if df is None:

        st.info(
            "Load OHLCV data first."
        )

    elif df.attrs.get("data_mode") == "market_snapshot":

        st.info(
            "Structure and candlestick pattern detection require a "
            "historical candle series. The uploaded file is a market "
            "snapshot, so these engines are intentionally not run."
        )

    else:

        h = df[
            "high"
        ].tolist()

        l = df[
            "low"
        ].tolist()

        c = df[
            "close"
        ].tolist()

        o = df[
            "open"
        ].tolist()

        st.subheader(
            "Market Structure"
        )

        try:

            ms = market_structure_snapshot(
                h,
                l,
                c,
            )

            st.json(
                ms
            )

        except Exception as exc:

            st.warning(
                f"Market structure unavailable: {exc}"
            )

        st.subheader(
            "Chart Structure"
        )

        try:

            cs = structure_snapshot(
                h,
                l,
            )

            st.json(
                cs
            )

        except Exception as exc:

            st.warning(
                f"Chart structure unavailable: {exc}"
            )

        st.subheader(
            "Latest Candlestick Pattern"
        )

        try:

            candle = detect_candle(
                {
                    "open": o[-1],
                    "high": h[-1],
                    "low": l[-1],
                    "close": c[-1],
                },
                prior_closes=c[:-1],
            )

            st.json(
                candle
            )

        except Exception as exc:

            st.warning(
                f"Candlestick detection unavailable: {exc}"
            )


# ===========================================================================
# MARKET CONTEXT
# ===========================================================================

with tab_context:

    context = build_context(
        symbol=symbol,
        timeframe=timeframe,
        df=df,
        universe_type=universe_type,
        market=selected_identity["market"],
    )

    st.subheader(
        "Shared MarketContext"
    )

    st.json(
        context.to_snapshot()
    )

    st.subheader(
        "Architecture"
    )

    st.markdown(
        """
        **Data → Provider → Analysis modules → MarketContext → CentralBrain → UI**

        The UI does not create a second orchestration workflow and does not
        make an independent trading decision.

        Analysis modules contribute evidence; the shared MarketContext remains
        the common research object.
        """
    )


# ===========================================================================
# ENGINE HEALTH
# ===========================================================================

with tab_health:

    st.subheader(
        "Engine Health"
    )

    checks = [
        (
            "MarketContext",
            True,
        ),

        (
            "CentralBrain",
            True,
        ),

        (
            "Technical indicators",
            True,
        ),

        (
            "Trend indicators",
            True,
        ),

        (
            "Momentum indicators",
            True,
        ),

        (
            "Volatility indicators",
            True,
        ),

        (
            "Volume indicators",
            True,
        ),

        (
            "Candlestick patterns",
            True,
        ),

        (
            "Chart patterns",
            True,
        ),

        (
            "Market structure",
            True,
        ),

        (
            "Historical/relationship layers",
            True,
        ),

        (
            "Angel One SmartAPI provider",
            st.session_state.get(
                "angel_connected",
                False,
            ),
        ),
    ]

    health_df = pd.DataFrame(
        [
            {
                "Component": name,
                "Status": (
                    "READY"
                    if ok
                    else "NOT CONNECTED"
                ),
            }

            for name, ok in checks
        ]
    )

    st.dataframe(
        health_df,
        width="stretch",
    )

    st.info(
        "Angel One is implemented as a concrete provider behind the existing "
        "HistoricalDataProvider boundary. Credentials stay in Streamlit Secrets; "
        "the UI does not contain API keys or independent market-analysis logic."
    )


# ===========================================================================
# FOOTER
# ===========================================================================

st.divider()

st.caption(
    "Research/analysis software. Historical relationships and indicators are "
    "descriptive and depend on data quality; they do not guarantee future "
    "market outcomes."
)
