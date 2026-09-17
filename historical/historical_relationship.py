"""Historical relationship snapshot."""
def relationship_snapshot(market_returns,company_returns,correlation_fn):
    return {"sample_size":min(len(market_returns),len(company_returns)),
            "correlation":correlation_fn(market_returns,company_returns),
            "calculation_status":"historical_observation",
            "causation_claim":False}
