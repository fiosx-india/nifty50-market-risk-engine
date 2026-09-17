"""
ADANIPORTS — Company Character Definition
==========================================

Purpose
-------
This module defines the business character of ADANIPORTS and its
relationship with the 9 research markets used by the NIFTY 50
Market Risk Engine.

IMPORTANT
---------
This file contains CHARACTER / RELATIONSHIP METADATA only.

It does NOT contain:
- hard-coded linkage scores
- fixed percentage impacts
- rankings
- predicted returns
- BUY/SELL decisions
- correlation results

Those values must be calculated later from real historical/live data.

Architecture
------------
Company Character
        ↓
Market Character
        ↓
Industry / Sector
        ↓
Exposure Type
        ↓
Impact Path
        ↓
Historical / Event / Indicator Calculation
        ↓
Research Evidence
"""

from dataclasses import dataclass, field
from typing import Dict, List


# ---------------------------------------------------------------------
# 1. MARKET CHARACTER
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class MarketCharacter:
    market: str
    character: str
    exposure_character: str
    impact_path: str
    calculation_logic: str


# ---------------------------------------------------------------------
# 2. COMPANY CHARACTER
# ---------------------------------------------------------------------

@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    company_character: str

    # Core business identity
    primary_businesses: List[str] = field(default_factory=list)
    operating_model: List[str] = field(default_factory=list)

    # Economic drivers
    revenue_drivers: List[str] = field(default_factory=list)
    cost_drivers: List[str] = field(default_factory=list)
    demand_drivers: List[str] = field(default_factory=list)

    # Structural relationships
    supply_chain_links: List[str] = field(default_factory=list)
    sector_links: List[str] = field(default_factory=list)

    # Market relationship map
    markets: Dict[str, MarketCharacter] = field(default_factory=dict)

    # Research behaviour
    important_indicators: List[str] = field(default_factory=list)
    important_events: List[str] = field(default_factory=list)
    preferred_timeframes: List[str] = field(default_factory=list)

    # Rules used by later calculation engines
    calculation_rules: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------
# 3. ADANIPORTS COMPANY CHARACTER
# ---------------------------------------------------------------------

ADANIPORTS_CHARACTER = CompanyCharacter(
    symbol="ADANIPORTS",
    company_name="Adani Ports and Special Economic Zone Limited",

    company_character=(
        "Integrated transport utility built around ports, logistics and "
        "marine operations. The company character is driven by cargo "
        "throughput, trade flows, logistics utilisation, marine activity, "
        "infrastructure economics and the broader industrial cycle."
    ),

    primary_businesses=[
        "Ports and terminal operations",
        "Integrated logistics",
        "Marine services",
        "Cargo handling",
        "Transportation and supply-chain services",
        "Port-linked infrastructure and logistics assets",
    ],

    operating_model=[
        "Port infrastructure",
        "Cargo throughput",
        "Container and bulk cargo handling",
        "Integrated logistics movement",
        "Marine and vessel-related services",
        "End-to-end supply-chain connectivity",
    ],

    revenue_drivers=[
        "Cargo volumes",
        "Container throughput",
        "Bulk cargo throughput",
        "Port handling activity",
        "Logistics volumes",
        "Marine services",
        "Storage and related logistics activity",
        "Trade and import/export activity",
    ],

    cost_drivers=[
        "Energy and electricity costs",
        "Fuel and marine operating costs",
        "Labour and terminal operating costs",
        "Maintenance and infrastructure costs",
        "Logistics and transportation costs",
        "Financing costs",
        "Capital expenditure",
    ],

    demand_drivers=[
        "Indian and global trade volumes",
        "Industrial production",
        "Infrastructure activity",
        "Automobile and manufacturing activity",
        "Energy and commodity trade",
        "Containerised trade",
        "Bulk commodity movement",
        "Domestic consumption and economic activity",
    ],

    supply_chain_links=[
        "Importers and exporters",
        "Industrial manufacturers",
        "Energy companies",
        "Automobile supply chains",
        "Construction and infrastructure supply chains",
        "Commodity producers and traders",
        "Container logistics",
        "Rail and road logistics",
        "Shipping and marine ecosystem",
    ],

    sector_links=[
        "Ports",
        "Logistics",
        "Transportation",
        "Marine services",
        "Infrastructure",
        "Industrial supply chain",
        "Energy logistics",
        "Commodity logistics",
    ],

    markets={

        # -------------------------------------------------------------
        # NIFTY 50
        # -------------------------------------------------------------
        "NIFTY 50": MarketCharacter(
            market="NIFTY 50",
            character=(
                "Broad Indian equity-market and systematic-risk environment "
                "that influences liquidity, valuation and investor sentiment."
            ),
            exposure_character=(
                "Primary systematic-market relationship"
            ),
            impact_path=(
                "NIFTY movement → market sentiment / liquidity / valuation "
                "→ ADANIPORTS stock behaviour"
            ),
            calculation_logic=(
                "Calculate return correlation, beta, rolling relationship, "
                "relative strength, downside sensitivity and lag impact. "
                "Separate broad-market effect from company-specific effects."
            ),
        ),

        # -------------------------------------------------------------
        # CRUDE OIL
        # -------------------------------------------------------------
        "Crude Oil": MarketCharacter(
            market="Crude Oil",
            character=(
                "Global energy commodity whose price influences energy trade, "
                "shipping economics, fuel costs and cargo flows."
            ),
            exposure_character=(
                "Direct cargo-flow + indirect fuel/logistics relationship"
            ),
            impact_path=(
                "Crude price / trade activity → energy cargo volumes + "
                "shipping/logistics economics + fuel conditions → "
                "company activity → stock behaviour"
            ),
            calculation_logic=(
                "Separate cargo-volume relationship from fuel-cost relationship. "
                "Test contemporaneous and lagged effects and control for NIFTY. "
                "Use cargo/throughput data where available instead of assuming "
                "that crude price alone represents company exposure."
            ),
        ),

        # -------------------------------------------------------------
        # GOLD
        # -------------------------------------------------------------
        "Gold": MarketCharacter(
            market="Gold",
            character=(
                "Precious-metal and macro-risk asset whose movement can reflect "
                "risk sentiment, currency conditions, liquidity and global uncertainty."
            ),
            exposure_character=(
                "Indirect trade-flow / macro relationship"
            ),
            impact_path=(
                "Gold movement → risk sentiment, currency/liquidity and trade "
                "conditions → cargo/logistics environment → stock behaviour"
            ),
            calculation_logic=(
                "Test whether gold adds explanatory power after controlling "
                "for NIFTY, trade variables and other commodities. Do not "
                "assume direct gold exposure."
            ),
        ),

        # -------------------------------------------------------------
        # SILVER
        # -------------------------------------------------------------
        "Silver": MarketCharacter(
            market="Silver",
            character=(
                "Precious and industrial metal whose movement can contain "
                "information about industrial demand and commodity-cycle conditions."
            ),
            exposure_character=(
                "Indirect industrial-trade relationship"
            ),
            impact_path=(
                "Silver movement → industrial demand / commodity cycle → "
                "cargo and trade activity → logistics environment → stock behaviour"
            ),
            calculation_logic=(
                "Measure historical return, rolling correlation, lag response "
                "and volatility relationship. Test incremental explanatory "
                "power after controlling for broad market and related metals."
            ),
        ),

        # -------------------------------------------------------------
        # NATURAL GAS
        # -------------------------------------------------------------
        "Natural Gas": MarketCharacter(
            market="Natural Gas",
            character=(
                "Energy commodity connected to industrial activity, power, "
                "gas trade and LNG-related logistics."
            ),
            exposure_character=(
                "Cargo-flow + energy-trade relationship"
            ),
            impact_path=(
                "Natural-gas / LNG conditions → energy cargo demand and trade "
                "flows → port volumes / logistics activity → stock behaviour"
            ),
            calculation_logic=(
                "Measure gas return against cargo and stock behaviour, including "
                "lag effects and event periods. Distinguish cargo-related impact "
                "from broad energy-market sentiment."
            ),
        ),

        # -------------------------------------------------------------
        # COPPER
        # -------------------------------------------------------------
        "Copper": MarketCharacter(
            market="Copper",
            character=(
                "Industrial metal and economic-cycle indicator linked to "
                "manufacturing, infrastructure, electrical and construction activity."
            ),
            exposure_character=(
                "Industrial cargo / trade-cycle relationship"
            ),
            impact_path=(
                "Copper cycle → industrial activity and trade demand → "
                "bulk/container cargo flows → logistics utilisation → stock behaviour"
            ),
            calculation_logic=(
                "Calculate copper-return relationship, rolling beta, lag response "
                "and interaction with industrial and market indicators."
            ),
        ),

        # -------------------------------------------------------------
        # ALUMINIUM
        # -------------------------------------------------------------
        "Aluminium": MarketCharacter(
            market="Aluminium",
            character=(
                "Industrial metal associated with manufacturing, transportation, "
                "construction, packaging and broader trade activity."
            ),
            exposure_character=(
                "Industrial cargo / commodity-cycle relationship"
            ),
            impact_path=(
                "Aluminium cycle → industrial production / trade → "
                "cargo throughput → port/logistics activity → stock behaviour"
            ),
            calculation_logic=(
                "Test aluminium return, volume/throughput relationship, "
                "rolling correlation and lag impact. Control for NIFTY and "
                "avoid treating aluminium price movement as direct causation."
            ),
        ),

        # -------------------------------------------------------------
        # ZINC
        # -------------------------------------------------------------
        "Zinc": MarketCharacter(
            market="Zinc",
            character=(
                "Industrial metal strongly associated with galvanising, "
                "construction, infrastructure, manufacturing and industrial supply chains."
            ),
            exposure_character=(
                "Industrial cargo / infrastructure-cycle relationship"
            ),
            impact_path=(
                "Zinc cycle → construction / industrial activity → "
                "cargo demand → port/logistics volumes → stock behaviour"
            ),
            calculation_logic=(
                "Measure historical and lagged relationship, rolling stability "
                "and interaction with other industrial metals. Avoid assuming "
                "direct causation from zinc price movement alone."
            ),
        ),

        # -------------------------------------------------------------
        # ELECTRICITY
        # -------------------------------------------------------------
        "Electricity": MarketCharacter(
            market="Electricity",
            character=(
                "Operating-input and infrastructure-cost factor affecting "
                "large physical assets, terminals, warehouses and logistics operations."
            ),
            exposure_character=(
                "Operational energy-cost relationship"
            ),
            impact_path=(
                "Electricity conditions → terminal / warehouse / logistics "
                "operating costs and infrastructure economics → margins / "
                "cash flows → stock behaviour"
            ),
            calculation_logic=(
                "Measure electricity-price and availability relationship where "
                "reliable data exists, including lag, volatility and event effects. "
                "Use regional/market-specific electricity data where appropriate."
            ),
        ),
    },

    important_indicators=[
        "Cargo throughput",
        "Container volumes",
        "Bulk cargo volumes",
        "Port utilisation",
        "Logistics volumes",
        "Marine activity",
        "Revenue growth",
        "EBITDA and operating margin",
        "Free cash flow",
        "Capital expenditure",
        "Net debt / financing conditions",
        "NIFTY 50 return",
        "Crude Oil return",
        "Gold return",
        "Silver return",
        "Natural Gas return",
        "Copper return",
        "Aluminium return",
        "Zinc return",
        "Electricity price / availability",
        "Volume and relative volume",
        "Volatility",
        "Relative strength",
    ],

    important_events=[
        "Quarterly results",
        "Annual results and annual-report disclosures",
        "Cargo-volume updates",
        "Port capacity additions",
        "New terminal or port developments",
        "Major customer / cargo contracts",
        "Logistics expansion",
        "Marine business developments",
        "Acquisitions or divestments",
        "Large capital expenditure announcements",
        "Debt or financing changes",
        "Credit-rating actions",
        "Regulatory developments",
        "Government infrastructure policy",
        "Major commodity-trade disruptions",
        "Shipping disruptions",
        "Geopolitical events affecting trade routes",
        "Natural disasters affecting ports or logistics",
        "Company exchange filings",
    ],

    preferred_timeframes=[
        "5m",
        "15m",
        "30m",
        "1h",
        "4h",
        "1d",
        "1w",
        "1M",
    ],

    calculation_rules=[
        "Never use a fixed market-impact score.",
        "Never assume correlation means causation.",
        "Calculate relationships from historical observations.",
        "Use lagged variables because commodity effects may not reach the company immediately.",
        "Control for NIFTY 50 when testing individual commodity relationships.",
        "Separate price effects from volume / throughput effects.",
        "Separate operating-cost effects from cargo-demand effects.",
        "Use rolling windows to detect relationship stability and regime changes.",
        "Use event studies around company-specific and market-specific events.",
        "Use volume confirmation when analysing stock-price reactions.",
        "Use data freshness as part of research evidence.",
        "Do not generate a final BUY/SELL decision inside this character module.",
        "Pass evidence to the central research / decision layer.",
    ],
)


# ---------------------------------------------------------------------
# 4. PUBLIC ACCESS FUNCTIONS
# ---------------------------------------------------------------------

def get_company_character() -> CompanyCharacter:
    """Return the complete ADANIPORTS company character."""
    return ADANIPORTS_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return the character for one of the 9 supported markets."""
    key = market.strip()

    if key not in ADANIPORTS_CHARACTER.markets:
        raise KeyError(
            f"Unsupported market '{market}'. "
            f"Supported markets: {', '.join(ADANIPORTS_CHARACTER.markets)}"
        )

    return ADANIPORTS_CHARACTER.markets[key]


def get_all_markets() -> Dict[str, MarketCharacter]:
    """Return all 9 market characters."""
    return dict(ADANIPORTS_CHARACTER.markets)


def get_company_summary() -> dict:
    """Return a compact machine-readable company summary."""
    return {
        "symbol": ADANIPORTS_CHARACTER.symbol,
        "company_name": ADANIPORTS_CHARACTER.company_name,
        "company_character": ADANIPORTS_CHARACTER.company_character,
        "primary_businesses": list(ADANIPORTS_CHARACTER.primary_businesses),
        "sector_links": list(ADANIPORTS_CHARACTER.sector_links),
        "market_count": len(ADANIPORTS_CHARACTER.markets),
        "markets": list(ADANIPORTS_CHARACTER.markets.keys()),
    }


def validate_character() -> bool:
    """
    Validate the character definition.

    This checks structure only. It does not validate historical
    market relationships or prove causality.
    """
    expected_markets = {
        "NIFTY 50",
        "Crude Oil",
        "Gold",
        "Silver",
        "Natural Gas",
        "Copper",
        "Aluminium",
        "Zinc",
        "Electricity",
    }

    actual_markets = set(ADANIPORTS_CHARACTER.markets.keys())

    if actual_markets != expected_markets:
        missing = expected_markets - actual_markets
        extra = actual_markets - expected_markets
        raise ValueError(
            f"Market character validation failed. "
            f"Missing={sorted(missing)}, Extra={sorted(extra)}"
        )

    if ADANIPORTS_CHARACTER.symbol != "ADANIPORTS":
        raise ValueError("Invalid company symbol.")

    for market_name, market in ADANIPORTS_CHARACTER.markets.items():
        required = (
            market.market,
            market.character,
            market.exposure_character,
            market.impact_path,
            market.calculation_logic,
        )

        if not all(required):
            raise ValueError(
                f"Incomplete market character definition: {market_name}"
            )

    return True


if __name__ == "__main__":
    validate_character()

    print("ADANIPORTS Character: VALID")
    print(f"Company: {ADANIPORTS_CHARACTER.company_name}")
    print(f"Markets: {len(ADANIPORTS_CHARACTER.markets)}")

    for name, market in ADANIPORTS_CHARACTER.markets.items():
        print(f"- {name}: {market.exposure_character}")
