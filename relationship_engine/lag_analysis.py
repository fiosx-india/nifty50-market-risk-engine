"""Lagged market/company alignment."""
def lag_pairs(market_returns,company_returns,lag):
    if lag<0: raise ValueError("lag must be >= 0")
    n=min(len(market_returns),len(company_returns))
    if n<=lag:return []
    m=list(map(float,market_returns[-n:])); c=list(map(float,company_returns[-n:]))
    return [(m[i],c[i+lag]) for i in range(n-lag)]
