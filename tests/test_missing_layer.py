"""Smoke tests for the missing layer."""
def test_normalizer():
    from data_providers.data_normalizer import normalize_records
    x = normalize_records([{"timestamp":"2026-01-01","open":100,"high":110,
                            "low":95,"close":105,"volume":1000}])
    assert x[0]["close"] == 105.0

def test_relationship():
    from calculation.market_relationship_calculator import calculate
    x = calculate([.01,.02,.03],[.02,.04,.06])
    assert x["sample_size"] == 3 and x["causation_claim"] is False

def test_lag():
    from calculation.lagged_relationship_calculator import calculate_lags
    x = calculate_lags([1,2,3],[10,20,30],[0,1])
    assert x[0]["sample_size"] == 3 and x[1]["sample_size"] == 2
