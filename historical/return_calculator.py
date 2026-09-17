"""Return calculations."""
def simple_returns(close):
    c=list(map(float,close))
    return [c[i]/c[i-1]-1 for i in range(1,len(c)) if c[i-1]!=0]
def cumulative_return(close):
    c=list(map(float,close))
    return None if len(c)<2 or c[0]==0 else c[-1]/c[0]-1
