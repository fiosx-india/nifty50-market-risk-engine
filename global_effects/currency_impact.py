"""FX normalization helpers. Caller must declare quote convention."""
def normalize_price(price,fx_rate): return float(price)*float(fx_rate)
def excess_return(local_return,fx_return): return float(local_return)-float(fx_return)
