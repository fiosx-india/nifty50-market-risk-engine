import streamlit as st
from datetime import datetime, timezone

from context.market_context import MarketContext
from orchestration.central_brain import CentralBrain

st.set_page_config(
    page_title="NIFTY 50 Market Risk Engine",
    page_icon="📊",
    layout="wide",
)

st.title("📊 NIFTY 50 Market Risk Engine")
st.caption("Research and risk-analysis engine • evidence-first architecture")

with st.sidebar:
    st.header("Engine")
    symbol = st.text_input("Symbol", "NIFTY 50")
    timeframe = st.selectbox("Timeframe", ["1m", "5m", "15m", "1H", "4H", "1D", "1W"])
    st.divider()
    st.info("This interface exposes the existing MarketContext and CentralBrain layers. It does not create a separate decision engine.")

if "context" not in st.session_state:
    st.session_state.context = None

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Engine", "ONLINE")
with col2:
    st.metric("Orchestrator", "CentralBrain")
with col3:
    st.metric("Context", "MarketContext")

if st.button("▶ Run Engine Check", type="primary"):
    context = MarketContext(
        symbol=symbol.strip() or "NIFTY 50",
        timestamp=datetime.now(timezone.utc).isoformat(),
    )
    context.market_observations["timeframe"] = timeframe
    result = CentralBrain().analyze(context)
    st.session_state.context = result
    st.success("Engine check completed.")

st.subheader("Market Data")
uploaded = st.file_uploader("Upload OHLCV CSV", type=["csv"])

if uploaded is not None:
    try:
        import pandas as pd

        df = pd.read_csv(uploaded)
        st.write(f"Rows: {len(df):,}  |  Columns: {len(df.columns)}")
        st.dataframe(df.tail(20), use_container_width=True)

        numeric = df.select_dtypes(include="number")
        if not numeric.empty:
            st.subheader("Basic Observations")
            st.dataframe(numeric.describe().T, use_container_width=True)
    except Exception as exc:
        st.error(f"Could not read the CSV: {exc}")

st.subheader("Shared Market Context")
if st.session_state.context is None:
    st.info("Click 'Run Engine Check' to initialize the shared context.")
else:
    snapshot = st.session_state.context.to_snapshot()
    st.json(snapshot)

st.caption("Research tool only. Outputs depend on data quality, historical observations and model assumptions; they are not guaranteed predictions.")
