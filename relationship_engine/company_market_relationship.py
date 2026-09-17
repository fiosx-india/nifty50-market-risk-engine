"""Company + market character relationship layer."""
def resolve_relationship(company_character,market_character):
    symbol=getattr(company_character,"symbol",getattr(company_character,"name","UNKNOWN"))
    return {"company":symbol,"market":market_character.market,
            "direct_channels":tuple(market_character.direct_exposure_patterns),
            "indirect_channels":tuple(market_character.indirect_exposure_patterns),
            "cost_channels":tuple(market_character.cost_channels),
            "revenue_channels":tuple(market_character.revenue_channels),
            "status":"requires_historical_validation"}
