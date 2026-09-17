"""
BHARTIARTL (Bharti Airtel Limited) — Company Character & 9-Market Relationship Engine

Character layer only:
- Describes what Bharti Airtel is and how each tracked market can affect it.
- Does NOT hard-code RANK, PCT_CHANGE, LINKAGE_SCORE or RELATION.
- Actual relationships must be calculated later from historical market,
  operating, financial, event and news data.

Architecture:
Company Character
    -> Industry / Sector Character
    -> 9 Market Characters
    -> Direct / Indirect Exposure
    -> Supply-chain / operating path
    -> Historical calculation
    -> Indicators / timeframes / events
    -> Shared Market Context
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


BHARTIARTL_MARKETS: Dict[str, MarketCharacter] = {

    "NIFTY 50": MarketCharacter(
        market="NIFTY 50",
        character=(
            "Primary systematic equity-market character for Bharti Airtel. "
            "Broad market liquidity, risk appetite, valuation multiples and "
            "large-cap institutional flows can influence the stock."
        ),
        exposure_character=(
            "Direct systematic equity exposure, with additional telecom-sector "
            "and large-cap factor exposure."
        ),
        impact_path=[
            "NIFTY 50 movement",
            "Indian equity risk appetite and liquidity",
            "large-cap / telecom sector flows",
            "Airtel valuation and relative performance",
        ],
        calculation_logic=[
            "Calculate Airtel return versus NIFTY 50 return over matched windows.",
            "Estimate rolling beta and rolling correlation rather than using a fixed score.",
            "Calculate excess return after controlling for NIFTY 50.",
            "Where data permits, control separately for telecom-sector movement.",
            "Test lead/lag effects across intraday, daily, weekly and monthly horizons.",
        ],
        relevant_indicators=[
            "Airtel return",
            "NIFTY 50 return",
            "rolling beta",
            "rolling correlation",
            "relative strength",
            "volume",
            "volatility",
        ],
        relevant_events=[
            "major market-wide risk events",
            "Union Budget / policy events",
            "RBI rate decisions",
            "telecom policy announcements",
            "Airtel earnings and guidance",
        ],
    ),

    "Crude Oil": MarketCharacter(
        market="Crude Oil",
        character=(
            "Energy-cost, inflation and household-spending macro character. "
            "Crude is not a core telecom revenue driver, but can influence "
            "network operating costs, logistics, inflation, disposable income "
            "and macro risk appetite."
        ),
        exposure_character=(
            "Mostly indirect, with potential operating-cost and demand effects."
        ),
        impact_path=[
            "Crude oil price",
            "fuel / transport / logistics costs and inflation",
            "consumer purchasing power and business costs",
            "telecom demand and Airtel margin expectations",
            "Airtel market response",
        ],
        calculation_logic=[
            "Measure contemporaneous and lagged crude-return sensitivity.",
            "Control for NIFTY 50 to distinguish broad-market effects.",
            "Where available, compare crude moves with inflation and ARPU/recharge trends.",
            "Separate operating-cost effects from consumer-demand effects.",
            "Use regime analysis for major crude shocks instead of assuming a permanent relationship.",
        ],
        relevant_indicators=[
            "crude return",
            "inflation proxy",
            "fuel-price proxy",
            "Airtel revenue / ARPU",
            "Airtel margin",
            "Airtel return",
        ],
        relevant_events=[
            "large crude-price shocks",
            "fuel-price changes",
            "inflation surprises",
            "major geopolitical energy events",
        ],
    ),

    "Gold": MarketCharacter(
        market="Gold",
        character=(
            "Safe-haven, real-rate and liquidity-sentiment character. "
            "Gold can act as a macro risk indicator rather than a direct Airtel input."
        ),
        exposure_character=(
            "Indirect macro and portfolio-flow exposure."
        ),
        impact_path=[
            "Gold price",
            "global risk / real-rate / liquidity signal",
            "Indian market sentiment and capital flows",
            "large-cap telecom valuation",
            "Airtel stock response",
        ],
        calculation_logic=[
            "Measure rolling and lagged Airtel-gold relationships.",
            "Control for NIFTY 50 and volatility conditions.",
            "Test whether the relationship changes during risk-off periods.",
            "Compare gold with USD, rates and equity-volatility variables where available.",
            "Do not interpret correlation alone as causation.",
        ],
        relevant_indicators=[
            "gold return",
            "USD/INR",
            "real-rate proxy",
            "volatility proxy",
            "Airtel relative strength",
        ],
        relevant_events=[
            "global risk-off events",
            "central-bank rate events",
            "major geopolitical events",
            "large currency moves",
        ],
    ),

    "Silver": MarketCharacter(
        market="Silver",
        character=(
            "Industrial-cycle plus precious-metal sentiment character. "
            "For Airtel, the relationship is mainly through macro liquidity, "
            "technology/electronics demand and industrial-cycle conditions."
        ),
        exposure_character=(
            "Indirect industrial and macro exposure."
        ),
        impact_path=[
            "Silver price",
            "industrial / technology-cycle signal",
            "business investment and market sentiment",
            "telecom capex environment",
            "Airtel valuation / stock response",
        ],
        calculation_logic=[
            "Calculate rolling and lagged silver/Airtel relationships.",
            "Compare silver behaviour with copper to identify common industrial-cycle effects.",
            "Control for NIFTY 50 and broader commodity conditions.",
            "Test whether the relationship is stronger during technology or capex cycles.",
        ],
        relevant_indicators=[
            "silver return",
            "copper return",
            "Airtel capex",
            "Airtel return",
            "industrial-cycle proxy",
        ],
        relevant_events=[
            "global industrial shocks",
            "technology-cycle changes",
            "commodity volatility events",
        ],
    ),

    "Natural Gas": MarketCharacter(
        market="Natural Gas",
        character=(
            "Indirect energy and industrial-cost character. "
            "Natural gas can influence electricity generation, industrial costs, "
            "inflation and the wider macro environment in which telecom operates."
        ),
        exposure_character=(
            "Mostly indirect through energy economics and macro conditions."
        ),
        impact_path=[
            "Natural-gas price",
            "energy / electricity economics",
            "inflation and operating-cost environment",
            "consumer and enterprise spending",
            "Airtel demand / margin expectations",
        ],
        calculation_logic=[
            "Measure lagged natural-gas/Airtel relationships.",
            "Control for NIFTY 50 and crude oil where possible.",
            "Test energy-price shocks against ARPU, subscriber and margin variables.",
            "Separate common macro effects from telecom-specific effects.",
        ],
        relevant_indicators=[
            "natural-gas return",
            "electricity proxy",
            "inflation proxy",
            "subscriber growth",
            "ARPU",
            "margin",
        ],
        relevant_events=[
            "energy supply disruptions",
            "major natural-gas price shocks",
            "inflation shocks",
            "large industrial-energy events",
        ],
    ),

    "Copper": MarketCharacter(
        market="Copper",
        character=(
            "Strong industrial, electrical and telecom-network input character. "
            "Copper is relevant to network equipment, cables, power systems, "
            "electronics and infrastructure investment."
        ),
        exposure_character=(
            "Indirect-to-moderate input-cost and capex exposure through telecom "
            "network infrastructure and supplier ecosystem."
        ),
        impact_path=[
            "Copper price",
            "cable / electrical / network-equipment input economics",
            "telecom infrastructure procurement cost",
            "Airtel capex and deployment economics",
            "margin / cash-flow expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged copper/Airtel relationships.",
            "Compare copper moves with Airtel capex and margin trends where available.",
            "Control for NIFTY 50 and broader industrial-metal movement.",
            "Test whether copper shocks affect Airtel with a deployment/procurement lag.",
            "Separate price-driven cost effects from demand-driven industrial effects.",
        ],
        relevant_indicators=[
            "copper return",
            "industrial-metals basket",
            "Airtel capex",
            "network rollout",
            "EBITDA margin",
            "free cash flow",
        ],
        relevant_events=[
            "large copper supply shocks",
            "network rollout announcements",
            "5G / fibre capex changes",
            "major equipment procurement events",
        ],
    ),

    "Aluminium": MarketCharacter(
        market="Aluminium",
        character=(
            "Telecom infrastructure and equipment input-cost character. "
            "Aluminium can enter tower, structural, enclosure, cable and "
            "equipment supply chains, while also reflecting industrial-capex conditions."
        ),
        exposure_character=(
            "Indirect-to-moderate exposure through network infrastructure, "
            "equipment and supplier costs."
        ),
        impact_path=[
            "Aluminium price",
            "tower / enclosure / structural / equipment costs",
            "network deployment cost",
            "Airtel capex and supplier economics",
            "cash-flow / margin expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged aluminium/Airtel relationships.",
            "Compare aluminium movement with capex and operating-margin indicators.",
            "Control for copper and broader industrial-metal conditions.",
            "Use procurement/deployment lag analysis rather than same-day correlation only.",
            "Test whether effects differ during accelerated network-capex periods.",
        ],
        relevant_indicators=[
            "aluminium return",
            "industrial-metals basket",
            "Airtel capex",
            "network rollout",
            "margin",
            "free cash flow",
        ],
        relevant_events=[
            "aluminium supply shocks",
            "5G/fibre rollout changes",
            "major capex announcements",
            "equipment procurement changes",
        ],
    ),

    "Zinc": MarketCharacter(
        market="Zinc",
        character=(
            "Indirect industrial and infrastructure-material character. "
            "Zinc can affect galvanised telecom towers and related infrastructure "
            "through the steel protection / fabrication supply chain."
        ),
        exposure_character=(
            "Indirect infrastructure and supplier-cost exposure."
        ),
        impact_path=[
            "Zinc price",
            "galvanising / fabricated telecom-infrastructure cost",
            "tower and network deployment economics",
            "Airtel capex",
            "cash-flow / margin expectations",
        ],
        calculation_logic=[
            "Measure rolling and lagged zinc/Airtel relationships.",
            "Compare zinc with aluminium and copper to isolate common industrial-metal factors.",
            "Control for NIFTY 50 and telecom capex cycles.",
            "Use deployment/procurement lag windows.",
            "Do not treat zinc correlation as direct causation without procurement evidence.",
        ],
        relevant_indicators=[
            "zinc return",
            "industrial-metals basket",
            "tower/infrastructure capex proxy",
            "Airtel capex",
            "free cash flow",
        ],
        relevant_events=[
            "zinc supply shocks",
            "tower-cost changes",
            "network rollout events",
            "major telecom infrastructure orders",
        ],
    ),

    "Electricity": MarketCharacter(
        market="Electricity",
        character=(
            "Direct operational-energy character. Telecom networks, data centres, "
            "offices and other digital infrastructure require continuous power, "
            "making electricity cost and availability more operationally relevant "
            "than most other tracked commodities."
        ),
        exposure_character=(
            "Direct operating-cost and infrastructure-reliability exposure."
        ),
        impact_path=[
            "Electricity price / availability",
            "network and data-centre operating cost",
            "energy opex",
            "Airtel EBITDA / margin / cash flow",
            "valuation response",
        ],
        calculation_logic=[
            "Use relevant Indian electricity-market/tariff data rather than a generic global series.",
            "Measure electricity-cost sensitivity with appropriate operating lags.",
            "Compare electricity movement with EBITDA margin and energy-cost disclosures where available.",
            "Separate price effects from outages/reliability effects.",
            "Test whether impact differs by network expansion and data-centre intensity.",
        ],
        relevant_indicators=[
            "electricity price",
            "power availability",
            "energy cost",
            "Airtel EBITDA margin",
            "capex",
            "free cash flow",
        ],
        relevant_events=[
            "electricity tariff changes",
            "power shortages / outages",
            "major grid events",
            "data-centre expansion",
            "network-energy efficiency initiatives",
        ],
    ),
}


BHARTIARTL_CHARACTER = CompanyCharacter(
    symbol="BHARTIARTL",
    company_name="Bharti Airtel Limited",
    sector="Telecommunications / Digital Communications",
    industry_character=(
        "Large integrated communications platform with mobile connectivity, "
        "home broadband, enterprise connectivity and digital services. Its economic "
        "character is subscription-driven, scale-driven, network-capex intensive, "
        "spectrum-sensitive and highly dependent on customer retention, ARPU, data "
        "usage, network quality, pricing discipline and regulatory conditions."
    ),
    business_character=[
        "Mobile voice and data services",
        "4G and 5G connectivity",
        "Prepaid and postpaid consumer services",
        "Home broadband / fibre connectivity",
        "Enterprise connectivity and communications",
        "Cloud and data-centre related services",
        "Cybersecurity and managed enterprise solutions",
        "IoT and connected-device services",
        "CPaaS / communications platforms",
        "Digital advertising and related digital services",
        "Direct-to-consumer digital entertainment ecosystem",
        "International telecom operations, especially Africa",
        "Wholesale / carrier connectivity",
        "Telecom infrastructure and network assets",
    ],
    demand_drivers=[
        "Mobile subscriber growth",
        "Customer retention and churn",
        "Data consumption per user",
        "ARPU growth",
        "5G adoption",
        "Smartphone penetration",
        "Home broadband penetration",
        "Enterprise digitalisation",
        "Cloud and cybersecurity demand",
        "IoT adoption",
        "Digital-content consumption",
        "African market subscriber and ARPU trends",
    ],
    revenue_drivers=[
        "Mobile ARPU",
        "Mobile subscriber base",
        "Postpaid mix",
        "Data usage",
        "5G monetisation",
        "Home broadband subscribers",
        "Enterprise revenue",
        "Digital services",
        "Cloud / data-centre services",
        "IoT / CPaaS",
        "International/Africa revenue",
        "Wholesale services",
    ],
    cost_drivers=[
        "Spectrum usage and spectrum-related costs",
        "Network capex",
        "Radio/network equipment",
        "Fibre deployment",
        "Tower and infrastructure costs",
        "Electricity and diesel / backup power",
        "Interconnect and network operating costs",
        "Content and digital-service costs",
        "Employee costs",
        "Lease / infrastructure costs",
        "Foreign-exchange movement for imported equipment and international operations",
        "Financing costs and debt servicing",
    ],
    supply_chain_character=[
        "Telecom network equipment vendors",
        "Radio access network suppliers",
        "Fibre and cable suppliers",
        "Tower and infrastructure ecosystem",
        "Data-centre and cloud ecosystem",
        "Handset and device ecosystem",
        "Technology and software partners",
        "International connectivity providers",
        "Energy and backup-power suppliers",
        "Enterprise technology partners",
        "Large Indian and international vendor ecosystem",
    ],
    strategic_drivers=[
        "5G network expansion and monetisation",
        "Fibre and home broadband expansion",
        "Network quality and coverage",
        "ARPU improvement",
        "Customer mix and premiumisation",
        "Enterprise digital transformation",
        "Cloud, cybersecurity and IoT growth",
        "Data-centre and digital-infrastructure expansion",
        "Africa business performance",
        "Digital ecosystem monetisation",
        "Capital efficiency and free-cash-flow generation",
        "Balance-sheet / leverage management",
        "Technology partnerships",
        "Spectrum strategy",
    ],
    key_indicators=[
        "mobile subscribers",
        "subscriber market share",
        "churn",
        "ARPU",
        "data usage per customer",
        "4G/5G subscriber base",
        "5G coverage",
        "home broadband subscribers",
        "enterprise revenue",
        "Africa revenue",
        "EBITDA",
        "EBITDA margin",
        "revenue growth",
        "capex",
        "free cash flow",
        "net debt",
        "net debt / EBITDA",
        "spectrum obligations",
        "network quality",
        "Airtel stock return",
        "Airtel volume",
        "relative strength versus NIFTY 50",
    ],
    key_events=[
        "tariff revisions",
        "ARPU improvement announcements",
        "major 5G rollout milestones",
        "large spectrum auctions / allocation changes",
        "telecom regulatory changes",
        "AGR / licence / regulatory developments",
        "major home-broadband expansion",
        "large enterprise contracts",
        "data-centre / cloud expansion",
        "cybersecurity or major technology events",
        "major network outages",
        "African-market regulatory changes",
        "currency shocks affecting Africa operations",
        "quarterly and annual results",
        "subscriber-market-share releases",
        "capex guidance",
        "debt refinancing / funding events",
        "major strategic partnerships",
        "large vendor / infrastructure contracts",
        "government digital-infrastructure initiatives",
    ],
    market_characters=BHARTIARTL_MARKETS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Bharti Airtel company character."""
    return BHARTIARTL_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return Bharti Airtel's character for one tracked market."""
    try:
        return BHARTIARTL_MARKETS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine Bharti Airtel market characters."""
    return dict(BHARTIARTL_MARKETS)


def validate_character() -> bool:
    """
    Validate the company-character contract.

    The character layer intentionally does not contain:
    RANK, PCT_CHANGE, LINKAGE_SCORE or RELATION.
    Those are outputs of the later historical calculation layer.
    """
    if BHARTIARTL_CHARACTER.symbol != "BHARTIARTL":
        return False

    if set(BHARTIARTL_MARKETS) != set(TRACKED_MARKETS):
        return False

    for market_name, character in BHARTIARTL_MARKETS.items():
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
    }

    if forbidden_fields.intersection(BHARTIARTL_CHARACTER.__dataclass_fields__):
        return False

    return True


if __name__ == "__main__":
    print(f"{BHARTIARTL_CHARACTER.company_name} ({BHARTIARTL_CHARACTER.symbol})")
    print(f"Tracked markets: {len(BHARTIARTL_MARKETS)}")
    print(f"Character validation: {validate_character()}")

    for market_name in TRACKED_MARKETS:
        character = BHARTIARTL_MARKETS[market_name]
        print(f"- {market_name}: {character.character}")
