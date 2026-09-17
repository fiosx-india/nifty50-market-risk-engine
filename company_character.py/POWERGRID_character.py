"""
POWERGRID Character Engine
--------------------------
Character layer for Power Grid Corporation of India Limited (POWERGRID).

Architecture:
    Company Character
        -> business identity
        -> operating model
        -> revenue/cash-flow drivers
        -> cost/supply-chain dependencies
        -> strategic themes
        -> indicators/events/risks

    Company Character
        -> 9 Market Characters
        -> later historical calculation engine

The CSV values RANK, PCT_CHANGE, LINKAGE_SCORE and RELATION are deliberately
NOT hard-coded here. They are observations/calculations for a later data layer.
"""

from dataclasses import dataclass, field
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
    symbol="POWERGRID",
    company_name="Power Grid Corporation of India Limited",
    business_character=(
        "POWERGRID is primarily a large-scale electricity transmission and "
        "power-grid infrastructure company. Its economic character is therefore "
        "different from a power generator: the core engine is transmission "
        "network ownership and operation, regulated/contracted transmission "
        "revenues, system availability, large capital expenditure, project "
        "execution and the expansion of India's inter-state and renewable-energy "
        "evacuation network. Its ecosystem also includes consultancy, telecom, "
        "energy services and related subsidiaries."
    ),
    core_businesses=(
        "Inter-state electricity transmission",
        "Transmission system operation and maintenance",
        "High-voltage and extra-high-voltage transmission",
        "Substation development and operation",
        "Transmission project development",
        "Renewable-energy evacuation infrastructure",
        "Green Energy Corridor infrastructure",
        "Power-system planning and grid modernisation",
        "Telecommunication infrastructure using power-grid assets",
        "Energy services and consultancy",
        "Central Transmission Utility ecosystem through subsidiaries",
        "International/adjacent power-sector services",
    ),
    operating_model=(
        "Asset-heavy regulated/contracted transmission infrastructure",
        "Long-life transmission lines and substations",
        "High system-availability operating model",
        "Large multi-year project pipeline",
        "Competitive/TBCB and other transmission project development",
        "Grid expansion linked to electricity demand and generation capacity",
        "Renewable-energy evacuation and interstate power transfer",
        "Large recurring capex programme",
        "Project commissioning followed by long-duration asset operation",
    ),
    revenue_and_cashflow_drivers=(
        "Transmission availability",
        "Transmission charges/revenues",
        "Commissioning of new transmission assets",
        "Regulated or awarded project returns",
        "Inter-state transmission infrastructure additions",
        "Transmission project pipeline",
        "System utilisation and power-transfer requirements",
        "Consultancy and power-sector service revenue",
        "Telecom/energy-service activities",
        "Subsidiary and joint-venture performance",
    ),
    cost_drivers=(
        "Transmission-line construction",
        "Substation construction",
        "Transformers and electrical equipment",
        "Conductors and cables",
        "Steel structures and towers",
        "Land and right-of-way acquisition",
        "Engineering, procurement and construction",
        "Financing cost",
        "Operations and maintenance",
        "Technology and grid-control systems",
        "Environmental and statutory compliance",
    ),
    supply_chain_dependencies=(
        "Transformers",
        "Conductors and cables",
        "Tower steel and structures",
        "Switchgear and protection systems",
        "HVDC and power-electronics equipment",
        "Substation equipment",
        "EPC contractors",
        "Engineering and project-management services",
        "Land/right-of-way availability",
        "Telecom and grid-control technology",
    ),
    demand_dependencies=(
        "Growth in electricity generation",
        "Growth in electricity consumption",
        "Industrial electrification",
        "Renewable-energy capacity",
        "Inter-state power transfers",
        "Peak electricity demand",
        "Data-centre and digital infrastructure demand",
        "EV and transport electrification",
        "Grid balancing and reliability requirements",
    ),
    strategic_themes=(
        "National transmission-grid expansion",
        "Renewable-energy evacuation",
        "Green Energy Corridors",
        "High-capacity interstate corridors",
        "HVDC development",
        "Grid modernisation and digitalisation",
        "Energy storage and renewable integration",
        "Large-scale capex execution",
        "Transmission project bidding/TBCB",
        "Power-system reliability",
        "Telecom and energy-service diversification",
    ),
    key_indicators=(
        "Transmission line kilometres",
        "Substation capacity",
        "Transformation capacity",
        "Network/system availability",
        "Transmission asset additions",
        "Capital expenditure",
        "Capitalisation of projects",
        "Project pipeline",
        "Projects awarded",
        "Projects commissioned",
        "Transmission revenue",
        "Receivables",
        "Debt and financing cost",
        "Return on capital",
        "Renewable evacuation capacity",
        "HVDC capacity",
    ),
    event_signals=(
        "Major transmission project award",
        "Transmission asset commissioning",
        "Green Energy Corridor award",
        "Renewable evacuation project",
        "HVDC project award",
        "Large capex announcement",
        "TBCB bidding outcome",
        "Land/right-of-way resolution",
        "Major project delay",
        "Grid outage or reliability event",
        "Transformer/equipment supply issue",
        "Regulatory/tariff change",
        "Interest-rate/financing changes",
        "Subsidiary or joint-venture development",
        "Telecom/energy-services expansion",
    ),
    risk_channels=(
        "Large-project execution delay",
        "Land/right-of-way constraints",
        "Equipment procurement delays",
        "Transformer/HVDC supply-chain risk",
        "Interest-rate and financing risk",
        "Regulatory changes",
        "Competitive transmission bidding pressure",
        "Transmission-system outage",
        "Technology/obsolescence risk",
        "Receivable/counterparty risk",
        "Large capex requirement",
        "Environmental and statutory approvals",
    ),
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Broad Indian equity-market and macro signal for POWERGRID valuation, "
        "liquidity, interest-rate expectations and infrastructure sentiment. "
        "The physical business link is indirect.",
        direct=("Equity-market valuation and market beta",),
        indirect=(
            "Indian economic cycle",
            "Infrastructure investment sentiment",
            "Institutional risk appetite",
            "Interest-rate expectations",
        ),
        channels=(
            "Market-wide repricing",
            "Valuation multiple changes",
            "Infrastructure-cycle transmission",
        ),
        demand=("Broad electricity and infrastructure demand",),
        strategy=("Capital-market valuation of transmission assets",),
        indicators=(
            "POWERGRID return",
            "NIFTY 50 return",
            "Rolling beta",
            "Rolling correlation",
            "Relative volatility",
            "Drawdown",
        ),
        events=("Major macro/rate events", "Infrastructure-policy events"),
        logic=(
            "Calculate POWERGRID versus NIFTY returns from observed data.",
            "Estimate rolling beta/correlation over multiple windows.",
            "Separate market-wide movement from electricity and project-specific events.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Weak indirect macro and construction-cost signal. Crude is not a core "
        "revenue commodity for POWERGRID; its main pathways are freight, fuel, "
        "inflation and the wider investment cycle.",
        indirect=(
            "Fuel and logistics",
            "Construction inflation",
            "Industrial cycle",
            "Macro inflation",
        ),
        channels=(
            "Project-input inflation",
            "Freight/logistics cost",
            "Macro growth transmission",
        ),
        supply=(
            "Heavy equipment transport",
            "EPC logistics",
            "Construction supply chain",
        ),
        demand=("Industrial and infrastructure investment",),
        cost=(
            "Freight",
            "Construction logistics",
            "Contractor input costs",
        ),
        strategy=("Large-capex project economics",),
        indicators=(
            "Crude return",
            "POWERGRID return",
            "Capex",
            "Project cost indicators",
            "Lagged relationship",
        ),
        events=("Large crude shocks", "Global supply disruptions"),
        logic=(
            "Treat crude as an indirect cost/macro variable.",
            "Test whether crude adds explanatory power after controlling for NIFTY.",
            "Use lagged windows for project-cost transmission.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Indirect macro risk, inflation and real-rate signal. Gold has no "
        "meaningful physical input relationship with POWERGRID.",
        indirect=(
            "Inflation expectations",
            "Real-rate expectations",
            "Risk-off sentiment",
            "Liquidity regime",
        ),
        channels=(
            "Macro-regime transmission",
            "Interest-rate transmission",
            "Investor risk appetite",
        ),
        demand=("Broad economic and infrastructure-cycle conditions",),
        strategy=("Defensive/cyclical market-regime monitoring",),
        indicators=(
            "Gold return",
            "POWERGRID return",
            "NIFTY return",
            "Rate proxy",
            "Rolling/lagged correlation",
        ),
        events=("Major rate shocks", "Global risk-off events"),
        logic=(
            "Use gold as a macro-state variable rather than a physical input.",
            "Test incremental information after controlling for NIFTY and rates.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial-cycle and macro signal. Silver can reflect "
        "industrial/electrification sentiment but is not a core POWERGRID input.",
        indirect=(
            "Industrial cycle",
            "Electrification investment",
            "Commodity sentiment",
        ),
        channels=(
            "Industrial-cycle transmission",
            "Risk-sentiment transmission",
        ),
        demand=("Industrial electrification and infrastructure activity",),
        strategy=("Industrial and energy-transition regime monitoring",),
        indicators=(
            "Silver return",
            "POWERGRID return",
            "Copper return",
            "Industrial-cycle proxies",
        ),
        events=("Industrial-metal shocks", "Major macro events"),
        logic=(
            "Check silver against POWERGRID after controlling for NIFTY.",
            "Test whether any observed relationship is stable across regimes.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect electricity-generation and energy-cycle signal. Gas prices "
        "can influence the generation mix, gas-fired dispatch and therefore the "
        "need for transmission capacity, but they are not a primary POWERGRID "
        "revenue input.",
        indirect=(
            "Gas-fired generation economics",
            "Power-generation mix",
            "Electricity-market conditions",
            "Energy-transition cycle",
        ),
        channels=(
            "Generation-mix transmission",
            "Electricity-demand transmission",
            "Power-system utilisation",
        ),
        supply=(
            "Gas-fired generation",
            "Power-sector fuel infrastructure",
        ),
        demand=(
            "Electricity demand",
            "Gas-to-power demand",
            "Grid balancing requirements",
        ),
        cost=("Limited indirect project/energy input effects",),
        strategy=(
            "Flexible generation integration",
            "Renewable integration",
            "Grid balancing",
        ),
        indicators=(
            "Natural gas price",
            "Gas-based generation",
            "Power demand",
            "Transmission utilisation proxies",
            "POWERGRID return",
        ),
        events=("Gas-price shocks", "Gas supply disruptions", "Power-mix changes"),
        logic=(
            "Model gas through electricity generation and grid-demand channels.",
            "Do not classify gas as a direct POWERGRID revenue commodity.",
            "Use lagged analysis around major generation-mix changes.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Meaningful indirect project-input character because transmission "
        "networks use electrical conductors, cables, transformers and other "
        "electrical equipment. Copper also reflects electrification and grid "
        "investment cycles.",
        indirect=(
            "Electrical conductors",
            "Cables",
            "Transformers/electrical equipment",
            "Grid expansion",
            "Electrification cycle",
        ),
        channels=(
            "Transmission-equipment procurement cost",
            "Project-capex transmission",
            "Electrification-cycle signal",
        ),
        supply=(
            "Conductors",
            "Cables",
            "Transformers",
            "Substation equipment",
            "Electrical components",
        ),
        demand=(
            "Grid expansion",
            "Renewable evacuation",
            "Industrial electrification",
            "EV/data-centre load growth",
        ),
        cost=(
            "Electrical equipment",
            "Conductor/cable procurement",
            "Project construction",
        ),
        strategy=(
            "Grid modernisation",
            "Renewable evacuation",
            "High-capacity corridors",
            "Electrification infrastructure",
        ),
        indicators=(
            "Copper return",
            "Copper procurement prices",
            "POWERGRID capex",
            "Project awards",
            "Project commissioning",
            "Equipment-cost proxies",
        ),
        events=("Large copper shocks", "Major global electrification investment changes"),
        logic=(
            "Measure copper-price effects through equipment/procurement and capex.",
            "Use project-level lag windows because procurement is not instantaneous.",
            "Separate copper price effects from broad industrial-cycle effects.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect but relevant transmission-infrastructure input and industrial "
        "cycle. Aluminium can be present in conductors, electrical applications, "
        "structures and other grid equipment.",
        indirect=(
            "Transmission conductors",
            "Electrical applications",
            "Structures and equipment",
            "Industrial capex",
        ),
        channels=(
            "Conductor procurement cost",
            "Equipment procurement",
            "Project-capex transmission",
            "Industrial-cycle signal",
        ),
        supply=(
            "Aluminium conductors",
            "Electrical equipment",
            "Transmission structures",
            "Grid-project supply chain",
        ),
        demand=(
            "Transmission expansion",
            "Renewable evacuation",
            "Grid modernisation",
            "Industrial electrification",
        ),
        cost=(
            "Conductors",
            "Equipment",
            "Project construction",
        ),
        strategy=(
            "Transmission expansion",
            "Renewable integration",
            "High-voltage corridors",
        ),
        indicators=(
            "Aluminium return",
            "Conductor prices",
            "POWERGRID capex",
            "Project awards",
            "Project commissioning",
        ),
        events=("Aluminium price shocks", "Large transmission-investment changes"),
        logic=(
            "Treat aluminium as an indirect project-input variable.",
            "Link observed aluminium movements to conductor/equipment costs where data exists.",
            "Test lags between commodity movement and project/capex indicators.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect infrastructure-input signal, mainly through galvanised steel "
        "used in towers and other corrosion-resistant grid structures.",
        indirect=(
            "Galvanised steel",
            "Transmission towers",
            "Grid structures",
            "Industrial construction",
        ),
        channels=(
            "Tower/material procurement",
            "Project construction cost",
            "Infrastructure-cycle signal",
        ),
        supply=(
            "Galvanised steel",
            "Transmission towers",
            "Steel structures",
            "Project contractors",
        ),
        demand=(
            "Transmission expansion",
            "Renewable-energy evacuation",
            "Grid infrastructure",
        ),
        cost=(
            "Tower steel",
            "Galvanising-related material cost",
            "Construction inputs",
        ),
        strategy=("Large transmission-network expansion",),
        indicators=(
            "Zinc return",
            "Steel prices",
            "Tower procurement costs",
            "POWERGRID capex",
            "Project awards",
        ),
        events=("Zinc/steel shocks", "Large grid-investment changes"),
        logic=(
            "Treat zinc as an indirect tower/galvanising input.",
            "Test observed relationships through project-cost and capex data.",
            "Control for broad industrial and market effects.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Core identity market for POWERGRID. Electricity transmission is the "
        "company's primary operating domain. Generation capacity, electricity "
        "demand, renewable additions, interstate power flows, peak demand and "
        "grid reliability determine the need for transmission infrastructure.",
        direct=(
            "Electricity transmission",
            "Inter-state transmission system",
            "Substations",
            "Grid-system availability",
            "Power evacuation",
            "Transmission capacity",
        ),
        indirect=(
            "Power demand",
            "Generation additions",
            "Renewable capacity",
            "Peak-load growth",
            "Grid balancing",
        ),
        channels=(
            "Transmission-capacity demand",
            "Grid-utilisation transmission",
            "Renewable-evacuation transmission",
            "Project-award transmission",
            "System-availability transmission",
        ),
        supply=(
            "Transmission lines",
            "Substations",
            "Transformers",
            "Conductors",
            "HVDC systems",
            "Grid-control systems",
        ),
        demand=(
            "Peak electricity demand",
            "Industrial load",
            "Commercial load",
            "Residential load",
            "Renewable generation",
            "EV charging",
            "Data centres",
            "Manufacturing electrification",
        ),
        cost=(
            "Transmission-project capex",
            "Equipment procurement",
            "Operations and maintenance",
            "Financing cost",
        ),
        strategy=(
            "National grid expansion",
            "Renewable-energy evacuation",
            "Green Energy Corridors",
            "HVDC corridors",
            "Grid modernisation",
            "Energy storage integration",
        ),
        indicators=(
            "Electricity demand",
            "Peak demand",
            "Generation capacity additions",
            "Renewable capacity additions",
            "Transmission capacity",
            "Line kilometres",
            "Substation capacity",
            "Network availability",
            "POWERGRID capex",
            "Project awards",
            "Project commissioning",
        ),
        events=(
            "Peak-demand records",
            "Major renewable capacity additions",
            "Green Energy Corridor awards",
            "HVDC project awards",
            "Major transmission commissioning",
            "Grid reliability events",
            "Power-sector policy changes",
        ),
        logic=(
            "Electricity is the primary operating market variable for POWERGRID.",
            "Calculate relationships using demand, generation additions, renewable "
            "capacity, transmission utilisation and project-award data.",
            "Use event studies around major grid and renewable-evacuation projects.",
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
    """Return the complete POWERGRID company character."""
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
    """Structural validation; historical linkage is calculated later."""
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
            and bool(COMPANY_CHARACTER.core_businesses)
            and bool(COMPANY_CHARACTER.key_indicators)
        ),
    }


if __name__ == "__main__":
    result = validate_character()

    print("POWERGRID CHARACTER VALIDATION")
    print("=" * 36)
    print(f"Company: {result['company_name']}")
    print(f"Markets: {result['market_character_count']}/9")
    print(f"Valid: {result['valid']}")

    if result["missing_markets"]:
        print("Missing:", result["missing_markets"])
    if result["extra_markets"]:
        print("Extra:", result["extra_markets"])

    print("\nMARKET CHARACTERS")
    print("=" * 36)

    for market in TRACKED_MARKETS:
        mc = MARKET_CHARACTERS[market]
        print(f"\n[{market}]")
        print(mc.character)
        print("Direct:", ", ".join(mc.direct_exposure) or "None")
        print("Indirect:", ", ".join(mc.indirect_exposure) or "None")
