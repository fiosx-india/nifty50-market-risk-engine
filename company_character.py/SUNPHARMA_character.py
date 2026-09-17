"""
SUNPHARMA Character Model
=========================
Research character definition for Sun Pharmaceutical Industries Limited.

Purpose
-------
This file defines the BUSINESS CHARACTER of SUNPHARMA and its relationship
character with the nine tracked markets.

Important:
- This file does NOT hard-code rank, price change, correlation, beta,
  linkage score, probability, or trading relation.
- Historical impact must be calculated later from real market/company data.
- The market character describes WHAT should be measured, not the result.
- Direct, cost-side, macro, FX, regulatory, supply-chain and demand channels
  are kept conceptually separate so the later calculation engine can test them.

Primary business character reflected here:
- India branded/generic pharmaceuticals
- US pharmaceuticals, including specialty and generics
- Emerging Markets
- Rest of World
- Global Specialty
- APIs and vertically integrated manufacturing
- Global Consumer Healthcare
- R&D, regulatory, manufacturing quality/compliance and product launches
- Acquisitions / business development
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
    business_segments: Tuple[str, ...]
    revenue_geographies: Tuple[str, ...]
    value_chain: Tuple[str, ...]
    demand_drivers: Tuple[str, ...]
    revenue_drivers: Tuple[str, ...]
    cost_drivers: Tuple[str, ...]
    supply_chain_dependencies: Tuple[str, ...]
    strategic_drivers: Tuple[str, ...]
    operational_risks: Tuple[str, ...]
    regulatory_risks: Tuple[str, ...]
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
    symbol="SUNPHARMA",
    company_name="Sun Pharmaceutical Industries Limited",
    primary_identity=(
        "Global pharmaceutical company with a diversified portfolio spanning "
        "India, the United States, Emerging Markets and Rest of World, with "
        "strong specialty, generics, API, consumer-health and vertically "
        "integrated manufacturing capabilities."
    ),
    business_segments=(
        "India Pharmaceuticals",
        "United States Pharmaceuticals",
        "Emerging Markets Pharmaceuticals",
        "Rest of World Pharmaceuticals",
        "Global Specialty",
        "Generics",
        "Specialty Pharmaceuticals",
        "Active Pharmaceutical Ingredients (API)",
        "Global Consumer Healthcare",
        "Complex and difficult-to-manufacture products",
        "Research and Development",
        "Business development and acquisitions",
    ),
    revenue_geographies=(
        "India",
        "United States",
        "Emerging Markets",
        "Rest of World",
    ),
    value_chain=(
        "Discovery and product selection",
        "Research and development",
        "Clinical and regulatory development",
        "API sourcing and manufacturing",
        "Drug-substance and formulation manufacturing",
        "Quality control and compliance",
        "Packaging",
        "Regulatory approvals",
        "Distribution",
        "Hospital / institutional channels",
        "Retail pharmacy channels",
        "Specialty distribution",
        "Digital and field-force engagement",
        "Consumer healthcare distribution",
    ),
    demand_drivers=(
        "Prescription volumes",
        "Therapy-area demand",
        "Chronic disease prevalence",
        "Specialty-drug adoption",
        "New product launches",
        "Market-share gains",
        "Doctor prescriptions",
        "Patient access and affordability",
        "India healthcare consumption",
        "US specialty demand",
        "Generic volume demand",
        "Emerging-market healthcare demand",
        "Consumer-health demand",
    ),
    revenue_drivers=(
        "India formulation volumes",
        "US specialty sales",
        "US generic sales",
        "Emerging-market sales",
        "Rest-of-World sales",
        "Global Specialty product performance",
        "New product launches",
        "Price and volume mix",
        "Product approvals",
        "Market-share changes",
        "Productivity of sales and field force",
        "Business development and acquired products",
        "Currency translation",
    ),
    cost_drivers=(
        "API and key raw-material costs",
        "Solvents and intermediates",
        "Packaging materials",
        "Manufacturing utilities",
        "Electricity",
        "Natural gas and other process energy",
        "Fuel and freight",
        "Quality and compliance costs",
        "R&D expenditure",
        "Clinical development expenditure",
        "Regulatory costs",
        "Sales and marketing expenditure",
        "Field-force expansion",
        "Capacity expansion",
        "Acquisition and integration costs",
    ),
    supply_chain_dependencies=(
        "API and intermediate suppliers",
        "Internal API manufacturing",
        "Chemical and pharmaceutical raw materials",
        "Packaging suppliers",
        "Manufacturing plants",
        "Cold-chain / temperature-sensitive logistics where applicable",
        "Specialty distribution channels",
        "Wholesale and pharmacy networks",
        "International logistics",
        "Regulatory release and quality systems",
        "Energy and utility availability",
    ),
    strategic_drivers=(
        "Increase specialty contribution",
        "Build differentiated and difficult-to-manufacture products",
        "Maintain India market leadership",
        "Expand international scale",
        "Grow specialty pipeline",
        "Use acquisitions to fill capability gaps",
        "Improve operational cost efficiency",
        "Leverage vertical integration",
        "Expand consumer healthcare",
        "Strengthen R&D and innovation",
        "Improve return on invested capital",
    ),
    operational_risks=(
        "Manufacturing interruption",
        "Quality-system deficiencies",
        "Regulatory observations",
        "Product recalls",
        "Supply shortages",
        "API availability",
        "Pricing pressure",
        "Generic competition",
        "Specialty-product competition",
        "Product concentration",
        "Acquisition integration",
        "Foreign-exchange movement",
    ),
    regulatory_risks=(
        "US FDA inspections and observations",
        "Product approvals or delays",
        "ANDA / generic regulatory actions",
        "Specialty-drug regulatory requirements",
        "Pricing and reimbursement changes",
        "India pharmaceutical regulation",
        "International health-authority requirements",
        "Patent and litigation outcomes",
        "Compliance and manufacturing remediation",
    ),
    key_indicators=(
        "India sales growth",
        "US sales growth",
        "Emerging Markets sales growth",
        "Rest of World sales growth",
        "Global Specialty sales",
        "Specialty contribution",
        "Generic sales",
        "API / other sales",
        "New product launches",
        "Market share",
        "Prescription growth",
        "Volume growth",
        "Realisation / price-mix",
        "Gross margin",
        "EBITDA margin",
        "R&D expenditure",
        "R&D pipeline",
        "Regulatory approvals",
        "Regulatory observations",
        "Manufacturing utilisation",
        "Capacity additions",
        "Working capital",
        "Inventory days",
        "Receivable days",
        "Free cash flow",
        "Currency exposure",
    ),
    event_types=(
        "Quarterly results",
        "Annual results",
        "New product launch",
        "Drug approval",
        "US FDA inspection",
        "Regulatory warning or remediation",
        "Product recall",
        "Patent litigation",
        "Settlement or litigation resolution",
        "Acquisition",
        "Licensing agreement",
        "Business development",
        "Specialty pipeline update",
        "Clinical trial update",
        "Manufacturing expansion",
        "Capacity expansion",
        "Plant shutdown or restart",
        "Supply disruption",
        "Major pricing change",
        "Credit-rating change",
        "Management guidance",
        "Capital allocation update",
    ),
    market_characters={},
)


MARKET_CHARACTERS: Dict[str, MarketCharacter] = {
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Direct equity-market and macro exposure",
        (
            "Market beta",
            "Pharmaceutical-sector sentiment",
            "Indian equity valuation",
            "Risk appetite",
            "Healthcare defensive characteristics",
        ),
        (
            "Equity-market access",
            "Institutional ownership and flows",
            "Domestic healthcare investment cycle",
        ),
        (
            "Indian economic activity",
            "Household healthcare spending",
            "Healthcare utilisation",
        ),
        (
            "Indirect financing and capital-market effects",
            "Valuation multiple sensitivity",
        ),
        (
            "Indian growth",
            "Interest rates",
            "Inflation",
            "Risk appetite",
        ),
        (
            "Rolling beta",
            "Rolling correlation",
            "Relative sector performance",
            "Volatility",
            "Market breadth",
            "Healthcare-sector relative strength",
        ),
        (
            "Earnings",
            "Guidance",
            "Regulatory events",
            "Major product launches",
            "M&A",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
        (
            "Do not treat NIFTY correlation as business causation.",
            "Separate broad market effect from pharmaceutical-specific events.",
            "Estimate rolling beta and residual return after market control.",
        ),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Primarily indirect cost, logistics and macro exposure",
        (
            "Fuel and freight cost",
            "Petrochemical input inflation",
            "Packaging-cost pressure",
            "Inflation",
            "Global economic activity",
        ),
        (
            "Transport and freight",
            "Packaging materials",
            "Petrochemical-derived chemicals and plastics",
            "Distribution logistics",
        ),
        (
            "Inflation-sensitive healthcare affordability",
            "Emerging-market consumption",
            "Economic activity",
        ),
        (
            "Freight",
            "Packaging",
            "Petrochemical-derived materials",
            "Manufacturing supply chain",
        ),
        (
            "Inflation",
            "Currency",
            "Interest rates",
            "Emerging-market demand",
        ),
        (
            "Crude return",
            "Freight proxy",
            "Input-cost indices",
            "Gross margin",
            "EBITDA margin",
            "Working capital",
        ),
        (
            "Sharp oil move",
            "Inflation surprise",
            "Major freight disruption",
            "Geopolitical supply shock",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Test cost channels separately from demand channels.",
            "Use lagged crude returns against margin and stock residual returns.",
            "Avoid assuming every crude move directly affects pharmaceutical demand.",
        ),
    ),
    "Gold": _mc(
        "Gold",
        "Primarily macro, risk, inflation and real-rate exposure",
        (
            "Risk sentiment",
            "Inflation expectations",
            "Real interest rates",
            "Defensive-sector flows",
            "Currency effects",
        ),
        (
            "No major direct physical gold input",
            "Indirect capital-market and macro channel",
        ),
        (
            "Household wealth",
            "Healthcare affordability",
            "Risk-off behaviour",
        ),
        (
            "Limited direct production-cost linkage",
            "Possible macro-driven funding effects",
        ),
        (
            "Real rates",
            "USD",
            "Inflation",
            "Risk aversion",
            "Global liquidity",
        ),
        (
            "Gold return",
            "Real yields",
            "USD index",
            "VIX/risk proxy",
            "Pharma-sector relative return",
        ),
        (
            "Large gold breakout",
            "Real-rate shock",
            "Global risk-off event",
            "Currency shock",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Treat gold primarily as a macro-state variable.",
            "Control for NIFTY and USD before testing residual relationships.",
            "Do not label gold as a direct pharmaceutical input.",
        ),
    ),
    "Silver": _mc(
        "Silver",
        "Primarily indirect industrial and macro exposure",
        (
            "Industrial-cycle signal",
            "Risk sentiment",
            "Commodity-cycle signal",
        ),
        (
            "No major direct silver input",
            "Indirect industrial supply-chain signal",
        ),
        (
            "Global industrial activity",
            "Healthcare demand via macro conditions",
        ),
        (
            "Limited direct manufacturing-cost linkage",
        ),
        (
            "Global growth",
            "Inflation",
            "Commodity sentiment",
            "Risk appetite",
        ),
        (
            "Silver return",
            "Industrial-metal basket",
            "Global PMI",
            "Pharma residual return",
        ),
        (
            "Industrial demand shock",
            "Commodity-cycle reversal",
            "Global growth surprise",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Use silver mainly as an industrial/macro regime variable.",
            "Do not infer a direct input-cost relationship without procurement evidence.",
        ),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Indirect-to-moderate manufacturing energy and supply-chain exposure",
        (
            "Manufacturing energy cost",
            "Process-heat cost",
            "Chemical-input cost",
            "Utility inflation",
        ),
        (
            "Pharmaceutical manufacturing",
            "Chemical intermediates",
            "API production",
            "Packaging and industrial suppliers",
        ),
        (
            "Industrial activity",
            "Healthcare demand through macro conditions",
        ),
        (
            "Process energy",
            "Chemical intermediates",
            "Manufacturing utility costs",
        ),
        (
            "Industrial inflation",
            "Global energy prices",
            "Currency",
            "Power-market conditions",
        ),
        (
            "Natural-gas return",
            "Energy cost",
            "Manufacturing margin",
            "Utility expense",
            "EBITDA margin",
        ),
        (
            "Gas price spike",
            "Energy-supply disruption",
            "Industrial utility-cost shock",
        ),
        ("1D", "1W", "1M", "3M", "6M"),
        (
            "Where plant-level gas exposure is available, replace generic assumptions with actual consumption data.",
            "Measure lag between energy-price movement and reported margins.",
        ),
    ),
    "Copper": _mc(
        "Copper",
        "Indirect industrial, electrical-equipment and capex exposure",
        (
            "Electrical equipment cost",
            "Plant maintenance/capex cost",
            "Industrial-cycle signal",
        ),
        (
            "Electrical systems",
            "Manufacturing equipment",
            "Plant construction",
            "Utility infrastructure",
        ),
        (
            "Industrial and healthcare capex",
            "Global manufacturing activity",
        ),
        (
            "Electrical equipment",
            "Engineering and construction inputs",
        ),
        (
            "Global industrial cycle",
            "Infrastructure investment",
            "Commodity inflation",
        ),
        (
            "Copper return",
            "Capex",
            "PP&E additions",
            "Utility/equipment costs",
            "Margin",
        ),
        (
            "Copper shock",
            "Capex cycle change",
            "Industrial slowdown",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Treat copper as a secondary industrial-cost/capex variable.",
            "Use procurement and capex disclosures to validate economic linkage.",
        ),
    ),
    "Aluminium": _mc(
        "Aluminium",
        "Indirect manufacturing, packaging and capex exposure",
        (
            "Packaging-material cost",
            "Manufacturing equipment cost",
            "Construction/capex cost",
            "Industrial-cycle signal",
        ),
        (
            "Packaging",
            "Plant equipment",
            "Construction",
            "Logistics equipment",
        ),
        (
            "Consumer-health demand",
            "Industrial activity",
            "Healthcare investment",
        ),
        (
            "Packaging",
            "Equipment",
            "Construction materials",
        ),
        (
            "Commodity inflation",
            "Industrial growth",
            "Global manufacturing cycle",
        ),
        (
            "Aluminium return",
            "Packaging cost",
            "Capex",
            "Gross margin",
            "Inventory value",
        ),
        (
            "Aluminium price shock",
            "Packaging-cost event",
            "Industrial-cycle reversal",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Separate packaging exposure from broader commodity-cycle effects.",
            "Use company disclosures to determine materiality before assigning a measurable coefficient.",
        ),
    ),
    "Zinc": _mc(
        "Zinc",
        "Indirect industrial, construction and equipment-cost exposure",
        (
            "Galvanised steel cost",
            "Plant and infrastructure capex",
            "Industrial-cycle signal",
        ),
        (
            "Galvanised steel",
            "Plant structures",
            "Utilities infrastructure",
            "Equipment",
        ),
        (
            "Industrial healthcare investment",
            "Construction activity",
            "Macro growth",
        ),
        (
            "Plant construction",
            "Equipment",
            "Infrastructure",
        ),
        (
            "Industrial growth",
            "Construction cycle",
            "Commodity inflation",
        ),
        (
            "Zinc return",
            "Industrial PMI",
            "Capex",
            "PP&E additions",
            "Margin",
        ),
        (
            "Zinc shock",
            "Construction slowdown",
            "Industrial supply shock",
        ),
        ("1W", "1M", "3M", "6M", "1Y"),
        (
            "Zinc is not treated as a primary pharmaceutical raw material.",
            "Test the relationship mainly through construction, equipment and industrial-cycle channels.",
        ),
    ),
    "Electricity": _mc(
        "Electricity",
        "Meaningful manufacturing operating-cost and uptime exposure",
        (
            "Plant operating cost",
            "Process energy",
            "Cold-chain / storage where applicable",
            "Manufacturing uptime",
            "Data and laboratory infrastructure",
        ),
        (
            "Manufacturing plants",
            "API facilities",
            "Formulation facilities",
            "Laboratories",
            "Warehousing",
            "Cold storage where applicable",
        ),
        (
            "Production capacity",
            "Supply reliability",
            "Product availability",
        ),
        (
            "Electricity consumption",
            "Process equipment",
            "HVAC",
            "Clean-room systems",
            "Laboratories",
            "Warehousing",
        ),
        (
            "Industrial power prices",
            "Grid reliability",
            "Renewable-power availability",
            "Regional electricity conditions",
        ),
        (
            "Electricity price",
            "Power consumption",
            "Utility expense",
            "Manufacturing utilisation",
            "Gross margin",
            "EBITDA margin",
            "Plant uptime",
        ),
        (
            "Power-price spike",
            "Grid disruption",
            "Plant outage",
            "Utility contract change",
        ),
        ("Intraday", "1D", "1W", "1M", "3M", "6M"),
        (
            "Where plant-level electricity data exists, calculate actual intensity and cost sensitivity.",
            "Measure whether utility shocks affect margins with reporting-period lags.",
            "Separate electricity price effects from production-volume effects.",
        ),
    ),
}


# Attach the nine market characters to the company character.
COMPANY_CHARACTER = CompanyCharacter(
    **{
        **COMPANY_CHARACTER.__dict__,
        "market_characters": MARKET_CHARACTERS,
    }
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Sun Pharma business character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return the character definition for one of the nine tracked markets."""
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
    """
    Structural validation only.

    This deliberately does NOT validate any historical score or market impact.
    Those values must come from the future calculation engine and real data.
    """
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
    print("SUNPHARMA character validation:", result)

    for market in TRACKED_MARKETS:
        character = get_market_character(market)
        print(
            f"{market}: "
            f"{character.exposure_type} | "
            f"{len(character.indicators_to_measure)} indicators | "
            f"{len(character.event_signals)} event groups"
        )
