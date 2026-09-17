"""Rolling relationship calculations."""
def rolling_windows(values,window):
    if window<=0:raise ValueError("window must be positive")
    return [values[i-window:i] for i in range(window,len(values)+1)]
def rolling_stat(x,y,window,stat_fn):
    n=min(len(x),len(y))
    return [stat_fn(x[i-window:i],y[i-window:i]) for i in range(window,n+1)]
