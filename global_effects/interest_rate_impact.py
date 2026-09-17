"""Rate and yield-curve observations."""
def rate_change(current,previous): return float(current)-float(previous)
def yield_curve_slope(long_rate,short_rate): return float(long_rate)-float(short_rate)
