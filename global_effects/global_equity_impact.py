"""Global equity relative-return helpers."""
def excess_return(asset_return,benchmark_return):
    return float(asset_return)-float(benchmark_return)
def relative_strength(asset,benchmark):
    return None if not benchmark or float(benchmark[-1])==0 else float(asset[-1])/float(benchmark[-1])
