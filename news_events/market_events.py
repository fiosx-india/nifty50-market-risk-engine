"""Market event taxonomy."""
EVENT_TYPES=("commodity_shock","rate_decision","inflation","FX_shock","geopolitical",
             "supply_disruption","demand_shock","weather","policy")
def classify_event(event):
    return event if event.get("type") in EVENT_TYPES else {**event,"type":"other"}
