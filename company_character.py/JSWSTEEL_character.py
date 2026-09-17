"""
JSWSTEEL — Company Character & 9-Market Relationship Definition.

This file defines the real business character of JSW Steel and the research
logic for the nine tracked markets. The supplied snapshot fields
RANK/PCT_CHANGE/LINKAGE_SCORE/RELATION are not hard-coded as permanent truth.

JSW Steel is an integrated steel producer with iron-ore and coking-coal
linkages, steelmaking, downstream/value-added products, captive/renewable
power, logistics, and large expansion/decarbonisation programs. The character
therefore treats electricity and steelmaking raw materials as core operating
drivers and the other tracked markets according to their actual transmission
paths.
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
        "Indian equity-market, liquidity and domestic growth regime.",
        "Direct equity valuation and market-beta exposure.",
        "NIFTY -> risk appetite/liquidity/growth expectations -> steel-sector valuation -> JSWSTEEL.",
        "Calculate JSWSTEEL excess return, rolling beta/correlation, volatility response and event-window returns versus NIFTY; separate market beta from steel-specific evidence.",
        ("JSWSTEEL return", "NIFTY return", "rolling beta", "rolling correlation",
         "India VIX", "JSWSTEEL volume", "FII/DII flows", "metal-sector index"),
        ("RBI policy", "Union Budget", "infrastructure policy",
         "steel-policy changes", "JSWSTEEL results", "major capex announcements"),
        ("intraday", "1D", "1W", "1M", "3M", "6M", "1Y"),
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Global energy, freight and inflation-cycle benchmark.",
        "Indirect-to-material cost exposure through fuel, logistics, petrochemical inputs and global inflation.",
        "Crude -> freight/fuel/input costs -> steel conversion/logistics cost; crude -> inflation/growth -> steel demand and spreads -> JSWSTEEL.",
        "Use crude with coking coal, iron ore, freight, steel prices and FX. Test lagged effects on EBITDA/tonne, conversion cost, margins and stock returns; do not treat crude as a direct steel price proxy.",
        ("Brent", "WTI", "freight rates", "diesel/fuel cost",
         "steel price", "EBITDA/tonne", "conversion cost", "USD/INR"),
        ("OPEC+ decisions", "geopolitical disruptions", "freight shocks",
         "energy-price shocks", "global demand shocks"),
        ("1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Gold": _mc(
        "Gold",
        "Precious-metal safe-haven, real-rate and global risk-sentiment market.",
        "Indirect macro exposure; gold is not a core steelmaking input.",
        "Gold -> real rates/risk sentiment/inflation -> investment activity and equity valuation -> JSWSTEEL.",
        "Test gold against JSWSTEEL after controlling for NIFTY, steel prices, rates, crude and FX. Use event studies for major risk-off episodes.",
        ("gold return", "INR gold", "real yields", "India VIX",
         "steel price", "NIFTY return", "JSWSTEEL return"),
        ("geopolitical shocks", "central-bank decisions",
         "inflation surprises", "risk-off events"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Silver": _mc(
        "Silver",
        "Precious/industrial-metal and global manufacturing-cycle signal.",
        "Indirect macro exposure through industrial activity and investor sentiment.",
        "Silver -> industrial cycle/inflation sentiment -> manufacturing/infrastructure demand -> steel demand -> JSWSTEEL.",
        "Measure incremental explanatory value after controlling for copper, aluminium, steel prices, NIFTY and global PMI.",
        ("silver return", "gold/silver ratio", "industrial-metals index",
         "global PMI", "steel price", "JSWSTEEL return"),
        ("industrial-cycle shocks", "inflation releases",
         "geopolitical events", "global manufacturing changes"),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),

    "Natural Gas": _mc(
        "Natural Gas",
        "Energy and industrial-input market with direct relevance to steelmaking transition.",
        "Material but variable exposure through gas-based processes, energy and planned green/transition steel projects.",
        "Natural gas -> steelmaking energy/fuel economics -> conversion cost/margins; gas -> industrial activity -> steel demand -> JSWSTEEL.",
        "Use plant/geography-specific gas prices where available. Test lagged gas impact against energy cost, EBITDA/tonne and production economics while controlling for electricity and coal.",
        ("gas benchmark", "regional gas price", "energy cost/tonne",
         "steel production", "EBITDA/tonne", "capacity utilisation"),
        ("gas supply disruption", "gas-price shocks",
         "green-steel project milestones", "energy-policy changes"),
        ("1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Copper": _mc(
        "Copper",
        "Global industrial, electrification and infrastructure-cycle metal.",
        "Indirect demand and downstream product exposure.",
        "Copper -> electrification/equipment/infrastructure capex -> steel demand, especially electrical/engineering grades -> JSWSTEEL.",
        "Use copper as an industrial-cycle factor and compare it with JSW's electrical-steel/engineering demand. Control for global PMI, steel prices and NIFTY.",
        ("LME copper", "global PMI", "India PMI", "electrical-equipment capex",
         "electrical steel demand", "steel price", "JSWSTEEL return"),
        ("China/global PMI shocks", "infrastructure stimulus",
         "copper supply disruptions", "electrification capex"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Aluminium": _mc(
        "Aluminium",
        "Industrial metal competing/complementing steel in transport, packaging and engineering.",
        "Indirect demand/cross-material exposure rather than a primary JSWSTEEL input.",
        "Aluminium -> auto/engineering/construction cycle -> steel demand and product substitution -> JSWSTEEL.",
        "Test aluminium against JSWSTEEL with steel prices, PMI, auto production and NIFTY controls. Separately study substitution in auto/lightweighting applications.",
        ("LME aluminium", "aluminium premium", "auto production",
         "engineering PMI", "steel price", "VASP mix", "JSWSTEEL return"),
        ("aluminium supply shocks", "auto-cycle changes",
         "industrial capex", "material-substitution events"),
        ("1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Zinc": _mc(
        "Zinc",
        "Industrial metal strongly connected to galvanising and steel downstream demand.",
        "High strategic relevance through galvanized/galvalume/zinc-coated steel products; zinc is also an upstream coating cost signal.",
        "Zinc -> galvanising/coating cost -> downstream steel margins; zinc -> construction/auto/infrastructure cycle -> coated-steel demand -> JSWSTEEL.",
        "Track zinc price/premium together with coated-steel realisations, coating spreads, sales mix and margins. Test lagged and partial relationships controlling for steel prices and demand.",
        ("LME zinc", "zinc premium", "galvanized steel realisation",
         "coating cost", "coated-steel volume", "VASP share", "EBITDA/tonne"),
        ("zinc supply disruptions", "galvanising demand",
         "auto/infrastructure cycle", "coated-steel capacity additions"),
        ("intraday", "1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),

    "Electricity": _mc(
        "Electricity",
        "Core steelmaking energy and operating-cost market.",
        "Direct and high-relevance operating exposure, partly mitigated by captive/renewable power and waste-gas/waste-heat recovery.",
        "Electricity -> EAF/steelmaking/rolling power cost -> conversion cost -> EBITDA/tonne and margins -> JSWSTEEL.",
        "Use plant/geography-specific industrial power prices, captive generation, renewable share and energy consumption per tonne. Calculate energy cost/tonne and lagged margin impact rather than using a generic electricity series alone.",
        ("industrial power tariff", "captive generation",
         "renewable capacity", "energy consumption/tonne",
         "power cost/tonne", "conversion cost", "EBITDA/tonne"),
        ("tariff changes", "power shortages", "renewable commissioning",
         "captive-power changes", "extreme weather"),
        ("intraday", "1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="JSWSTEEL",
    company_name="JSW Steel Limited",
    sector="Steel / Metals & Mining",
    industry_character=(
        "Integrated steel producer with iron-ore resources, coking-coal security, "
        "steelmaking, downstream/value-added products, captive and renewable power, "
        "logistics and global operations."
    ),
    business_character=(
        "Highly integrated, capital-intensive steel business whose economics are "
        "driven by steel realisations and spreads versus iron ore, coking coal, "
        "energy and logistics costs. Capacity utilisation, raw-material security, "
        "product mix, domestic/international steel cycles, electricity, freight, "
        "FX, capex and deleveraging interact. The company also has a strong "
        "downstream/value-added character including automotive, electrical steel, "
        "coated products, construction and engineering applications."
    ),
    demand_drivers=(
        "Indian infrastructure spending",
        "Construction activity",
        "Automobile production",
        "Engineering and manufacturing",
        "Renewable-energy buildout",
        "Power-sector investment",
        "Capital goods cycle",
        "Housing and urbanisation",
        "Global steel demand",
        "Export demand",
        "Industrial production",
        "Government infrastructure capex",
        "Value-added steel demand",
        "Electrical-steel demand",
    ),
    revenue_drivers=(
        "Crude steel production",
        "Saleable steel volumes",
        "Steel realisations",
        "Hot-rolled products",
        "Cold-rolled products",
        "Galvanized/galvalume products",
        "Automotive steel",
        "Electrical steel",
        "Specialty/value-added steel",
        "Domestic sales",
        "Export sales",
        "Product mix",
        "Capacity utilisation",
        "Branded retail steel",
        "JSW One/steel distribution ecosystem",
    ),
    cost_drivers=(
        "Iron ore",
        "Coking coal",
        "PCI coal",
        "Electricity",
        "Natural gas",
        "Fuel",
        "Limestone and fluxes",
        "Scrap",
        "Freight and logistics",
        "Rail/port costs",
        "Consumables",
        "Electrode/refractory costs",
        "Employee costs",
        "Maintenance",
        "Interest expense",
        "Foreign exchange",
        "Carbon/decarbonisation capex",
    ),
    supply_chain_character=(
        "Captive iron-ore mines",
        "Domestic iron-ore suppliers",
        "Coking-coal mines and linkages",
        "Overseas metallurgical coal",
        "Ports and shipping",
        "Rail and slurry-pipeline logistics",
        "Power and captive generation",
        "Renewable-energy suppliers",
        "Steelmaking equipment",
        "Refractories and electrodes",
        "Automotive OEMs",
        "Construction/infrastructure customers",
        "Engineering and electrical-equipment customers",
        "Distributors and retail network",
    ),
    strategic_drivers=(
        "Capacity expansion",
        "50 MTPA India capacity ambition",
        "Value-added product mix",
        "Raw-material security",
        "Coking-coal diversification",
        "Captive iron-ore integration",
        "Downstream expansion",
        "Automotive steel",
        "Electrical steel",
        "Galvanized/coated products",
        "Renewable energy",
        "Green steel",
        "Hydrogen-based steelmaking",
        "Digital/AI-led operational optimisation",
        "Cost leadership",
        "Balance-sheet deleveraging",
    ),
    key_indicators=(
        "Crude steel production",
        "Saleable steel sales",
        "Capacity utilisation",
        "Steel realisation/tonne",
        "EBITDA/tonne",
        "EBITDA",
        "PAT",
        "EBITDA margin",
        "Iron ore consumption and captive share",
        "Coking coal cost",
        "Energy cost/tonne",
        "Conversion cost/tonne",
        "Domestic steel spreads",
        "Export volumes",
        "Value-added/value-added-specialty share",
        "Automotive steel volumes",
        "Electrical steel volumes",
        "Coated steel volumes",
        "Net debt",
        "Net debt/EBITDA",
        "Capex",
        "Free cash flow",
        "JSWSTEEL return and volatility",
    ),
    key_events=(
        "Quarterly/annual results",
        "Steel-price changes",
        "Domestic safeguard/anti-dumping duties",
        "Import/export policy",
        "Iron-ore mine developments",
        "Coking-coal supply events",
        "Coal/ore price shocks",
        "Capacity commissioning",
        "Dolvi/Vijayanagar/other expansion milestones",
        "Downstream product-line commissioning",
        "Electrical-steel projects",
        "Renewable-power commissioning",
        "Green-hydrogen projects",
        "Major capex approvals",
        "Global steel demand shocks",
        "China steel export changes",
        "Geopolitical/freight disruptions",
        "Material exchange filings",
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
    if COMPANY_CHARACTER.symbol != "JSWSTEEL":
        return False
    if set(MARKET_CHARACTERS) != set(TRACKED_MARKETS):
        return False
    for market in TRACKED_MARKETS:
        mc = MARKET_CHARACTERS[market]
        if mc.market != market or not mc.character or not mc.exposure_character:
            return False
        if not mc.impact_path or not mc.calculation_logic:
            return False
        if not mc.relevant_indicators or not mc.expected_timeframes:
            return False
    return True


if __name__ == "__main__":
    print("JSWSTEEL character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
