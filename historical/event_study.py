"""Abnormal-return event study."""
def abnormal_returns(asset_returns,benchmark_returns):
    n=min(len(asset_returns),len(benchmark_returns))
    return [float(asset_returns[i])-float(benchmark_returns[i]) for i in range(n)]
def cumulative_abnormal_return(asset_returns,benchmark_returns):
    x=abnormal_returns(asset_returns,benchmark_returns)
    return sum(x) if x else None
