"""
NTPC Character Engine
---------------------
Purpose:
    Define NTPC's business character and its structural relationship with the
    nine tracked markets. This file intentionally does NOT hard-code:
    RANK, PCT_CHANGE, LINKAGE_SCORE, correlation, beta, probability,
    trading decisions, or fixed relationship scores.

    Historical/real-time calculations should be performed by the later
    analysis layer using observed data, lags, events, volume, and
    market/company fundamentals.

Company:
    NTPC Limited

Tracked markets:
    1. NIFTY 50
    2. Crude Oil
    3. Gold
    4. Silver
    5. Natural Gas
    6. Copper
    7. Aluminium
    8. Zinc
    9. Electricity
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


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
    """How a tracked market can transmit information into NTPC."""

    market: str
    character: str
    direct_exposure: Tuple[str, ...] = ()
    indirect_exposure: Tuple[str, ...] = ()
    impact_channels: Tuple[str, ...] = ()
    supply_chain_links: Tuple[str, ...] = ()
    demand_channels: Tuple[str, ...] = ()
    cost_channels: Tuple[str, ...] = ()
    strategic_channels: Tuple[str, ...] = ()
    key_indicators: Tuple[str, ...] = ()
    event_signals: Tuple[str, ...] = ()
    calculation_logic: Tuple[str, ...] = ()


@dataclass(frozen=True)
class CompanyCharacter:
    """Business identity of NTPC independent of current market prices."""

    symbol: str
    company_name: str
    business_character: str
    core_businesses: Tuple[str, ...]
    operating_model: Tuple[str, ...]
    revenue_and_cashflow_drivers: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_dependencies: Tuple[str, ...]
    demand_dependencies: Tuple[str, ...]
    strategic_themes: Tuple[str, ...]
    key_indicators: Tuple[str, ...]
    event_signals: Tuple[str, ...]
    risk_channels: Tuple[str, ...]
    market_characters: Dict[str, MarketCharacter] = field(default_factory=dict)


def _mc(
    market: str,
    character: str,
    *,
    direct: Tuple[str, ...] = (),
    indirect: Tuple[str, ...] = (),
    channels: Tuple[str, ...] = (),
    supply: Tuple[str, ...] = (),
    demand: Tuple[str, ...] = (),
    cost: Tuple[str, ...] = (),
    strategy: Tuple[str, ...] = (),
    indicators: Tuple[str, ...] = (),
    events: Tuple[str, ...] = (),
    logic: Tuple[str, ...] = (),
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        character=character,
        direct_exposure=direct,
        indirect_exposure=indirect,
        impact_channels=channels,
        supply_chain_links=supply,
        demand_channels=demand,
        cost_channels=cost,
        strategic_channels=strategy,
        key_indicators=indicators,
        event_signals=events,
        calculation_logic=logic,
    )


COMPANY_CHARACTER = CompanyCharacter(
    symbol="NTPC",
    company_name="NTPC Limited",
    business_character=(
        "NTPC is a large integrated Indian power-generation and energy platform. "
        "Its character is dominated by electricity generation, thermal assets, "
        "fuel security, regulated/contracted power economics, grid-linked demand, "
        "large infrastructure capex and an expanding non-fossil portfolio. "
        "The business also extends into coal mining, power trading, consultancy, "
        "renewable energy, hydro, nuclear-related development, green hydrogen and "
        "other energy-transition activities."
    ),
    core_businesses=(
        "Coal-based thermal power generation",
        "Gas/liquid-fuel power generation",
        "Hydro power generation",
        "Renewable power generation",
        "Nuclear power development/participation",
        "Coal mining and fuel management",
        "Power trading and electricity-related services",
        "Power project construction, renovation and modernization",
        "Green hydrogen and green chemicals",
        "Waste-to-energy and ash utilisation",
        "EV charging and related energy infrastructure",
        "Technical consultancy and energy services",
    ),
    operating_model=(
        "Large asset-heavy generation fleet",
        "Long-life power assets with high fixed-cost characteristics",
        "Fuel sourcing and logistics integrated with generation operations",
        "Grid-connected electricity generation",
        "Long-term power purchase and contracted supply relationships",
        "Capacity addition through thermal, hydro and renewable projects",
        "Diversification through subsidiaries and joint ventures",
        "Increasing renewable and energy-storage orientation",
    ),
    revenue_and_cashflow_drivers=(
        "Electricity generation volume",
        "Plant availability and plant load factor",
        "Capacity utilisation",
        "Power sale/offtake under contracts",
        "Power demand and dispatch requirements",
        "Tariff and regulated-return framework where applicable",
        "Fuel-cost pass-through/recovery mechanisms where applicable",
        "Power trading activity",
        "Mining and fuel-management economics",
        "Commissioning of new capacity",
        "Renewable generation growth",
    ),
    cost_drivers=(
        "Coal procurement and coal logistics",
        "Natural gas/fuel costs for gas-based assets",
        "Rail and transportation availability/cost",
        "Plant operations and maintenance",
        "Engineering and construction costs",
        "Power-plant equipment and spares",
        "Electricity used across auxiliary systems",
        "Financing costs for large capital projects",
        "Environmental compliance and emissions-management costs",
        "Water availability and water-management costs",
    ),
    supply_chain_dependencies=(
        "Coal mines and coal suppliers",
        "Rail and bulk logistics",
        "Ports and fuel transportation where relevant",
        "Power-plant equipment suppliers",
        "Engineering, procurement and construction contractors",
        "Turbines, boilers, generators and electrical equipment",
        "Transmission/grid connectivity",
        "Water resources for thermal and hydro operations",
        "Renewable equipment and project-development ecosystem",
    ),
    demand_dependencies=(
        "Industrial electricity demand",
        "Commercial electricity demand",
        "Residential electricity demand",
        "Infrastructure and manufacturing electrification",
        "EV charging growth",
        "Data-centre and digital-infrastructure electricity demand",
        "Agricultural and rural electricity demand",
        "Peak-load requirements and grid balancing needs",
    ),
    strategic_themes=(
        "Expansion of non-fossil generation",
        "Renewable energy capacity growth",
        "Energy storage and pumped-storage development",
        "Fuel security and vertical integration",
        "Coal mining integration",
        "Power-system reliability",
        "Energy transition and emissions reduction",
        "Green hydrogen and green chemical development",
        "Power trading and energy-market participation",
        "Digitalisation and operational efficiency",
    ),
    key_indicators=(
        "Generation in billion units",
        "Plant load factor",
        "Plant availability",
        "Capacity additions",
        "Thermal versus hydro versus renewable generation mix",
        "Coal consumption and coal stock",
        "Coal supply/dispatch performance",
        "Fuel cost and fuel availability",
        "Power offtake and demand",
        "Receivables and collection cycle",
        "Tariff/regulatory developments",
        "Capital expenditure",
        "Project commissioning milestones",
        "Renewable capacity additions",
        "Energy-storage pipeline",
        "Financing cost",
        "Cash flow from operations",
    ),
    event_signals=(
        "New power-project awards or commissioning",
        "Large capacity additions",
        "Renewable project commissioning",
        "Power purchase agreement developments",
        "Tariff orders and regulatory changes",
        "Coal mine production/dispatch changes",
        "Fuel-supply agreements",
        "Major plant outages or restoration",
        "Large equipment or EPC contracts",
        "Acquisitions, subsidiaries or joint ventures",
        "Green hydrogen/green chemical project milestones",
        "Energy-storage project awards",
        "Government power-policy changes",
        "Environmental or emissions-related regulation",
        "Credit-rating or financing developments",
    ),
    risk_channels=(
        "Fuel supply disruption",
        "Coal quality or logistics constraints",
        "Natural gas price/availability for gas assets",
        "Power demand weakness",
        "Regulatory/tariff changes",
        "Large-project execution delays",
        "High capital intensity",
        "Financing-rate changes",
        "Plant outage and availability risk",
        "Environmental and transition-policy risk",
        "Water availability risk",
        "Grid/transmission constraints",
        "Receivable and counterparty risk",
    ),
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Broad Indian equity-market and macro cycle signal for NTPC valuation, "
        "capital-market conditions and investor risk appetite.",
        direct=("Equity valuation and market beta",),
        indirect=(
            "Indian economic cycle",
            "Interest-rate expectations",
            "Institutional risk appetite",
            "Infrastructure investment sentiment",
        ),
        channels=(
            "Equity-market repricing",
            "Macro growth expectations",
            "Financing and valuation conditions",
        ),
        demand=(
            "Industrial and commercial electricity demand",
            "Infrastructure-led power demand",
        ),
        strategy=(
            "Market valuation of regulated/utility assets",
            "Capital allocation for large projects",
        ),
        indicators=(
            "NTPC return versus NIFTY 50",
            "Rolling beta",
            "Rolling correlation",
            "Relative volatility",
            "Drawdown behaviour",
        ),
        events=(
            "Major Indian macro announcements",
            "Budget/infrastructure policy",
            "Interest-rate cycle changes",
        ),
        logic=(
            "Measure contemporaneous and lagged NTPC returns against NIFTY 50.",
            "Estimate rolling beta/correlation over multiple windows.",
            "Separate market-wide movement from company-specific events.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect energy-cost, logistics, inflation and macro-demand signal. "
        "Crude is not a primary fuel for NTPC's core coal fleet, so the pathway "
        "must be separated from direct coal economics.",
        indirect=(
            "Inflation",
            "Transportation and logistics",
            "Engineering/EPC input costs",
            "Industrial demand",
            "Energy-sector sentiment",
        ),
        channels=(
            "Inflation transmission",
            "Freight/logistics cost",
            "Industrial-cycle transmission",
        ),
        supply=(
            "Construction logistics",
            "Heavy transport",
            "Equipment and project supply chain",
        ),
        demand=(
            "Industrial electricity demand",
            "Economic activity",
        ),
        cost=(
            "Logistics/freight",
            "Construction and project input inflation",
        ),
        strategy=("Energy-sector diversification and macro sensitivity",),
        indicators=(
            "Crude return",
            "NTPC return",
            "Freight/inflation proxies",
            "Lagged cross-correlation",
        ),
        events=("Sharp oil-price shocks", "Major global supply disruptions"),
        logic=(
            "Test crude returns against NTPC returns with lag windows.",
            "Control for NIFTY to distinguish broad macro effects.",
            "Use event studies for major oil shocks rather than assuming causation.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Macro risk, inflation-expectation and defensive-asset signal. "
        "Its influence on NTPC is primarily indirect through rates, liquidity "
        "and investor risk sentiment.",
        indirect=(
            "Inflation expectations",
            "Real-rate expectations",
            "Risk-off sentiment",
            "Currency/macro stress",
        ),
        channels=(
            "Macro regime transmission",
            "Interest-rate expectations",
            "Investor risk appetite",
        ),
        demand=("Broad investment and economic-cycle conditions",),
        strategy=("Defensive-versus-cyclical market regime detection",),
        indicators=(
            "Gold return",
            "NTPC return",
            "Gold/NIFTY regime",
            "Rolling lag correlation",
        ),
        events=("Large gold-price regime shifts", "Major central-bank/rate shocks"),
        logic=(
            "Treat gold as a macro-state variable rather than a direct NTPC input.",
            "Measure lagged relationships across different market regimes.",
            "Control for NIFTY and rates where data is available.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Mixed precious-metal and industrial-cycle signal. Its industrial "
        "component can reflect broader electrification/manufacturing activity, "
        "while the precious-metal component reflects risk and macro conditions.",
        indirect=(
            "Industrial cycle",
            "Electrification investment",
            "Risk sentiment",
            "Inflation expectations",
        ),
        channels=(
            "Industrial-cycle transmission",
            "Macro risk transmission",
        ),
        demand=(
            "Manufacturing activity",
            "Electrification and infrastructure cycle",
        ),
        strategy=("Energy-transition and industrial-cycle monitoring",),
        indicators=(
            "Silver return",
            "Industrial-metal basket",
            "NTPC return",
            "Lagged correlation",
        ),
        events=("Industrial-metal shocks", "Major macro risk events"),
        logic=(
            "Compare silver with NTPC after controlling for NIFTY.",
            "Check whether any relationship is regime-dependent.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Mixed direct and indirect energy input. NTPC operates gas/liquid-fuel "
        "generation assets, while gas prices can also influence the broader "
        "power-market merit order and energy economics.",
        direct=(
            "Gas-based power-generation fuel economics",
            "Gas plant dispatch economics",
        ),
        indirect=(
            "Power-market merit order",
            "Industrial energy costs",
            "Energy transition economics",
        ),
        channels=(
            "Fuel-cost transmission",
            "Gas-plant dispatch",
            "Power-market pricing",
        ),
        supply=(
            "Gas supply availability",
            "Gas transportation/infrastructure",
        ),
        demand=(
            "Electricity demand and peak-load requirements",
            "Gas-based balancing demand",
        ),
        cost=(
            "Fuel cost for gas assets",
            "Fuel availability/transportation",
        ),
        strategy=(
            "Role of flexible gas generation",
            "Transition from conventional to lower-carbon generation",
        ),
        indicators=(
            "Natural-gas price",
            "Gas-plant generation",
            "Gas availability",
            "Gas plant PLF",
            "NTPC generation",
            "Power-market prices",
        ),
        events=(
            "Gas supply disruptions",
            "LNG/global gas shocks",
            "Gas-plant dispatch changes",
        ),
        logic=(
            "Separate NTPC gas-asset exposure from coal and renewable assets.",
            "Compare gas-price changes with gas-generation and total-generation data.",
            "Test lags because fuel-price changes may transmit through dispatch and tariffs.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Industrial and electrification input signal. Copper is relevant to "
        "power infrastructure, electrical equipment, project construction and "
        "the broader electricity-demand cycle rather than being a core fuel input.",
        indirect=(
            "Electrical equipment costs",
            "Grid and infrastructure capex",
            "Industrial/electrification cycle",
        ),
        channels=(
            "Project input-cost transmission",
            "Electrical-equipment cost",
            "Capex-cycle transmission",
        ),
        supply=(
            "Cables and conductors",
            "Transformers and electrical equipment",
            "Power-project EPC supply chain",
        ),
        demand=(
            "Grid expansion",
            "Industrial electrification",
            "Renewable and storage deployment",
        ),
        cost=(
            "Electrical equipment",
            "Construction and project procurement",
        ),
        strategy=(
            "Grid modernisation",
            "Renewable and storage infrastructure",
            "Electrification growth",
        ),
        indicators=(
            "Copper return",
            "NTPC capex",
            "Project awards",
            "Electrical-equipment cost proxies",
            "Lagged correlation",
        ),
        events=("Large copper shocks", "Major global infrastructure-cycle changes"),
        logic=(
            "Test copper against NTPC returns and capex/project activity.",
            "Use lagged windows because procurement and construction transmit slowly.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Industrial input and infrastructure-cycle signal. Aluminium can affect "
        "power-project equipment, structures and electrical applications, while "
        "also reflecting broader industrial and infrastructure demand.",
        indirect=(
            "Power-project equipment",
            "Construction inputs",
            "Industrial capex",
            "Electrical applications",
        ),
        channels=(
            "Procurement-cost transmission",
            "Industrial-cycle transmission",
            "Infrastructure-capex signal",
        ),
        supply=(
            "Project equipment",
            "Cables and conductors",
            "Construction materials",
        ),
        demand=(
            "Infrastructure investment",
            "Industrial electrification",
            "Renewable project deployment",
        ),
        cost=(
            "Equipment and material procurement",
            "Construction inputs",
        ),
        strategy=(
            "Renewable build-out",
            "Grid and transmission infrastructure",
        ),
        indicators=(
            "Aluminium return",
            "NTPC capex",
            "Project commissioning",
            "Procurement-cost proxies",
            "Lagged relationship",
        ),
        events=("Large aluminium price shocks", "Infrastructure investment cycles"),
        logic=(
            "Do not treat aluminium as a direct NTPC revenue driver.",
            "Measure its relationship through capex, procurement and industrial-cycle data.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Industrial and infrastructure-cycle signal with an indirect connection "
        "through galvanised steel, structures and equipment used in power projects.",
        indirect=(
            "Galvanised steel",
            "Power-plant structures",
            "Transmission infrastructure",
            "Industrial construction",
        ),
        channels=(
            "Construction-input transmission",
            "Infrastructure-capex transmission",
        ),
        supply=(
            "Galvanised structures",
            "Transmission and distribution equipment",
            "Industrial construction",
        ),
        demand=(
            "Grid expansion",
            "Power infrastructure",
            "Industrial capex",
        ),
        cost=(
            "Steel/galvanising-related project inputs",
            "Construction materials",
        ),
        strategy=(
            "Transmission and infrastructure expansion",
            "Renewable project construction",
        ),
        indicators=(
            "Zinc return",
            "Steel/galvanising proxies",
            "NTPC capex",
            "Project awards",
            "Lagged correlation",
        ),
        events=("Zinc/steel input shocks", "Major infrastructure investment changes"),
        logic=(
            "Treat zinc as an indirect project-cost and industrial-cycle variable.",
            "Test whether observed relationships remain after controlling for NIFTY.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Core identity market for NTPC. Electricity is the primary product and "
        "operating environment: generation volume, demand, dispatch, tariffs, "
        "power-market prices and grid conditions directly shape the business.",
        direct=(
            "Electricity generation",
            "Power offtake",
            "Power-market participation",
            "Grid-connected generation",
            "Tariff/contract economics",
        ),
        indirect=(
            "Industrial electricity demand",
            "Peak-load demand",
            "Grid balancing",
            "Power-sector policy",
        ),
        channels=(
            "Generation-volume transmission",
            "Tariff and contracted-revenue transmission",
            "Dispatch/merit-order transmission",
            "Power-market-price transmission",
            "Capacity-utilisation transmission",
        ),
        supply=(
            "Coal and fuel availability",
            "Gas availability",
            "Grid connectivity",
            "Transmission availability",
            "Plant availability",
        ),
        demand=(
            "Total electricity demand",
            "Peak demand",
            "Industrial load",
            "Commercial load",
            "Residential load",
            "EV charging",
            "Data centres",
            "Manufacturing electrification",
        ),
        cost=(
            "Fuel cost per unit",
            "Auxiliary consumption",
            "Operations and maintenance",
            "Transmission/grid charges where applicable",
        ),
        strategy=(
            "Thermal fleet utilisation",
            "Renewable capacity expansion",
            "Hydro and storage",
            "Power trading",
            "Grid reliability",
            "Energy transition",
        ),
        indicators=(
            "NTPC generation",
            "Generation growth",
            "Plant load factor",
            "Plant availability",
            "Capacity utilisation",
            "Power demand growth",
            "Peak demand",
            "Power-market prices",
            "Tariff/order developments",
            "Receivables",
            "Renewable generation",
        ),
        events=(
            "Peak-demand records",
            "Power shortages/surpluses",
            "Tariff orders",
            "Power purchase agreements",
            "Major plant commissioning",
            "Major outages",
            "Grid/transmission events",
            "Power-sector policy changes",
        ),
        logic=(
            "Electricity must be treated as the core business variable, not merely "
            "as another market return series.",
            "Calculate relationships using generation, demand, PLF, availability, "
            "power prices and tariff data where available.",
            "Use event studies around major power-demand, tariff and commissioning events.",
        ),
    ),
}


# Rebind the immutable company character with its market-character map.
COMPANY_CHARACTER = CompanyCharacter(
    **{
        **COMPANY_CHARACTER.__dict__,
        "market_characters": MARKET_CHARACTERS,
    }
)


def get_company_character() -> CompanyCharacter:
    """Return the complete NTPC company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one market character by exact market name."""
    try:
        return MARKET_CHARACTERS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Supported markets: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine market characters."""
    return dict(MARKET_CHARACTERS)


def validate_character() -> Dict[str, object]:
    """
    Structural validation only.

    This function does not validate historical relationships because those
    require real observed data and belong to the later calculation layer.
    """
    missing = [m for m in TRACKED_MARKETS if m not in MARKET_CHARACTERS]
    extra = [m for m in MARKET_CHARACTERS if m not in TRACKED_MARKETS]

    return {
        "symbol": COMPANY_CHARACTER.symbol,
        "company_name": COMPANY_CHARACTER.company_name,
        "tracked_market_count": len(TRACKED_MARKETS),
        "market_character_count": len(MARKET_CHARACTERS),
        "missing_markets": missing,
        "extra_markets": extra,
        "valid": (
            len(TRACKED_MARKETS) == 9
            and not missing
            and not extra
            and len(COMPANY_CHARACTER.core_businesses) > 0
            and len(COMPANY_CHARACTER.key_indicators) > 0
        ),
    }


if __name__ == "__main__":
    result = validate_character()
    print("NTPC CHARACTER VALIDATION")
    print("=" * 32)
    print(f"Company: {result['company_name']}")
    print(f"Markets: {result['market_character_count']}/9")
    print(f"Valid: {result['valid']}")

    if result["missing_markets"]:
        print("Missing:", result["missing_markets"])
    if result["extra_markets"]:
        print("Extra:", result["extra_markets"])

    print("\nMARKET CHARACTERS")
    print("=" * 32)
    for market in TRACKED_MARKETS:
        mc = MARKET_CHARACTERS[market]
        print(f"\n[{market}]")
        print(mc.character)
        print("Direct:", ", ".join(mc.direct_exposure) or "None")
        print("Indirect:", ", ".join(mc.indirect_exposure) or "None")
