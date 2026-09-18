"""Canonical research universe for the NIFTY 50 risk-research engine.

Identifiers only: no prices, scores, ranks, correlations, probabilities,
signals, or other calculated results.
"""

NIFTY50_SYMBOLS = (
    "HDFCBANK", "ICICIBANK", "RELIANCE", "SBIN", "LT", "M&M",
    "AXISBANK", "SHRIRAMFIN", "INFY", "TCS", "TATASTEEL", "BHARTIARTL",
    "KOTAKBANK", "BAJFINANCE", "ITC", "BEL", "HCLTECH", "MARUTI", "TMPV",
    "ETERNAL", "BAJAJ-AUTO", "HINDALCO", "COALINDIA", "GRASIM", "JIOFIN",
    "ULTRACEMCO", "SUNPHARMA", "INDIGO", "EICHERMOT", "TECHM", "NESTLEIND",
    "ADANIENT", "JSWSTEEL", "NTPC", "HDFCLIFE", "ONGC", "APOLLOHOSP",
    "HINDUNILVR", "POWERGRID", "WIPRO", "TITAN", "ADANIPORTS", "TRENT",
    "MAXHEALTH", "TATACONSUM", "ASIANPAINT", "SBILIFE", "DRREDDY",
    "CIPLA", "BAJAJFINSV",
)

TRACKED_MARKETS = (
    "NIFTY 50", "Crude Oil", "Gold", "Silver", "Natural Gas",
    "Copper", "Aluminium", "Zinc", "Electricity",
)


def validate_universe():
    """Validate the fixed 50-company and 9-market universe."""
    if len(NIFTY50_SYMBOLS) != 50:
        raise ValueError(f"Expected 50 companies, found {len(NIFTY50_SYMBOLS)}")
    if len(set(NIFTY50_SYMBOLS)) != len(NIFTY50_SYMBOLS):
        raise ValueError("Duplicate company symbol in NIFTY50_SYMBOLS")
    if any(not isinstance(s, str) or not s.strip() for s in NIFTY50_SYMBOLS):
        raise ValueError("NIFTY50_SYMBOLS contains an empty or invalid symbol")

    if len(TRACKED_MARKETS) != 9:
        raise ValueError(f"Expected 9 markets, found {len(TRACKED_MARKETS)}")
    if len(set(TRACKED_MARKETS)) != len(TRACKED_MARKETS):
        raise ValueError("Duplicate market in TRACKED_MARKETS")
    if any(not isinstance(m, str) or not m.strip() for m in TRACKED_MARKETS):
        raise ValueError("TRACKED_MARKETS contains an empty or invalid market")

    return True


def is_company(symbol):
    return isinstance(symbol, str) and symbol in NIFTY50_SYMBOLS


def is_tracked_market(market):
    return isinstance(market, str) and market in TRACKED_MARKETS


def get_company_symbols():
    return NIFTY50_SYMBOLS


def get_tracked_markets():
    return TRACKED_MARKETS
