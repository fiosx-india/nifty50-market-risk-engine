"""Smoke tests for the new calculation layer."""
def test_candlestick():
    from indicators.candlestick_patterns import doji
    assert doji(100,105,95,100)
def test_returns():
    from historical.return_calculator import simple_returns
    assert simple_returns([100,110]) == [0.1]
