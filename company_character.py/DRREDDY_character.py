"""
DRREDDY (Dr. Reddy's Laboratories Limited)
Company Character & 9-Market Relationship Engine

CHARACTER LAYER ONLY
--------------------
This module describes:
    Company Character
        -> pharmaceutical / global-generics character
        -> API + PSAI + CDMO character
        -> innovative / proprietary-products character
        -> geography and currency character
        -> manufacturing / regulatory / supply-chain character
        -> 9 tracked market characters
        -> historical-calculation instructions

It deliberately does NOT hard-code:
    RANK
    PCT_CHANGE
    LINKAGE_SCORE
    RELATION

Those are outputs of the later historical-analysis layer.
"""

from dataclasses import dataclass, field
from typing import Dict, List


TRACKED_MARKETS = (
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
    impact_path: List[str]
    calculation_logic: List[str]
    relevant_indicators: List[str] = field(default_factory=list)
    relevant_events: List[str] = field(default_factory=list)
    expected_timeframes: List[str] = field(
        default_factory=lambda: [
            "intraday", "1D", "1W", "1M", "3M", "6M", "1Y"
        ]
    )


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    sector: str
    industry_character: str
    business_character: List[str]
    demand_drivers: List[str]
    revenue_drivers: List[str]
    cost_drivers: List[str]
    supply_chain_character: List[str]
    strategic_drivers: List[str]
    key_indicators: List[str]
    key_events: List[str]
    market_characters: Dict[str, MarketCharacter]


DRREDDY_MARKETS: Dict[str, MarketCharacter] = {

    "NIFTY 50": MarketCharacter(
        market="NIFTY 50",
        character=(
            "Primary systematic equity-market character for Dr. Reddy's. "
            "Broad Indian equity liquidity, large-cap flows, defensive-sector "
            "sentiment and pharmaceutical-sector valuation can influence the stock."
        ),
        exposure_character=(
            "Direct systematic equity exposure with additional healthcare/"
            "pharmaceutical and defensive-factor exposure."
        ),
        impact_path=[
            "NIFTY 50 movement",
            "Indian equity liquidity and risk appetite",
            "large-cap / healthcare sector flows",
            "Dr. Reddy's valuation",
            "DRREDDY relative performance",
        ],
        calculation_logic=[
            "Calculate DRREDDY returns against NIFTY 50 over matched windows.",
            "Estimate rolling beta and rolling correlation instead of using the supplied fixed linkage.",
            "Calculate excess return after controlling for NIFTY 50.",
            "Where available, control separately for pharma-sector returns.",
            "Test daily, weekly and monthly lead/lag behaviour.",
        ],
        relevant_indicators=[
            "DRREDDY return",
            "NIFTY 50 return",
            "rolling beta",
            "rolling correlation",
            "relative strength",
            "volume",
            "volatility",
        ],
        relevant_events=[
            "broad-market risk-on/risk-off events",
            "healthcare policy changes",
            "RBI / macro events",
            "pharma-sector events",
            "quarterly and annual results",
        ],
    ),

    "Crude Oil": MarketCharacter(
        market="Crude Oil",
        character=(
            "Indirect pharmaceutical-input, packaging, logistics and inflation "
            "character. Crude can influence petrochemical-derived materials, "
            "solvents/chemicals, freight and the global inflation environment."
        ),
        exposure_character=(
            "Indirect manufacturing-cost and macro exposure, with sensitivity "
            "varying by product, geography and procurement contract."
        ),
        impact_path=[
            "Crude oil price",
            "petrochemical / chemical / packaging / freight costs",
            "manufacturing and distribution cost",
            "gross margin / EBITDA",
            "DRREDDY earnings expectations",
        ],
        calculation_logic=[
            "Measure contemporaneous and lagged crude/DRREDDY relationships.",
            "Control for NIFTY 50, USD/INR and broad pharmaceutical-sector movement.",
            "Compare crude shocks with gross-margin and EBITDA-margin changes where data permits.",
            "Separate direct cost effects from inflation and currency effects.",
            "Use event studies for unusually large crude movements.",
        ],
        relevant_indicators=[
            "crude return",
            "freight proxy",
            "chemical/input-cost proxy",
            "gross margin",
            "EBITDA margin",
            "DRREDDY return",
        ],
        relevant_events=[
            "large crude shocks",
            "global energy disruptions",
            "freight-cost shocks",
            "inflation surprises",
        ],
    ),

    "Gold": MarketCharacter(
        market="Gold",
        character=(
            "Safe-haven, real-rate, currency and liquidity character. Gold is "
            "not a core Dr. Reddy's manufacturing input; it is primarily useful "
            "as a macro risk-regime and defensive-equity variable."
        ),
        exposure_character="Indirect macro, liquidity and portfolio-flow exposure.",
        impact_path=[
            "Gold price",
            "real-rate / global-risk / liquidity regime",
            "defensive-equity and healthcare-sector flows",
            "large-cap pharma valuation",
            "DRREDDY stock response",
        ],
        calculation_logic=[
            "Measure rolling and lagged gold/DRREDDY relationships.",
            "Control for NIFTY 50, USD/INR and volatility.",
            "Test the relationship separately in risk-off and normal regimes.",
            "Compare gold with rates and currency to identify common macro drivers.",
            "Do not interpret correlation alone as causation.",
        ],
        relevant_indicators=[
            "gold return",
            "USD/INR",
            "real-rate proxy",
            "volatility proxy",
            "DRREDDY relative strength",
        ],
        relevant_events=[
            "global risk-off events",
            "central-bank rate events",
            "geopolitical shocks",
            "currency stress events",
        ],
    ),

    "Silver": MarketCharacter(
        market="Silver",
        character=(
            "Indirect industrial-cycle and precious-metal sentiment character. "
            "Silver is not a principal drug input; it can provide information "
            "about global industrial activity, technology demand and commodity risk."
        ),
        exposure_character="Indirect industrial-cycle and macro exposure.",
        impact_path=[
            "Silver price",
            "industrial / commodity-cycle signal",
            "manufacturing and global-growth environment",
            "pharma-sector risk appetite",
            "DRREDDY market response",
        ],
        calculation_logic=[
            "Measure rolling and lagged silver/DRREDDY relationships.",
            "Compare silver with copper to isolate common industrial-cycle effects.",
            "Control for NIFTY 50 and broad commodity conditions.",
            "Test whether sensitivity changes across growth and risk-off regimes.",
        ],
        relevant_indicators=[
            "silver return",
            "copper return",
            "industrial-cycle proxy",
            "DRREDDY return",
            "relative strength",
        ],
        relevant_events=[
            "global industrial shocks",
            "commodity-volatility events",
            "global growth surprises",
        ],
    ),

    "Natural Gas": MarketCharacter(
        market="Natural Gas",
        character=(
            "Indirect pharmaceutical-manufacturing energy and chemical-cost "
            "character. Natural gas can affect process energy, electricity, "
            "industrial heating and the broader chemical input chain."
        ),
        exposure_character=(
            "Indirect manufacturing-cost exposure, with geography-specific "
            "sensitivity across Dr. Reddy's facilities."
        ),
        impact_path=[
            "Natural-gas price",
            "industrial energy / chemical economics",
            "plant utility and manufacturing cost",
            "gross margin / operating margin",
            "DRREDDY earnings expectations",
        ],
        calculation_logic=[
            "Measure lagged natural-gas/DRREDDY relationships.",
            "Control for crude oil, electricity and NIFTY 50 where possible.",
            "Compare energy shocks with margin and plant-operating indicators.",
            "Use geography-relevant energy series where available.",
            "Test whether sustained energy shocks have stronger effects than short spikes.",
        ],
        relevant_indicators=[
            "natural-gas return",
            "electricity-price proxy",
            "energy-cost proxy",
            "gross margin",
            "EBITDA margin",
            "DRREDDY return",
        ],
        relevant_events=[
            "energy supply disruptions",
            "natural-gas price shocks",
            "manufacturing-cost inflation",
            "geopolitical energy events",
        ],
    ),

    "Copper": MarketCharacter(
        market="Copper",
        character=(
            "Indirect electrical, engineering, manufacturing and plant-capex "
            "character. Copper can influence electrical systems, equipment, "
            "utilities and infrastructure costs across pharmaceutical facilities."
        ),
        exposure_character=(
            "Indirect manufacturing, maintenance and capital-expenditure exposure."
        ),
        impact_path=[
            "Copper price",
            "electrical / engineering / equipment input costs",
            "plant maintenance and capex economics",
            "manufacturing cost / project economics",
            "DRREDDY margin and cash-flow expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged copper/DRREDDY relationships.",
            "Compare copper movement with capex and margin indicators.",
            "Control for aluminium, zinc and broader industrial-metal movement.",
            "Separate input-cost effects from industrial-demand effects.",
            "Use procurement and project lags rather than only same-day correlation.",
        ],
        relevant_indicators=[
            "copper return",
            "industrial-metals basket",
            "capex",
            "gross margin",
            "EBITDA margin",
            "operating cash flow",
        ],
        relevant_events=[
            "copper supply disruptions",
            "major plant-capex announcements",
            "manufacturing expansion",
            "equipment procurement changes",
        ],
    ),

    "Aluminium": MarketCharacter(
        market="Aluminium",
        character=(
            "Indirect pharmaceutical packaging, engineering and manufacturing "
            "input character. Aluminium can matter through packaging materials, "
            "equipment, plant infrastructure and industrial-capex conditions."
        ),
        exposure_character=(
            "Indirect-to-moderate packaging, manufacturing and capex-cost exposure."
        ),
        impact_path=[
            "Aluminium price",
            "packaging / equipment / engineering costs",
            "manufacturing and plant economics",
            "cost of goods / capex",
            "DRREDDY margin and cash-flow expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged aluminium/DRREDDY relationships.",
            "Test sensitivity against gross margin and EBITDA margin.",
            "Control for copper, crude and broader industrial-metal conditions.",
            "Where packaging data exists, compare aluminium with packaging-cost indicators.",
            "Use procurement lags instead of relying only on same-day correlation.",
        ],
        relevant_indicators=[
            "aluminium return",
            "industrial-metals basket",
            "packaging-cost proxy",
            "gross margin",
            "EBITDA margin",
            "capex",
        ],
        relevant_events=[
            "aluminium supply shocks",
            "packaging-cost changes",
            "plant expansion",
            "manufacturing-capex events",
        ],
    ),

    "Zinc": MarketCharacter(
        market="Zinc",
        character=(
            "Indirect pharmaceutical-plant infrastructure and fabrication "
            "character. Zinc can affect galvanised steel and industrial equipment "
            "supply chains, but is not a principal pharmaceutical input."
        ),
        exposure_character="Indirect infrastructure and supplier-cost exposure.",
        impact_path=[
            "Zinc price",
            "galvanised steel / fabrication costs",
            "plant and infrastructure project economics",
            "capex / maintenance cost",
            "DRREDDY cash-flow and margin expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged zinc/DRREDDY relationships.",
            "Compare zinc with copper and aluminium as a common industrial factor.",
            "Control for NIFTY 50 and pharmaceutical-sector conditions.",
            "Use project/procurement lag analysis.",
            "Do not treat zinc correlation as direct causation without supply-chain evidence.",
        ],
        relevant_indicators=[
            "zinc return",
            "industrial-metals basket",
            "capex",
            "maintenance-cost proxy",
            "DRREDDY margin",
            "DRREDDY return",
        ],
        relevant_events=[
            "zinc supply shocks",
            "industrial construction-cost changes",
            "plant expansion",
            "major infrastructure projects",
        ],
    ),

    "Electricity": MarketCharacter(
        market="Electricity",
        character=(
            "Important direct pharmaceutical-manufacturing and quality-system "
            "operating character. Drug manufacturing, HVAC, clean rooms, water "
            "systems, laboratories, cold-chain requirements, testing and digital "
            "infrastructure require reliable power."
        ),
        exposure_character=(
            "Direct operational-energy cost and reliability exposure."
        ),
        impact_path=[
            "Electricity price / availability",
            "manufacturing, HVAC, clean-room and laboratory energy cost",
            "plant operating expense and production reliability",
            "gross margin / EBITDA / product availability",
            "DRREDDY earnings and cash-flow expectations",
        ],
        calculation_logic=[
            "Use electricity-price and tariff data relevant to major operating geographies.",
            "Measure lagged electricity-cost sensitivity against margins and operating indicators.",
            "Separate price impact from outage/reliability impact.",
            "Control for natural-gas and broader industrial-inflation effects.",
            "Test whether energy sensitivity differs by geography, plant and product type.",
        ],
        relevant_indicators=[
            "electricity price",
            "industrial tariff proxy",
            "power availability",
            "energy cost",
            "gross margin",
            "EBITDA margin",
            "plant utilisation",
            "capacity",
        ],
        relevant_events=[
            "electricity tariff changes",
            "power shortages / outages",
            "grid events",
            "energy-efficiency projects",
            "new manufacturing facilities",
            "major capacity expansions",
        ],
    ),
}


DRREDDY_CHARACTER = CompanyCharacter(
    symbol="DRREDDY",
    company_name="Dr. Reddy's Laboratories Limited",
    sector="Pharmaceuticals / Global Generics / API & Pharmaceutical Services",
    industry_character=(
        "Integrated global, science-led pharmaceutical company with Global "
        "Generics, Pharmaceutical Services and Active Ingredients (PSAI), and "
        "additional innovative/proprietary businesses. Its character is global, "
        "manufacturing-intensive, regulatory-sensitive, R&D-driven and exposed "
        "to product launches, generic price erosion, API/intermediate economics, "
        "currency movements, quality/compliance and geographically diversified demand."
    ),
    business_character=[
        "Global Generics",
        "Branded generics",
        "Unbranded generics",
        "Over-the-counter medicines",
        "Biosimilars",
        "Consumer healthcare",
        "Nicotine replacement therapy",
        "Active pharmaceutical ingredients (APIs)",
        "API intermediates",
        "Pharmaceutical Services",
        "Contract development and manufacturing (CDMO)",
        "Complex and differentiated formulations",
        "Proprietary products",
        "Innovative medicines",
        "Oncology discovery and development",
        "Inflammation research",
        "Digital therapeutics / technology-enabled healthcare",
        "Licensing and collaborative product development",
    ],
    demand_drivers=[
        "Generic-medicine adoption",
        "Healthcare spending",
        "Chronic disease prevalence",
        "Ageing population",
        "Patient affordability",
        "New product launches",
        "Complex-generic demand",
        "Biosimilar adoption",
        "North American healthcare demand",
        "Indian pharmaceutical-market growth",
        "Europe demand",
        "Emerging-market healthcare access",
        "Consumer-health demand",
        "API outsourcing demand",
        "CDMO demand",
    ],
    revenue_drivers=[
        "Global Generics sales",
        "North America sales",
        "India sales",
        "Europe sales",
        "Russia / CIS and emerging-market sales",
        "API sales",
        "PSAI services",
        "CDMO revenue",
        "Consumer-health products",
        "Biosimilars",
        "New product launches",
        "Volume growth",
        "Product mix",
        "Price changes / generic price erosion",
        "Licensing milestones",
        "Royalty income",
    ],
    cost_drivers=[
        "APIs and key starting materials",
        "Chemical intermediates",
        "Excipients",
        "Packaging materials",
        "Solvents and process chemicals",
        "Electricity",
        "Natural gas / process energy",
        "Freight and logistics",
        "Employee costs",
        "R&D costs",
        "Regulatory compliance",
        "Quality testing and validation",
        "Plant maintenance",
        "Capacity expansion",
        "Currency movement",
        "Remediation / compliance investments",
    ],
    supply_chain_character=[
        "API and key-starting-material suppliers",
        "Chemical and intermediate suppliers",
        "Excipient suppliers",
        "Packaging suppliers",
        "Global logistics providers",
        "Contract manufacturing ecosystem",
        "CDMO partners and customers",
        "Regulated-market distribution networks",
        "Multi-country manufacturing network",
        "Technology and licensing partners",
        "Specialty raw-material suppliers",
        "Cold-chain / temperature-controlled logistics where required",
    ],
    strategic_drivers=[
        "Global Generics scale",
        "Complex and differentiated products",
        "North America pipeline",
        "India branded-generics growth",
        "API differentiation",
        "CDMO expansion",
        "Consumer-health expansion",
        "Biosimilars and innovative medicines",
        "R&D productivity",
        "Regulatory compliance",
        "Manufacturing capacity expansion",
        "Supply-chain resilience",
        "Strategic partnerships and licensing",
        "Geographic diversification",
        "Digital therapeutics and technology-enabled healthcare",
    ],
    key_indicators=[
        "revenue growth",
        "Global Generics revenue",
        "North America revenue",
        "India revenue",
        "Europe revenue",
        "Russia/CIS revenue",
        "Emerging Markets revenue",
        "PSAI revenue",
        "API volume",
        "CDMO revenue",
        "new product launches",
        "product pipeline",
        "market share",
        "volume growth",
        "price / mix",
        "gross margin",
        "EBITDA margin",
        "PAT",
        "R&D expenditure",
        "R&D intensity",
        "capex",
        "working capital",
        "inventory",
        "receivables",
        "operating cash flow",
        "USFDA status",
        "regulatory observations",
        "ANDA / filing pipeline",
        "USD/INR",
        "EUR/INR",
        "RUB/INR",
        "DRREDDY stock return",
        "DRREDDY volume",
        "relative strength versus NIFTY 50",
    ],
    key_events=[
        "USFDA inspections and observations",
        "regulatory approvals",
        "ANDA approvals",
        "new product launches",
        "complex-generic launches",
        "biosimilar approvals",
        "API capacity expansion",
        "CDMO contracts",
        "major licensing agreements",
        "strategic partnerships",
        "acquisitions",
        "divestments",
        "plant shutdowns or interruptions",
        "manufacturing quality events",
        "product recalls",
        "R&D milestones",
        "clinical-trial milestones",
        "India pricing / regulatory changes",
        "US generic pricing changes",
        "international regulatory changes",
        "currency shocks",
        "geopolitical supply-chain disruptions",
        "quarterly and annual results",
        "management guidance",
        "major litigation / intellectual-property events",
    ],
    market_characters=DRREDDY_MARKETS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Dr. Reddy's company character."""
    return DRREDDY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return Dr. Reddy's character for one of the nine tracked markets."""
    try:
        return DRREDDY_MARKETS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine Dr. Reddy's market characters."""
    return dict(DRREDDY_MARKETS)


def validate_character() -> bool:
    """Validate the Dr. Reddy's character contract."""
    if DRREDDY_CHARACTER.symbol != "DRREDDY":
        return False

    if set(DRREDDY_MARKETS) != set(TRACKED_MARKETS):
        return False

    for market_name, character in DRREDDY_MARKETS.items():
        if character.market != market_name:
            return False
        if not character.character:
            return False
        if not character.exposure_character:
            return False
        if not character.impact_path:
            return False
        if not character.calculation_logic:
            return False

    forbidden_fields = {
        "RANK",
        "PCT_CHANGE",
        "LINKAGE_SCORE",
        "RELATION",
        "SCORE",
    }

    if forbidden_fields.intersection(DRREDDY_CHARACTER.__dataclass_fields__):
        return False

    return True


if __name__ == "__main__":
    print(f"{DRREDDY_CHARACTER.company_name} ({DRREDDY_CHARACTER.symbol})")
    print(f"Tracked markets: {len(DRREDDY_MARKETS)}")
    print(f"Character validation: {validate_character()}")

    for market_name in TRACKED_MARKETS:
        character = DRREDDY_MARKETS[market_name]
        print(f"- {market_name}: {character.character}")
