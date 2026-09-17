"""
TCS Character Model
===================
Business character + nine tracked market characters for Tata Consultancy Services.

This file defines WHAT should be measured. It does not hard-code:
RANK, PCT_CHANGE, LINKAGE_SCORE, RELATION, correlation, beta, probability,
or any trading decision.

TCS is modelled as a global IT services, consulting and business-solutions
company. Its important economic channels are client technology spending,
AI/cloud/data/cybersecurity adoption, contract wins, utilisation, talent
costs, global delivery, foreign exchange and client-industry cycles.
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
    industry_verticals: Tuple[str, ...]
    service_lines: Tuple[str, ...]
    geographies: Tuple[str, ...]
    delivery_model: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_dependencies: Tuple[str, ...]
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
    symbol="TCS",
    company_name="Tata Consultancy Services Limited",
    primary_identity=(
        "Global IT services, consulting and business-solutions company that "
        "helps enterprises transform technology estates and business "
        "processes through application services, cloud, data, AI, "
        "cybersecurity, engineering, automation, consulting and platforms."
    ),
    business_segments=(
        "IT Services",
        "Consulting",
        "Business Solutions",
        "Application Development and Management",
        "Cloud Services",
        "AI and Data Services",
        "Cybersecurity",
        "Engineering Services",
        "Cognitive Business Operations",
        "Products and Platforms",
        "Digital Transformation",
        "Enterprise Solutions",
    ),
    industry_verticals=(
        "Banking, Financial Services and Insurance",
        "Communication, Media and Technology",
        "Consumer Business",
        "Life Sciences and Healthcare",
        "Manufacturing",
        "Energy, Resources and Utilities",
        "Public Services",
        "Technology and Services",
        "Regional Markets and Others",
    ),
    service_lines=(
        "Application development and management",
        "Cloud transformation",
        "Data platforms",
        "Artificial intelligence and GenAI",
        "Agentic AI",
        "Cybersecurity",
        "Digital engineering",
        "IoT",
        "Enterprise solutions",
        "Systems integration",
        "IT infrastructure",
        "Business process transformation",
        "Cognitive business operations",
        "Automation",
        "Consulting",
        "Customer experience",
        "Software engineering",
        "Products and platforms",
    ),
    geographies=(
        "North America",
        "Latin America",
        "United Kingdom",
        "Continental Europe",
        "Asia Pacific",
        "India",
        "Middle East and Africa",
    ),
    delivery_model=(
        "Global delivery centres",
        "Onshore delivery",
        "Nearshore delivery",
        "Offshore delivery",
        "Distributed engineering teams",
        "Global talent pool",
        "Automation-enabled delivery",
        "AI-enabled delivery",
        "Partner ecosystem",
        "Cloud-provider ecosystem",
        "Enterprise software ecosystem",
    ),
    demand_drivers=(
        "Enterprise technology modernisation",
        "Legacy modernisation",
        "Cloud adoption",
        "Data modernisation",
        "AI and GenAI adoption",
        "Agentic AI adoption",
        "Cybersecurity requirements",
        "Cost optimisation",
        "Vendor consolidation",
        "Digital transformation",
        "Customer-experience transformation",
        "Automation",
        "Regulatory technology requirements",
        "Industry-specific transformation",
        "Technology debt reduction",
        "Enterprise resilience",
    ),
    revenue_drivers=(
        "Total contract value",
        "Large-deal wins",
        "Order book",
        "Client additions",
        "Revenue growth",
        "Volume growth",
        "Pricing",
        "Utilisation",
        "Service mix",
        "AI and cloud revenue",
        "Digital revenue",
        "Engineering revenue",
        "Geographic growth",
        "Industry-vertical growth",
        "Renewals",
        "Cross-sell",
        "Client wallet share",
    ),
    cost_drivers=(
        "Employee compensation",
        "Subcontractor costs",
        "Talent acquisition",
        "Reskilling and training",
        "Attrition",
        "Travel",
        "Facilities",
        "Data-centre and cloud infrastructure",
        "Technology platforms",
        "Cybersecurity infrastructure",
        "Sales and marketing",
        "Currency movement",
        "Acquisition and integration",
        "AI infrastructure investment",
    ),
    supply_chain_dependencies=(
        "Global talent",
        "Cloud providers",
        "Hyperscalers",
        "Enterprise software partners",
        "Technology vendors",
        "Data-centre infrastructure",
        "Telecommunications",
        "Cybersecurity ecosystem",
        "Universities and talent pipeline",
        "Global delivery infrastructure",
    ),
    strategic_drivers=(
        "Become a leading AI-led technology services company",
        "Build full-stack AI capabilities",
        "Scale AI infrastructure-to-intelligence services",
        "Expand cloud and data modernisation",
        "Strengthen cybersecurity",
        "Industrialise AI-enabled delivery",
        "Increase productivity through automation",
        "Deepen strategic client relationships",
        "Expand large-deal pipeline",
        "Strengthen partner ecosystem",
        "Invest in talent and reskilling",
        "Expand industry-specific platforms",
        "Grow regional markets",
    ),
    operational_risks=(
        "Client technology-spending slowdown",
        "Large-client concentration",
        "Deal delays",
        "Project execution risk",
        "Talent attrition",
        "Wage inflation",
        "Cybersecurity incident",
        "Data-security incident",
        "AI disruption to traditional services",
        "Cloud/vendor dependency",
        "Foreign-exchange volatility",
        "Geopolitical disruption",
        "Regulatory restrictions",
    ),
    regulatory_and_client_risks=(
        "Data privacy regulation",
        "Cybersecurity regulation",
        "AI regulation",
        "Responsible-AI requirements",
        "Cross-border data rules",
        "Client compliance requirements",
        "Sector-specific financial regulation",
        "Healthcare data requirements",
        "Export-control requirements",
        "Immigration/work-permit rules",
        "Government technology procurement rules",
    ),
    key_indicators=(
        "Revenue growth",
        "Constant-currency growth",
        "Total contract value",
        "Order book",
        "Large-deal TCV",
        "Book-to-bill",
        "Client additions",
        "$100M+ clients",
        "$50M+ clients",
        "$10M+ clients",
        "Utilisation",
        "Attrition",
        "Employee headcount",
        "Employee pyramid",
        "Subcontractor ratio",
        "Operating margin",
        "EBIT margin",
        "Net margin",
        "Free cash flow",
        "Cash conversion",
        "Days sales outstanding",
        "AI revenue",
        "Cloud revenue",
        "Cybersecurity growth",
        "Engineering growth",
        "Digital growth",
        "Industry-vertical growth",
        "Geographic growth",
        "Dividend payout",
        "Buyback",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "Large deal win",
        "Large deal loss",
        "Order-book change",
        "AI partnership",
        "Cloud partnership",
        "Cybersecurity partnership",
        "New AI product/platform",
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
        "Global IT-spending slowdown",
        "Management guidance",
        "Capital-allocation update",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market beta plus Indian technology-sector and global-growth sentiment",
        (
            "Market beta",
            "IT-sector valuation",
            "Global risk appetite",
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
            "Indian business investment",
            "Global economic growth",
        ),
        (
            "Valuation multiple",
            "Funding conditions",
        ),
        (
            "GDP growth",
            "Interest rates",
            "Risk appetite",
            "Global technology spending",
            "Liquidity",
        ),
        (
            "Rolling beta",
            "Rolling correlation",
            "IT-sector relative strength",
            "Volatility",
            "Residual return",
        ),
        (
            "Quarterly results",
            "Large deals",
            "Guidance",
            "AI announcements",
            "Client-spending commentary",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Remove NIFTY and IT-sector effects before testing commodity-specific relationships.",
            "Use residual TCS returns for cross-market attribution.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Primarily indirect macro, inflation, client-spending and travel/logistics exposure",
        (
            "Global inflation",
            "Client discretionary IT spending",
            "Energy-sector client demand",
            "Travel and facilities cost",
            "Global growth signal",
        ),
        (
            "Travel",
            "Facilities",
            "Data-centre infrastructure",
            "Energy-sector client ecosystem",
        ),
        (
            "Energy-sector technology spending",
            "Global enterprise activity",
            "Consumer purchasing power",
        ),
        (
            "Travel",
            "Facilities",
            "Energy and infrastructure",
        ),
        (
            "Inflation",
            "Global growth",
            "Interest rates",
            "Energy-sector capex",
            "Currency",
        ),
        (
            "Crude return",
            "Global PMI",
            "Energy capex",
            "TCS energy-vertical growth",
            "Operating margin",
            "Travel/facility expense",
        ),
        (
            "Oil-price shock",
            "Global inflation shock",
            "Energy-sector capex change",
            "Global recession signal",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Crude is not a core TCS input.",
            "Test it as a macro and client-industry variable, especially through Energy/Resources/Utilities demand.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Primarily global risk, real-rate, liquidity and defensive-sentiment exposure",
        (
            "Risk appetite",
            "Real rates",
            "Global liquidity",
            "Defensive rotation",
            "Currency",
        ),
        (
            "No major direct physical gold dependency",
            "Indirect capital-market channel",
        ),
        (
            "Enterprise confidence",
            "Technology-budget sentiment",
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
            "Global liquidity",
        ),
        (
            "Gold return",
            "Real yields",
            "USD",
            "VIX/risk proxy",
            "Global IT-spending indicators",
            "Residual TCS return",
        ),
        (
            "Gold breakout",
            "Real-rate shock",
            "Global risk-off event",
            "Liquidity shock",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Treat gold as a macro regime variable, not an IT-service input.",
            "Control for rates, USD and NIFTY before attribution.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial-cycle and technology-infrastructure signal",
        (
            "Industrial cycle",
            "Technology investment sentiment",
            "Risk appetite",
            "Electrification/infrastructure cycle",
        ),
        (
            "No major direct silver dependency",
            "Indirect technology infrastructure channel",
        ),
        (
            "Enterprise investment",
            "Manufacturing digitisation",
            "Infrastructure technology spending",
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
            "Residual TCS return",
        ),
        (
            "Industrial slowdown",
            "Commodity-cycle reversal",
            "Global growth shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Use silver mainly as an industrial/macro regime variable.",
            "Do not infer direct IT-service cost exposure.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect energy, macro and Energy/Resources/Utilities client-demand exposure",
        (
            "Energy-sector technology spending",
            "Global industrial activity",
            "Inflation",
            "Energy infrastructure investment",
        ),
        (
            "Energy-sector clients",
            "Utilities clients",
            "Data-centre energy ecosystem",
        ),
        (
            "Energy capex",
            "Utility modernisation",
            "Industrial digitisation",
            "Infrastructure investment",
        ),
        (
            "Limited direct TCS production cost",
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
            "Energy-sector TCV",
            "Utilities growth",
            "Data-centre energy metrics",
        ),
        (
            "Gas-price shock",
            "Energy investment cycle",
            "Utility spending change",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Separate Energy/Utilities client demand from TCS's own infrastructure cost.",
            "Where data permits, compare energy-sector TCV and growth with gas-price regimes.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect technology-infrastructure, data-centre, industrial and client-capex exposure",
        (
            "Digital infrastructure capex",
            "Data-centre buildout",
            "Telecom infrastructure",
            "Industrial automation",
            "Global capex cycle",
        ),
        (
            "Data centres",
            "Networking equipment",
            "Telecom infrastructure",
            "Electrical systems",
            "Cloud infrastructure",
        ),
        (
            "Enterprise digitisation",
            "Data-centre investment",
            "Telecom investment",
            "Industrial automation",
            "Energy-grid modernisation",
        ),
        (
            "Technology infrastructure",
            "Data-centre equipment",
            "Facilities capex",
        ),
        (
            "Global industrial cycle",
            "Electrification",
            "AI infrastructure investment",
            "Capex cycle",
        ),
        (
            "Copper return",
            "Data-centre capex",
            "Hyperscaler capex",
            "Telecom capex",
            "TCS AI/cloud growth",
            "Engineering growth",
        ),
        (
            "Copper shock",
            "AI infrastructure capex change",
            "Telecom investment cycle",
            "Industrial slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Copper can be useful as a proxy for physical digital-infrastructure investment.",
            "Validate with hyperscaler, telecom and data-centre capex rather than assuming a direct commodity link.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect data-centre, telecom, engineering and global industrial-cycle exposure",
        (
            "Data-centre infrastructure",
            "Telecom equipment",
            "Engineering capex",
            "Industrial activity",
        ),
        (
            "Data centres",
            "Server and infrastructure equipment",
            "Telecom networks",
            "Engineering infrastructure",
        ),
        (
            "Digital transformation",
            "Cloud investment",
            "Telecom expansion",
            "Industrial automation",
        ),
        (
            "Limited direct TCS delivery cost",
            "Potential facilities/equipment capex",
        ),
        (
            "Global manufacturing cycle",
            "Infrastructure investment",
            "Technology capex",
        ),
        (
            "Aluminium return",
            "Technology capex",
            "Data-centre investment",
            "Telecom capex",
            "TCS cloud/engineering growth",
        ),
        (
            "Aluminium shock",
            "Infrastructure capex change",
            "Industrial-cycle reversal",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Treat aluminium as an infrastructure/capex proxy, not a core TCS input.",
            "Use physical infrastructure spending to validate the relationship.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect industrial, construction and infrastructure investment signal",
        (
            "Industrial cycle",
            "Construction",
            "Infrastructure capex",
            "Enterprise investment",
        ),
        (
            "Office infrastructure",
            "Data centres",
            "Telecom infrastructure",
            "Industrial facilities",
        ),
        (
            "Enterprise capex",
            "Industrial digitisation",
            "Infrastructure investment",
        ),
        (
            "Limited direct TCS operating-cost exposure",
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
            "Capex",
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
            "Use zinc mainly as an industrial/infrastructure regime variable.",
            "Do not interpret zinc as a direct TCS input cost.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Indirect but increasingly relevant digital-infrastructure and operating-cost exposure",
        (
            "Data-centre power demand",
            "Office and delivery-centre operating cost",
            "Cloud infrastructure",
            "AI compute economics",
            "Grid availability",
        ),
        (
            "Data centres",
            "Delivery centres",
            "Office infrastructure",
            "Cloud and AI infrastructure",
            "Telecom networks",
        ),
        (
            "AI adoption",
            "Cloud adoption",
            "Data-centre expansion",
            "Digital transformation",
            "Enterprise technology spending",
        ),
        (
            "Data-centre electricity",
            "Facilities",
            "AI compute",
            "Cloud infrastructure",
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
            "Facilities expense",
            "Operating margin",
            "Cloud/AI growth",
        ),
        (
            "Power-price spike",
            "Grid disruption",
            "Data-centre capacity constraint",
            "Renewable-power event",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M"),
        (
            "Electricity should be linked primarily to digital infrastructure and operating economics.",
            "As AI/data-centre intensity rises, test whether power economics becomes more material.",
            "Separate TCS own-cost exposure from client demand for energy-sector technology.",
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
    """Return the complete TCS company character."""
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
    print("TCS character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
