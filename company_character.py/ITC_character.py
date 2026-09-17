"""
ITC Limited — Company Character and 9 Market Characters.

This module defines business/exposure character only. Snapshot CSV fields such
as RANK, PCT_CHANGE, LINKAGE_SCORE and RELATION are intentionally not stored
as permanent conclusions. They belong to the later historical calculation
engine.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Tuple


TRACKED_MARKETS: Tuple[str, ...] = (
    "NIFTY 50", "Crude Oil", "Gold", "Silver", "Natural Gas",
    "Copper", "Aluminium", "Zinc", "Electricity",
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


def _mc(market, character, exposure, path, logic, indicators, events, timeframes):
    return MarketCharacter(
        market=market,
        character=character,
        exposure_character=exposure,
        impact_path=path,
        calculation_logic=logic,
        relevant_indicators=indicators,
        relevant_events=events,
        expected_timeframes=timeframes,
    )


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Indian large-cap equity, liquidity and risk regime.",
        "Direct equity-market and valuation exposure.",
        "NIFTY regime -> flows/risk appetite -> valuation and liquidity -> ITC.",
        "Calculate ITC excess return, rolling beta/correlation, volatility response and event-window return versus NIFTY.",
        ("ITC return", "NIFTY return", "rolling beta", "rolling correlation",
         "India VIX", "ITC volume", "FII/DII flows", "consumer-sector index"),
        ("RBI policy", "Union Budget", "tax changes", "ITC results",
         "corporate actions", "major regulatory events"),
        ("intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Global energy, inflation and petrochemical-input benchmark.",
        "Indirect but meaningful cost and macro exposure.",
        "Crude -> petrochemical/packaging/freight costs -> margins; crude -> inflation/purchasing power -> consumer demand -> ITC.",
        "Test crude with packaging/resin, freight and inflation proxies; calculate lagged effects on FMCG margins, volumes and ITC returns while controlling for NIFTY and FX.",
        ("Brent", "WTI", "resin/petrochemical prices", "freight",
         "CPI/WPI", "FMCG margin", "volume growth", "ITC return"),
        ("OPEC+ decisions", "Middle-East disruptions", "fuel shocks",
         "inflation surprises", "freight disruptions"),
        ("1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Gold": _mc(
        "Gold",
        "Precious-metal, wealth, inflation and safe-haven sentiment market.",
        "Indirect macro exposure; not a core ITC operating input.",
        "Gold -> wealth/inflation/risk sentiment -> consumption and savings behaviour -> FMCG/hospitality demand and valuation -> ITC.",
        "Test gold against ITC after controlling for NIFTY, inflation, rates and FX; use event studies for risk-off episodes.",
        ("gold return", "INR gold", "real yields", "CPI",
         "India VIX", "consumer confidence", "ITC return"),
        ("geopolitical shocks", "inflation surprises",
         "central-bank decisions", "risk-off events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Silver": _mc(
        "Silver",
        "Precious/industrial-metal and global-cycle market.",
        "Indirect macro exposure; no core direct silver input is assumed.",
        "Silver -> industrial cycle/inflation sentiment -> consumer/business activity -> ITC.",
        "Calculate rolling/lagged association controlling for NIFTY, crude, inflation and other metals; require incremental explanatory value.",
        ("silver return", "gold/silver ratio", "industrial-metals index",
         "global PMI", "CPI", "ITC return"),
        ("industrial-cycle shocks", "inflation releases", "geopolitical events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Energy and industrial-input market affecting power and chemicals.",
        "Indirect cost exposure through manufacturing, packaging and energy.",
        "Natural gas -> energy/chemical costs -> manufacturing/packaging economics -> ITC margins; gas -> inflation -> demand.",
        "Test gas with crude, electricity, inflation, NIFTY and FX; investigate manufacturing and packaging channels separately.",
        ("gas benchmark", "regional gas price", "electricity price",
         "chemical/feedstock cost", "CPI/WPI", "ITC margin", "ITC return"),
        ("gas supply disruptions", "weather shocks",
         "power stress", "geopolitical events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Copper": _mc(
        "Copper",
        "Global industrial, electrical and infrastructure-cycle metal.",
        "Indirect exposure through electrical equipment, infrastructure and economic activity.",
        "Copper -> industrial/electrical capex -> manufacturing and infrastructure environment -> ITC.",
        "Use copper as an industrial-cycle and supply-chain signal; test incremental association after controlling for NIFTY, crude, aluminium and PMI.",
        ("LME copper", "copper return", "global PMI",
         "electrical equipment costs", "capex cycle", "ITC return"),
        ("China/global PMI shocks", "infrastructure stimulus",
         "copper supply disruptions", "industrial capex changes"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Industrial metal used in packaging, equipment and manufacturing.",
        "Meaningful indirect exposure through packaging/material and equipment costs.",
        "Aluminium -> packaging/material and equipment costs -> FMCG/Paper/Packaging margins and capex -> ITC.",
        "Track aluminium price/premium and packaging-material proxies; test lagged effects on segment margins and ITC returns.",
        ("LME aluminium", "aluminium premium", "packaging material cost",
         "paper/board cost", "FMCG margin", "ITC return"),
        ("aluminium supply shocks", "packaging-cost changes",
         "import policy", "industrial-cycle events"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Zinc": _mc(
        "Zinc",
        "Industrial metal linked to galvanising, manufacturing and infrastructure.",
        "Low-to-indirect exposure through infrastructure and manufacturing.",
        "Zinc -> industrial/material cost cycle -> manufacturing/infrastructure economics -> ITC cost environment.",
        "Require incremental explanatory power beyond copper, aluminium, crude and NIFTY before treating zinc as material.",
        ("LME zinc", "global PMI", "infrastructure cycle",
         "manufacturing cost index", "ITC return"),
        ("infrastructure cycle", "metal supply shocks",
         "manufacturing changes", "trade-policy changes"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Electricity": _mc(
        "Electricity",
        "Power-market condition affecting factories, paper mills, hotels and offices.",
        "Direct operating-cost and availability exposure across manufacturing and hospitality infrastructure.",
        "Electricity -> factory/paper/packaging/hotel costs -> segment margins and capex -> ITC.",
        "Use regional industrial/commercial tariffs and company energy data where available; test lagged effects on segment margins and profitability.",
        ("industrial electricity tariff", "power availability",
         "energy consumption", "renewable-energy share",
         "Paper/Packaging margin", "FMCG margin", "ITC return"),
        ("tariff changes", "power shortages", "extreme weather",
         "renewable-energy projects", "capacity additions"),
        ("1D", "1W", "1M", "1Q", "1Y"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="ITC",
    company_name="ITC Limited",
    sector="Diversified FMCG, Agri, Paper & Packaging and IT",
    industry_character=(
        "Diversified Indian consumer and value-chain enterprise spanning "
        "FMCG, cigarettes, agri business, paperboards/paper/packaging and "
        "technology, with hotel exposure through the group-company ecosystem."
    ),
    business_character=(
        "Multi-engine business model linking agricultural sourcing, branded "
        "consumer products, cigarettes, paperboards and packaging, hospitality "
        "and technology. The important character is vertical integration and "
        "shared capabilities: agri sourcing supports FMCG/cigarettes, packaging "
        "supports branded businesses, and distribution connects products to a "
        "large consumer base. Market effects must therefore be traced by business "
        "chain instead of treating ITC as one homogeneous commodity exposure."
    ),
    demand_drivers=(
        "Indian household consumption", "rural demand", "urban consumption",
        "consumer confidence", "disposable income", "premiumisation",
        "FMCG category growth", "cigarette volumes and legal tobacco demand",
        "food and beverage consumption", "hotel occupancy", "travel/business activity",
        "packaging demand", "industrial activity", "agri demand", "export demand",
        "technology spending",
    ),
    revenue_drivers=(
        "cigarette volume and pricing", "branded-food volumes", "personal-care sales",
        "stationery products", "agri commodity throughput", "leaf tobacco exports",
        "paperboard volumes", "specialty paper", "packaging and printing volumes",
        "domestic/export mix", "pricing and realisation", "hotel revenue",
        "technology-services revenue", "brand portfolio", "distribution reach",
        "modern trade/e-commerce",
    ),
    cost_drivers=(
        "leaf tobacco", "wheat", "rice", "coffee", "spices",
        "vegetable oils and food inputs", "paper/pulp/fibre inputs",
        "chemicals and resins", "packaging materials", "crude-linked inputs",
        "freight/logistics", "electricity/fuel", "employee costs",
        "advertising/brand building", "hotel operating costs",
        "technology infrastructure", "foreign exchange", "tax/excise/regulation",
    ),
    supply_chain_character=(
        "farmers and agri-value chains", "FPO/rural procurement ecosystem",
        "leaf tobacco supply", "food-grain suppliers", "spices and coffee chains",
        "food processing", "paper/pulp/fibre supply", "paperboard manufacturing",
        "flexible/carton packaging", "logistics and warehousing",
        "distributors and retailers", "modern trade/e-commerce",
        "hospitality ecosystem", "technology/cloud ecosystem",
    ),
    strategic_drivers=(
        "ITC Next", "FMCG scale-up", "Mother-brand leverage", "premiumisation",
        "backward integration", "agri value-chain leadership",
        "multi-channel distribution", "packaging innovation",
        "sustainable paper/packaging", "renewable energy",
        "digital consumer insights", "AI-led consumer analytics",
        "Fresh Food growth", "new FMCG categories", "capital allocation",
    ),
    key_indicators=(
        "FMCG revenue growth", "FMCG segment PBIT", "cigarette volume growth",
        "cigarette net revenue", "FMCG-Others growth", "food-category growth",
        "personal-care growth", "agri revenue/throughput", "agri exports",
        "paperboard volume", "paper/packaging revenue", "packaging volume",
        "segment margins", "gross margin", "EBITDA", "EBITDA margin", "PAT",
        "free cash flow", "capex", "working capital", "brand investment",
        "market share", "rural/urban demand", "ITC return and volatility",
    ),
    key_events=(
        "quarterly/annual results", "cigarette tax/excise changes",
        "tobacco regulation", "FMCG launches", "food/raw-material shocks",
        "agri export/import policy", "paperboard import policy",
        "anti-dumping/trade actions", "packaging regulation",
        "commodity supply disruptions", "hotel developments",
        "ITC Hotels developments", "ITC Infotech developments",
        "acquisitions/amalgamations", "major capex", "geopolitical/logistics shocks",
        "management guidance", "material exchange filings",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    try:
        return MARKET_CHARACTERS[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    return dict(MARKET_CHARACTERS)


def validate_character() -> bool:
    if COMPANY_CHARACTER.symbol != "ITC":
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
    print("ITC character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
