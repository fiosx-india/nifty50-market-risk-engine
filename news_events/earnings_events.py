"""Earnings event record."""
def earnings_event(symbol,timestamp,period,actual=None,estimate=None):
    return {"symbol":symbol,"timestamp":timestamp,"period":period,
            "actual":actual,"estimate":estimate}
