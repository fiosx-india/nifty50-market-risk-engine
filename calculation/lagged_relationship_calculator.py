"""Lagged company/market observations."""
def calculate_lags(market_returns, company_returns, lags):
    m = list(map(float, market_returns))
    c = list(map(float, company_returns))
    out = []
    for lag in lags:
        lag = int(lag)
        if lag < 0:
            raise ValueError("lag must be >= 0")
        n = min(len(m), len(c))
        pairs = [] if n <= lag else [(m[-n:][i], c[-n:][i+lag]) for i in range(n-lag)]
        out.append({
            "lag": lag,
            "sample_size": len(pairs),
            "pairs": pairs,
            "status": "calculated" if pairs else "insufficient_data",
        })
    return out
