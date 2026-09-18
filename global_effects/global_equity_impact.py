"""Global-equity relative-return helpers."""


def excess_return(asset_return, benchmark_return):
    return float(asset_return) - float(benchmark_return)


def relative_strength(asset, benchmark):
    if not asset or not benchmark:
        return None
    benchmark_last = float(benchmark[-1])
    return None if benchmark_last == 0 else float(asset[-1]) / benchmark_last
