"""
ONGC Character Engine
---------------------
Character layer for ONGC Limited.

This module defines:
    Company Character -> business identity, operating model, drivers, risks
    Market Character  -> how each of the nine tracked markets can transmit
                         information into ONGC

IMPORTANT:
    The CSV supplied for this company may contain RANK, PCT_CHANGE,
    LINKAGE_SCORE and RELATION. Those are NOT hard-coded here.

    This file defines what should be measured. Historical linkage, beta,
    correlation, lag, impact magnitude, probability and trading decisions
    belong to the later data/calculation layer and must be derived from
    observed data.
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
    symbol="ONGC",
    company_name="Oil and Natural Gas Corporation Limited",
    business_character=(
        "ONGC is an integrated upstream-focused energy company whose core "
        "economic character is exploration, development and production of "
        "crude oil and natural gas. Its business is therefore strongly exposed "
        "to hydrocarbon prices, production volumes, reserves, field performance, "
        "realisations, government/regulatory mechanisms and large-scale "
        "capital-intensive exploration and development. The company also has "
        "downstream and adjacent energy exposure through its group ecosystem, "
        "but the primary character remains upstream oil and gas."
    ),
    core_businesses=(
        "Crude oil exploration",
        "Crude oil production",
        "Natural gas exploration",
        "Natural gas production",
        "Field development and redevelopment",
        "Offshore and onshore hydrocarbon operations",
        "Exploration drilling and seismic activity",
        "Oil and gas processing and gathering",
        "Hydrocarbon reserves replacement",
        "Energy and petrochemical-related group ecosystem",
        "Renewable and lower-carbon energy initiatives",
        "International/overseas upstream participation through group entities",
    ),
    operating_model=(
        "Asset-heavy upstream exploration and production",
        "Long-cycle field development",
        "Reserve and resource replacement",
        "Production from offshore and onshore assets",
        "Large exploration and drilling programme",
        "Infrastructure-linked hydrocarbon gathering and processing",
        "Capital-intensive project execution",
        "Exposure to administered, regulated and market-linked pricing mechanisms",
        "Integrated energy ecosystem through subsidiaries and group entities",
    ),
    revenue_and_cashflow_drivers=(
        "Crude oil production volume",
        "Natural gas production volume",
        "Realised crude oil price",
        "Realised natural gas price",
        "Production mix",
        "Reserve replacement and field productivity",
        "New field commissioning",
        "Well productivity",
        "Export/import parity where relevant",
        "Government pricing and policy mechanisms",
        "Overseas upstream performance where applicable",
        "Capital allocation and project ramp-up",
    ),
    cost_drivers=(
        "Exploration drilling expenditure",
        "Development drilling expenditure",
        "Offshore operations",
        "Rig and oilfield-service costs",
        "Steel and tubular equipment",
        "Subsea and offshore equipment",
        "Power and fuel used in operations",
        "Logistics and marine support",
        "Employee and operating costs",
        "Environmental compliance",
        "Decommissioning and restoration obligations",
        "Financing and project-development costs",
    ),
    supply_chain_dependencies=(
        "Drilling rigs and oilfield services",
        "Offshore vessels and marine logistics",
        "Subsea equipment",
        "Steel, pipes and OCTG",
        "Electrical and instrumentation equipment",
        "Engineering and EPC contractors",
        "Refineries and downstream offtake ecosystem",
        "Gas transportation and pipeline infrastructure",
        "Ports and logistics",
        "Specialised exploration technology and seismic services",
    ),
    demand_dependencies=(
        "Domestic crude oil demand",
        "Domestic natural gas demand",
        "Refining and petrochemical demand",
        "Power-sector gas demand",
        "Fertiliser-sector gas demand",
        "Industrial gas demand",
        "Transport and mobility fuel demand",
        "Global hydrocarbon demand",
        "Energy-security requirements",
    ),
    strategic_themes=(
        "Reserve replacement",
        "Domestic oil and gas production growth",
        "Exploration success",
        "Deepwater and difficult-field development",
        "Enhanced recovery and field redevelopment",
        "Natural gas production growth",
        "Energy security",
        "Renewable and lower-carbon diversification",
        "Operational technology and digital oilfield capability",
        "Capital discipline and project execution",
    ),
    key_indicators=(
        "Crude oil production",
        "Natural gas production",
        "Total hydrocarbon production",
        "Realised crude oil price",
        "Realised gas price",
        "Average daily production",
        "Reserve additions",
        "Reserve replacement ratio",
        "Exploration wells",
        "Development wells",
        "Success rate of exploration wells",
        "Field production ramp-up",
        "Capex",
        "Finding and development cost",
        "Operating cost per unit",
        "EBITDA and operating cash flow",
        "Receivables",
        "Government pricing/regulatory changes",
    ),
    event_signals=(
        "Major oil or gas discovery",
        "Exploration success or dry well",
        "New field development approval",
        "First oil/first gas",
        "Production ramp-up",
        "Major drilling campaign",
        "Deepwater project milestone",
        "Gas-price policy change",
        "Crude-oil pricing/regulatory change",
        "Government levy/tax changes",
        "Major oilfield-service contract",
        "Large capex announcement",
        "Asset acquisition or divestment",
        "International upstream development",
        "Renewable/energy-transition project milestones",
        "Major operational outage or incident",
    ),
    risk_channels=(
        "Crude oil price volatility",
        "Natural gas price and policy risk",
        "Production decline",
        "Exploration failure",
        "Reserve replacement risk",
        "Project execution delays",
        "Offshore operational risk",
        "Environmental and regulatory risk",
        "Government intervention in pricing",
        "Taxes, levies and windfall-related policy",
        "Oilfield-service inflation",
        "Geopolitical energy risk",
        "Foreign-exchange exposure",
        "Large-project capital intensity",
    ),
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Broad Indian equity-market, macro and risk-appetite signal. For ONGC, "
        "this is mainly a valuation, liquidity and domestic macro channel rather "
        "than a physical operating input.",
        direct=("Equity-market valuation and market beta",),
        indirect=(
            "Indian economic cycle",
            "Institutional risk appetite",
            "Interest-rate expectations",
            "Energy-sector valuation regime",
        ),
        channels=(
            "Market-wide repricing",
            "Valuation multiple changes",
            "Liquidity and risk-appetite transmission",
        ),
        demand=(
            "Domestic energy demand",
            "Industrial and transport activity",
        ),
        strategy=("Capital-market valuation of upstream energy assets",),
        indicators=(
            "ONGC return",
            "NIFTY 50 return",
            "Rolling beta",
            "Rolling correlation",
            "Relative volatility",
            "Sector-relative performance",
        ),
        events=("Major Indian macro/rate events", "Budget and energy-policy events"),
        logic=(
            "Measure ONGC versus NIFTY returns over multiple rolling windows.",
            "Estimate beta and correlation from observed data rather than hard-coding them.",
            "Separate market-wide movement from crude, gas and company-specific events.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Primary direct commodity character for ONGC. Crude prices influence "
        "realised upstream oil revenue, cash generation, project economics and "
        "the valuation of reserves, subject to pricing mechanisms, taxes and "
        "domestic policy.",
        direct=(
            "Crude oil production revenue",
            "Realised oil price",
            "Upstream cash generation",
            "Reserve economics",
        ),
        indirect=(
            "Energy-sector valuation",
            "Domestic inflation",
            "Oilfield-service costs",
            "Government fiscal/tax response",
        ),
        channels=(
            "Revenue realisation",
            "Operating cash flow",
            "Reserve valuation",
            "Capex economics",
            "Fiscal/regulatory transmission",
        ),
        supply=(
            "Oilfield services",
            "Drilling rigs",
            "Offshore logistics",
            "Storage and transportation",
        ),
        demand=(
            "Global crude demand",
            "Domestic refinery demand",
            "Energy-security demand",
        ),
        cost=(
            "Oilfield-service inflation",
            "Marine logistics",
            "Drilling and development cost",
        ),
        strategy=(
            "Exploration investment",
            "Field development",
            "Enhanced recovery",
            "Reserve replacement",
        ),
        indicators=(
            "Brent/WTI or relevant benchmark crude",
            "ONGC realised oil price",
            "Crude production",
            "Oil revenue",
            "Operating cash flow",
            "Capex",
            "Tax/levy burden",
        ),
        events=(
            "OPEC+ production decisions",
            "Major global supply disruptions",
            "Large crude-price shocks",
            "Domestic pricing/tax changes",
        ),
        logic=(
            "Use benchmark crude returns and ONGC realised-price data separately.",
            "Test same-day and lagged relationships between crude and ONGC.",
            "Decompose price effect from production-volume effect.",
            "Control for NIFTY when estimating equity-market transmission.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Primary direct commodity character for ONGC alongside crude oil. Gas "
        "production, realised gas price, domestic pricing policy, demand from "
        "fertiliser/power/industry and new gas-field output directly affect the "
        "company's economics.",
        direct=(
            "Natural gas production",
            "Realised gas price",
            "Gas-field economics",
            "Gas revenue",
        ),
        indirect=(
            "Power-sector demand",
            "Fertiliser demand",
            "Industrial gas demand",
            "Energy-transition economics",
        ),
        channels=(
            "Gas revenue",
            "Production-volume transmission",
            "Gas-price realisation",
            "Field-development economics",
            "Domestic pricing-policy transmission",
        ),
        supply=(
            "Gas processing",
            "Gas gathering",
            "Pipeline infrastructure",
            "Offshore/onshore field equipment",
        ),
        demand=(
            "Fertiliser sector",
            "Power generation",
            "City gas distribution",
            "Industrial users",
            "Petrochemical users",
        ),
        cost=(
            "Gas-field development",
            "Processing and gathering",
            "Offshore operations",
        ),
        strategy=(
            "Gas production growth",
            "New-field development",
            "Energy-security strategy",
            "Lower-carbon transition",
        ),
        indicators=(
            "Natural gas benchmark prices",
            "ONGC gas production",
            "Realised gas price",
            "Gas revenue",
            "Gas-field commissioning",
            "Gas demand by sector",
        ),
        events=(
            "Domestic gas-pricing policy changes",
            "New gas discoveries",
            "First gas from major projects",
            "Gas-production ramp-up",
            "Major LNG/global gas shocks",
        ),
        logic=(
            "Use observed gas-price and realised-price data.",
            "Separate price impact from production-volume impact.",
            "Model sector-specific gas demand where available.",
            "Test lagged effects around new-field commissioning and pricing changes.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Indirect but operationally relevant energy-input and industrial-demand "
        "character. Electricity affects field operations and processing costs, "
        "while electricity demand also reflects the wider energy and industrial "
        "cycle influencing hydrocarbon demand.",
        indirect=(
            "Field operating electricity consumption",
            "Processing and pumping energy",
            "Industrial activity",
            "Power-sector gas demand",
        ),
        channels=(
            "Operating-cost transmission",
            "Industrial-demand transmission",
            "Gas-to-power demand transmission",
        ),
        supply=(
            "Grid electricity",
            "Captive/backup power",
            "Field and processing infrastructure",
        ),
        demand=(
            "Industrial power demand",
            "Gas-fired generation",
            "Economic activity",
        ),
        cost=(
            "Electricity used in production and processing",
            "Power and pumping costs",
        ),
        strategy=(
            "Operational efficiency",
            "Energy transition",
            "Gas-to-power ecosystem",
        ),
        indicators=(
            "Electricity prices",
            "Industrial power demand",
            "ONGC operating cost",
            "Gas demand from power",
            "Lagged ONGC relationship",
        ),
        events=("Major power-price shocks", "Large changes in industrial electricity demand"),
        logic=(
            "Treat electricity as an indirect operating-cost and demand variable.",
            "Do not assume a direct equity relationship without observed evidence.",
            "Test electricity data against operating costs, gas demand and ONGC returns.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Macro risk, inflation and real-rate signal. Gold has no primary physical "
        "production linkage with ONGC; its relevance is through the broader macro "
        "and commodity investment regime.",
        indirect=(
            "Inflation expectations",
            "Real interest rates",
            "Risk-off sentiment",
            "Commodity-investment regime",
        ),
        channels=(
            "Macro-regime transmission",
            "Risk sentiment",
            "Commodity-cycle transmission",
        ),
        demand=("Global macro and investment conditions",),
        strategy=("Commodity-sector regime detection",),
        indicators=(
            "Gold return",
            "ONGC return",
            "Crude return",
            "NIFTY return",
            "Real-rate proxy",
        ),
        events=("Major real-rate shifts", "Global risk-off events"),
        logic=(
            "Use gold as a macro state variable, not as a direct ONGC input.",
            "Check whether gold adds information after controlling for crude and NIFTY.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect precious-metal and industrial-cycle signal. Silver can provide "
        "information about commodity sentiment and industrial activity but is not "
        "a core physical input or revenue commodity for ONGC.",
        indirect=(
            "Industrial cycle",
            "Commodity sentiment",
            "Inflation/risk regime",
        ),
        channels=(
            "Commodity-cycle transmission",
            "Industrial-demand signal",
            "Risk-sentiment transmission",
        ),
        demand=("Global industrial activity",),
        strategy=("Commodity-regime monitoring",),
        indicators=(
            "Silver return",
            "ONGC return",
            "Crude return",
            "Industrial-metal basket",
        ),
        events=("Industrial commodity shocks", "Major global macro events"),
        logic=(
            "Test silver against ONGC after controlling for crude and NIFTY.",
            "Check whether any relationship is stable across commodity regimes.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect industrial-capex and energy-transition signal. Copper is "
        "relevant to ONGC mainly through project equipment, electrical systems, "
        "offshore infrastructure and the broader industrial cycle.",
        indirect=(
            "Electrical equipment",
            "Offshore/project infrastructure",
            "Industrial capex",
            "Energy-transition investment",
        ),
        channels=(
            "Project input-cost transmission",
            "Industrial-cycle transmission",
            "Energy-transition capex signal",
        ),
        supply=(
            "Cables and electrical systems",
            "Transformers and equipment",
            "Offshore/project infrastructure",
        ),
        demand=(
            "Industrial investment",
            "Energy infrastructure",
            "Electrification",
        ),
        cost=(
            "Electrical equipment",
            "Engineering and project procurement",
        ),
        strategy=(
            "Offshore development",
            "Digital/electrical infrastructure",
            "Energy-transition projects",
        ),
        indicators=(
            "Copper return",
            "ONGC capex",
            "Project awards",
            "Oilfield equipment costs",
            "Lagged correlation",
        ),
        events=("Large copper shocks", "Global industrial-capex shifts"),
        logic=(
            "Treat copper as an indirect project-cost and industrial-cycle variable.",
            "Use lagged analysis because procurement contracts and project execution take time.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect project-input and industrial-cycle signal. Aluminium can enter "
        "equipment, structures, electrical applications and engineering supply "
        "chains used in large energy projects.",
        indirect=(
            "Engineering equipment",
            "Electrical applications",
            "Project structures",
            "Industrial capex",
        ),
        channels=(
            "Procurement-cost transmission",
            "Project-execution transmission",
            "Industrial-cycle signal",
        ),
        supply=(
            "Equipment suppliers",
            "Electrical components",
            "Engineering and construction",
        ),
        demand=(
            "Energy infrastructure",
            "Industrial investment",
            "Renewable projects",
        ),
        cost=(
            "Equipment and material procurement",
            "Project construction",
        ),
        strategy=(
            "Large energy-project execution",
            "Energy-transition infrastructure",
        ),
        indicators=(
            "Aluminium return",
            "ONGC capex",
            "Project pipeline",
            "Equipment-cost proxies",
            "Lagged relationship",
        ),
        events=("Aluminium price shocks", "Large industrial-capex changes"),
        logic=(
            "Do not treat aluminium as a direct revenue commodity for ONGC.",
            "Measure its relevance through project costs and industrial activity.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect infrastructure and industrial-input signal. Zinc is mainly "
        "connected through galvanised steel, corrosion-resistant structures, "
        "equipment and large energy-infrastructure projects.",
        indirect=(
            "Galvanised steel",
            "Offshore structures",
            "Pipelines and infrastructure",
            "Industrial construction",
        ),
        channels=(
            "Project procurement",
            "Infrastructure-capex transmission",
            "Industrial-cycle signal",
        ),
        supply=(
            "Galvanised structures",
            "Steel equipment",
            "Energy infrastructure",
        ),
        demand=(
            "Energy-sector capex",
            "Industrial construction",
            "Infrastructure investment",
        ),
        cost=(
            "Steel and galvanising inputs",
            "Project construction",
        ),
        strategy=("Large upstream and energy-infrastructure projects",),
        indicators=(
            "Zinc return",
            "Steel-price proxies",
            "ONGC capex",
            "Project awards",
            "Lagged relationship",
        ),
        events=("Zinc/steel input shocks", "Infrastructure-cycle changes"),
        logic=(
            "Treat zinc as an indirect project-cost variable.",
            "Test whether zinc contains information after controlling for NIFTY and crude.",
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
    """Return the complete ONGC company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one of ONGC's nine market characters."""
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

    Historical linkage is deliberately not validated here because it requires
    real market/company observations and belongs to the calculation layer.
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
            and bool(COMPANY_CHARACTER.core_businesses)
            and bool(COMPANY_CHARACTER.key_indicators)
        ),
    }


if __name__ == "__main__":
    result = validate_character()

    print("ONGC CHARACTER VALIDATION")
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
