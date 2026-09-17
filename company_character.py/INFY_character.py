"""
INFY — Infosys Company Character & 9-Market Relationship Definition

This module describes Infosys' business character and defines what a later
historical engine should calculate for each of the nine tracked markets.

The supplied snapshot CSV values (RANK, PCT_CHANGE, LINKAGE_SCORE, RELATION)
are deliberately NOT hard-coded as conclusions. They are observation inputs
for a future calculation layer, not permanent company-character facts.

Company basis: Infosys is a global digital/IT services and consulting company
with strong AI, cloud, data, cybersecurity, engineering, application,
infrastructure and business-process capabilities. Its economic exposure is
therefore primarily through global enterprise technology spending, client
budgets, workforce costs, utilization, pricing, geography/currency mix and
energy/technology infrastructure rather than direct commodity consumption.
"""

from __future__ import annotations

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
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Indian large-cap equity-market and risk/liquidity regime.",
        "Direct equity-market exposure plus a broad domestic/global risk benchmark.",
        "NIFTY regime -> risk appetite, valuation and foreign/domestic flows -> IT-sector valuation -> INFY.",
        "Calculate INFY excess return versus NIFTY, rolling beta, correlation, volatility response and event-window returns. Separate broad market movement from INFY-specific events.",
        (
            "INFY return", "NIFTY return", "rolling beta",
            "rolling correlation", "India VIX", "INFY volume",
            "FII/DII flows", "IT sector index",
        ),
        (
            "RBI policy", "Union Budget", "market-wide risk events",
            "INFY earnings", "large deal announcements",
            "major technology/AI announcements",
        ),
        ("intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Global energy-price and inflation-cycle benchmark.",
        "Indirect macro exposure; crude is not a major direct revenue/cost input for Infosys.",
        "Crude -> inflation/interest-rate expectations and client cost pressure -> enterprise technology budgets/risk appetite -> INFY.",
        "Test crude returns against INFY after controlling for NIFTY, USD/INR and global tech indicators. Examine whether relationships operate through inflation, rates or client spending rather than assuming direct causation.",
        (
            "Brent return", "WTI return", "USD/INR",
            "US inflation", "US rates", "global PMI",
            "INFY return", "IT sector return",
        ),
        (
            "OPEC+ decisions", "energy shocks", "geopolitical disruptions",
            "inflation surprises", "central-bank decisions",
        ),
        ("1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Gold": _mc(
        "Gold",
        "Safe-haven, real-rate and global risk-sentiment market.",
        "Indirect macro and investor-sentiment exposure; gold is not a core operating input.",
        "Gold -> real rates/risk sentiment/wealth preservation -> global investment confidence and equity valuation -> INFY.",
        "Calculate rolling and lagged association with INFY while controlling for NIFTY, USD/INR, rates and volatility. Use event studies for major risk-off episodes.",
        (
            "gold return", "USD gold", "INR gold",
            "US real yield", "India VIX", "USD/INR",
            "INFY return",
        ),
        (
            "geopolitical shocks", "central-bank decisions",
            "inflation surprises", "major risk-off events",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Silver": _mc(
        "Silver",
        "Precious/industrial-metal and global-cycle sentiment market.",
        "Indirect macro exposure; no core direct silver consumption is assumed.",
        "Silver/industrial cycle -> global growth and inflation expectations -> enterprise spending/risk appetite -> INFY.",
        "Measure incremental association after controlling for NIFTY, crude, rates and USD/INR. Treat any relationship as evidence to investigate, not causation.",
        (
            "silver return", "gold/silver ratio",
            "industrial-metals index", "global PMI",
            "USD/INR", "INFY return",
        ),
        (
            "industrial-cycle shocks", "inflation releases",
            "geopolitical events",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Global/regional energy market influencing inflation, power and industrial activity.",
        "Indirect exposure through macro conditions and the operating cost of technology infrastructure.",
        "Natural gas -> energy/power costs and inflation -> client budgets, data-centre economics and macro demand -> INFY.",
        "Test gas returns against INFY with controls for crude, electricity, NIFTY and FX. Only retain a meaningful linkage if historical data shows incremental explanatory value.",
        (
            "gas benchmark", "regional gas price",
            "electricity price", "inflation", "USD/INR",
            "INFY return", "global PMI",
        ),
        (
            "gas supply disruptions", "weather shocks",
            "power-market stress", "geopolitical events",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Copper": _mc(
        "Copper",
        "Global industrial, infrastructure and electrification-cycle metal.",
        "Indirect exposure through technology hardware, data-centre/electrical infrastructure and global economic activity.",
        "Copper -> industrial/electrification capex and hardware ecosystem -> enterprise investment cycle -> INFY.",
        "Use copper as a global activity proxy and test incremental association with INFY after controlling for NIFTY, global tech indices, PMI and FX.",
        (
            "LME copper", "copper return", "global PMI",
            "technology capex", "semiconductor cycle",
            "INFY return",
        ),
        (
            "China/global PMI shocks", "infrastructure stimulus",
            "copper supply disruptions", "AI/data-centre capex cycle",
        ),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Global industrial metal used in electronics, equipment, buildings and transport.",
        "Indirect exposure through IT hardware, data-centre/equipment supply chains and global industrial activity.",
        "Aluminium -> hardware/equipment and infrastructure costs -> technology capex and client investment environment -> INFY.",
        "Calculate rolling/lagged association with INFY while controlling for global technology spending, NIFTY, FX and broad metals. Do not classify aluminium as a direct Infosys revenue driver.",
        (
            "LME aluminium", "aluminium premium",
            "global PMI", "server/data-centre capex",
            "hardware-cost proxy", "INFY return",
        ),
        (
            "aluminium supply shocks", "data-centre buildout",
            "technology hardware cycle", "global industrial shocks",
        ),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Zinc": _mc(
        "Zinc",
        "Industrial metal linked to galvanising, construction and manufacturing.",
        "Low-to-indirect exposure through office/data-centre infrastructure and broad industrial activity.",
        "Zinc -> infrastructure/manufacturing cycle -> technology investment environment -> INFY.",
        "Require incremental explanatory power beyond NIFTY, copper, aluminium and global PMI before treating zinc as a meaningful INFY factor.",
        (
            "LME zinc", "global PMI", "construction cycle",
            "technology capex", "INFY return",
        ),
        (
            "infrastructure cycle", "metal supply shocks",
            "global manufacturing changes",
        ),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Electricity": _mc(
        "Electricity",
        "Power-market condition affecting offices, campuses and technology infrastructure.",
        "Direct operating-infrastructure exposure, but generally much smaller than employee and subcontractor costs.",
        "Electricity -> campus/data-centre/technology infrastructure cost and availability -> operating margin/capex -> INFY.",
        "Use reliable regional electricity data and compare it with Infosys energy consumption, infrastructure cost proxies and margins. Avoid using a single arbitrary electricity benchmark for all geographies.",
        (
            "commercial/industrial tariff", "renewable power share",
            "data-centre power use", "energy cost",
            "operating margin", "INFY return",
        ),
        (
            "tariff changes", "power shortages",
            "extreme-weather disruptions", "data-centre expansion",
            "renewable-energy projects",
        ),
        ("1D", "1W", "1M", "1Q", "1Y"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="INFY",
    company_name="Infosys Limited",
    sector="Information Technology / IT Services",
    industry_character=(
        "Global enterprise technology-services and consulting business spanning "
        "AI, cloud, data, digital transformation, consulting, engineering, "
        "cybersecurity, applications, infrastructure and business-process services."
    ),
    business_character=(
        "Asset-light, talent-intensive global technology-services model. Revenue "
        "depends primarily on enterprise technology budgets, client spending, "
        "large-deal wins, digital/AI/cloud adoption, geographic and industry mix, "
        "pricing, utilization and delivery capacity. Costs are dominated by people, "
        "subcontracting, facilities, technology infrastructure, sales and currency."
    ),
    demand_drivers=(
        "Global enterprise technology spending",
        "AI and generative-AI adoption",
        "Cloud migration and modernization",
        "Data and analytics investment",
        "Cybersecurity spending",
        "Application modernization",
        "Digital transformation",
        "Enterprise cost-optimization programs",
        "Engineering and product development",
        "Global GCC expansion",
        "Client industry investment cycles",
        "Large transformation programs",
        "Technology refresh cycles",
        "Macroeconomic confidence",
    ),
    revenue_drivers=(
        "Digital services revenue",
        "AI services and Infosys Topaz",
        "Cloud services and Infosys Cobalt",
        "Data and analytics",
        "Consulting",
        "Engineering services",
        "Cybersecurity",
        "Application development and maintenance",
        "Infrastructure services",
        "Business-process management",
        "Large deal TCV",
        "Client count and wallet share",
        "Utilization",
        "Billing rates",
        "Geography mix",
        "Industry vertical mix",
        "Currency translation",
    ),
    cost_drivers=(
        "Employee compensation",
        "Hiring and attrition",
        "Subcontractor costs",
        "Training and reskilling",
        "Travel",
        "Sales and marketing",
        "Facilities and campuses",
        "Data-centre and technology infrastructure",
        "Cloud/software costs",
        "Depreciation",
        "Acquisitions",
        "Currency movements",
        "Employee utilisation",
    ),
    supply_chain_character=(
        "Global technology/cloud partners",
        "AI model and infrastructure ecosystem",
        "Enterprise software vendors",
        "Hardware and semiconductor ecosystem",
        "Cybersecurity technology vendors",
        "Data and analytics platforms",
        "Telecom/network infrastructure",
        "Cloud infrastructure",
        "Technology subcontractors",
        "Global talent ecosystem",
        "Universities and training partners",
    ),
    strategic_drivers=(
        "AI-first enterprise transformation",
        "Infosys Topaz",
        "Infosys Cobalt",
        "Cloud modernization",
        "Data and analytics",
        "Cybersecurity",
        "Application modernization",
        "Engineering and ER&D",
        "Large-deal execution",
        "Talent reskilling",
        "Automation and productivity",
        "Global partnerships",
        "Industry-specific solutions",
        "Cost efficiency",
        "Free-cash-flow generation",
    ),
    key_indicators=(
        "Revenue growth",
        "Constant-currency growth",
        "Operating margin",
        "Free cash flow",
        "Large deal TCV",
        "Net new large-deal TCV",
        "Client count",
        "US$50m+ clients",
        "Utilization",
        "Attrition",
        "Employee headcount",
        "Hiring",
        "Digital revenue mix",
        "AI revenue/AI program activity",
        "Cloud revenue/activity",
        "Geography mix",
        "Industry vertical mix",
        "Pricing",
        "Volume growth",
        "Revenue per employee",
        "Cash and investments",
        "EPS",
        "USD/INR",
        "INFY return and volatility",
    ),
    key_events=(
        "Quarterly and annual results",
        "Management guidance",
        "Large deal wins",
        "Client contract cancellations or expansions",
        "AI/Topaz launches",
        "Major cloud partnerships",
        "Acquisitions",
        "Major client concentration changes",
        "US/Europe technology spending changes",
        "Visa/immigration policy changes",
        "Global recession or recovery signals",
        "Currency shocks",
        "Major cybersecurity events",
        "Regulatory changes",
        "Material exchange filings",
        "Employee/attrition changes",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Infosys company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one of the nine market characters."""
    try:
        return MARKET_CHARACTERS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine tracked market characters."""
    return dict(MARKET_CHARACTERS)


def validate_character() -> bool:
    """Validate structure only; no scores or market predictions are calculated."""
    if COMPANY_CHARACTER.symbol != "INFY":
        return False
    if set(MARKET_CHARACTERS) != set(TRACKED_MARKETS):
        return False

    for market in TRACKED_MARKETS:
        mc = MARKET_CHARACTERS[market]
        if mc.market != market:
            return False
        if not mc.character or not mc.exposure_character:
            return False
        if not mc.impact_path or not mc.calculation_logic:
            return False
        if not mc.relevant_indicators or not mc.expected_timeframes:
            return False

    return True


if __name__ == "__main__":
    print("INFY character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
