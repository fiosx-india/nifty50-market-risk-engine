"""
BEL (Bharat Electronics Limited) — Company Character & 9-Market Relationship Engine

Purpose:
- Store BEL's business character and the character of its relationship with the
  9 tracked markets.
- Describe WHAT should be calculated later; do not store hard-coded ranks,
  percentage changes, linkage scores, or relationship labels.
- Historical calculation belongs to the shared research/calculation layer.

Architecture:
Company Character
    -> Sector / Industry Character
    -> Market Character
    -> Supply-chain / dependency path
    -> Historical data calculation
    -> Indicators / timeframes / events
    -> Shared Market Context / Decision layer
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
        default_factory=lambda: ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"]
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


BEL_MARKETS: Dict[str, MarketCharacter] = {
    "NIFTY 50": MarketCharacter(
        market="NIFTY 50",
        character="Primary systematic equity-market character for BEL.",
        exposure_character="Direct market-valuation, risk-appetite and domestic-equity factor exposure.",
        impact_path=[
            "NIFTY 50 movement",
            "Indian equity risk appetite",
            "defence/PSU/industrial sector sentiment",
            "BEL valuation and relative performance",
        ],
        calculation_logic=[
            "Calculate BEL return versus NIFTY 50 return over matched windows.",
            "Use rolling correlation and rolling beta rather than a fixed linkage score.",
            "Measure excess return: BEL return minus estimated NIFTY contribution.",
            "Separate broad-market effect from defence/industrial-sector effect where data permits.",
            "Test lead/lag relationships across multiple horizons.",
        ],
        relevant_indicators=[
            "BEL return",
            "NIFTY 50 return",
            "rolling correlation",
            "rolling beta",
            "relative strength",
            "volatility",
            "volume",
        ],
        relevant_events=[
            "NIFTY-wide risk-off/risk-on events",
            "major budget/policy announcements",
            "defence-sector policy changes",
            "large BEL order announcements",
            "earnings and guidance",
        ],
    ),
    "Crude Oil": MarketCharacter(
        market="Crude Oil",
        character="Indirect energy, logistics, inflation and macro-cost character.",
        exposure_character="Mostly indirect; crude can affect logistics, imported inflation, government finances and industrial input costs.",
        impact_path=[
            "Crude oil price",
            "fuel/logistics cost and inflation",
            "industrial/government spending environment",
            "BEL project economics and market sentiment",
        ],
        calculation_logic=[
            "Measure BEL sensitivity to crude returns with lagged windows.",
            "Test crude impact on BEL after controlling for NIFTY 50.",
            "Separate direct company-cost effects from macro/inflation effects.",
            "Use event studies around large crude shocks.",
        ],
        relevant_indicators=["crude return", "fuel/inflation proxies", "BEL return", "NIFTY return"],
        relevant_events=["large crude shocks", "inflation surprises", "fiscal-policy changes"],
    ),
    "Gold": MarketCharacter(
        market="Gold",
        character="Indirect macro, safe-haven and liquidity-sentiment character.",
        exposure_character="Indirect exposure through global risk sentiment, real rates, liquidity and portfolio rotation.",
        impact_path=[
            "Gold price",
            "global risk/real-rate/liquidity signal",
            "Indian equity and PSU/defence sentiment",
            "BEL valuation/flow behaviour",
        ],
        calculation_logic=[
            "Measure rolling and lagged BEL-gold return relationships.",
            "Control for NIFTY 50 to isolate non-market gold effects.",
            "Compare behaviour during risk-off and high-volatility regimes.",
            "Use regime-conditioned statistics rather than a permanent relationship label.",
        ],
        relevant_indicators=["gold return", "real-rate proxy", "VIX/risk proxy", "BEL relative strength"],
        relevant_events=["geopolitical shocks", "central-bank/rate events", "global risk-off episodes"],
    ),
    "Silver": MarketCharacter(
        market="Silver",
        character="Indirect industrial-cycle and precious-metal sentiment character.",
        exposure_character="Indirect exposure through industrial activity, electronics sentiment and broader commodity risk appetite.",
        impact_path=[
            "Silver price",
            "industrial/precious-metal sentiment",
            "electronics and capital-spending expectations",
            "BEL market response",
        ],
        calculation_logic=[
            "Measure rolling and lagged silver/BEL relationships.",
            "Compare silver sensitivity with copper sensitivity to distinguish industrial-cycle effects.",
            "Control for NIFTY 50 and broad commodity conditions.",
            "Check whether effects differ during industrial expansion and risk-off regimes.",
        ],
        relevant_indicators=["silver return", "copper return", "BEL return", "industrial-cycle proxy"],
        relevant_events=["global industrial shocks", "commodity volatility events"],
    ),
    "Natural Gas": MarketCharacter(
        market="Natural Gas",
        character="Indirect industrial-energy and manufacturing-cost character.",
        exposure_character="Mostly indirect through energy costs, industrial activity and government/defence supply-chain economics.",
        impact_path=[
            "Natural-gas price",
            "industrial energy economics",
            "supplier/manufacturing cost environment",
            "BEL margins/order execution expectations",
        ],
        calculation_logic=[
            "Measure lagged natural-gas/BEL relationships over multiple windows.",
            "Test energy-price sensitivity after controlling for NIFTY 50.",
            "Use company/sector cost indicators where available.",
            "Do not infer causation from correlation alone.",
        ],
        relevant_indicators=["natural-gas return", "industrial-energy proxy", "BEL margins", "BEL return"],
        relevant_events=["energy shocks", "industrial-cost shocks", "major geopolitical supply disruptions"],
    ),
    "Copper": MarketCharacter(
        market="Copper",
        character="Industrial electronics, electrical and manufacturing-cycle character.",
        exposure_character="Indirect-to-moderate input-chain exposure through electrical/electronic components, industrial equipment and supplier costs.",
        impact_path=[
            "Copper price",
            "electrical/electronics input-cost and industrial-cycle signal",
            "BEL procurement/supplier economics",
            "project margins/order execution expectations",
        ],
        calculation_logic=[
            "Measure BEL sensitivity to copper returns using rolling and lagged windows.",
            "Compare copper moves with BEL gross/operating margin proxies when available.",
            "Control for NIFTY 50 and broader industrial-metal conditions.",
            "Distinguish commodity-price effect from demand-cycle effect.",
        ],
        relevant_indicators=[
            "copper return",
            "industrial-metals basket",
            "BEL margin",
            "BEL order execution",
            "BEL return",
        ],
        relevant_events=[
            "major copper supply disruptions",
            "large commodity shocks",
            "electronics/input-cost disclosures",
            "major BEL order wins",
        ],
    ),
    "Aluminium": MarketCharacter(
        market="Aluminium",
        character="Industrial lightweight-metal and electronics/manufacturing input character.",
        exposure_character="Indirect-to-moderate exposure through aluminium-containing components, enclosures, structures, manufacturing and supplier costs.",
        impact_path=[
            "Aluminium price",
            "component/enclosure/industrial input costs",
            "supplier economics and project cost",
            "BEL margin/order-execution expectations",
        ],
        calculation_logic=[
            "Measure lagged aluminium/BEL relationships across multiple windows.",
            "Test aluminium sensitivity after controlling for NIFTY 50 and other industrial metals.",
            "Where company disclosures permit, compare commodity moves with procurement and margin indicators.",
            "Separate input-cost effect from industrial-demand effect.",
        ],
        relevant_indicators=[
            "aluminium return",
            "industrial-metals basket",
            "BEL operating margin",
            "BEL return",
        ],
        relevant_events=[
            "aluminium supply shocks",
            "input-cost disclosures",
            "large procurement changes",
            "major defence orders",
        ],
    ),
    "Zinc": MarketCharacter(
        market="Zinc",
        character="Indirect industrial-metal and fabrication/supply-chain character.",
        exposure_character="Indirect exposure through metal components, fabrication, galvanised infrastructure and industrial supplier costs.",
        impact_path=[
            "Zinc price",
            "industrial/fabrication input-cost signal",
            "supplier/project economics",
            "BEL execution and margin expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged zinc/BEL relationships.",
            "Compare zinc with copper and aluminium to identify common industrial-metal factors.",
            "Control for NIFTY 50 and industrial-cycle variables.",
            "Use event studies for abnormal commodity moves.",
        ],
        relevant_indicators=["zinc return", "industrial-metals basket", "BEL margin", "BEL return"],
        relevant_events=["zinc supply shocks", "industrial-cycle shocks", "major project/order announcements"],
    ),
    "Electricity": MarketCharacter(
        market="Electricity",
        character="Direct-to-indirect manufacturing, testing, R&D and facility energy-cost character.",
        exposure_character="Operational exposure through electricity consumption at manufacturing, testing, R&D and facility locations.",
        impact_path=[
            "Electricity price/availability",
            "manufacturing and testing operating cost",
            "production/project execution",
            "BEL margins and delivery expectations",
        ],
        calculation_logic=[
            "Use relevant electricity-price or power-market data for the operating geography.",
            "Measure lagged relationship with BEL margins and operating metrics where available.",
            "Separate electricity-price effect from broader industrial inflation.",
            "Include availability/reliability disruptions, not only price.",
            "Do not use a generic power-price series when a more relevant Indian market series is available.",
        ],
        relevant_indicators=[
            "electricity price",
            "power availability",
            "industrial tariff proxy",
            "BEL operating margin",
            "capacity/utilisation proxy",
        ],
        relevant_events=[
            "power shortages",
            "tariff changes",
            "major grid events",
            "manufacturing-expansion announcements",
        ],
    ),
}


BEL_CHARACTER = CompanyCharacter(
    symbol="BEL",
    company_name="Bharat Electronics Limited",
    sector="Defence Electronics / Strategic Electronics / Diversified Electronics",
    industry_character=(
        "Strategic-electronics manufacturer and systems integrator serving defence "
        "and selected non-defence markets. The business is project/order-book driven, "
        "technology and R&D intensive, procurement-sensitive and strongly influenced "
        "by government/defence programmes, indigenous-content policy, execution and "
        "long-cycle customer requirements."
    ),
    business_character=[
        "Defence communication systems",
        "Land-based radars",
        "Naval systems",
        "Electronic warfare systems",
        "Avionics",
        "Electro-optics",
        "Tank and armoured-vehicle electronics",
        "Weapon systems and upgrades",
        "C4I and network-centric systems",
        "Navigation systems",
        "Unmanned systems and counter-drone related solutions",
        "Seekers, fuzes, batteries, components and related electronics",
        "Rail and metro solutions",
        "Civil aviation solutions",
        "Homeland security and smart-city solutions",
        "Space electronics and satellite-related systems",
        "Telecom, communication and broadcast systems",
        "E-governance / EVM-related products",
        "Cyber/software and other non-defence electronics",
    ],
    demand_drivers=[
        "Indian defence capital expenditure",
        "Defence modernisation programmes",
        "Domestic indigenisation and import substitution",
        "DRDO and armed-forces programmes",
        "Large radar, communication, electronic-warfare, avionics and naval programmes",
        "Order inflow and conversion of order pipeline into execution",
        "Export opportunities",
        "Non-defence diversification",
        "Technology upgrades and replacement cycles",
        "Geopolitical and strategic-security requirements",
    ],
    revenue_drivers=[
        "Order intake",
        "Order-book execution",
        "Large system and turnkey projects",
        "Product deliveries",
        "Upgrades, spares and services",
        "Export orders",
        "Non-defence systems",
        "New indigenous products",
        "Technology partnerships and collaborative programmes",
    ],
    cost_drivers=[
        "Electronic components and devices",
        "Metals and fabricated components",
        "Imported inputs and foreign-exchange movement",
        "Contract/subcontract manufacturing",
        "Employee and engineering cost",
        "R&D expenditure",
        "Testing and certification",
        "Manufacturing and facility energy cost",
        "Logistics and project execution cost",
        "Warranty/service obligations",
    ],
    supply_chain_character=[
        "Multi-tier electronics and component suppliers",
        "Indian MSME and start-up ecosystem",
        "Strategic technology partners",
        "DRDO / national design-agency collaboration",
        "Domestic and foreign technology partners",
        "Manufacturing, system integration and testing",
        "Long-cycle defence procurement and acceptance process",
        "Project-specific components and subsystems",
        "Import substitution and indigenous-content expansion",
    ],
    strategic_drivers=[
        "Indigenisation and self-reliance",
        "R&D-led product development",
        "Technology absorption and joint development",
        "Defence-sector localisation",
        "Export expansion",
        "Non-defence diversification",
        "Manufacturing modernisation",
        "Digital/software capability",
        "Supply-chain strengthening",
        "Long-term strategic customer relationships",
    ],
    key_indicators=[
        "order intake",
        "order book",
        "book-to-bill ratio",
        "revenue growth",
        "execution rate",
        "EBITDA/operating margin",
        "profit margin",
        "working capital",
        "receivables",
        "inventory",
        "cash flow",
        "export revenue",
        "defence versus non-defence mix",
        "R&D expenditure",
        "R&D intensity",
        "indigenous-content ratio",
        "capacity/utilisation indicators",
        "BEL stock return",
        "BEL volume",
        "relative strength versus NIFTY 50",
    ],
    key_events=[
        "large defence order wins",
        "order cancellations or delays",
        "major radar/missile/communication/naval/avionics contracts",
        "DRDO collaboration or technology-transfer events",
        "defence-budget announcements",
        "Make in India / indigenisation policy changes",
        "export orders",
        "major joint ventures or strategic partnerships",
        "new product launches",
        "R&D breakthroughs or technology approvals",
        "capacity expansion",
        "quarterly and annual results",
        "management guidance",
        "working-capital changes",
        "major customer acceptance/delivery milestones",
        "regulatory or government procurement changes",
        "geopolitical developments affecting defence procurement",
    ],
    market_characters=BEL_MARKETS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete BEL company character."""
    return BEL_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return BEL's character for one of the nine tracked markets."""
    try:
        return BEL_MARKETS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine BEL market characters."""
    return dict(BEL_MARKETS)


def validate_character() -> bool:
    """Validate the BEL character definition and the nine-market contract."""
    if BEL_CHARACTER.symbol != "BEL":
        return False

    if set(BEL_MARKETS) != set(TRACKED_MARKETS):
        return False

    for market_name, character in BEL_MARKETS.items():
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

    # The character layer must not contain computed market results.
    forbidden_fields = {
        "RANK",
        "PCT_CHANGE",
        "LINKAGE_SCORE",
        "RELATION",
        "SCORE",
    }
    actual_fields = set(BEL_CHARACTER.__dataclass_fields__)
    if forbidden_fields.intersection(actual_fields):
        return False

    return True


if __name__ == "__main__":
    print(f"{BEL_CHARACTER.company_name} ({BEL_CHARACTER.symbol})")
    print(f"Tracked markets: {len(BEL_MARKETS)}")
    print(f"Character validation: {validate_character()}")
    for market_name in TRACKED_MARKETS:
        mc = BEL_MARKETS[market_name]
        print(f"- {market_name}: {mc.character}")
