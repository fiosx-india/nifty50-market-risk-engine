"""Tracked-market symbol configuration. No calculated relationships."""
TRACKED_MARKETS = (
    "NIFTY 50", "Crude Oil", "Gold", "Silver", "Natural Gas",
    "Copper", "Aluminium", "Zinc", "Electricity",
)
DEFAULT_SYMBOLS = {market: () for market in TRACKED_MARKETS}

def validate_market(market):
    return market in TRACKED_MARKETS

def get_candidates(market):
    if not validate_market(market):
        raise KeyError(f"Unsupported tracked market: {market}")
    return tuple(DEFAULT_SYMBOLS[market])
