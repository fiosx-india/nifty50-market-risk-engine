"""
TATASTEEL Character Model
==========================
Business character + nine tracked market characters for Tata Steel.

This file defines the causal channels and data that should be measured.
It does NOT hard-code RANK, PCT_CHANGE, LINKAGE_SCORE, RELATION,
correlation, beta, probability, or trading decisions.

Tata Steel is treated as an integrated, globally diversified steel producer:
raw materials -> ironmaking/steelmaking -> downstream/value-added products
-> distribution -> end-use industries, with significant energy, logistics,
commodity and capex exposure.
"""

from dataclasses import dataclass
from typing import Dict, Tuple


TRACKED_MARKETS: Tuple[str, ...] = (
    "NIFTY 50",
    "Crude Oil",
    "Gold",
    "Silver",
    "Natural Gas",
    "Copper",
    "Aluminium",
    "Zinc",
    "Electricity",
)


@dataclass(frozen=True)
class MarketCharacter:
    market: str
    exposure_type: str
    impact_channels: Tuple[str, ...]
    supply_chain_links: Tuple[str, ...]
    demand_links: Tuple[str, ...]
    cost_links: Tuple[str, ...]
    macro_links: Tuple[str, ...]
    indicators_to_measure: Tuple[str, ...]
    event_signals: Tuple[str, ...]
    time_horizon: Tuple[str, ...]
    calculation_notes: Tuple[str, ...]


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    primary_identity: str
    business_segments: Tuple[str, ...]
    geographies: Tuple[str, ...]
    upstream_assets: Tuple[str, ...]
    manufacturing_and_downstream: Tuple[str, ...]
    end_markets: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    raw_material_dependencies: Tuple[str, ...]
    energy_dependencies: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_dependencies: Tuple[str, ...]
    strategic_drivers: Tuple[str, ...]
    operational_risks: Tuple[str, ...]
    regulatory_and_transition_risks: Tuple[str, ...]
    key_indicators: Tuple[str, ...]
    event_types: Tuple[str, ...]
    market_characters: Dict[str, MarketCharacter]


def _mc(
    market: str,
    exposure_type: str,
    impact_channels: Tuple[str, ...],
    supply_chain_links: Tuple[str, ...],
    demand_links: Tuple[str, ...],
    cost_links: Tuple[str, ...],
    macro_links: Tuple[str, ...],
    indicators_to_measure: Tuple[str, ...],
    event_signals: Tuple[str, ...],
    time_horizon: Tuple[str, ...],
    calculation_notes: Tuple[str, ...],
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        exposure_type=exposure_type,
        impact_channels=impact_channels,
        supply_chain_links=supply_chain_links,
        demand_links=demand_links,
        cost_links=cost_links,
        macro_links=macro_links,
        indicators_to_measure=indicators_to_measure,
        event_signals=event_signals,
        time_horizon=time_horizon,
        calculation_notes=calculation_notes,
    )


COMPANY_CHARACTER = CompanyCharacter(
    symbol="TATASTEEL",
    company_name="Tata Steel Limited",
    primary_identity=(
        "Globally diversified integrated steel producer with captive and "
        "strategic raw-material assets, primary steelmaking, downstream "
        "value-added products, automotive and construction exposure, and an "
        "ongoing transition toward lower-emission steelmaking."
    ),
    business_segments=(
        "India steel business",
        "Tata Steel Nederland",
        "Tata Steel UK",
        "Tata Steel Thailand",
        "Tata Steel Minerals Canada",
        "Ferro alloys and minerals",
        "Downstream steel products",
        "Specialty/value-added steel",
        "Tubes and wires",
        "Tinplate and packaging steel",
        "Bearings and industrial products",
        "Engineering and fabrication",
        "Branded construction steel",
        "Recycling and circular steel",
    ),
    geographies=(
        "India",
        "Netherlands",
        "United Kingdom",
        "Thailand",
        "Canada",
        "Other international downstream markets",
    ),
    upstream_assets=(
        "Captive iron ore mines",
        "Captive coal mines",
        "Iron ore processing",
        "Coal beneficiation",
        "Chromite",
        "Manganese",
        "Ferroalloys",
        "Pellet supply",
        "Scrap sourcing",
        "Raw-material logistics",
    ),
    manufacturing_and_downstream=(
        "Sintering",
        "Coke and coal processing",
        "Blast furnace steelmaking",
        "Direct reduced iron where applicable",
        "Electric Arc Furnace steelmaking",
        "Continuous casting",
        "Hot rolling",
        "Cold rolling",
        "Galvanising",
        "Coating",
        "Tinplate",
        "Tubes",
        "Wires",
        "Bearings",
        "Downstream fabrication",
        "Specialty steel",
        "Recycling",
    ),
    end_markets=(
        "Construction and infrastructure",
        "Automotive and auto components",
        "Engineering and capital goods",
        "Energy",
        "Oil and gas",
        "Wind and solar",
        "Packaging",
        "Consumer durables",
        "Shipbuilding",
        "Manufacturing",
        "Retail construction",
        "Downstream processors",
    ),
    demand_drivers=(
        "Indian infrastructure spending",
        "Construction activity",
        "Automotive production",
        "Capital-goods investment",
        "Engineering demand",
        "Energy infrastructure",
        "Packaging demand",
        "Consumer durable production",
        "Global steel demand",
        "European industrial activity",
        "Asian industrial activity",
        "Steel replacement and repair demand",
    ),
    revenue_drivers=(
        "Steel volumes",
        "Realised steel prices",
        "Product mix",
        "Value-added steel mix",
        "Automotive volumes",
        "Construction volumes",
        "Export volumes",
        "Domestic market share",
        "Downstream volumes",
        "By-product sales",
        "Raw-material integration",
        "Regional steel spreads",
        "Scrap economics",
    ),
    raw_material_dependencies=(
        "Iron ore",
        "Coking coal",
        "PCI coal",
        "Scrap",
        "Limestone",
        "Dolomite",
        "Manganese",
        "Chromite",
        "Ferroalloys",
        "Pellets",
        "Steelmaking additives",
    ),
    energy_dependencies=(
        "Electricity",
        "Coking coal",
        "Natural gas",
        "Coal-derived energy",
        "Steam",
        "Industrial fuels",
        "Renewable electricity",
        "Grid availability",
    ),
    cost_drivers=(
        "Coking coal",
        "Iron ore",
        "Electricity",
        "Natural gas",
        "Freight",
        "Rail logistics",
        "Shipping",
        "Scrap",
        "Limestone and fluxes",
        "Ferroalloys",
        "Labour",
        "Maintenance",
        "Carbon and emissions costs",
        "Environmental compliance",
    ),
    supply_chain_dependencies=(
        "Mines",
        "Railways",
        "Ports",
        "Bulk shipping",
        "Raw-material handling",
        "Coal beneficiation",
        "Pellet plants",
        "Steel plants",
        "Distribution centres",
        "Automotive OEM supply chains",
        "Construction supply chains",
        "Energy infrastructure",
    ),
    strategic_drivers=(
        "Expand profitable Indian capacity",
        "Increase value-added steel",
        "Improve cost competitiveness",
        "Strengthen raw-material security",
        "Increase downstream integration",
        "Grow automotive and engineering products",
        "Decarbonise steelmaking",
        "Expand EAF and scrap-based steelmaking",
        "Develop DRI and low-carbon technologies",
        "Improve logistics efficiency",
        "Increase circularity and recycling",
        "Use Industry 4.0 and AI for productivity",
        "Strengthen global green-steel positioning",
    ),
    operational_risks=(
        "Steel-price volatility",
        "Coking-coal volatility",
        "Iron-ore volatility",
        "Plant outage",
        "Blast-furnace disruption",
        "EAF commissioning risk",
        "Raw-material logistics disruption",
        "Port disruption",
        "Rail disruption",
        "Energy shortage",
        "Demand slowdown",
        "Capacity ramp-up risk",
        "Quality issues",
        "Currency exposure",
    ),
    regulatory_and_transition_risks=(
        "Environmental regulation",
        "Carbon pricing",
        "EU CBAM",
        "UK decarbonisation requirements",
        "Indian emissions requirements",
        "Mine approvals",
        "Land and environmental permissions",
        "Energy-transition regulation",
        "Trade tariffs",
        "Import/export restrictions",
        "Steel quality standards",
    ),
    key_indicators=(
        "Crude steel production",
        "Steel deliveries",
        "Capacity utilisation",
        "Realised steel price",
        "EBITDA per tonne",
        "Steel spread",
        "Domestic sales",
        "Export sales",
        "Automotive sales",
        "Construction demand",
        "Value-added product mix",
        "Iron ore production",
        "Iron ore dispatch",
        "Coking coal consumption",
        "Coking coal cost",
        "Coal blend",
        "Scrap consumption",
        "Electricity consumption",
        "Natural gas consumption",
        "Freight and handling cost",
        "Working capital",
        "Inventory days",
        "Net debt",
        "Net debt / EBITDA",
        "Capex",
        "Project progress",
        "Plant utilisation",
        "Energy intensity",
        "Carbon intensity",
        "CO2 emissions",
        "Renewable-power share",
        "Free cash flow",
        "ROCE",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "Steel-price movement",
        "Coking-coal shock",
        "Iron-ore shock",
        "Capacity expansion",
        "New plant commissioning",
        "EAF commissioning",
        "Blast-furnace outage",
        "Plant maintenance",
        "Mine production change",
        "Raw-material supply disruption",
        "Rail disruption",
        "Port disruption",
        "Trade-tariff change",
        "EU CBAM development",
        "UK decarbonisation policy",
        "Major customer contract",
        "Automotive demand change",
        "Infrastructure spending change",
        "Acquisition",
        "Strategic partnership",
        "Capital expenditure update",
        "Debt/refinancing event",
        "Management guidance",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market beta plus Indian industrial and steel-cycle exposure",
        (
            "Market beta",
            "Industrial-cycle sentiment",
            "Infrastructure sentiment",
            "Equity valuation",
            "Institutional flows",
        ),
        (
            "Capital-market access",
            "Industrial investment cycle",
            "Institutional ownership",
        ),
        (
            "Indian GDP growth",
            "Infrastructure spending",
            "Automotive production",
            "Capital expenditure",
        ),
        (
            "Valuation multiple",
            "Funding conditions",
            "Capex financing",
        ),
        (
            "GDP growth",
            "Interest rates",
            "Inflation",
            "Infrastructure spending",
            "Risk appetite",
        ),
        (
            "Rolling beta",
            "Rolling correlation",
            "Steel-sector relative strength",
            "Industrial PMI",
            "Volatility",
        ),
        (
            "Quarterly results",
            "Steel-price cycle",
            "Capex announcements",
            "Government infrastructure spending",
            "Trade policy",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Control for broad market and metal-sector effects.",
            "Calculate residual Tata Steel returns before testing commodity-specific relationships.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect but meaningful fuel, freight, inflation and industrial-cycle exposure",
        (
            "Freight cost",
            "Shipping cost",
            "Fuel cost",
            "Industrial inflation",
            "Steel demand through macro activity",
        ),
        (
            "Raw-material logistics",
            "Bulk shipping",
            "Road transport",
            "Port operations",
        ),
        (
            "Industrial demand",
            "Infrastructure spending",
            "Automotive production",
            "Energy-sector capex",
        ),
        (
            "Freight",
            "Fuel",
            "Logistics",
            "Input-cost inflation",
        ),
        (
            "Inflation",
            "Global growth",
            "Interest rates",
            "Energy investment",
        ),
        (
            "Crude return",
            "Freight index",
            "Fuel expense",
            "Steel demand",
            "EBITDA/tonne",
            "Free cash flow",
        ),
        (
            "Oil-price spike",
            "Freight shock",
            "Energy inflation",
            "Global growth shock",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Crude is not a primary steel raw material.",
            "Separate freight/fuel cost from the macro-demand channel.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Primarily macro, risk and real-rate exposure",
        (
            "Risk appetite",
            "Inflation expectations",
            "Real-rate signal",
            "Commodity sentiment",
        ),
        (
            "No major direct gold input",
            "Indirect macro and capital-market channel",
        ),
        (
            "Industrial investment through macro conditions",
            "Risk-on/risk-off cycle",
        ),
        (
            "Limited direct steelmaking cost",
        ),
        (
            "Real rates",
            "USD",
            "Inflation",
            "Global risk aversion",
        ),
        (
            "Gold return",
            "Real yields",
            "USD",
            "VIX/risk proxy",
            "Steel residual return",
        ),
        (
            "Gold breakout",
            "Real-rate shock",
            "Global risk-off event",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Use gold as a macro regime variable, not a steel input.",
            "Control for NIFTY and rates before attribution.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial-metal and macro-cycle exposure",
        (
            "Industrial-cycle signal",
            "Commodity sentiment",
            "Risk appetite",
            "Electrification-cycle signal",
        ),
        (
            "No major direct silver input",
            "Indirect industrial ecosystem",
        ),
        (
            "Industrial production",
            "Infrastructure",
            "Manufacturing activity",
        ),
        (
            "Limited direct production-cost linkage",
        ),
        (
            "Global growth",
            "Industrial PMI",
            "Commodity inflation",
        ),
        (
            "Silver return",
            "Industrial PMI",
            "Metal basket",
            "Steel demand",
            "Residual stock return",
        ),
        (
            "Industrial slowdown",
            "Commodity-cycle reversal",
            "Global growth shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Use silver mainly to identify industrial and commodity regimes.",
            "Do not treat it as a primary steelmaking input.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Meaningful energy and steelmaking-cost exposure",
        (
            "Process energy",
            "Heating and reheating",
            "DRI/EAF economics where applicable",
            "Energy transition",
            "Industrial demand",
        ),
        (
            "Steel plants",
            "DRI facilities",
            "Reheating furnaces",
            "Downstream processing",
            "Energy infrastructure",
        ),
        (
            "Power and industrial demand",
            "Steel demand through energy investment",
        ),
        (
            "Natural-gas consumption",
            "Process heat",
            "Fuel switching",
            "Energy cost",
        ),
        (
            "Global gas prices",
            "Power prices",
            "Industrial inflation",
            "Energy transition",
        ),
        (
            "Natural-gas return",
            "Gas consumption",
            "Energy cost/tonne",
            "EBITDA/tonne",
            "Energy intensity",
            "Production",
        ),
        (
            "Gas-price spike",
            "Supply disruption",
            "Fuel-switching event",
            "Energy-policy change",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Use plant-level fuel mix wherever disclosed.",
            "Separate gas used as process energy from broad macro energy effects.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect industrial-demand, capex and equipment-cost exposure",
        (
            "Electrical equipment cost",
            "Industrial capex",
            "Infrastructure demand",
            "Manufacturing cycle",
        ),
        (
            "Electrical equipment",
            "Motors",
            "Transformers",
            "Plant construction",
            "Power infrastructure",
        ),
        (
            "Infrastructure",
            "Power-grid investment",
            "Automotive",
            "Engineering goods",
            "Capital goods",
        ),
        (
            "Electrical equipment",
            "Plant capex",
            "Maintenance",
        ),
        (
            "Industrial growth",
            "Electrification",
            "Infrastructure spending",
            "Commodity inflation",
        ),
        (
            "Copper return",
            "Industrial PMI",
            "Capex",
            "PP&E",
            "Steel demand",
            "Equipment cost",
        ),
        (
            "Copper shock",
            "Infrastructure-cycle change",
            "Industrial slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Copper is mainly a demand/capex and equipment variable for Tata Steel.",
            "Validate materiality using procurement and capex data.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect metal-cycle, downstream competition/substitution and equipment-cost exposure",
        (
            "Industrial-cycle signal",
            "Material substitution",
            "Automotive demand",
            "Packaging and engineering demand",
            "Equipment/capex cost",
        ),
        (
            "Industrial equipment",
            "Automotive supply chain",
            "Construction",
            "Engineering",
        ),
        (
            "Automotive production",
            "Construction",
            "Capital goods",
            "Consumer durables",
        ),
        (
            "Equipment",
            "Plant construction",
            "Material substitution economics",
        ),
        (
            "Industrial growth",
            "Metal substitution",
            "Commodity cycle",
            "Automotive cycle",
        ),
        (
            "Aluminium return",
            "Steel/aluminium spread",
            "Auto production",
            "Industrial PMI",
            "Capex",
            "Value-added product demand",
        ),
        (
            "Aluminium price shock",
            "Substitution event",
            "Auto/industrial cycle change",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Aluminium should be analysed as a competing/substitute material and industrial-cycle signal.",
            "Do not treat aluminium as a simple direct Tata Steel input.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Meaningful galvanised-steel value-chain and construction/auto exposure",
        (
            "Galvanised steel economics",
            "Coated-steel demand",
            "Construction",
            "Automotive",
            "Infrastructure",
        ),
        (
            "Galvanising",
            "Coated steel",
            "Construction steel",
            "Automotive steel",
            "Zinc procurement",
        ),
        (
            "Construction",
            "Automotive",
            "Infrastructure",
            "Engineering",
        ),
        (
            "Zinc coating cost",
            "Galvanising economics",
            "Downstream product margin",
        ),
        (
            "Construction cycle",
            "Auto cycle",
            "Infrastructure spending",
            "Metal prices",
        ),
        (
            "Zinc return",
            "Galvanised-steel spread",
            "Coated-steel volume",
            "Zinc consumption",
            "Construction demand",
            "Auto demand",
        ),
        (
            "Zinc-price shock",
            "Galvanising-margin change",
            "Construction cycle",
            "Auto-cycle change",
        ),
        ("1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Zinc has a more specific downstream linkage than gold or silver because Tata Steel has coated/galvanised products.",
            "Measure zinc price against coated-steel spreads and actual zinc consumption.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Core steelmaking operating-cost, production and transition exposure",
        (
            "Steelmaking energy cost",
            "EAF economics",
            "Rolling and finishing energy",
            "Plant uptime",
            "Grid reliability",
            "Decarbonisation",
        ),
        (
            "Steel plants",
            "EAF",
            "Rolling mills",
            "Finishing lines",
            "Captive/contract power",
            "Renewable power",
        ),
        (
            "Electricity demand from industrial growth",
            "Grid expansion",
            "Renewable infrastructure",
            "Industrial investment",
        ),
        (
            "Power consumption",
            "EAF electricity",
            "Rolling-mill electricity",
            "Energy contracts",
            "Power procurement",
        ),
        (
            "Power prices",
            "Grid reliability",
            "Renewable availability",
            "Energy policy",
            "Carbon economics",
        ),
        (
            "Electricity price",
            "Power consumption",
            "Energy cost/tonne",
            "EAF utilisation",
            "Production",
            "EBITDA/tonne",
            "Energy intensity",
            "Renewable share",
        ),
        (
            "Power-price spike",
            "Grid disruption",
            "EAF outage",
            "Renewable-power event",
            "Energy contract change",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M"),
        (
            "Electricity is a core Tata Steel operating variable, especially as EAF and lower-emission routes expand.",
            "Calculate plant-level electricity intensity and lagged margin impact wherever data permits.",
            "Separate electricity-price effects from steel-price and raw-material effects.",
        ),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    **{
        **COMPANY_CHARACTER.__dict__,
        "market_characters": MARKET_CHARACTERS,
    }
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Tata Steel company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one market character from the fixed nine-market universe."""
    normalized = market.strip()
    if normalized not in MARKET_CHARACTERS:
        raise KeyError(
            f"Unsupported market: {market!r}. "
            f"Supported markets: {', '.join(TRACKED_MARKETS)}"
        )
    return MARKET_CHARACTERS[normalized]


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine market characters."""
    return dict(MARKET_CHARACTERS)


def validate_character() -> dict:
    """Structural validation only; historical impact is calculated elsewhere."""
    markets = tuple(MARKET_CHARACTERS.keys())
    missing = tuple(m for m in TRACKED_MARKETS if m not in MARKET_CHARACTERS)
    extra = tuple(m for m in markets if m not in TRACKED_MARKETS)

    return {
        "symbol": COMPANY_CHARACTER.symbol,
        "valid": not missing and not extra and len(markets) == 9,
        "market_count": len(markets),
        "expected_market_count": 9,
        "missing_markets": missing,
        "extra_markets": extra,
        "hard_coded_result_fields_present": False,
        "historical_calculation_required": True,
    }


if __name__ == "__main__":
    result = validate_character()
    print("TATASTEEL character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
