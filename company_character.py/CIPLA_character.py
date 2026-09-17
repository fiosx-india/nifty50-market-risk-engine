"""
CIPLA (Cipla Limited) — Company Character & 9-Market Relationship Engine

This is the CHARACTER layer.

It describes:
    Company character
        -> pharmaceutical industry character
        -> business / therapy mix
        -> supply-chain and manufacturing character
        -> 9 tracked market characters
        -> what the historical engine should calculate

It intentionally does NOT hard-code:
    RANK
    PCT_CHANGE
    LINKAGE_SCORE
    RELATION

Those are calculated outputs and belong to the later historical-analysis layer.
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


CIPLA_MARKETS: Dict[str, MarketCharacter] = {

    "NIFTY 50": MarketCharacter(
        market="NIFTY 50",
        character=(
            "Primary systematic equity-market character for Cipla. "
            "Broad Indian equity liquidity, risk appetite, large-cap flows "
            "and pharmaceutical-sector valuation can influence the stock."
        ),
        exposure_character=(
            "Direct systematic equity exposure with additional healthcare/"
            "pharmaceutical-sector and defensive-factor exposure."
        ),
        impact_path=[
            "NIFTY 50 movement",
            "Indian equity liquidity and risk appetite",
            "large-cap / healthcare sector flows",
            "Cipla valuation and relative performance",
        ],
        calculation_logic=[
            "Calculate Cipla returns against NIFTY 50 over matched windows.",
            "Estimate rolling correlation and rolling beta instead of a fixed linkage score.",
            "Calculate excess return after controlling for NIFTY 50.",
            "Where available, separately control for pharmaceutical-sector returns.",
            "Test lead/lag effects across daily, weekly and monthly horizons.",
        ],
        relevant_indicators=[
            "Cipla return",
            "NIFTY 50 return",
            "rolling beta",
            "rolling correlation",
            "relative strength",
            "volume",
            "volatility",
        ],
        relevant_events=[
            "broad market risk-on/risk-off events",
            "Union Budget / healthcare policy",
            "RBI and macro events",
            "pharma-sector regulatory events",
            "Cipla results and guidance",
        ],
    ),

    "Crude Oil": MarketCharacter(
        market="Crude Oil",
        character=(
            "Indirect pharmaceutical-input, packaging, logistics and inflation "
            "character. Crude can affect petrochemical-derived materials, "
            "transportation, solvent/chemical economics and macro inflation."
        ),
        exposure_character=(
            "Indirect cost and macro-demand exposure; effects can differ by "
            "API, formulation, packaging and geography."
        ),
        impact_path=[
            "Crude oil price",
            "petrochemical / chemical / packaging / logistics costs",
            "manufacturing and distribution cost",
            "gross margin / operating margin",
            "Cipla earnings expectations and valuation",
        ],
        calculation_logic=[
            "Measure contemporaneous and lagged crude/Cipla relationships.",
            "Test crude sensitivity after controlling for NIFTY 50.",
            "Where cost disclosures exist, compare crude moves with input-cost and margin trends.",
            "Separate direct input/logistics effects from inflation and currency effects.",
            "Use event studies around unusually large crude shocks.",
        ],
        relevant_indicators=[
            "crude return",
            "inflation proxy",
            "chemical/input-cost proxy",
            "gross margin",
            "EBITDA margin",
            "Cipla return",
        ],
        relevant_events=[
            "large crude shocks",
            "global energy disruptions",
            "inflation surprises",
            "major geopolitical supply disruptions",
        ],
    ),

    "Gold": MarketCharacter(
        market="Gold",
        character=(
            "Macro safe-haven, real-rate and currency-sentiment character. "
            "Gold is not a core Cipla production input; its importance is mainly "
            "through global risk, liquidity, currency and defensive-equity flows."
        ),
        exposure_character=(
            "Indirect macro, liquidity and portfolio-flow exposure."
        ),
        impact_path=[
            "Gold price",
            "real-rate / risk / liquidity signal",
            "defensive-sector and equity-flow behaviour",
            "pharmaceutical valuation sentiment",
            "Cipla stock response",
        ],
        calculation_logic=[
            "Calculate rolling and lagged gold/Cipla relationships.",
            "Control for NIFTY 50 and volatility.",
            "Test the relationship during risk-off and high-volatility regimes.",
            "Compare gold with USD/INR and rate variables where data permits.",
            "Do not interpret correlation alone as causation.",
        ],
        relevant_indicators=[
            "gold return",
            "USD/INR",
            "real-rate proxy",
            "volatility proxy",
            "Cipla relative strength",
        ],
        relevant_events=[
            "global risk-off episodes",
            "central-bank/rate events",
            "currency shocks",
            "geopolitical events",
        ],
    ),

    "Silver": MarketCharacter(
        market="Silver",
        character=(
            "Indirect industrial, electronics and precious-metal sentiment "
            "character. Cipla's relationship is primarily through industrial "
            "activity, input economics and macro risk rather than silver being "
            "a core pharmaceutical input."
        ),
        exposure_character=(
            "Indirect industrial-cycle and macro exposure."
        ),
        impact_path=[
            "Silver price",
            "industrial-cycle / commodity sentiment",
            "manufacturing and investment environment",
            "pharmaceutical sector risk appetite",
            "Cipla valuation / stock response",
        ],
        calculation_logic=[
            "Measure rolling and lagged silver/Cipla relationships.",
            "Compare silver with copper to identify common industrial-cycle factors.",
            "Control for NIFTY 50 and broad commodity conditions.",
            "Test whether the relationship changes across growth and risk-off regimes.",
        ],
        relevant_indicators=[
            "silver return",
            "copper return",
            "industrial-cycle proxy",
            "Cipla return",
            "Cipla relative strength",
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
            "character. Natural gas can influence industrial energy economics, "
            "electricity, heating/process costs and the broader chemical chain."
        ),
        exposure_character=(
            "Indirect manufacturing-cost and macro exposure, with different "
            "sensitivity across plants and geographies."
        ),
        impact_path=[
            "Natural-gas price",
            "industrial energy / chemical economics",
            "manufacturing and utility cost",
            "margin / production economics",
            "Cipla earnings and valuation",
        ],
        calculation_logic=[
            "Measure lagged natural-gas/Cipla relationships.",
            "Control for crude oil, electricity and NIFTY 50 where possible.",
            "Compare energy shocks with margin and manufacturing indicators.",
            "Use geography-specific energy data when available instead of one generic series.",
            "Test whether effects are stronger during sustained energy shocks.",
        ],
        relevant_indicators=[
            "natural-gas return",
            "electricity-price proxy",
            "energy-cost proxy",
            "EBITDA margin",
            "gross margin",
            "Cipla return",
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
            "Indirect industrial-electronics and manufacturing-input character. "
            "Copper can matter through electrical systems, plant equipment, "
            "engineering infrastructure, utilities and industrial capex."
        ),
        exposure_character=(
            "Indirect manufacturing, maintenance and capex-cost exposure."
        ),
        impact_path=[
            "Copper price",
            "electrical / engineering / equipment input costs",
            "plant maintenance and capex economics",
            "manufacturing cost and project economics",
            "Cipla margin / cash-flow expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged copper/Cipla relationships.",
            "Compare copper moves with capex and margin indicators where available.",
            "Control for NIFTY 50 and industrial-metal basket movement.",
            "Separate input-cost effects from industrial-demand effects.",
            "Use lag windows appropriate to procurement and project cycles.",
        ],
        relevant_indicators=[
            "copper return",
            "industrial-metals basket",
            "capex",
            "EBITDA margin",
            "cash flow",
            "Cipla return",
        ],
        relevant_events=[
            "copper supply disruptions",
            "plant-capex announcements",
            "manufacturing expansion",
            "major equipment procurement",
        ],
    ),

    "Aluminium": MarketCharacter(
        market="Aluminium",
        character=(
            "Indirect pharmaceutical packaging, engineering and manufacturing "
            "input character. Aluminium can be relevant to blister/packaging "
            "materials, equipment, utilities and plant infrastructure."
        ),
        exposure_character=(
            "Indirect-to-moderate input-cost and manufacturing-capex exposure."
        ),
        impact_path=[
            "Aluminium price",
            "packaging / engineering / equipment cost",
            "manufacturing and plant economics",
            "cost of goods / capex",
            "Cipla margin and cash-flow expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged aluminium/Cipla relationships.",
            "Test aluminium sensitivity against gross margin and operating margin.",
            "Control for copper, crude and broader industrial-metal conditions.",
            "Where packaging disclosures exist, compare price movements with packaging-cost indicators.",
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
            "Indirect pharmaceutical-plant, fabrication and infrastructure "
            "material character. Zinc can affect galvanised steel and industrial "
            "equipment/facility supply chains, but is not a core Cipla drug input."
        ),
        exposure_character=(
            "Indirect infrastructure and supplier-cost exposure."
        ),
        impact_path=[
            "Zinc price",
            "galvanised steel / fabrication costs",
            "plant and infrastructure project economics",
            "capex / maintenance cost",
            "Cipla cash-flow and margin expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged zinc/Cipla relationships.",
            "Compare zinc with aluminium and copper to isolate common industrial factors.",
            "Control for NIFTY 50 and pharmaceutical-sector conditions.",
            "Use project/procurement lag analysis.",
            "Do not treat zinc correlation as direct causation without supply-chain evidence.",
        ],
        relevant_indicators=[
            "zinc return",
            "industrial-metals basket",
            "capex",
            "maintenance-cost proxy",
            "Cipla margin",
            "Cipla return",
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
            "Important direct manufacturing and cold-chain/quality-control "
            "operating-cost character. Pharmaceutical plants, laboratories, "
            "HVAC, clean rooms, water systems, refrigeration, testing and "
            "continuous manufacturing processes require reliable power."
        ),
        exposure_character=(
            "Direct operational-energy cost and reliability exposure."
        ),
        impact_path=[
            "Electricity price / availability",
            "manufacturing, HVAC, clean-room and laboratory energy cost",
            "plant operating expense and production reliability",
            "gross/EBITDA margin and product availability",
            "Cipla earnings / cash-flow expectations",
        ],
        calculation_logic=[
            "Use electricity-price/tariff data relevant to Cipla's operating geographies.",
            "Measure lagged electricity-cost sensitivity against margin and production indicators.",
            "Separate price impact from power-reliability/outage impact.",
            "Control for broader industrial inflation and natural-gas effects.",
            "Test whether energy sensitivity differs by manufacturing geography and product type.",
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
            "power shortages/outages",
            "grid events",
            "energy-efficiency projects",
            "new manufacturing facilities",
            "major capacity expansions",
        ],
    ),
}


CIPLA_CHARACTER = CompanyCharacter(
    symbol="CIPLA",
    company_name="Cipla Limited",
    sector="Pharmaceuticals",
    industry_character=(
        "Diversified pharmaceutical company with a strong India franchise, "
        "North America presence, Africa and Emerging Markets/Europe operations, "
        "API manufacturing, R&D and differentiated/complex product capabilities. "
        "Its business character is therapy-driven, regulatory-driven, "
        "manufacturing-intensive, quality-sensitive and exposed to global supply "
        "chains, currency movements, product launches, pricing and healthcare demand."
    ),
    business_character=[
        "Branded prescription medicines",
        "Generic medicines",
        "Trade generics",
        "Consumer health / wellness",
        "Respiratory therapies",
        "Anti-infectives",
        "Cardiac therapies",
        "Anti-diabetes therapies",
        "Urology",
        "Dermatology",
        "Central nervous system therapies",
        "Oncology",
        "Complex generics",
        "Respiratory inhalation products",
        "APIs",
        "Specialty and differentiated products",
        "North America regulated-market business",
        "Africa business",
        "Emerging Markets and Europe",
        "Global key accounts",
        "Licensing and strategic partnerships",
    ],
    demand_drivers=[
        "Chronic-disease prevalence",
        "Respiratory disease burden",
        "Healthcare spending",
        "Population growth and ageing",
        "Generic medicine adoption",
        "India prescription-market growth",
        "US generic and complex-generic demand",
        "Africa healthcare demand",
        "Emerging-market healthcare access",
        "New product launches",
        "Therapy expansion",
        "Patient affordability",
        "Regulatory approvals",
    ],
    revenue_drivers=[
        "One India branded prescription revenue",
        "India trade-generics revenue",
        "Consumer-health revenue",
        "North America product launches",
        "Respiratory portfolio",
        "Complex generic products",
        "Africa revenue",
        "Emerging Markets and Europe",
        "API sales",
        "Global key accounts",
        "New product launches",
        "Licensing and partnerships",
        "Product mix",
        "Volume growth",
        "Price / market-share changes",
    ],
    cost_drivers=[
        "API and key starting materials",
        "Chemical intermediates",
        "Excipients",
        "Packaging materials",
        "Solvents and process chemicals",
        "Electricity",
        "Natural gas / process energy",
        "Logistics and freight",
        "Employee and R&D costs",
        "Regulatory compliance",
        "Quality testing and validation",
        "Plant maintenance",
        "Currency movement",
        "US / international regulatory remediation",
        "Technology and manufacturing investments",
    ],
    supply_chain_character=[
        "API and key-starting-material suppliers",
        "Chemical and intermediate suppliers",
        "Excipient suppliers",
        "Packaging suppliers",
        "Contract manufacturers / partners",
        "Global logistics providers",
        "Cold-chain and temperature-controlled distribution where required",
        "Regulated-market manufacturing and quality systems",
        "Indian and international distribution networks",
        "US / global regulatory supply requirements",
        "Multi-country manufacturing footprint",
        "Strategic technology and licensing partners",
    ],
    strategic_drivers=[
        "Respiratory leadership",
        "Differentiated and complex-generic pipeline",
        "North America portfolio expansion",
        "One India chronic-therapy growth",
        "Africa market expansion",
        "Emerging Markets and Europe growth",
        "API manufacturing scale and differentiation",
        "R&D and new product pipeline",
        "Regulatory compliance and manufacturing quality",
        "Strategic licensing and partnerships",
        "Manufacturing resilience",
        "Supply-chain diversification",
        "Digital and technology-enabled healthcare",
        "Portfolio mix improvement",
    ],
    key_indicators=[
        "revenue growth",
        "One India revenue",
        "North America revenue",
        "Africa revenue",
        "Emerging Markets and Europe revenue",
        "API revenue",
        "respiratory growth",
        "chronic-therapy growth",
        "product launches",
        "market share",
        "volume growth",
        "price/mix",
        "gross margin",
        "EBITDA margin",
        "PAT",
        "R&D expenditure",
        "R&D intensity",
        "capex",
        "working capital",
        "inventory",
        "receivables",
        "cash flow",
        "regulatory status",
        "USFDA observations",
        "ANDA/NDA pipeline",
        "Cipla stock return",
        "Cipla volume",
        "relative strength versus NIFTY 50",
    ],
    key_events=[
        "USFDA inspections and observations",
        "regulatory approvals",
        "ANDA/NDA approvals",
        "major product launches",
        "complex-generic launches",
        "respiratory product developments",
        "major API supply events",
        "key starting-material supply disruptions",
        "plant shutdowns or manufacturing interruptions",
        "new manufacturing facilities",
        "capacity expansion",
        "R&D milestones",
        "licensing agreements",
        "strategic partnerships",
        "acquisitions",
        "divestments",
        "India pricing/regulatory changes",
        "US pricing and generic-market changes",
        "Africa regulatory events",
        "currency shocks",
        "geopolitical supply-chain disruptions",
        "quarterly and annual results",
        "management guidance",
        "major litigation / intellectual-property events",
        "quality or product-recall events",
    ],
    market_characters=CIPLA_MARKETS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Cipla company character."""
    return CIPLA_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return Cipla's character for one of the nine tracked markets."""
    try:
        return CIPLA_MARKETS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine Cipla market characters."""
    return dict(CIPLA_MARKETS)


def validate_character() -> bool:
    """
    Validate the Cipla character contract.

    Historical result fields are deliberately excluded from this layer.
    """
    if CIPLA_CHARACTER.symbol != "CIPLA":
        return False

    if set(CIPLA_MARKETS) != set(TRACKED_MARKETS):
        return False

    for market_name, character in CIPLA_MARKETS.items():
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

    if forbidden_fields.intersection(CIPLA_CHARACTER.__dataclass_fields__):
        return False

    return True


if __name__ == "__main__":
    print(f"{CIPLA_CHARACTER.company_name} ({CIPLA_CHARACTER.symbol})")
    print(f"Tracked markets: {len(CIPLA_MARKETS)}")
    print(f"Character validation: {validate_character()}")

    for market_name in TRACKED_MARKETS:
        character = CIPLA_MARKETS[market_name]
        print(f"- {market_name}: {character.character}")
