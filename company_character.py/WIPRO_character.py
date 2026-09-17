"""
WIPRO Character Model
=====================
Wipro Limited.

Business character + nine tracked market characters.

The supplied CSV is treated only as research input. RANK, PCT_CHANGE,
LINKAGE_SCORE and RELATION are intentionally excluded from this character
model. Actual market impact must be calculated later using real historical
prices, client-demand indicators, FX, technology spending, energy data,
company financials, news/events and lag-aware statistical methods.
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
    operating_segments: Tuple[str, ...]
    global_business_model: Tuple[str, ...]
    consulting_character: Tuple[str, ...]
    technology_services_character: Tuple[str, ...]
    engineering_character: Tuple[str, ...]
    business_process_services_character: Tuple[str, ...]
    ai_and_data_character: Tuple[str, ...]
    cloud_and_infrastructure_character: Tuple[str, ...]
    cybersecurity_character: Tuple[str, ...]
    industry_exposure: Tuple[str, ...]
    geography_exposure: Tuple[str, ...]
    delivery_and_partner_ecosystem: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_and_dependency_character: Tuple[str, ...]
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
    symbol="WIPRO",
    company_name="Wipro Limited",
    primary_identity=(
        "Global consulting-led, AI-powered technology services company whose "
        "core business is enterprise transformation across consulting, "
        "technology services, engineering and business process services."
    ),
    operating_segments=(
        "IT Services",
        "IT Products",
        "Consulting",
        "Technology Services",
        "Engineering",
        "Business Process Services",
        "AI-Native Business and Platforms",
        "Capco",
    ),
    global_business_model=(
        "Enterprise technology transformation",
        "Consulting-led transformation",
        "AI-powered solutions",
        "Managed services",
        "Global delivery",
        "Long-term enterprise relationships",
        "Partner ecosystem",
        "Hyperscaler ecosystem",
        "Technology-platform ecosystem",
        "Recurring/annuity-like managed-services relationships",
    ),
    consulting_character=(
        "Business consulting",
        "Technology consulting",
        "Digital strategy",
        "Transformation strategy",
        "Operating-model transformation",
        "Industry consulting",
        "AI transformation advisory",
        "Cloud strategy",
        "Cybersecurity strategy",
        "Data strategy",
    ),
    technology_services_character=(
        "Cloud services",
        "Infrastructure services",
        "Network services",
        "Digital workplace",
        "Enterprise applications",
        "Application modernization",
        "Quality engineering",
        "Testing",
        "Digital operations",
        "Platform services",
        "Data and analytics",
        "Artificial intelligence",
    ),
    engineering_character=(
        "Digital engineering",
        "Product engineering",
        "Engineering and R&D",
        "Semiconductor engineering",
        "Silicon engineering",
        "5G",
        "Connected products",
        "Industry 4.0",
        "Smart manufacturing",
        "Cloud products and platforms",
        "Embedded engineering",
        "Systems engineering",
    ),
    business_process_services_character=(
        "Business process outsourcing",
        "Digital operations",
        "Customer experience",
        "Finance and accounting processes",
        "Procurement processes",
        "Industry-specific process transformation",
        "Automation",
        "AI-assisted operations",
        "Managed business processes",
    ),
    ai_and_data_character=(
        "AI-first transformation",
        "Generative AI",
        "Agentic AI",
        "AI platforms",
        "AI-powered enterprise transformation",
        "Data engineering",
        "Data analytics",
        "Machine learning",
        "Responsible AI",
        "AI governance",
        "AI productivity",
        "AI-enabled software delivery",
    ),
    cloud_and_infrastructure_character=(
        "Cloud transformation",
        "Hybrid cloud",
        "Multi-cloud",
        "Cloud migration",
        "Cloud-native applications",
        "Infrastructure management",
        "Digital workplace",
        "Network transformation",
        "Data centres",
        "Hyperscaler partnerships",
        "Cloud optimisation",
        "Infrastructure security",
    ),
    cybersecurity_character=(
        "Cybersecurity consulting",
        "Security strategy",
        "Cyber transformation",
        "Managed security",
        "Threat detection",
        "Identity and access management",
        "Data security",
        "Cloud security",
        "Security operations",
        "Zero Trust",
        "AI security",
        "Governance risk and compliance",
    ),
    industry_exposure=(
        "Banking",
        "Financial Services",
        "Insurance",
        "Healthcare",
        "Technology",
        "Communications",
        "Consumer",
        "Energy",
        "Manufacturing",
        "Resources",
        "Retail",
        "Public sector",
        "Travel and transportation",
        "Automotive",
        "Media",
        "Telecom",
        "Oil and gas",
    ),
    geography_exposure=(
        "Americas",
        "North America",
        "United States",
        "Canada",
        "Europe",
        "United Kingdom",
        "APMEA",
        "India",
        "Middle East",
        "Africa",
        "Asia Pacific",
        "Global delivery markets",
    ),
    delivery_and_partner_ecosystem=(
        "Global delivery centres",
        "Onshore delivery",
        "Nearshore delivery",
        "Offshore delivery",
        "Distributed engineering",
        "Hyperscaler partnerships",
        "Enterprise software partnerships",
        "SAP ecosystem",
        "Oracle ecosystem",
        "Salesforce ecosystem",
        "ServiceNow ecosystem",
        "Microsoft ecosystem",
        "Google Cloud ecosystem",
        "Cloud infrastructure partners",
        "AI technology ecosystem",
    ),
    demand_drivers=(
        "Enterprise IT spending",
        "Cloud migration",
        "AI adoption",
        "Generative AI adoption",
        "Cybersecurity spending",
        "Digital transformation",
        "Application modernisation",
        "Cost optimisation programmes",
        "Outsourcing",
        "Managed services",
        "Business-process transformation",
        "Engineering R&D spending",
        "5G investment",
        "Data-centre investment",
        "Industry 4.0 investment",
        "Technology refresh cycles",
        "Global GDP growth",
    ),
    revenue_drivers=(
        "IT Services revenue",
        "IT Products revenue",
        "Consulting revenue",
        "Technology Services revenue",
        "Engineering revenue",
        "Business Process Services revenue",
        "AI transformation revenue",
        "Cloud revenue",
        "Cybersecurity revenue",
        "Data and analytics revenue",
        "Application services revenue",
        "Managed services revenue",
        "Digital engineering revenue",
        "Client additions",
        "Large deals",
        "Deal bookings",
        "Order pipeline",
        "Utilisation",
        "Billing rates",
        "Geographic growth",
        "Industry growth",
        "Acquisition contribution",
    ),
    cost_drivers=(
        "Employee compensation",
        "Subcontracting",
        "Attrition",
        "Hiring",
        "Training",
        "Cloud infrastructure",
        "Data-centre costs",
        "Office costs",
        "Travel",
        "Sales and marketing",
        "Technology investment",
        "AI investment",
        "Cybersecurity investment",
        "Acquisition/integration costs",
        "Foreign exchange",
        "Depreciation",
    ),
    supply_chain_and_dependency_character=(
        "Talent supply",
        "Engineering talent",
        "AI talent",
        "Cloud infrastructure",
        "Hyperscalers",
        "Enterprise software vendors",
        "Technology partners",
        "Data-centre infrastructure",
        "Telecom networks",
        "Cybersecurity technology",
        "Semiconductor ecosystem",
        "Global internet connectivity",
        "Client technology budgets",
        "Cross-border delivery",
    ),
    strategic_drivers=(
        "AI-first transformation",
        "Consulting-led growth",
        "Scale AI platforms",
        "Cloud transformation",
        "Cybersecurity growth",
        "Engineering growth",
        "Data and analytics",
        "Agentic AI",
        "Large-deal conversion",
        "Client mining",
        "Industry specialisation",
        "Hyperscaler partnerships",
        "Strategic acquisitions",
        "Delivery productivity",
        "Automation",
        "Global expansion",
    ),
    operational_risks=(
        "Enterprise IT-spending slowdown",
        "Client budget cuts",
        "Deal delays",
        "Pricing pressure",
        "Talent attrition",
        "Wage inflation",
        "AI-led pricing disruption",
        "Technology obsolescence",
        "Cybersecurity incident",
        "Data breach",
        "Cloud concentration",
        "Client concentration",
        "Currency volatility",
        "Geopolitical disruption",
        "Acquisition integration",
        "Delivery disruption",
    ),
    regulatory_and_market_risks=(
        "Data privacy laws",
        "AI regulation",
        "Cybersecurity regulation",
        "Cross-border data rules",
        "Digital sovereignty",
        "Export controls",
        "Immigration/visa policy",
        "Labour regulation",
        "Tax changes",
        "Transfer pricing",
        "Sector-specific financial regulation",
        "Healthcare data regulation",
        "Responsible AI requirements",
        "Contractual compliance",
    ),
    key_indicators=(
        "IT Services revenue",
        "IT Products revenue",
        "Constant-currency growth",
        "Reported revenue growth",
        "Large deal bookings",
        "Order book",
        "Bookings",
        "Utilisation",
        "Attrition",
        "Headcount",
        "Revenue per employee",
        "Employee cost",
        "Operating margin",
        "EBIT margin",
        "Free cash flow",
        "DSO",
        "Cash balance",
        "Net cash/debt",
        "Americas growth",
        "Europe growth",
        "APMEA growth",
        "BFSI growth",
        "Technology/Communications growth",
        "Consumer growth",
        "Energy/Manufacturing growth",
        "AI revenue/AI bookings where disclosed",
        "Cloud revenue where disclosed",
        "Cybersecurity bookings",
        "Engineering growth",
        "BPS growth",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "Large deal win",
        "Large deal loss",
        "Client spending change",
        "AI partnership",
        "Hyperscaler partnership",
        "Cloud partnership",
        "Cybersecurity partnership",
        "Strategic acquisition",
        "Acquisition integration",
        "Major client contract",
        "Leadership change",
        "Wage revision",
        "Hiring change",
        "Layoffs/restructuring",
        "Cybersecurity incident",
        "Data breach",
        "AI regulation",
        "Visa/immigration policy",
        "FX shock",
        "Global recession signal",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity beta plus Indian/global technology-sector valuation and risk-cycle exposure",
        (
            "Equity beta",
            "IT-sector valuation",
            "Risk appetite",
            "Indian market liquidity",
            "Global growth sentiment",
        ),
        (
            "Capital-market liquidity",
            "Technology-sector flows",
            "Corporate investment cycle",
        ),
        (
            "Enterprise spending",
            "Indian/global growth",
            "Technology budgets",
            "Corporate confidence",
        ),
        (
            "Funding conditions",
            "Valuation multiple",
            "Talent-cost expectations",
        ),
        (
            "GDP growth",
            "Interest rates",
            "Global PMI",
            "Liquidity",
            "Risk appetite",
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
            "IT-spending outlook",
            "AI strategy",
            "Management guidance",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Control for NIFTY and IT-sector effects before testing commodity-specific relationships.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Indirect macro and client-industry exposure, especially energy, oil & gas, travel and manufacturing",
        (
            "Energy-client technology spending",
            "Oil-and-gas capex",
            "Travel-sector economics",
            "Global inflation",
            "Enterprise budget pressure",
        ),
        (
            "Energy clients",
            "Oil-and-gas clients",
            "Manufacturing clients",
            "Travel/logistics clients",
        ),
        (
            "Energy-sector IT spending",
            "Industrial capex",
            "Global business activity",
            "Enterprise technology budgets",
        ),
        (
            "Travel costs",
            "Office/facility energy",
            "Logistics",
            "General inflation",
        ),
        (
            "Global inflation",
            "Interest rates",
            "Industrial activity",
            "USD",
        ),
        (
            "Crude return",
            "Global PMI",
            "Energy-sector capex",
            "IT spending",
            "Wipro growth",
            "Operating margin",
        ),
        (
            "Oil-price shock",
            "Energy-capex shock",
            "Global inflation shock",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Crude is not a direct Wipro input.",
            "Use energy/oil-and-gas client spending and global macro variables as mediators.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Indirect global risk, real-rate, liquidity and enterprise-confidence exposure",
        (
            "Risk appetite",
            "Real rates",
            "Liquidity",
            "Safe-haven demand",
            "Enterprise confidence",
        ),
        (
            "Global capital markets",
            "Corporate investment",
            "Financial-services clients",
        ),
        (
            "Technology budgets",
            "Financial-services spending",
            "Discretionary enterprise projects",
        ),
        (
            "No major direct production-input channel",
        ),
        (
            "Real rates",
            "Inflation",
            "USD",
            "Risk aversion",
        ),
        (
            "Gold return",
            "Gold volatility",
            "Global PMI",
            "IT spending",
            "Wipro growth",
            "Client budgets",
        ),
        (
            "Gold-price shock",
            "Risk-off event",
            "Real-rate shock",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Treat gold primarily as a macro/risk control variable.",
            "Do not infer a physical commodity relationship.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Indirect industrial and technology-infrastructure cycle exposure",
        (
            "Industrial cycle",
            "Electronics demand",
            "Technology infrastructure",
            "Risk sentiment",
        ),
        (
            "Semiconductor ecosystem",
            "Electronics",
            "Data-centre infrastructure",
            "Telecom infrastructure",
        ),
        (
            "Digital infrastructure",
            "AI infrastructure",
            "Enterprise technology spending",
        ),
        (
            "Minor hardware/equipment exposure",
            "Infrastructure costs",
        ),
        (
            "Industrial growth",
            "Electronics cycle",
            "Risk appetite",
        ),
        (
            "Silver return",
            "Industrial production",
            "Data-centre capex",
            "AI infrastructure spending",
            "Wipro growth",
        ),
        (
            "Silver-price shock",
            "Industrial slowdown",
            "Technology-capex event",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Silver is secondary; test it through technology and industrial-capex variables.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect energy-sector client demand and global industrial-cycle exposure",
        (
            "Energy-sector technology spending",
            "Utilities technology spending",
            "Industrial activity",
            "Energy inflation",
        ),
        (
            "Energy clients",
            "Utilities clients",
            "Industrial clients",
            "Data-centre energy ecosystem",
        ),
        (
            "Energy capex",
            "Digital infrastructure",
            "Industrial transformation",
            "Cloud/data-centre demand",
        ),
        (
            "Office/facility energy",
            "Data-centre energy",
            "Supplier energy",
        ),
        (
            "Energy inflation",
            "Industrial production",
            "Power-market conditions",
        ),
        (
            "Natural-gas return",
            "Energy capex",
            "Data-centre power demand",
            "IT spending",
            "Wipro growth",
        ),
        (
            "Gas-price shock",
            "Energy-capex shock",
            "Industrial slowdown",
        ),
        ("1W", "1M", "3M", "6M"),
        (
            "Use energy-sector client spending as the main mediator.",
            "Avoid treating gas as a direct Wipro production input.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect technology-infrastructure, telecom, data-centre, semiconductor and electrification exposure",
        (
            "Data-centre capex",
            "Telecom infrastructure",
            "Network equipment",
            "Semiconductor ecosystem",
            "Electrification",
        ),
        (
            "Data centres",
            "Telecom networks",
            "Electrical infrastructure",
            "Semiconductor engineering",
            "Cloud infrastructure",
        ),
        (
            "AI infrastructure",
            "Cloud demand",
            "5G investment",
            "Digital transformation",
            "Industrial automation",
        ),
        (
            "Hardware",
            "Engineering equipment",
            "Data-centre infrastructure",
        ),
        (
            "Technology capex",
            "Industrial growth",
            "Electrification",
        ),
        (
            "Copper return",
            "Data-centre capex",
            "Telecom capex",
            "AI infrastructure spending",
            "Engineering bookings",
            "Wipro growth",
        ),
        (
            "Copper-price shock",
            "Data-centre buildout",
            "Telecom investment change",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Copper should be interpreted mainly as a technology/electrification activity proxy, not a major Wipro material input.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect data-centre, telecom, electronics, engineering and industrial-capex exposure",
        (
            "Data-centre construction",
            "Telecom equipment",
            "Engineering infrastructure",
            "Industrial capex",
        ),
        (
            "Data centres",
            "Telecom infrastructure",
            "Industrial equipment",
            "Engineering ecosystem",
        ),
        (
            "Digital infrastructure",
            "Cloud expansion",
            "AI infrastructure",
            "Industrial transformation",
        ),
        (
            "Hardware",
            "Engineering equipment",
            "Facility infrastructure",
        ),
        (
            "Industrial growth",
            "Technology capex",
            "Construction cycle",
        ),
        (
            "Aluminium return",
            "Data-centre capex",
            "Technology capex",
            "Engineering bookings",
            "Cloud demand",
            "Wipro growth",
        ),
        (
            "Aluminium-price shock",
            "Infrastructure-capex event",
            "Industrial slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Use aluminium mainly as an infrastructure/industrial-capex proxy.",
            "Do not assign a direct commodity-cost coefficient to Wipro.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect construction, data-centre, telecom and industrial-infrastructure cycle exposure",
        (
            "Data-centre construction",
            "Telecom infrastructure",
            "Office/facility construction",
            "Industrial capex",
        ),
        (
            "Data centres",
            "Telecom sites",
            "Offices",
            "Engineering facilities",
        ),
        (
            "Digital infrastructure",
            "Cloud expansion",
            "AI infrastructure",
            "Enterprise capex",
        ),
        (
            "Facility construction",
            "Infrastructure",
            "Equipment",
        ),
        (
            "Construction cycle",
            "Industrial growth",
            "Technology capex",
        ),
        (
            "Zinc return",
            "Data-centre construction",
            "Capex",
            "AI infrastructure",
            "Wipro growth",
        ),
        (
            "Zinc-price shock",
            "Construction slowdown",
            "Infrastructure-capex event",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Zinc is an infrastructure-cycle variable for Wipro rather than a core service-delivery input.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Indirect but strategically meaningful exposure through data centres, cloud, AI compute, telecom and delivery infrastructure",
        (
            "AI compute",
            "Data-centre power demand",
            "Cloud infrastructure",
            "Telecom networks",
            "Delivery-centre operations",
            "Office operations",
        ),
        (
            "Data centres",
            "Cloud infrastructure",
            "Telecom infrastructure",
            "Global delivery centres",
            "Office facilities",
        ),
        (
            "AI adoption",
            "Cloud growth",
            "Data-centre investment",
            "Digital transformation",
            "5G",
        ),
        (
            "Data-centre electricity",
            "Office electricity",
            "Cloud infrastructure",
            "Compute cost",
        ),
        (
            "Power prices",
            "Grid reliability",
            "AI compute economics",
            "Renewable-energy availability",
        ),
        (
            "Electricity price",
            "Data-centre power demand",
            "AI compute capacity",
            "Cloud capex",
            "Delivery-centre cost",
            "Wipro growth",
        ),
        (
            "Power-price shock",
            "Grid disruption",
            "Data-centre expansion",
            "AI infrastructure event",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Electricity is not a traditional raw-material cost for Wipro, but it is strategically important through AI compute, cloud/data centres and telecom infrastructure.",
            "Separate electricity-price effects from the much larger enterprise-technology-demand effect.",
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
    """Return the complete Wipro business character."""
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
    """Structural validation only; actual impact is calculated later."""
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
    print("WIPRO character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: {character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
