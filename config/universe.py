"""The fixed research universe for this project: 50 NIFTY 50 companies + 9 tracked markets.

This file contains identifiers only. It does not contain prices, ranks, scores,
correlations, probabilities, signals, or other calculated outputs.
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
    "NIFTY 50",
    "Crude Oil",
    "Gold",
    "Silver",
    "Natural Gas",
    "Copper",
    "Aluminium",
    "Zinc",
    "Electricity",
)

def validate_universe():
    if len(NIFTY50_SYMBOLS) != 50:
        raise ValueError(f"Expected 50 companies, found {len(NIFTY50_SYMBOLS)}")
    if len(set(NIFTY50_SYMBOLS)) != len(NIFTY50_SYMBOLS):
        raise ValueError("Duplicate company symbol in NIFTY50_SYMBOLS")
    if len(TRACKED_MARKETS) != 9:
        raise ValueError(f"Expected 9 markets, found {len(TRACKED_MARKETS)}")
    if len(set(TRACKED_MARKETS)) != len(TRACKED_MARKETS):
        raise ValueError("Duplicate market in TRACKED_MARKETS")
    return True
