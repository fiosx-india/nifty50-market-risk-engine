"""
TMPV Character Model
====================
Tata Motors Passenger Vehicles Limited.

Business character + nine tracked market characters.

The model deliberately does not copy the supplied RANK/PCT_CHANGE/
LINKAGE_SCORE/RELATION values. Those are observations or prior outputs,
not permanent company-character facts. Historical impact must be estimated
from real data with appropriate lags, controls and event studies.
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
    passenger_vehicle_portfolio: Tuple[str, ...]
    powertrain_character: Tuple[str, ...]
    ev_character: Tuple[str, ...]
    customer_and_market_channels: Tuple[str, ...]
    manufacturing_and_value_chain: Tuple[str, ...]
    technology_and_rd: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    commodity_dependencies: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_dependencies: Tuple[str, ...]
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
    symbol="TMPV",
    company_name="Tata Motors Passenger Vehicles Limited",
    primary_identity=(
        "Indian passenger-vehicle business focused on SUVs, hatchbacks, "
        "CNG and electric mobility, with a multi-powertrain portfolio, "
        "large domestic distribution network, manufacturing operations, "
        "supplier ecosystem and technology-led product development."
    ),
    business_segments=(
        "Passenger Vehicles",
        "Electric Vehicles",
        "Connected and technology-enabled vehicles",
        "Passenger-vehicle after-sales and service ecosystem",
        "International passenger-vehicle business",
    ),
    passenger_vehicle_portfolio=(
        "SUVs",
        "Hatchbacks",
        "Sedans",
        "Compact SUVs",
        "Mid-size SUVs",
        "Premium SUVs",
        "CNG passenger vehicles",
        "ICE passenger vehicles",
        "Electric passenger vehicles",
        "New-generation vehicle platforms",
        "Punch",
        "Nexon",
        "Curvv",
        "Harrier",
        "Safari",
        "Tiago",
        "Tigor",
        "Sierra and future products",
    ),
    powertrain_character=(
        "Internal combustion engines",
        "CNG",
        "Battery electric vehicles",
        "Multi-powertrain strategy",
        "Powertrain localisation",
        "Battery and electric-drive integration",
        "Charging ecosystem",
        "Energy-efficiency engineering",
    ),
    ev_character=(
        "Tata EV passenger vehicles",
        "EV product launches",
        "Battery systems",
        "Electric drive systems",
        "Charging ecosystem",
        "Connected EV software",
        "EV service capability",
        "Battery sourcing",
        "Localisation",
        "EV cost reduction",
        "EV customer adoption",
    ),
    customer_and_market_channels=(
        "Private buyers",
        "Urban consumers",
        "Rural/semi-urban consumers",
        "Fleet and institutional customers",
        "Dealers",
        "Retail financing ecosystem",
        "Digital lead generation",
        "Test-drive network",
        "After-sales service",
        "Parts distribution",
        "Used-car ecosystem",
        "Exports",
    ),
    manufacturing_and_value_chain=(
        "Vehicle design",
        "Platform development",
        "Powertrain engineering",
        "Battery integration",
        "Component sourcing",
        "Steel and aluminium body structures",
        "Castings",
        "Electrical/electronic systems",
        "Semiconductors",
        "Tyres and rubber",
        "Glass",
        "Plastics and polymers",
        "Paints and coatings",
        "Seat/interior systems",
        "Transmission systems",
        "Assembly",
        "Quality control",
        "Logistics",
        "Warehousing",
        "Dealer distribution",
        "Service and spare parts",
    ),
    technology_and_rd=(
        "Vehicle architecture",
        "EV technology",
        "Battery technology",
        "Connected-car systems",
        "ADAS and safety technology",
        "Infotainment",
        "Software-defined vehicle capabilities",
        "Powertrain efficiency",
        "CNG technology",
        "Design and styling",
        "Crash and safety engineering",
        "Localisation",
        "Supplier engineering",
    ),
    demand_drivers=(
        "Household income",
        "Consumer confidence",
        "Vehicle affordability",
        "Interest rates",
        "Vehicle financing availability",
        "Fuel prices",
        "CNG economics",
        "EV running-cost advantage",
        "SUV preference",
        "New model launches",
        "Product freshness",
        "Safety perception",
        "Technology features",
        "Brand preference",
        "Rural demand",
        "Urban demand",
        "Fleet demand",
        "Government incentives",
        "Charging infrastructure",
    ),
    revenue_drivers=(
        "Wholesale volumes",
        "Retail registrations",
        "Average selling price",
        "SUV mix",
        "EV mix",
        "CNG mix",
        "Premium mix",
        "Model mix",
        "New launches",
        "Market share",
        "Dealer inventory",
        "Export volumes",
        "After-sales revenue",
        "Parts revenue",
        "Accessories",
        "Financing conversion",
    ),
    commodity_dependencies=(
        "Crude oil",
        "Aluminium",
        "Steel",
        "Copper",
        "Zinc",
        "Natural gas",
        "Electricity",
        "Rubber",
        "Plastics and petrochemicals",
        "Glass",
        "Lithium and battery materials",
        "Semiconductors",
        "Precious metals in electronics",
    ),
    cost_drivers=(
        "Raw materials",
        "Steel",
        "Aluminium",
        "Copper",
        "Zinc",
        "Battery materials",
        "Energy",
        "Electricity",
        "Natural gas",
        "Fuel",
        "Freight",
        "Logistics",
        "Semiconductors",
        "Tyres",
        "Plastics",
        "Wages",
        "Warranty",
        "Marketing",
        "R&D",
        "Dealer incentives",
        "Foreign exchange",
    ),
    supply_chain_dependencies=(
        "Tier-1 suppliers",
        "Tier-2 suppliers",
        "Steel suppliers",
        "Aluminium suppliers",
        "Copper/electrical suppliers",
        "Battery suppliers",
        "Semiconductor suppliers",
        "Tyre suppliers",
        "Plastic/polymer suppliers",
        "Glass suppliers",
        "Logistics providers",
        "Ports",
        "Dealers",
        "Charging ecosystem",
    ),
    strategic_drivers=(
        "Strengthen SUV portfolio",
        "Expand EV portfolio",
        "Improve EV economics",
        "Scale CNG portfolio",
        "Increase product freshness",
        "Improve market share",
        "Expand premiumisation",
        "Increase localisation",
        "Develop new vehicle platforms",
        "Improve after-sales service",
        "Expand charging ecosystem",
        "Improve manufacturing efficiency",
        "Digitise customer journey",
        "Strengthen export markets",
        "Reduce vehicle cost",
    ),
    operational_risks=(
        "Commodity-price volatility",
        "Supply-chain disruption",
        "Semiconductor shortages",
        "Battery-material price volatility",
        "Model-launch execution risk",
        "Dealer inventory build-up",
        "Demand slowdown",
        "EV competition",
        "Price competition",
        "Warranty/quality risk",
        "Manufacturing disruption",
        "Logistics disruption",
        "Foreign-exchange risk",
        "Technology obsolescence",
        "Cybersecurity risk",
    ),
    regulatory_and_market_risks=(
        "Emission regulations",
        "Fuel-economy requirements",
        "EV policy",
        "CNG policy",
        "Vehicle safety regulation",
        "Crash-test requirements",
        "Battery regulation",
        "Battery recycling requirements",
        "Import duties",
        "GST/tax changes",
        "FAME/EV incentive changes",
        "Scrappage policy",
        "Environmental regulation",
        "Data/privacy requirements for connected vehicles",
    ),
    key_indicators=(
        "Wholesale sales",
        "Retail registrations",
        "Market share",
        "SUV market share",
        "EV market share",
        "CNG volumes",
        "EV volumes",
        "ICE volumes",
        "Average selling price",
        "Revenue",
        "EBITDA",
        "EBITDA margin",
        "PBT",
        "Free cash flow",
        "Dealer inventory",
        "Days inventory",
        "New model volumes",
        "Launch contribution",
        "Export volumes",
        "After-sales revenue",
        "Warranty cost",
        "Material cost",
        "Employee cost",
        "R&D spend",
        "Capex",
        "Plant utilisation",
        "Capacity",
        "Battery cost",
        "EV gross margin",
        "Working capital",
        "Net debt",
    ),
    event_types=(
        "Monthly sales",
        "Quarterly results",
        "Annual results",
        "New model launch",
        "EV launch",
        "CNG launch",
        "Price increase",
        "Discount/incentive change",
        "Commodity-price shock",
        "Battery-material shock",
        "Semiconductor disruption",
        "Production shutdown",
        "Plant expansion",
        "Capacity expansion",
        "EV policy change",
        "Emission regulation",
        "Safety regulation",
        "Major recall",
        "Major order/fleet contract",
        "Dealer network expansion",
        "Export-market event",
        "Charging partnership",
        "Technology partnership",
        "Management guidance",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market beta plus Indian auto/consumer/economic-cycle exposure",
        (
            "Equity beta",
            "Consumer confidence",
            "Economic growth",
            "Vehicle-financing sentiment",
            "Risk appetite",
        ),
        (
            "Equity liquidity",
            "Auto-sector capital flows",
            "Supplier financing conditions",
        ),
        (
            "Household income",
            "Vehicle affordability",
            "Urban demand",
            "Rural demand",
            "Fleet demand",
        ),
        (
            "Financing cost",
            "Dealer funding",
            "Capital-market conditions",
        ),
        (
            "GDP growth",
            "Interest rates",
            "Inflation",
            "Consumer confidence",
            "Liquidity",
        ),
        (
            "Rolling beta",
            "Rolling correlation",
            "Auto-sector relative strength",
            "Retail registration growth",
            "Volatility",
        ),
        (
            "Quarterly results",
            "Monthly auto sales",
            "Management guidance",
            "New-model launches",
            "Policy changes",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Control for NIFTY before estimating commodity-specific effects.",
            "Use residual stock returns to isolate non-market effects.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Meaningful indirect exposure through fuel affordability, petrochemical inputs, logistics and inflation",
        (
            "Fuel affordability",
            "Petrochemical input costs",
            "Tyre/plastic/rubber costs",
            "Freight",
            "Consumer inflation",
            "Vehicle running-cost perception",
        ),
        (
            "Petrochemical materials",
            "Plastics",
            "Rubber",
            "Tyres",
            "Paints",
            "Logistics",
            "Freight",
        ),
        (
            "Fuel affordability",
            "Vehicle purchase decision",
            "Consumer confidence",
            "Fleet economics",
            "Rural purchasing power",
        ),
        (
            "Petrochemical materials",
            "Plastic components",
            "Rubber",
            "Freight",
            "Logistics",
        ),
        (
            "Inflation",
            "Disposable income",
            "Interest rates",
            "Currency",
        ),
        (
            "Crude return",
            "Fuel prices",
            "CPI",
            "Freight cost",
            "Material-cost index",
            "PV volumes",
            "EV share",
            "CNG share",
            "EBITDA margin",
        ),
        (
            "Oil-price spike",
            "Fuel-price shock",
            "Inflation surprise",
            "Consumer-demand slowdown",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Separate demand impact from raw-material/logistics impact.",
            "For vehicle demand, test fuel prices and crude with lags rather than using same-day correlation alone.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Indirect macro/wealth/risk-sentiment exposure; not a core automotive input",
        (
            "Household wealth",
            "Risk appetite",
            "Savings allocation",
            "Consumer confidence",
        ),
        (
            "Household balance sheets",
            "Consumer financing",
            "Retail liquidity",
        ),
        (
            "Discretionary vehicle demand",
            "Premium vehicle demand",
            "Consumer confidence",
        ),
        (
            "No major direct production-cost channel",
            "Potential indirect financing/wealth channel",
        ),
        (
            "Real rates",
            "Inflation",
            "Risk aversion",
            "Household wealth",
            "Currency",
        ),
        (
            "Gold return",
            "Gold volatility",
            "Vehicle registrations",
            "Consumer confidence",
            "Auto-loan growth",
            "PV volumes",
        ),
        (
            "Gold-price shock",
            "Risk-off event",
            "Household wealth shift",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Do not interpret a raw gold correlation as a physical-input relationship.",
            "Test gold through wealth, risk and financing variables.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial-cycle and electronics/material sentiment exposure",
        (
            "Industrial cycle",
            "Electronics/material sentiment",
            "Risk appetite",
        ),
        (
            "Electrical components",
            "Electronics",
            "Industrial suppliers",
        ),
        (
            "Industrial activity",
            "Consumer confidence",
            "Technology adoption",
        ),
        (
            "Minor component/material exposure",
            "Supplier cost changes",
        ),
        (
            "Industrial growth",
            "Risk sentiment",
            "Commodity cycle",
        ),
        (
            "Silver return",
            "Industrial production",
            "Electronics input costs",
            "PV volumes",
            "EV volumes",
            "Margin",
        ),
        (
            "Silver-price shock",
            "Industrial slowdown",
            "Electronics supply shock",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Silver should remain a secondary variable unless product-level sourcing data shows a stronger channel.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect manufacturing-energy and supplier-cost exposure",
        (
            "Factory energy",
            "Process heat",
            "Supplier energy",
            "Industrial inflation",
        ),
        (
            "Metal processing",
            "Glass",
            "Paints",
            "Component manufacturing",
            "Battery manufacturing",
        ),
        (
            "Industrial activity",
            "Vehicle supply",
            "Consumer demand through inflation",
        ),
        (
            "Factory energy",
            "Supplier energy",
            "Material processing",
        ),
        (
            "Energy inflation",
            "Industrial production",
            "Power prices",
        ),
        (
            "Natural-gas return",
            "Factory utility cost",
            "Supplier inflation",
            "Plant utilisation",
            "Material cost",
            "EBITDA margin",
        ),
        (
            "Gas-price spike",
            "Industrial energy shock",
            "Supplier disruption",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Treat gas mainly as a manufacturing/supplier variable.",
            "Use plant-level energy data where available.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Meaningful vehicle electrical/electronic, wiring, motor and EV-system input exposure",
        (
            "Wiring cost",
            "Electrical systems",
            "Motor systems",
            "EV power electronics",
            "Electronic components",
            "Charging hardware",
        ),
        (
            "Wiring harness",
            "Motors",
            "Electrical components",
            "Power electronics",
            "Charging systems",
            "Supplier manufacturing",
        ),
        (
            "EV adoption",
            "Feature-rich vehicles",
            "Connected vehicles",
            "Electrification",
        ),
        (
            "Copper procurement",
            "Electrical components",
            "Motor components",
            "Harnesses",
        ),
        (
            "Electrification cycle",
            "Industrial growth",
            "EV investment",
        ),
        (
            "Copper return",
            "Copper input-cost index",
            "EV volumes",
            "Electrical-component cost",
            "Material cost",
            "Gross margin",
        ),
        (
            "Copper-price shock",
            "Electrical-component disruption",
            "EV supply-chain event",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Copper exposure is stronger for EVs and electronics than for the whole vehicle portfolio.",
            "Estimate weighted exposure by powertrain and component content.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Direct and meaningful vehicle-material exposure through body structures, castings, components and lightweighting",
        (
            "Vehicle body material",
            "Castings",
            "Engine/transmission components",
            "EV lightweighting",
            "Battery-related structures",
            "Supplier input costs",
        ),
        (
            "Aluminium suppliers",
            "Castings",
            "Body structures",
            "Wheels/components",
            "Battery/EV structures",
        ),
        (
            "Lightweight vehicle demand",
            "EV efficiency",
            "Fuel efficiency",
            "Premium vehicle content",
        ),
        (
            "Aluminium procurement",
            "Casting cost",
            "Component cost",
            "Supplier pricing",
        ),
        (
            "Industrial cycle",
            "Auto cycle",
            "EV investment",
            "Commodity inflation",
        ),
        (
            "Aluminium return",
            "Aluminium input-cost index",
            "Vehicle material cost",
            "EV volumes",
            "SUV volumes",
            "Gross margin",
            "Material-cost percentage",
        ),
        (
            "Aluminium-price shock",
            "Supplier price revision",
            "Production disruption",
        ),
        ("1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Aluminium should be modelled through actual material content and procurement exposure.",
            "Separate price impact from demand/vehicle-mix effects.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Moderate indirect vehicle-input exposure through galvanised steel and corrosion-protection systems",
        (
            "Galvanised steel cost",
            "Body corrosion protection",
            "Sheet-metal input cost",
            "Supplier cost",
        ),
        (
            "Galvanised steel",
            "Auto sheet",
            "Stamping",
            "Body-in-white",
            "Corrosion-protection supply chain",
        ),
        (
            "Vehicle production",
            "Auto industrial cycle",
            "New model production",
        ),
        (
            "Zinc-coated steel",
            "Sheet-metal",
            "Supplier pricing",
        ),
        (
            "Steel cycle",
            "Industrial growth",
            "Construction/auto demand",
        ),
        (
            "Zinc return",
            "Galvanised-steel cost",
            "Steel cost",
            "Production volume",
            "Material cost",
            "Margin",
        ),
        (
            "Zinc-price shock",
            "Steel-price shock",
            "Supplier price revision",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "The channel is mainly zinc -> galvanising -> steel sheet -> vehicle body/component cost.",
            "Use steel and galvanised-sheet prices as mediating variables.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Direct manufacturing, assembly, battery/EV operations, tooling and facility-cost exposure",
        (
            "Plant operating cost",
            "Assembly cost",
            "Battery/EV manufacturing",
            "Machine utilisation",
            "Plant uptime",
            "Charging infrastructure",
        ),
        (
            "Vehicle plants",
            "Battery/EV facilities",
            "Paint shops",
            "Press shops",
            "Assembly lines",
            "Warehouses",
            "Supplier plants",
        ),
        (
            "Production capacity",
            "EV manufacturing",
            "New model ramp-up",
            "Plant utilisation",
        ),
        (
            "Electricity tariff",
            "Peak demand charges",
            "Factory power",
            "Charging infrastructure",
        ),
        (
            "Power prices",
            "Grid reliability",
            "Renewable electricity",
            "Industrial tariffs",
        ),
        (
            "Electricity price",
            "Power consumption",
            "Energy intensity",
            "Plant utilisation",
            "Production volume",
            "Manufacturing cost",
            "EBITDA margin",
        ),
        (
            "Power-price spike",
            "Grid outage",
            "Plant shutdown",
            "Renewable-power transition",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Measure electricity against plant-level manufacturing cost and production volumes.",
            "Do not confuse electricity-price effects with overall industrial demand effects.",
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
    """Return the complete TMPV business character."""
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
    """Structural validation only; impact is calculated by later research modules."""
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
    print("TMPV character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
