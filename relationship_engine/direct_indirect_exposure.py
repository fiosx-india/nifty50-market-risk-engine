"""Exposure classification without directional assumptions."""
def classify(market_character):
    return {"direct":tuple(market_character.direct_exposure_patterns),
            "indirect":tuple(market_character.indirect_exposure_patterns)}
