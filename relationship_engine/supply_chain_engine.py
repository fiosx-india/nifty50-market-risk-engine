"""Supply-chain pathway builder."""
def build_path(market_character,industry,company):
    return {"market":market_character.market,"industry":industry,
            "company":company,"path":tuple(market_character.supply_chain_channels)}
def validate_path(path):
    return bool(path.get("market") and path.get("company") and path.get("path"))
