"""Commodity exposure pathway helpers.

Character files describe possible direct and indirect pathways. This module
does not turn those pathways into a fixed score or directional conclusion.
"""


def classify_pathway(market_character):
    return {
        "direct": tuple(market_character.direct_exposure_patterns),
        "indirect": tuple(market_character.indirect_exposure_patterns),
        "cost": tuple(market_character.cost_channels),
        "revenue": tuple(market_character.revenue_channels),
    }


def observation(market_return, company_return, lag):
    return {
        "market_return": float(market_return),
        "company_return": float(company_return),
        "lag": int(lag),
        "causation_claim": False,
    }
