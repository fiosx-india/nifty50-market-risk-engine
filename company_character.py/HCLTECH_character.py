"""
HCLTECH — Company Character & 9-Market Research Model

This module describes HCLTech's business character and its research exposure
to the 9 tracked markets.

The market definitions are research hypotheses/measurement plans, not
precomputed correlations or trading signals. Historical linkage must be
calculated later from real market, company, financial, event and macro data.
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
    character: str
    exposure_character: str
    impact_path: str
    calculation_logic: str
    relevant_indicators: Tuple[str, ...]
    relevant_events: Tuple[str, ...]
    expected_timeframes: Tuple[str, ...]


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    sector: str
    industry_character: str
    business_character: str
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_character: Tuple[str, ...]
    strategic_drivers: Tuple[str, ...]
    key_indicators: Tuple[str, ...]
    key_events: Tuple[str, ...]
    market_characters: Dict[str, MarketCharacter]


def _mc(
    market: str,
    character: str,
    exposure_character: str,
    impact_path: str,
    calculation_logic: str,
    indicators: Tuple[str, ...],
    events: Tuple[str, ...],
    timeframes: Tuple[str, ...],
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        character=character,
        exposure_character=exposure_character,
        impact_path=impact_path,
        calculation_logic=calculation_logic,
        relevant_indicators=indicators,
        relevant_events=events,
        expected_timeframes=timeframes,
    )


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "Aluminium": _mc(
        "Aluminium",
        "Industrial-metals and technology-hardware cost/demand signal.",
        "Primarily indirect exposure. Aluminium can affect clients in "
        "manufacturing, automotive, electronics, telecom equipment, data-centre "
        "infrastructure and engineering; it is not a primary HCLTech revenue "
        "input.",
        "Aluminium -> client manufacturing/equipment economics -> client IT/ER&D "
        "budgets and product-engineering demand -> HCLTech bookings/revenue.",
        "Calculate lagged correlation and regression between aluminium returns and "
        "HCLTech returns, but also test aluminium against manufacturing/technology "
        "spending proxies. Control for NIFTY, USD/INR and global tech conditions "
        "to distinguish a commodity-cycle effect from general risk sentiment.",
        (
            "aluminium return",
            "aluminium volatility",
            "global manufacturing proxy",
            "HCLTech return/volume",
            "technology-sector relative strength",
        ),
        (
            "large aluminium price shock",
            "global manufacturing slowdown",
            "electronics/auto production changes",
            "industrial capex cycle changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Copper": _mc(
        "Copper",
        "Electrical, semiconductor, telecom, data-centre and industrial-cycle signal.",
        "Indirect exposure through clients whose engineering and technology "
        "budgets depend on electrical infrastructure, networking, semiconductor, "
        "industrial automation, mobility and energy-transition investment.",
        "Copper -> electrical/industrial capex cycle -> engineering, embedded, "
        "cloud/edge and digital-transformation demand -> HCLTech ER&D/ITBS pipeline.",
        "Use copper returns and lagged changes as a macro explanatory variable. "
        "Compare against semiconductor/electronics and industrial-capex proxies, "
        "then control for NIFTY and global technology indices. Test whether copper "
        "provides incremental predictive information.",
        (
            "copper return",
            "copper volatility",
            "semiconductor-cycle proxy",
            "industrial-production proxy",
            "HCLTech relative return",
        ),
        (
            "global manufacturing changes",
            "semiconductor cycle turns",
            "grid/renewable investment changes",
            "major copper supply disruptions",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Global inflation, client-cost and macro-demand shock.",
        "Indirect exposure through global clients: oil affects transportation, "
        "industrial costs, inflation, consumer spending and corporate technology "
        "budgets. It may also affect travel/onsite costs and discretionary IT spend.",
        "Crude -> inflation/growth expectations and client operating costs -> IT "
        "budget decisions -> discretionary transformation demand -> HCLTech "
        "bookings/revenue/margins.",
        "Test oil shocks with lagged regression and event studies. Include USD/INR, "
        "global growth, rates and NIFTY controls. Separately test revenue-growth "
        "and margin sensitivity because the same oil shock can affect demand and "
        "operating costs differently.",
        (
            "Brent/WTI return",
            "oil volatility",
            "USD/INR",
            "global PMI/growth proxy",
            "HCLTech return",
            "operating margin",
        ),
        (
            "OPEC+ decisions",
            "geopolitical supply shocks",
            "large oil-price spikes",
            "global inflation surprises",
            "major recession/growth events",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Electricity": _mc(
        "Electricity",
        "Direct operating-infrastructure input plus client capex signal.",
        "Direct exposure through offices, campuses, data-centre/cloud infrastructure "
        "and technology operations; indirect exposure through clients' electricity-"
        "intensive businesses and digital infrastructure investments.",
        "Electricity cost/reliability -> HCLTech operating expense and delivery "
        "capacity; electricity investment -> client infrastructure/automation "
        "spending -> ER&D/ITBS demand.",
        "Where company-specific power and data-centre information is available, "
        "measure cost sensitivity directly. For external power prices, use "
        "regional proxies and lagged regression. Separate company operating-cost "
        "effects from client-demand effects.",
        (
            "regional power price",
            "power-demand proxy",
            "data-centre capacity",
            "HCLTech operating margin",
            "HCLTech return/volume",
        ),
        (
            "power shortages",
            "data-centre expansion",
            "renewable procurement",
            "major infrastructure outages",
            "energy-policy changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Gold": _mc(
        "Gold",
        "Safe-haven, liquidity, real-rates and global risk-sentiment signal.",
        "Primarily indirect macro exposure. Gold can proxy changes in risk appetite, "
        "real rates, liquidity and geopolitical uncertainty that influence global "
        "technology spending and valuation multiples.",
        "Gold -> real rates/risk sentiment/liquidity -> global equity valuation and "
        "enterprise spending expectations -> HCLTech valuation and demand.",
        "Use gold only as one macro factor. Run multivariate models controlling for "
        "NIFTY, global technology indices, USD/INR, bond yields and volatility. "
        "Test incremental explanatory power rather than assuming a direct business "
        "relationship.",
        (
            "gold return",
            "real-yield proxy",
            "USD/INR",
            "VIX/global volatility",
            "global technology index",
            "HCLTech relative return",
        ),
        (
            "central-bank rate decisions",
            "inflation surprises",
            "geopolitical shocks",
            "major safe-haven flows",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Indian systematic-equity and risk-appetite benchmark.",
        "Direct stock-market exposure through beta, sector rotation, liquidity and "
        "valuation regime. Business exposure is indirect because HCLTech earns "
        "primarily from global technology clients.",
        "NIFTY -> Indian market risk/liquidity -> HCLTech valuation and investor "
        "flows -> stock return/volume; separately, global technology demand -> "
        "company fundamentals.",
        "Calculate rolling correlation, beta, downside beta, relative strength, "
        "drawdown and residual return versus NIFTY. For the business model, combine "
        "this with global technology and USD/INR factors rather than treating NIFTY "
        "as the sole driver.",
        (
            "NIFTY return",
            "rolling beta",
            "relative strength",
            "volume",
            "market volatility",
            "drawdown",
        ),
        (
            "RBI policy",
            "Union Budget/fiscal policy",
            "major index rebalancing",
            "global risk-off events",
            "HCLTech earnings",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q", "1Y"),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Energy-cost and industrial-client-cycle signal.",
        "Indirect exposure through energy-intensive clients, industrial automation, "
        "manufacturing and utilities. It can influence enterprise capex and operating "
        "budgets, but is not a core HCLTech revenue input.",
        "Natural gas -> industrial energy economics -> client capex/automation and "
        "digital-transformation budgets -> ER&D/ITBS demand.",
        "Use gas returns with industrial-production, PMI and energy-sector controls. "
        "Measure lagged relationships and event responses; separately examine whether "
        "gas shocks coincide with changes in large-deal activity or client vertical "
        "demand.",
        (
            "natural-gas return",
            "gas volatility",
            "industrial PMI",
            "industrial-production proxy",
            "HCLTech return",
        ),
        (
            "LNG/gas supply disruptions",
            "global gas-price shocks",
            "industrial energy-policy changes",
            "manufacturing-cycle changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Silver": _mc(
        "Silver",
        "Industrial-technology plus precious-metals macro-cycle signal.",
        "Indirect exposure through electronics, semiconductor, solar, industrial "
        "technology and global risk sentiment. The relationship should be tested "
        "through client-industry demand rather than assumed as a direct input.",
        "Silver -> industrial/electronics cycle and risk sentiment -> technology "
        "capex and engineering demand -> HCLTech ER&D/ITBS activity.",
        "Compare silver with copper and technology-sector indicators. Use rolling "
        "and lagged regression and event studies, controlling for gold, NIFTY, "
        "global technology performance and USD/INR.",
        (
            "silver return",
            "silver volatility",
            "gold/silver ratio",
            "semiconductor/electronics proxy",
            "HCLTech relative return",
        ),
        (
            "electronics demand changes",
            "solar-capex changes",
            "industrial-cycle shocks",
            "precious-metals risk events",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Zinc": _mc(
        "Zinc",
        "Industrial, manufacturing and infrastructure-cycle signal.",
        "Indirect exposure through clients in manufacturing, mobility, industrial "
        "products, construction and infrastructure. Zinc itself is not a material "
        "direct HCLTech operating input.",
        "Zinc -> manufacturing/construction cycle -> client technology and engineering "
        "spending -> HCLTech ER&D/ITBS demand.",
        "Use zinc as an industrial-cycle variable with steel, PMI and industrial-"
        "production controls. Test lagged effects and incremental explanatory power "
        "against NIFTY and global technology factors.",
        (
            "zinc return",
            "steel return",
            "industrial-production proxy",
            "manufacturing PMI",
            "HCLTech return/volume",
        ),
        (
            "infrastructure spending changes",
            "manufacturing-cycle turns",
            "zinc supply disruptions",
            "large industrial-capex changes",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="HCLTECH",
    company_name="HCL Technologies Limited",
    sector="Information Technology / Technology Services / Engineering & R&D / Enterprise Software",
    industry_character=(
        "Global technology-services and software business whose economic character "
        "is driven primarily by enterprise technology spending, digital "
        "transformation, cloud, AI, cybersecurity, engineering/R&D and software "
        "subscriptions rather than physical commodity consumption. HCLTech operates "
        "across IT and Business Services, Engineering and R&D Services and "
        "HCLSoftware, with a broad global industry/client footprint."
    ),
    business_character=(
        "Three-layer technology character: IT and Business Services provides "
        "applications, AI, infrastructure, cloud and business-process operations; "
        "Engineering and R&D Services spans product engineering from chip to cloud, "
        "edge and physical systems; HCLSoftware provides enterprise software and "
        "IP-led products. The core economic chain is client demand -> deal wins/"
        "TCV -> bookings/backlog -> revenue conversion -> utilisation/pricing -> "
        "margin and cash flow."
    ),
    demand_drivers=(
        "global enterprise technology budgets",
        "AI and GenAI adoption",
        "cloud migration and modernization",
        "cybersecurity and digital resilience",
        "application modernization",
        "data and analytics investment",
        "engineering/R&D outsourcing",
        "semiconductor and embedded-system engineering",
        "5G, edge and connected-product investment",
        "digital manufacturing and Industry 4.0",
        "enterprise software modernization",
        "business-process automation",
        "global macroeconomic and corporate-capex conditions",
    ),
    revenue_drivers=(
        "IT and Business Services revenue",
        "Engineering and R&D Services revenue",
        "HCLSoftware revenue",
        "new deal TCV",
        "large-deal wins",
        "client additions and wallet share",
        "AI-led services and AI revenue",
        "cloud and application-modernization demand",
        "engineering/product-development demand",
        "software subscriptions and renewals",
        "geographic and vertical mix",
        "pricing and volume",
    ),
    cost_drivers=(
        "employee compensation",
        "subcontracting",
        "onsite/offshore delivery mix",
        "attrition and hiring",
        "training and AI upskilling",
        "cloud/data-centre infrastructure",
        "travel and onsite delivery",
        "sales and marketing",
        "research and development",
        "currency movements",
        "facility and electricity costs",
        "acquisitions and integration costs",
    ),
    supply_chain_character=(
        "global technology talent and engineering workforce",
        "cloud and hyperscaler ecosystem",
        "software/platform partners",
        "semiconductor and hardware ecosystem",
        "telecom and network ecosystem",
        "enterprise application vendors",
        "technology alliances and strategic partners",
        "global delivery centres and offices",
        "data-centre/cloud infrastructure",
        "client procurement and enterprise technology-budget cycles",
    ),
    strategic_drivers=(
        "AI and GenAI services",
        "Agentic AI and AI-led automation",
        "Physical AI and engineering intelligence",
        "cloud and application modernization",
        "cybersecurity and resilience",
        "engineering/R&D scale-up",
        "semiconductor and chip-to-cloud engineering",
        "HCLSoftware product/IP expansion",
        "large strategic client relationships",
        "vertical specialization",
        "deal pipeline and TCV quality",
        "margin discipline and utilization",
        "free cash flow and capital allocation",
    ),
    key_indicators=(
        "constant-currency revenue growth",
        "reported revenue growth",
        "ITBS revenue",
        "Engineering and R&D Services revenue",
        "HCLSoftware revenue",
        "EBIT/EBITDA margin",
        "utilization",
        "attrition",
        "employee headcount",
        "new deal TCV",
        "large-deal TCV",
        "client-count by revenue bands",
        "AI revenue",
        "geographic revenue mix",
        "vertical revenue mix",
        "USD/INR",
        "free cash flow",
        "HCLTECH return, volume and relative strength",
    ),
    key_events=(
        "quarterly results",
        "annual results and annual report",
        "large deal announcements",
        "AI/GenAI product or service launches",
        "major client wins or losses",
        "acquisitions/divestments",
        "HCLSoftware product releases",
        "major cloud/technology partnerships",
        "semiconductor/engineering investments",
        "workforce hiring or restructuring",
        "major regulatory or data-privacy changes",
        "currency and global macro shocks",
        "changes in client technology spending",
        "management guidance changes",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete HCLTech company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return HCLTech's character/exposure model for one tracked market."""
    try:
        return COMPANY_CHARACTER.market_characters[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all 9 market character definitions."""
    return dict(COMPANY_CHARACTER.market_characters)


def validate_character() -> bool:
    """
    Validate structure only.

    This function deliberately does not calculate or invent market scores,
    ranks, percentage changes, correlations or trading decisions.
    """
    if COMPANY_CHARACTER.symbol != "HCLTECH":
        return False

    if tuple(COMPANY_CHARACTER.market_characters.keys()) != TRACKED_MARKETS:
        return False

    for market in TRACKED_MARKETS:
        item = COMPANY_CHARACTER.market_characters[market]
        if item.market != market:
            return False
        if not item.character or not item.exposure_character:
            return False
        if not item.impact_path or not item.calculation_logic:
            return False
        if not item.relevant_indicators or not item.relevant_events:
            return False
        if not item.expected_timeframes:
            return False

    return True


if __name__ == "__main__":
    print("HCLTECH character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
    print("Company:", COMPANY_CHARACTER.company_name)
    print("Business character:", COMPANY_CHARACTER.business_character)
