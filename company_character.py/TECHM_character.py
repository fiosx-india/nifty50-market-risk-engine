"""
TECHM Character Model
=====================
Business character + nine tracked market characters for Tech Mahindra Limited.

This file defines the causal/business channels and the data that should be
measured later. It does NOT hard-code RANK, PCT_CHANGE, LINKAGE_SCORE,
RELATION, correlation, beta, probability, or trading decisions.

Tech Mahindra is modelled as a global technology-services company with
particularly important exposure to Communications/Telecom, Manufacturing,
Technology/Media/Entertainment, BFSI, Healthcare, Energy & Utilities,
Retail, Travel/Transportation and other enterprise sectors.
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
    business_capabilities: Tuple[str, ...]
    industry_verticals: Tuple[str, ...]
    service_lines: Tuple[str, ...]
    geographies: Tuple[str, ...]
    delivery_model: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    ecosystem_dependencies: Tuple[str, ...]
    strategic_drivers: Tuple[str, ...]
    operational_risks: Tuple[str, ...]
    regulatory_and_client_risks: Tuple[str, ...]
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
    symbol="TECHM",
    company_name="Tech Mahindra Limited",
    primary_identity=(
        "Global technology and digital-transformation services company with "
        "deep Communications/Telecom heritage and capabilities spanning "
        "AI, cloud, enterprise applications, engineering, network services, "
        "business-process services, experience services and consulting."
    ),
    business_capabilities=(
        "Artificial Intelligence",
        "Agentic development and modernization",
        "Cloud and infrastructure services",
        "Digital enterprise applications",
        "Business process services",
        "Engineering services",
        "Experience services",
        "Network services",
        "Testing services",
        "Consulting",
        "Data and analytics",
        "Cybersecurity",
        "Digital transformation",
        "Automation",
        "Telecom transformation",
        "Product engineering",
    ),
    industry_verticals=(
        "Communications",
        "Banking and Financial Services",
        "Insurance",
        "Manufacturing",
        "Automotive",
        "Technology",
        "Media and Entertainment",
        "Healthcare and Life Sciences",
        "Energy and Utilities",
        "Oil and Gas",
        "Retail and Consumer Goods",
        "Travel, Transportation and Logistics",
        "Education",
        "Professional Services",
        "Private Equity",
    ),
    service_lines=(
        "AI and GenAI",
        "Agentic AI",
        "Application modernization",
        "Digital enterprise applications",
        "Cloud transformation",
        "Hybrid and multi-cloud",
        "Data and analytics",
        "Cybersecurity",
        "Digital engineering",
        "Product engineering",
        "Network transformation",
        "5G services",
        "Network cloudification",
        "ORAN/VRAN",
        "Enterprise Network-as-a-Service",
        "Business process transformation",
        "Customer experience",
        "Digital workplace",
        "Testing and quality engineering",
        "Consulting",
        "Managed services",
    ),
    geographies=(
        "North America",
        "Europe",
        "United Kingdom",
        "Asia Pacific",
        "India",
        "Middle East and Africa",
        "Latin America",
    ),
    delivery_model=(
        "Global delivery centres",
        "Onshore delivery",
        "Nearshore delivery",
        "Offshore delivery",
        "Distributed engineering",
        "Telecom network operations",
        "Managed services",
        "Cloud partner ecosystem",
        "Hyperscaler ecosystem",
        "Enterprise software ecosystem",
        "AI-enabled delivery",
        "Automation-enabled delivery",
    ),
    demand_drivers=(
        "Telecom network modernisation",
        "5G adoption",
        "Network cloudification",
        "AI and GenAI adoption",
        "Agentic AI adoption",
        "Cloud migration",
        "Legacy modernisation",
        "Cybersecurity requirements",
        "Digital engineering",
        "Manufacturing digitisation",
        "Smart-factory transformation",
        "Customer-experience transformation",
        "Business-process automation",
        "Cost optimisation",
        "Enterprise technology consolidation",
        "Data and analytics adoption",
    ),
    revenue_drivers=(
        "Total contract value",
        "Large-deal wins",
        "Order book",
        "Revenue growth",
        "Constant-currency growth",
        "Volume growth",
        "Pricing",
        "Utilisation",
        "Client additions",
        "Client wallet share",
        "Telecom revenue",
        "Enterprise revenue",
        "Engineering revenue",
        "Cloud revenue",
        "AI revenue",
        "Geographic growth",
        "Industry-vertical growth",
        "Renewals",
        "Cross-sell",
    ),
    cost_drivers=(
        "Employee compensation",
        "Subcontractor costs",
        "Talent acquisition",
        "Reskilling",
        "Attrition",
        "Facilities",
        "Travel",
        "Telecom/network infrastructure",
        "Cloud infrastructure",
        "AI compute",
        "Cybersecurity infrastructure",
        "Sales and marketing",
        "Currency movement",
        "Acquisition and integration",
    ),
    ecosystem_dependencies=(
        "Global technology talent",
        "Telecom operators",
        "Hyperscalers",
        "Cloud providers",
        "Enterprise software vendors",
        "Network equipment ecosystem",
        "Cybersecurity vendors",
        "Data-centre infrastructure",
        "Semiconductor and device ecosystem",
        "Partner ecosystem",
        "Global delivery infrastructure",
    ),
    strategic_drivers=(
        "Scale AI-led transformation",
        "Expand agentic development and modernization",
        "Deepen telecom/network leadership",
        "Grow cloud and infrastructure services",
        "Expand engineering and product services",
        "Strengthen cybersecurity",
        "Increase automation-led productivity",
        "Grow large deals",
        "Deepen strategic accounts",
        "Expand industry-specific platforms",
        "Improve delivery efficiency",
        "Build hyperscaler and ecosystem partnerships",
        "Increase AI-enabled delivery",
    ),
    operational_risks=(
        "Enterprise IT-spending slowdown",
        "Telecom capex slowdown",
        "Client concentration",
        "Deal delays",
        "Project execution risk",
        "Talent attrition",
        "Wage inflation",
        "Cybersecurity incident",
        "Data-security incident",
        "AI disruption to legacy services",
        "Cloud/vendor dependency",
        "Geopolitical disruption",
        "Foreign-exchange volatility",
    ),
    regulatory_and_client_risks=(
        "Data privacy regulation",
        "Cybersecurity regulation",
        "AI regulation",
        "Responsible-AI requirements",
        "Cross-border data rules",
        "Telecom regulation",
        "Financial-services regulation",
        "Healthcare data regulation",
        "Export controls",
        "Immigration/work-permit rules",
        "Client compliance requirements",
    ),
    key_indicators=(
        "Revenue growth",
        "Constant-currency growth",
        "Total contract value",
        "Large-deal TCV",
        "Order book",
        "Book-to-bill",
        "Client additions",
        "$100M+ clients",
        "$50M+ clients",
        "$10M+ clients",
        "Utilisation",
        "Attrition",
        "Headcount",
        "Employee pyramid",
        "Subcontractor ratio",
        "Operating margin",
        "EBIT margin",
        "Free cash flow",
        "Cash conversion",
        "Days sales outstanding",
        "AI growth",
        "Cloud growth",
        "Network-services growth",
        "Engineering growth",
        "Digital-services growth",
        "Telecom vertical growth",
        "Manufacturing vertical growth",
        "Geographic growth",
        "Large-deal conversion",
        "Dividend and capital allocation",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "Large deal win",
        "Large deal loss",
        "Order-book change",
        "Telecom contract",
        "5G project",
        "AI partnership",
        "Cloud partnership",
        "Hyperscaler partnership",
        "Cybersecurity partnership",
        "Major client win",
        "Major client loss",
        "Acquisition",
        "Strategic investment",
        "Leadership change",
        "Attrition change",
        "Wage revision",
        "Regulatory change",
        "Cybersecurity incident",
        "AI regulation",
        "Currency shock",
        "Global IT-spending change",
        "Telecom capex cycle change",
        "Management guidance",
        "Capital-allocation update",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market beta plus Indian technology and global-growth sentiment",
        (
            "Market beta",
            "IT-sector valuation",
            "Risk appetite",
            "Indian equity flows",
            "Technology-cycle sentiment",
        ),
        (
            "Capital-market liquidity",
            "Institutional flows",
            "Technology-sector valuation",
        ),
        (
            "Enterprise technology spending",
            "Telecom capex",
            "Indian business investment",
            "Global growth",
        ),
        (
            "Valuation multiple",
            "Funding conditions",
        ),
        (
            "GDP growth",
            "Interest rates",
            "Liquidity",
            "Risk appetite",
            "Global IT spending",
        ),
        (
            "Rolling beta",
            "Rolling correlation",
            "IT-sector relative strength",
            "Telecom-sector strength",
            "Volatility",
            "Residual return",
        ),
        (
            "Quarterly results",
            "Large deals",
            "Guidance",
            "AI announcements",
            "Telecom-spending commentary",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Remove NIFTY and IT-sector effects before testing commodity-specific relationships.",
            "Use residual TECHM returns for cross-market attribution.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect macro, Energy/Oil & Gas client and inflation exposure",
        (
            "Global inflation",
            "Energy-sector technology spending",
            "Oil & gas client capex",
            "Global growth",
            "Travel/facility costs",
        ),
        (
            "Oil and gas clients",
            "Energy infrastructure",
            "Travel",
            "Facilities",
        ),
        (
            "Oil & gas digital transformation",
            "Energy capex",
            "Industrial activity",
            "Global enterprise spending",
        ),
        (
            "Travel",
            "Facilities",
            "Energy-related infrastructure",
        ),
        (
            "Inflation",
            "Global growth",
            "Interest rates",
            "Energy capex",
            "Currency",
        ),
        (
            "Crude return",
            "Oil & gas capex",
            "Energy-vertical TCV",
            "Global PMI",
            "Operating margin",
        ),
        (
            "Oil-price shock",
            "Energy capex change",
            "Global inflation shock",
            "Oil & gas spending cycle",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Crude is not a core TECHM input.",
            "Test the relationship through Oil & Gas/Energy client spending and macro conditions.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Primarily global risk, real-rate and liquidity regime exposure",
        (
            "Risk appetite",
            "Real rates",
            "Global liquidity",
            "Defensive rotation",
            "Currency",
        ),
        (
            "No major direct gold dependency",
            "Indirect capital-market channel",
        ),
        (
            "Enterprise confidence",
            "Technology budgets",
            "Global investment cycle",
        ),
        (
            "Limited direct operating-cost linkage",
        ),
        (
            "Real yields",
            "USD",
            "Inflation",
            "Risk aversion",
            "Liquidity",
        ),
        (
            "Gold return",
            "Real yields",
            "USD",
            "VIX/risk proxy",
            "Global IT spending",
            "Residual TECHM return",
        ),
        (
            "Gold breakout",
            "Real-rate shock",
            "Global risk-off event",
            "Liquidity shock",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Treat gold as a macro-state variable, not an IT input.",
            "Control for rates, USD and NIFTY before attribution.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial, technology-infrastructure and macro-cycle signal",
        (
            "Industrial cycle",
            "Technology investment",
            "Risk appetite",
            "Electrification cycle",
        ),
        (
            "No major direct silver dependency",
            "Indirect technology-infrastructure channel",
        ),
        (
            "Manufacturing digitisation",
            "Infrastructure investment",
            "Enterprise capex",
        ),
        (
            "Limited direct operating cost",
        ),
        (
            "Global industrial growth",
            "Commodity cycle",
            "Inflation",
            "Risk appetite",
        ),
        (
            "Silver return",
            "Global PMI",
            "Capex cycle",
            "Technology spending",
            "Residual TECHM return",
        ),
        (
            "Industrial slowdown",
            "Commodity reversal",
            "Global growth shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Use silver mainly as an industrial/macro regime variable.",
            "Do not infer direct service-delivery cost exposure.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect Energy/Utilities client, industrial-cycle and infrastructure exposure",
        (
            "Energy-sector technology spending",
            "Utility modernisation",
            "Industrial activity",
            "Energy-infrastructure capex",
        ),
        (
            "Energy and utilities clients",
            "Power infrastructure",
            "Data-centre energy ecosystem",
        ),
        (
            "Energy capex",
            "Utility digitisation",
            "Industrial automation",
            "Infrastructure investment",
        ),
        (
            "Limited direct TECHM delivery cost",
            "Potential data-centre energy economics",
        ),
        (
            "Industrial inflation",
            "Energy capex",
            "Global growth",
            "Power-market conditions",
        ),
        (
            "Natural-gas return",
            "Energy capex",
            "Energy/Utilities TCV",
            "Industrial PMI",
            "AI/data-centre power economics",
        ),
        (
            "Gas-price shock",
            "Energy investment-cycle change",
            "Utility spending change",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Separate Energy/Utilities client demand from TECHM's own operating costs.",
            "Use client-vertical TCV and capex data where available.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect telecom, data-centre, network, industrial and electrification-capex exposure",
        (
            "Telecom infrastructure",
            "Data-centre construction",
            "Network equipment",
            "Industrial automation",
            "Electrification",
        ),
        (
            "Telecom networks",
            "Data centres",
            "Electrical infrastructure",
            "Industrial equipment",
            "5G infrastructure",
        ),
        (
            "5G investment",
            "Network modernisation",
            "Cloud infrastructure",
            "Industrial digitisation",
            "Smart manufacturing",
        ),
        (
            "Technology infrastructure",
            "Network equipment",
            "Facilities capex",
        ),
        (
            "Global industrial cycle",
            "Electrification",
            "AI infrastructure",
            "Telecom capex",
        ),
        (
            "Copper return",
            "Telecom capex",
            "Data-centre capex",
            "5G deployment",
            "Engineering growth",
            "Network-services growth",
        ),
        (
            "Copper shock",
            "5G capex change",
            "Data-centre investment change",
            "Industrial slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Copper can proxy physical communications and digital-infrastructure investment.",
            "Validate with telecom capex, hyperscaler capex and data-centre construction.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect telecom, engineering, data-centre and global industrial-capex exposure",
        (
            "Telecom equipment",
            "Data-centre infrastructure",
            "Engineering capex",
            "Industrial activity",
        ),
        (
            "Network equipment",
            "Data centres",
            "Telecom infrastructure",
            "Engineering facilities",
        ),
        (
            "5G expansion",
            "Cloud investment",
            "Industrial digitisation",
            "Engineering transformation",
        ),
        (
            "Limited direct TECHM operating-cost exposure",
            "Potential infrastructure/equipment capex",
        ),
        (
            "Industrial growth",
            "Technology capex",
            "Infrastructure investment",
        ),
        (
            "Aluminium return",
            "Telecom capex",
            "Data-centre investment",
            "Engineering demand",
            "Cloud growth",
            "Network-services growth",
        ),
        (
            "Aluminium shock",
            "Infrastructure capex change",
            "Industrial-cycle reversal",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Treat aluminium as a physical-infrastructure/capex proxy.",
            "Do not treat it as a major direct software-service input.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect construction, industrial and infrastructure-capex regime exposure",
        (
            "Data-centre construction",
            "Telecom infrastructure",
            "Industrial facilities",
            "Enterprise capex",
        ),
        (
            "Data centres",
            "Telecom infrastructure",
            "Industrial facilities",
            "Office infrastructure",
        ),
        (
            "Enterprise transformation",
            "Industrial digitisation",
            "Network expansion",
            "Infrastructure investment",
        ),
        (
            "Limited direct TECHM operating-cost exposure",
        ),
        (
            "Industrial growth",
            "Construction cycle",
            "Global capex",
            "Commodity inflation",
        ),
        (
            "Zinc return",
            "Global PMI",
            "Construction activity",
            "Data-centre construction",
            "Enterprise IT spending",
        ),
        (
            "Zinc shock",
            "Construction slowdown",
            "Industrial capex reversal",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Use zinc mainly as an infrastructure/industrial regime variable.",
            "Do not interpret it as a direct TECHM cost input.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Indirect but increasingly important digital-infrastructure, telecom and AI-compute exposure",
        (
            "Data-centre power demand",
            "AI compute economics",
            "Network infrastructure",
            "Delivery-centre operating cost",
            "Cloud infrastructure",
            "Grid reliability",
        ),
        (
            "Data centres",
            "Telecom networks",
            "Delivery centres",
            "Cloud infrastructure",
            "AI infrastructure",
        ),
        (
            "AI adoption",
            "Cloud adoption",
            "5G/network expansion",
            "Data-centre investment",
            "Digital transformation",
        ),
        (
            "AI compute",
            "Data-centre electricity",
            "Office/delivery-centre utilities",
            "Network infrastructure",
        ),
        (
            "Power prices",
            "Grid reliability",
            "Renewable availability",
            "AI infrastructure economics",
        ),
        (
            "Electricity price",
            "Data-centre power consumption",
            "AI compute intensity",
            "Network-services growth",
            "Facilities expense",
            "Operating margin",
        ),
        (
            "Power-price spike",
            "Grid disruption",
            "Data-centre capacity constraint",
            "AI infrastructure event",
            "5G network-power event",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M"),
        (
            "Separate TECHM's own power cost from client demand for energy-sector technology.",
            "As AI and data-centre intensity rises, test whether electricity becomes a stronger explanatory variable.",
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
    """Return the complete Tech Mahindra company character."""
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
    """Structural validation only; actual impact is calculated elsewhere."""
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
    print("TECHM character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
