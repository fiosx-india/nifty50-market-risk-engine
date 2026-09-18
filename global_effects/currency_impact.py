"""FX normalization helpers.

The caller must declare the quote convention and timestamp alignment. These
helpers perform arithmetic only and do not infer economic direction.
"""


def normalize_price(price, fx_rate):
    return float(price) * float(fx_rate)


def excess_return(local_return, fx_return):
    return float(local_return) - float(fx_return)
