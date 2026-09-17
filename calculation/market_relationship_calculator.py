"""Historical company/market relationship calculations only."""
from statistics import mean

def _aligned(a, b):
    n = min(len(a), len(b))
    return list(map(float, a[-n:])), list(map(float, b[-n:]))

def _pearson(a, b):
    n = min(len(a), len(b))
    if n < 2:
        return None
    a, b = _aligned(a, b)
    ma, mb = mean(a), mean(b)
    da = [x-ma for x in a]
    db = [x-mb for x in b]
    den = (sum(x*x for x in da) * sum(x*x for x in db)) ** 0.5
    return sum(x*y for x, y in zip(da, db))/den if den else None

def calculate(market_returns, company_returns, benchmark_returns=None):
    m, c = _aligned(market_returns, company_returns)
    result = {
        "sample_size": len(m),
        "correlation": _pearson(m, c),
        "mean_market_return": mean(m) if m else None,
        "mean_company_return": mean(c) if c else None,
        "causation_claim": False,
        "status": "calculated" if len(m) >= 2 else "insufficient_data",
    }
    if benchmark_returns is not None:
        b, c2 = _aligned(benchmark_returns, company_returns)
        n = min(len(b), len(c2))
        result["benchmark_excess_return_mean"] = (
            mean(c2[-n:][i] - b[-n:][i] for i in range(n)) if n else None
        )
    return result
