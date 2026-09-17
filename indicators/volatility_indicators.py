"""Volatility measurements."""
def returns(close):
    c=list(map(float,close))
    return [c[i]/c[i-1]-1 for i in range(1,len(c)) if c[i-1]!=0]

def realized_volatility(close, annualization=None):
    r=returns(close)
    if len(r)<2: return None
    m=sum(r)/len(r)
    v=(sum((x-m)**2 for x in r)/(len(r)-1))**0.5
    return v*(annualization**0.5) if annualization else v

def volatility_percentile(current, history):
    h=sorted(map(float,history))
    return None if not h else 100*sum(x<=float(current) for x in h)/len(h)

def true_range_series(high,low,close):
    return [max(float(high[i])-float(low[i]),
                abs(float(high[i])-float(close[i-1])),
                abs(float(low[i])-float(close[i-1])))
            for i in range(1,len(close))]
