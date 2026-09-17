"""
APOLLOHOSP — Company Character Definition
==========================================

Apollo Hospitals Enterprise Limited
NIFTY 50 Market Risk Engine

This module describes the company's business character and its
relationship with the 9 research markets.

It contains research metadata, not fixed impact scores.

No hard-coded:
- linkage scores
- ranks
- percentage impacts
- BUY/SELL signals
- predicted returns

Historical relationships must be calculated from actual data.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class MarketCharacter:
    market: str
    character: str
    exposure_character: str
    impact_path: str
    calculation_logic: str


@dataclass(frozen=True)
class CompanyCharacter:
    symbol: str
    company_name: str
    company_character: str
    primary_businesses: List[str] = field(default_factory=list)
    operating_model: List[str] = field(default_factory=list)
    revenue_drivers: List[str] = field(default_factory=list)
    cost_drivers: List[str] = field(default_factory=list)
    demand_drivers: List[str] = field(default_factory=list)
    supply_chain_links: List[str] = field(default_factory=list)
    sector_links: List[str] = field(default_factory=list)
    markets: Dict[str, MarketCharacter] = field(default_factory=dict)
    important_indicators: List[str] = field(default_factory=list)
    important_events: List[str] = field(default_factory=list)
    preferred_timeframes: List[str] = field(default_factory=list)
    calculation_rules: List[str] = field(default_factory=list)


APOLLOHOSP_CHARACTER = CompanyCharacter(
    symbol="APOLLOHOSP",
    company_name="Apollo Hospitals Enterprise Limited",

    company_character=(
        "Integrated healthcare-services platform built around hospitals, "
        "clinical and diagnostic services, retail health, pharmacy distribution "
        "and digital healthcare. Its economic character is driven primarily by "
        "patient demand, occupancy and case mix, healthcare pricing, clinical "
        "capacity, medical talent, pharmacy/diagnostic activity and expansion "
        "of healthcare infrastructure."
    ),

    primary_businesses=[
        "Hospital healthcare services",
        "Secondary, tertiary and super-specialty care",
        "Retail health and diagnostics",
        "Pharmacy distribution",
        "Digital healthcare services",
        "Clinics and specialised healthcare formats",
        "Home and connected healthcare services",
    ],

    operating_model=[
        "Hospital beds and clinical capacity",
        "Patient admissions and procedures",
        "Occupancy and case mix",
        "Doctor and clinical-specialist network",
        "Diagnostics and retail healthcare",
        "Pharmacy procurement and distribution",
        "Digital healthcare platform",
        "Healthcare infrastructure expansion",
    ],

    revenue_drivers=[
        "Inpatient admissions",
        "Outpatient consultations",
        "Surgeries and procedures",
        "Occupancy",
        "Average revenue per occupied bed",
        "Case mix and specialty mix",
        "Diagnostics",
        "Pharmacy sales and distribution",
        "Digital healthcare services",
        "Medical tourism",
        "New hospital capacity",
        "Hospital expansion and managed facilities",
    ],

    cost_drivers=[
        "Medical consumables",
        "Pharmaceutical procurement",
        "Medical devices and equipment",
        "Employee and clinician costs",
        "Electricity and utilities",
        "Hospital infrastructure maintenance",
        "Technology and digital-platform costs",
        "Property and facility costs",
        "Financing costs",
        "Expansion capital expenditure",
    ],

    demand_drivers=[
        "Population health needs",
        "Ageing population",
        "Chronic diseases",
        "Acute and emergency care demand",
        "Specialised and complex procedures",
        "Health awareness",
        "Insurance penetration",
        "Household healthcare spending",
        "Corporate healthcare demand",
        "Medical tourism",
        "Healthcare infrastructure demand",
    ],

    supply_chain_links=[
        "Pharmaceutical manufacturers and distributors",
        "Medical-device manufacturers",
        "Diagnostic equipment suppliers",
        "Medical consumables suppliers",
        "Healthcare professionals",
        "Insurance companies and TPAs",
        "Laboratories and diagnostic networks",
        "Technology providers",
        "Hospital infrastructure vendors",
        "Utilities and electricity providers",
    ],

    sector_links=[
        "Hospitals",
        "Healthcare services",
        "Diagnostics",
        "Retail pharmacy",
        "Digital health",
        "Medical technology",
        "Healthcare infrastructure",
        "Medical tourism",
    ],

    markets={

        "NIFTY 50": MarketCharacter(
            market="NIFTY 50",
            character=(
                "Broad Indian equity-market environment affecting liquidity, "
                "risk appetite, valuation multiples and institutional flows."
            ),
            exposure_character="Primary systematic-market relationship",
            impact_path=(
                "NIFTY movement → market sentiment / liquidity / valuation "
                "→ healthcare-stock valuation and APOLLOHOSP behaviour"
            ),
            calculation_logic=(
                "Calculate return correlation, beta, rolling beta, relative "
                "strength, downside sensitivity and lag response. Separate "
                "systematic market movement from healthcare/company-specific news."
            ),
        ),

        "Crude Oil": MarketCharacter(
            market="Crude Oil",
            character=(
                "Global energy commodity affecting transport, inflation, "
                "fuel costs and the broader macroeconomic environment."
            ),
            exposure_character=(
                "Indirect macro + operating-cost relationship"
            ),
            impact_path=(
                "Crude movement → inflation / transport / energy costs and "
                "household purchasing power → healthcare cost and demand "
                "environment → APOLLOHOSP"
            ),
            calculation_logic=(
                "Test crude returns against APOLLOHOSP returns, margins and "
                "healthcare-sector variables. Use lagged effects and control "
                "for NIFTY and inflation where data is available. Do not treat "
                "crude as a direct healthcare revenue driver."
            ),
        ),

        "Gold": MarketCharacter(
            market="Gold",
            character=(
                "Precious-metal and macro-risk asset that can reflect risk "
                "aversion, currency conditions, liquidity and uncertainty."
            ),
            exposure_character="Indirect macro / risk-sentiment relationship",
            impact_path=(
                "Gold movement → risk sentiment / currency / liquidity "
                "→ valuation environment → APOLLOHOSP"
            ),
            calculation_logic=(
                "Measure incremental explanatory power after controlling for "
                "NIFTY, currency, rates and broader risk indicators. Use rolling "
                "and lagged analysis rather than assuming direct healthcare exposure."
            ),
        ),

        "Silver": MarketCharacter(
            market="Silver",
            character=(
                "Precious and industrial metal whose movement may contain "
                "information about industrial activity, inflation and commodity risk."
            ),
            exposure_character="Indirect macro / industrial-cycle relationship",
            impact_path=(
                "Silver movement → commodity/inflation cycle and risk sentiment "
                "→ macroeconomic conditions → healthcare valuation/demand → stock"
            ),
            calculation_logic=(
                "Test return, rolling correlation, lag and volatility relationships "
                "after controlling for NIFTY, gold and macro variables. Avoid "
                "assuming a direct silver-to-hospital operating relationship."
            ),
        ),

        "Natural Gas": MarketCharacter(
            market="Natural Gas",
            character=(
                "Energy commodity linked to power generation, industrial energy "
                "costs and broader inflationary conditions."
            ),
            exposure_character="Indirect energy-cost / macro relationship",
            impact_path=(
                "Natural gas movement → energy costs / inflation → hospital "
                "utility economics and macro demand conditions → APOLLOHOSP"
            ),
            calculation_logic=(
                "Measure lagged and contemporaneous relationships with stock "
                "returns and operating margins where reliable data exists. "
                "Separate direct utility-cost effects from broad energy sentiment."
            ),
        ),

        "Copper": MarketCharacter(
            market="Copper",
            character=(
                "Industrial metal associated with construction, electrical "
                "equipment, infrastructure and global economic activity."
            ),
            exposure_character="Indirect healthcare-capex / industrial-cycle relationship",
            impact_path=(
                "Copper cycle → construction/equipment/infrastructure costs "
                "and economic activity → hospital expansion economics / macro "
                "conditions → APOLLOHOSP"
            ),
            calculation_logic=(
                "Test copper returns against APOLLOHOSP returns, capex-sensitive "
                "periods and healthcare-sector activity. Use lagged analysis and "
                "control for NIFTY; do not assume direct copper exposure."
            ),
        ),

        "Aluminium": MarketCharacter(
            market="Aluminium",
            character=(
                "Industrial metal used across construction, transportation, "
                "equipment and infrastructure supply chains."
            ),
            exposure_character="Indirect infrastructure / equipment-cost relationship",
            impact_path=(
                "Aluminium cycle → construction/equipment/material costs "
                "→ hospital expansion and infrastructure economics → stock"
            ),
            calculation_logic=(
                "Measure historical return, rolling correlation, lag effects and "
                "interaction with capital-expenditure periods. Control for NIFTY "
                "and distinguish capex effects from general commodity sentiment."
            ),
        ),

        "Zinc": MarketCharacter(
            market="Zinc",
            character=(
                "Industrial metal associated with galvanising, construction, "
                "infrastructure and manufacturing activity."
            ),
            exposure_character="Indirect construction / infrastructure relationship",
            impact_path=(
                "Zinc cycle → construction/infrastructure activity and material "
                "costs → healthcare infrastructure expansion environment → stock"
            ),
            calculation_logic=(
                "Test historical and lagged relationships, particularly around "
                "hospital construction and expansion cycles. Control for NIFTY "
                "and related industrial metals. Do not assume direct zinc exposure."
            ),
        ),

        "Electricity": MarketCharacter(
            market="Electricity",
            character=(
                "Important operating input for hospitals, diagnostics, "
                "medical equipment, refrigeration, data systems and continuous "
                "healthcare operations."
            ),
            exposure_character="Direct operational energy-cost relationship",
            impact_path=(
                "Electricity price/availability → hospital and diagnostic "
                "operating costs + continuity of operations → margins/cash flow "
                "→ APOLLOHOSP"
            ),
            calculation_logic=(
                "Where reliable regional electricity data exists, measure price, "
                "volatility, availability and outage-event relationships against "
                "operating margins and stock behaviour. Account for geography "
                "because Apollo operates across multiple locations."
            ),
        ),
    },

    important_indicators=[
        "Hospital occupancy",
        "Operational beds",
        "Average revenue per occupied bed",
        "Patient volumes",
        "Inpatient and outpatient volumes",
        "Case mix",
        "Procedure volumes",
        "ARPOB",
        "Hospital EBITDA margin",
        "Pharmacy revenue",
        "Diagnostics revenue",
        "Digital healthcare activity",
        "New bed additions",
        "Hospital capacity utilisation",
        "Medical tourism activity",
        "Revenue growth",
        "EBITDA growth",
        "Free cash flow",
        "Capital expenditure",
        "Net debt and financing costs",
        "NIFTY 50 return",
        "Healthcare-sector performance",
        "Crude Oil return",
        "Gold return",
        "Silver return",
        "Natural Gas return",
        "Copper return",
        "Aluminium return",
        "Zinc return",
        "Electricity price/availability",
        "Trading volume",
        "Relative volume",
        "Volatility",
        "Relative strength",
    ],

    important_events=[
        "Quarterly results",
        "Annual results",
        "Annual report disclosures",
        "Hospital expansion announcements",
        "New hospital openings",
        "New beds / capacity additions",
        "Major medical-specialty launches",
        "Major technology or digital-health developments",
        "Pharmacy business developments",
        "Diagnostics expansion",
        "Acquisitions and strategic transactions",
        "Partnerships and joint ventures",
        "Regulatory healthcare changes",
        "Insurance and reimbursement-policy changes",
        "Drug and medical-device regulatory changes",
        "Major healthcare-sector policy changes",
        "Doctor / specialist recruitment developments",
        "Credit-rating or financing changes",
        "Large capex announcements",
        "Cybersecurity or digital-platform events",
        "Public-health emergencies",
        "Medical-tourism policy changes",
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
        "Do not use the supplied historical rank, percentage change or linkage score as permanent company characteristics.",
        "Treat the supplied linkage values only as an old snapshot, not as ground truth.",
        "Calculate market relationships from actual historical observations.",
        "Control NIFTY 50 when testing individual commodity relationships.",
        "Separate operating-cost effects from macroeconomic effects.",
        "Use lagged variables because commodity and macro effects may reach healthcare businesses with delay.",
        "Use rolling windows to detect whether relationships are stable or regime-dependent.",
        "Use event studies around company-specific healthcare announcements.",
        "Use volume confirmation for stock-price reactions.",
        "Use sector-relative performance to distinguish healthcare-specific movement from the broad market.",
        "Account for regional electricity and operating conditions because hospital assets are geographically distributed.",
        "Do not infer causation from correlation alone.",
        "Use real filings, results, operating metrics and market data as evidence.",
        "Do not make the final BUY/SELL decision inside this character module.",
        "Pass evidence to the central research/decision layer.",
    ],
)


def get_company_character() -> CompanyCharacter:
    """Return the complete APOLLOHOSP company character."""
    return APOLLOHOSP_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one supported market character."""
    key = market.strip()

    if key not in APOLLOHOSP_CHARACTER.markets:
        raise KeyError(
            f"Unsupported market '{market}'. "
            f"Supported markets: {', '.join(APOLLOHOSP_CHARACTER.markets)}"
        )

    return APOLLOHOSP_CHARACTER.markets[key]


def get_all_markets() -> Dict[str, MarketCharacter]:
    """Return all 9 market characters."""
    return dict(APOLLOHOSP_CHARACTER.markets)


def get_company_summary() -> dict:
    """Return a compact machine-readable company summary."""
    return {
        "symbol": APOLLOHOSP_CHARACTER.symbol,
        "company_name": APOLLOHOSP_CHARACTER.company_name,
        "company_character": APOLLOHOSP_CHARACTER.company_character,
        "primary_businesses": list(APOLLOHOSP_CHARACTER.primary_businesses),
        "sector_links": list(APOLLOHOSP_CHARACTER.sector_links),
        "market_count": len(APOLLOHOSP_CHARACTER.markets),
        "markets": list(APOLLOHOSP_CHARACTER.markets.keys()),
    }


def validate_character() -> bool:
    """Validate the 9-market structure."""
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

    actual_markets = set(APOLLOHOSP_CHARACTER.markets.keys())

    if actual_markets != expected_markets:
        raise ValueError(
            f"Market character validation failed. "
            f"Missing={sorted(expected_markets - actual_markets)}, "
            f"Extra={sorted(actual_markets - expected_markets)}"
        )

    if APOLLOHOSP_CHARACTER.symbol != "APOLLOHOSP":
        raise ValueError("Invalid company symbol.")

    for market_name, market in APOLLOHOSP_CHARACTER.markets.items():
        if not all([
            market.market,
            market.character,
            market.exposure_character,
            market.impact_path,
            market.calculation_logic,
        ]):
            raise ValueError(
                f"Incomplete market character definition: {market_name}"
            )

    return True


if __name__ == "__main__":
    validate_character()
    print("APOLLOHOSP Character: VALID")
    print(f"Company: {APOLLOHOSP_CHARACTER.company_name}")
    print(f"Markets: {len(APOLLOHOSP_CHARACTER.markets)}")
    for name, market in APOLLOHOSP_CHARACTER.markets.items():
        print(f"- {name}: {market.exposure_character}")
