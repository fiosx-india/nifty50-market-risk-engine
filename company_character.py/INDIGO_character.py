"""
INDIGO — Company Character & 9-Market Relationship Definition

This module defines IndiGo's business character and the research rules that a
later historical engine should use to calculate market impact.

No rank, daily percentage change, linkage score, or relation from a snapshot
CSV is hard-coded here. Historical relationships must be calculated from real
data, with controls and lag analysis.
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
        "Broad Indian equity-market and domestic risk/liquidity regime.",
        "Market-level exposure, not a physical airline input.",
        "NIFTY regime -> investor risk appetite/liquidity -> airline valuation and passenger-demand expectations -> INDIGO.",
        "Calculate INDIGO excess return versus NIFTY, rolling beta, rolling correlation, volatility sensitivity and event-window response. Separate market beta from company-specific moves.",
        ("NIFTY return", "INDIGO return", "rolling beta", "rolling correlation",
         "India VIX", "market breadth", "FII/DII flows", "INDIGO volume"),
        ("RBI policy", "Union Budget", "aviation policy", "earnings",
         "fleet/order announcements", "major geopolitical events"),
        ("intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Global energy benchmark and major input-price signal for aviation fuel.",
        "High economic relevance through ATF/jet-fuel costs; crude itself is not the airline's purchased fuel.",
        "Crude -> refinery/product prices -> ATF -> fuel expense -> fares/fuel surcharge -> passenger demand and margins -> INDIGO.",
        "Use crude returns plus ATF/jet-fuel data where available. Test lagged relationships with INDIGO margins, earnings, fares and stock returns; control for FX and NIFTY.",
        ("Brent return", "WTI return", "ATF/jet-fuel price", "fuel expense",
         "fuel cost per ASK", "fuel surcharge", "USD/INR", "RASK", "CASK"),
        ("OPEC+ decisions", "Middle-East disruptions", "fuel-price shocks",
         "fuel-surcharge changes", "earnings guidance"),
        ("intraday", "1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Gold": _mc(
        "Gold",
        "Precious-metal safe-haven and household-wealth/risk-sentiment market.",
        "Indirect macro exposure; gold is not a core physical airline input.",
        "Gold/risk regime -> inflation, rates, wealth and risk sentiment -> travel demand/investor sentiment -> INDIGO.",
        "Test gold returns against INDIGO after controlling for NIFTY, crude, USD/INR and broad risk variables. Use event windows around monetary or geopolitical shocks.",
        ("gold return", "USD gold", "INR gold", "India VIX",
         "USD/INR", "real yields", "INDIGO return"),
        ("geopolitical shocks", "central-bank decisions",
         "inflation surprises", "major risk-off events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Silver": _mc(
        "Silver",
        "Industrial precious-metal and risk/sentiment market.",
        "Indirect macro exposure; no core direct silver consumption is assumed.",
        "Silver/risk-industrial cycle -> economic activity, inflation and sentiment -> travel environment/investor positioning -> INDIGO.",
        "Calculate rolling and lagged association with INDIGO while controlling for NIFTY and crude. Compare incremental explanatory power against broader macro variables.",
        ("silver return", "gold/silver ratio", "industrial-metals basket",
         "USD/INR", "INDIGO return", "NIFTY return"),
        ("industrial-cycle shocks", "inflation releases",
         "major geopolitical events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Global/regional energy market with industrial and power-system linkages.",
        "Indirect operating and macro exposure; not a primary airline fuel benchmark.",
        "Natural gas -> power/industrial costs and energy complex -> inflation, demand and airport/ground-service economics -> INDIGO.",
        "Test gas returns against INDIGO with controls for crude, electricity, NIFTY and FX. Increase importance only if historical data shows stable incremental explanatory power.",
        ("gas benchmark", "regional gas price", "electricity price",
         "inflation", "USD/INR", "INDIGO return"),
        ("gas supply disruptions", "weather shocks",
         "power-market stress", "geopolitical events"),
        ("1D", "1W", "1M", "1Q"),
    ),

    "Copper": _mc(
        "Copper",
        "Global industrial and infrastructure-cycle metal.",
        "Indirect exposure through aircraft, airport, electrical and engineering supply chains and broad economic activity.",
        "Copper cycle -> industrial/infrastructure demand and supplier costs -> macro growth/travel demand/capex environment -> INDIGO.",
        "Measure incremental association after controlling for NIFTY and crude. For supply-chain analysis, separately track aircraft/airport capex and supplier-price evidence.",
        ("LME copper", "copper return", "industrial-metals index",
         "global PMI", "INDIGO capex", "INDIGO return"),
        ("China/global PMI shocks", "infrastructure stimulus",
         "major supply disruptions"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Lightweight industrial metal used broadly in transport and engineering.",
        "Indirect but strategically relevant through aircraft materials, parts, airport infrastructure, engineering and supplier costs.",
        "Aluminium -> aircraft/component and airport/supplier economics -> fleet capex and operating ecosystem -> INDIGO.",
        "Use aluminium returns and, where available, aircraft/component cost data. Test lagged effects on capex, fleet economics and INDIGO returns. Do not treat aluminium as a direct fuel-cost driver.",
        ("LME aluminium", "aluminium premium", "aircraft/component cost proxies",
         "fleet additions", "capex", "INDIGO return"),
        ("aluminium supply shocks", "aircraft supply-chain disruptions",
         "large fleet orders", "airport capex"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Zinc": _mc(
        "Zinc",
        "Industrial metal linked to galvanising, infrastructure and manufacturing.",
        "Low-to-indirect exposure through airport infrastructure, ground equipment and industrial supply chains.",
        "Zinc -> galvanised steel/infrastructure cost cycle -> airport/industrial capex -> INDIGO ecosystem.",
        "Use historical tests only; require incremental explanatory power beyond NIFTY, copper and aluminium before treating zinc as meaningful.",
        ("LME zinc", "steel/infrastructure basket", "airport capex",
         "INDIGO capex", "INDIGO return"),
        ("infrastructure cycle", "metal supply shocks",
         "airport expansion announcements"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Electricity": _mc(
        "Electricity",
        "Power-market condition affecting airports, ground operations and energy-intensive infrastructure.",
        "Indirect operating-cost and infrastructure exposure through airport facilities, offices, data systems, maintenance and ground operations.",
        "Electricity cost/availability -> airport and ground-operation expense -> service economics and infrastructure costs -> INDIGO.",
        "Where reliable local electricity/industrial tariff data exists, compare it with operating-cost metrics and INDIGO returns. Use regional data appropriate to the airports operated.",
        ("commercial/industrial tariff", "airport power cost where available",
         "power availability", "fuel/energy mix", "CASK", "INDIGO return"),
        ("power shortages", "tariff changes",
         "airport infrastructure events", "extreme-weather disruptions"),
        ("1D", "1W", "1M", "1Q"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="INDIGO",
    company_name="InterGlobe Aviation Limited (IndiGo)",
    sector="Airlines / Aviation",
    industry_character=(
        "Large-scale low-cost airline built around network density, fleet utilisation, "
        "affordable fares, operational reliability, capacity discipline and increasingly "
        "international connectivity."
    ),
    business_character=(
        "Passenger-airline operating model where traffic volume, fares/yield, load factor, "
        "aircraft utilisation, fleet availability, airport capacity, fuel cost, foreign "
        "exchange, maintenance and operating efficiency interact. The engine must separate "
        "demand effects, direct cost effects, supply constraints, macro effects and market beta."
    ),
    demand_drivers=(
        "Domestic passenger traffic", "International passenger traffic",
        "Fare affordability", "Consumer and business travel demand",
        "GDP/economic activity", "Corporate travel", "Tourism/leisure",
        "Seasonality/festivals", "Holiday periods", "Network expansion",
        "Airport connectivity", "Competitive capacity", "Customer confidence",
        "Foreign travel demand",
    ),
    revenue_drivers=(
        "Passenger ticket revenue", "Passenger load factor", "Average fare",
        "Yield", "Available seat kilometres", "Revenue passenger kilometres",
        "Ancillary revenue", "Cargo revenue", "International expansion",
        "Fleet utilisation", "Capacity deployment", "Fuel charges when applicable",
        "Route mix",
    ),
    cost_drivers=(
        "Aviation turbine fuel", "Fuel price and consumption", "USD/INR and FX",
        "Aircraft lease and ownership costs", "Maintenance and repair",
        "Aircraft and engine availability", "Employee and crew costs",
        "Airport and navigation charges", "Handling and ground services",
        "Engineering/technical services", "Distribution and sales", "Technology",
        "Insurance", "Depreciation", "Interest/finance costs",
        "Foreign-currency liabilities",
    ),
    supply_chain_character=(
        "Aircraft and engine manufacturers", "Aircraft lessors",
        "Maintenance/repair/overhaul ecosystem", "ATF suppliers/refiners",
        "Airports", "Air navigation/airport authorities",
        "Ground-handling providers", "Catering and inflight suppliers",
        "Technology/reservation systems", "Crew and aviation training",
        "Aircraft parts/component suppliers", "Travel distribution ecosystem",
    ),
    strategic_drivers=(
        "Network density", "Fleet scale and availability", "International expansion",
        "Operational reliability", "Affordable-fare positioning",
        "Aircraft utilisation", "Airport slot access", "Route economics",
        "Premium and ancillary monetisation", "Digital customer experience",
        "Operational efficiency", "Fleet renewal/fuel efficiency",
        "Supply-chain resilience",
    ),
    key_indicators=(
        "Passengers carried", "Load factor", "Available seat kilometres",
        "Revenue passenger kilometres", "Yield", "Passenger revenue",
        "Ancillary revenue", "Cargo revenue", "RASK", "CASK",
        "CASK excluding fuel", "Fuel cost", "Fuel cost per ASK",
        "Fleet size", "Aircraft utilisation", "Aircraft grounded/unavailable",
        "Daily departures", "Domestic market share", "International capacity",
        "EBITDAR", "EBITDA", "EBIT margin", "Profit after tax",
        "Cash balance", "Net debt/lease liabilities", "USD/INR exposure",
        "INDIGO return and volatility",
    ),
    key_events=(
        "Quarterly/annual results", "Monthly operational statistics",
        "Fleet orders and deliveries", "Aircraft grounding/supply constraints",
        "New routes and international expansion", "Airport slot/capacity changes",
        "Fuel-charge announcements", "Major ATF price shocks",
        "Major FX moves", "Aircraft/engine manufacturer disruptions",
        "Maintenance/safety material events", "Regulatory changes",
        "Geopolitical events affecting routes or fuel", "Management guidance",
        "Credit-rating changes", "Material exchange filings",
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
    if COMPANY_CHARACTER.symbol != "INDIGO":
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
    print("INDIGO character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
