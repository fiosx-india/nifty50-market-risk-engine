"""
ULTRACEMCO Character Model
==========================
UltraTech Cement Limited.

Business character + nine tracked market characters.

The supplied CSV is NOT treated as permanent truth. RANK, PCT_CHANGE,
LINKAGE_SCORE and RELATION are intentionally excluded. Actual impact must
later be calculated from historical market data, company operating data,
cost data, capacity/utilisation, news/events and lag-aware models.
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
    cement_character: Tuple[str, ...]
    rmc_character: Tuple[str, ...]
    white_cement_and_building_products: Tuple[str, ...]
    building_solutions_character: Tuple[str, ...]
    cables_and_wires_character: Tuple[str, ...]
    manufacturing_and_supply_chain: Tuple[str, ...]
    energy_and_decarbonisation: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    commodity_dependencies: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    strategic_drivers: Tuple[str, ...]
    operational_risks: Tuple[str, ...]
    regulatory_and_market_risks: Tuple[str, ...]
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
    symbol="ULTRACEMCO",
    company_name="UltraTech Cement Limited",
    primary_identity=(
        "Large integrated building-solutions company centred on cement and "
        "cement-related products, with grey cement, ready-mix concrete, white "
        "cement, wall care/building products, a pan-India channel network and "
        "an expanding construction-materials portfolio."
    ),
    business_segments=(
        "Grey Cement",
        "Clinker",
        "Ready-Mix Concrete",
        "White Cement",
        "Wall Care Putty",
        "Building Products",
        "UltraTech Building Solutions",
        "Cement logistics and distribution",
        "Cables and Wires",
        "International cement operations",
    ),
    cement_character=(
        "Integrated cement plants",
        "Grinding units",
        "Clinkerisation",
        "Cement manufacturing",
        "Bulk cement",
        "Bagged cement",
        "Retail cement",
        "Institutional cement",
        "Infrastructure projects",
        "Residential construction",
        "Commercial construction",
        "Industrial construction",
    ),
    rmc_character=(
        "Ready-Mix Concrete",
        "Institutional construction",
        "Infrastructure projects",
        "Urban construction",
        "High-rise construction",
        "Speciality concrete",
        "Concrete solutions",
        "RMC plants",
        "Batching operations",
        "Aggregate/cement admixture supply",
    ),
    white_cement_and_building_products=(
        "Birla White",
        "White cement",
        "Wall Care Putty",
        "Construction chemicals and solutions",
        "Speciality building products",
        "New-age construction products",
    ),
    building_solutions_character=(
        "UltraTech Building Solutions",
        "One-stop construction-material model",
        "Individual home builders",
        "Masons and contractors",
        "Retail channel",
        "Construction advisory",
        "Multi-category construction products",
        "Digital customer engagement",
        "Channel-partner ecosystem",
    ),
    cables_and_wires_character=(
        "Ultravolt",
        "Wires",
        "Cables",
        "Residential electrical construction",
        "Building-material distribution",
        "Retailer network",
        "Electrician ecosystem",
        "Construction value-chain expansion",
        "New manufacturing capacity",
        "New-business ramp-up",
    ),
    manufacturing_and_supply_chain=(
        "Limestone mining",
        "Raw-material sourcing",
        "Clinker production",
        "Grinding",
        "Cement blending",
        "Packing",
        "Bulk dispatch",
        "Rail logistics",
        "Road logistics",
        "Ports and coastal logistics",
        "RMC aggregates",
        "Fly ash",
        "Slag",
        "Gypsum",
        "Alternative fuels",
        "Warehousing",
        "Dealer/channel network",
    ),
    energy_and_decarbonisation=(
        "Thermal power",
        "Waste Heat Recovery Systems",
        "Renewable power",
        "Green power",
        "Captive power",
        "Power procurement",
        "Fuel substitution",
        "Alternative fuels",
        "Clinker-factor reduction",
        "Carbon-efficiency",
        "Energy efficiency",
        "Net-zero concrete roadmap",
    ),
    demand_drivers=(
        "Housing construction",
        "Infrastructure spending",
        "Roads",
        "Railways",
        "Urbanisation",
        "Commercial construction",
        "Industrial capex",
        "Individual home builders",
        "Government capex",
        "Real-estate cycle",
        "Cement price",
        "Regional demand",
        "Monsoon",
        "Construction season",
    ),
    revenue_drivers=(
        "Cement volumes",
        "Realisation per tonne",
        "Cement prices",
        "Grey cement mix",
        "RMC volumes",
        "White cement volumes",
        "Wall-care products",
        "Building-products sales",
        "Channel expansion",
        "Institutional sales",
        "Retail sales",
        "Cables and wires volumes",
        "Capacity additions",
        "International volumes",
    ),
    commodity_dependencies=(
        "Petcoke",
        "Coal",
        "Imported coal",
        "Domestic coal",
        "Limestone",
        "Gypsum",
        "Fly ash",
        "Slag",
        "Crude-oil-linked fuels",
        "Natural gas where applicable",
        "Electricity",
        "Aluminium",
        "Copper",
        "Zinc",
        "Steel",
        "Cables and electrical inputs",
    ),
    cost_drivers=(
        "Fuel cost",
        "Petcoke",
        "Coal",
        "Power",
        "Electricity",
        "Freight",
        "Rail freight",
        "Road freight",
        "Limestone mining",
        "Gypsum",
        "Fly ash",
        "Slag",
        "Packaging",
        "Employee cost",
        "Maintenance",
        "Capex",
        "Cables/wires raw materials",
    ),
    strategic_drivers=(
        "Capacity expansion",
        "Scale beyond 200 MTPA",
        "Cement-market leadership",
        "Acquisition integration",
        "Network optimisation",
        "RMC expansion",
        "Building-products expansion",
        "UltraTech Building Solutions",
        "Cables and wires",
        "Green power",
        "Waste heat recovery",
        "Alternative fuels",
        "Clinker efficiency",
        "Logistics optimisation",
        "Premium products",
        "Channel expansion",
    ),
    operational_risks=(
        "Fuel-price volatility",
        "Power-price volatility",
        "Freight inflation",
        "Cement-price competition",
        "Demand slowdown",
        "Capacity under-utilisation",
        "Acquisition integration",
        "Plant outage",
        "Mining disruption",
        "Logistics disruption",
        "Monsoon disruption",
        "Environmental compliance",
        "New-business execution risk",
        "Working-capital risk",
    ),
    regulatory_and_market_risks=(
        "Mining permissions",
        "Environmental clearances",
        "Carbon regulation",
        "Emission norms",
        "GST",
        "Import duties on fuels",
        "Rail freight policy",
        "Power-market regulation",
        "Construction regulation",
        "Building standards",
        "Waste-management rules",
        "Renewable-power policy",
        "Cables and wires standards",
    ),
    key_indicators=(
        "Cement sales volume",
        "Grey cement volume",
        "Capacity utilisation",
        "Realisation per tonne",
        "Net sales",
        "PBIDT/EBITDA",
        "EBITDA per tonne",
        "Fuel cost per tonne",
        "Power cost per tonne",
        "Freight cost per tonne",
        "Petcoke price",
        "Coal price",
        "Blended fuel cost",
        "RMC volume",
        "White cement volume",
        "Wall-care volume",
        "Building-products revenue",
        "Channel partners",
        "Market reach",
        "Capacity",
        "New capacity commissioning",
        "Capex",
        "Green power share",
        "Renewable capacity",
        "WHRS capacity",
        "Alternative-fuel rate",
        "Clinker factor",
        "CO2 intensity",
        "Working capital",
        "Net debt",
        "Free cash flow",
        "Cables/wires capacity and volume",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "Monthly sales update",
        "Cement-price change",
        "Capacity commissioning",
        "Capacity expansion",
        "Acquisition",
        "Acquisition integration",
        "Plant shutdown",
        "Mining disruption",
        "Coal/petcoke price shock",
        "Power-price shock",
        "Freight-rate shock",
        "Government infrastructure spending",
        "Housing demand change",
        "Environmental regulation",
        "Carbon policy",
        "Green-power commissioning",
        "WHRS commissioning",
        "Cables and wires commissioning",
        "Management guidance",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity beta plus Indian infrastructure, construction and economic-cycle exposure",
        (
            "Equity beta",
            "Infrastructure sentiment",
            "Construction cycle",
            "Interest-rate sensitivity",
            "Risk appetite",
        ),
        (
            "Capital-market liquidity",
            "Infrastructure financing",
            "Construction-sector investment",
        ),
        (
            "Housing",
            "Infrastructure",
            "Commercial construction",
            "Industrial capex",
        ),
        (
            "Funding cost",
            "Capex financing",
            "Valuation multiple",
        ),
        (
            "GDP growth",
            "Interest rates",
            "Government capex",
            "Inflation",
            "Liquidity",
        ),
        (
            "Rolling beta",
            "Rolling correlation",
            "Construction-sector relative strength",
            "Cement volume growth",
            "Volatility",
        ),
        (
            "Quarterly results",
            "Government capex announcements",
            "Cement demand outlook",
            "Capacity expansion",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Control for NIFTY and construction-cycle variables before attributing residual stock moves to commodities.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Meaningful indirect exposure through petcoke/fuel, freight, packaging and inflation",
        (
            "Fuel cost",
            "Petcoke economics",
            "Freight",
            "Logistics",
            "Inflation",
        ),
        (
            "Road freight",
            "Rail logistics",
            "Coastal logistics",
            "Fuel supply",
            "Packaging",
        ),
        (
            "Construction affordability",
            "Housing demand",
            "Infrastructure activity",
            "Industrial capex",
        ),
        (
            "Fuel",
            "Petcoke",
            "Freight",
            "Packaging",
        ),
        (
            "Inflation",
            "Interest rates",
            "Construction costs",
            "Industrial activity",
        ),
        (
            "Crude return",
            "Petcoke price",
            "Fuel cost per tonne",
            "Freight cost per tonne",
            "Cement volume",
            "EBITDA per tonne",
        ),
        (
            "Oil-price spike",
            "Petcoke shock",
            "Freight shock",
            "Inflation surprise",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Use petcoke/coal/fuel and freight as mediating variables.",
            "Do not assume crude moves cement earnings one-for-one.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Indirect macro, real-rate and risk-sentiment exposure",
        (
            "Risk appetite",
            "Real rates",
            "Household wealth",
            "Investment sentiment",
        ),
        (
            "No major direct cement-input pathway",
            "Construction financing sentiment",
        ),
        (
            "Housing wealth",
            "Construction confidence",
            "Investment cycle",
        ),
        (
            "No major direct production-cost channel",
        ),
        (
            "Real rates",
            "Inflation",
            "Risk aversion",
            "Currency",
        ),
        (
            "Gold return",
            "Gold volatility",
            "Cement volume",
            "Infrastructure spending",
            "Construction activity",
        ),
        (
            "Gold-price shock",
            "Risk-off event",
            "Real-rate shock",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Gold is not a primary UltraTech input.",
            "Use it mainly as a macro/risk control variable.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial-cycle and infrastructure sentiment exposure",
        (
            "Industrial cycle",
            "Electrification sentiment",
            "Commodity risk appetite",
        ),
        (
            "No major direct cement-input pathway",
            "Electrical/infrastructure ecosystem",
        ),
        (
            "Industrial capex",
            "Infrastructure",
            "Construction cycle",
        ),
        (
            "Minor equipment/electrical exposure",
        ),
        (
            "Industrial production",
            "Commodity cycle",
            "Risk sentiment",
        ),
        (
            "Silver return",
            "Industrial production",
            "Cement volumes",
            "Infrastructure spending",
            "Capex",
        ),
        (
            "Silver-price shock",
            "Industrial slowdown",
            "Commodity shock",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Keep silver secondary unless actual equipment/material procurement data shows a stronger link.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Energy and industrial-cost exposure, with importance varying by plant/fuel mix",
        (
            "Industrial energy",
            "Process heat",
            "Supplier energy",
            "Power-market interaction",
        ),
        (
            "Cement manufacturing",
            "RMC operations",
            "Building-products suppliers",
            "Industrial suppliers",
        ),
        (
            "Industrial activity",
            "Construction demand",
            "Energy-intensive project activity",
        ),
        (
            "Energy cost",
            "Supplier processing cost",
        ),
        (
            "Energy inflation",
            "Industrial production",
            "Power prices",
        ),
        (
            "Natural-gas return",
            "Plant fuel mix",
            "Energy cost per tonne",
            "Cement volume",
            "EBITDA per tonne",
        ),
        (
            "Gas-price shock",
            "Industrial energy shock",
            "Supplier disruption",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Model natural gas according to actual plant-level fuel usage.",
            "Do not treat gas as equivalent to petcoke/coal across all plants.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect electrical, equipment, capex and cables/wires exposure",
        (
            "Electrical equipment",
            "Plant maintenance",
            "Capex",
            "Cables and wires business input",
        ),
        (
            "Plant electrical systems",
            "Transformers",
            "Motors",
            "Cables",
            "Building-products infrastructure",
        ),
        (
            "Construction",
            "Electrical infrastructure",
            "Building-material demand",
        ),
        (
            "Electrical equipment",
            "Cables/wires raw material",
            "Plant capex",
        ),
        (
            "Industrial capex",
            "Electrification",
            "Construction cycle",
        ),
        (
            "Copper return",
            "Equipment cost",
            "Capex",
            "Cables/wires input cost",
            "Cement volume",
            "EBITDA",
        ),
        (
            "Copper-price shock",
            "Electrical-equipment shock",
            "Cables/wires input-cost shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Copper is secondary to cement but gains a distinct channel through electrical infrastructure and the new cables/wires business.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect equipment, packaging, electrical infrastructure and building-products exposure",
        (
            "Plant equipment",
            "Electrical systems",
            "Packaging",
            "Building-material products",
            "Cables/wires ecosystem",
        ),
        (
            "Equipment suppliers",
            "Electrical equipment",
            "Packaging",
            "Building-products suppliers",
        ),
        (
            "Construction",
            "Building products",
            "Infrastructure",
            "Industrial capex",
        ),
        (
            "Equipment",
            "Packaging",
            "Electrical systems",
        ),
        (
            "Industrial cycle",
            "Construction cycle",
            "Commodity inflation",
        ),
        (
            "Aluminium return",
            "Equipment cost",
            "Capex",
            "Building-products revenue",
            "Cement volume",
            "Margin",
        ),
        (
            "Aluminium-price shock",
            "Equipment-cost shock",
            "Construction-material shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Aluminium is not a core cement fuel/input variable.",
            "Test it through equipment, building products and construction activity.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect galvanised-steel, plant infrastructure and construction-cycle exposure",
        (
            "Galvanised steel",
            "Plant infrastructure",
            "Equipment",
            "Construction cycle",
        ),
        (
            "Cement plants",
            "Steel structures",
            "Warehouses",
            "RMC infrastructure",
            "Building-material facilities",
        ),
        (
            "Construction",
            "Infrastructure",
            "Industrial capex",
        ),
        (
            "Steel structures",
            "Plant maintenance",
            "Equipment",
        ),
        (
            "Construction cycle",
            "Industrial growth",
            "Commodity inflation",
        ),
        (
            "Zinc return",
            "Steel cost",
            "Capex",
            "Plant maintenance",
            "Cement demand",
        ),
        (
            "Zinc-price shock",
            "Steel-price shock",
            "Construction slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "The main channel is zinc -> galvanising -> steel structures/equipment -> capex.",
            "Use steel prices as a mediating variable.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Primary operating-cost and production-availability exposure for cement manufacturing",
        (
            "Grinding power",
            "Clinker production",
            "Crushing",
            "Material handling",
            "RMC operations",
            "Plant uptime",
            "Green-power economics",
        ),
        (
            "Integrated plants",
            "Grinding units",
            "Clinker units",
            "RMC plants",
            "Bulk terminals",
            "Warehouses",
        ),
        (
            "Production capacity",
            "Plant utilisation",
            "Construction demand",
            "Capacity expansion",
        ),
        (
            "Power tariff",
            "Captive power",
            "Renewable power",
            "WHRS",
            "Grid power",
        ),
        (
            "Power prices",
            "Grid reliability",
            "Renewable availability",
            "Industrial tariffs",
        ),
        (
            "Electricity price",
            "Power cost per tonne",
            "Power consumption per tonne",
            "Plant utilisation",
            "Cement volume",
            "EBITDA per tonne",
            "Green-power share",
        ),
        (
            "Power-price spike",
            "Grid disruption",
            "Plant outage",
            "Renewable commissioning",
            "WHRS commissioning",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M"),
        (
            "Electricity must be treated as a core cement operating variable.",
            "Separate tariff effects from utilisation and demand effects.",
            "Track green power and WHRS because they can change sensitivity to grid/fossil power prices.",
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
    """Return the complete UltraTech business character."""
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
    """Structural validation only; actual market impact is calculated later."""
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
    print("ULTRACEMCO character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
