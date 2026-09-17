"""
HINDALCO — Company Character & 9-Market Research Model

This module defines Hindalco's actual business character and the research
logic for its exposure to the project's 9 tracked markets.

The supplied CSV may contain rank, daily change and linkage values, but those
values are intentionally NOT hard-coded here. Historical linkage is to be
calculated later from real market, company, segment, event and macro data.

No fixed linkage scores, ranks, percentage changes or trading decisions are
stored in this character file.
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
    "Aluminium": _mc(
        "Aluminium",
        "Core operating commodity and downstream value-chain signal.",
        "Direct and structurally central exposure. Hindalco is integrated across "
        "bauxite mining, alumina refining, smelting, rolling, extrusion, foil, "
        "recycling and value-added aluminium products, with Novelis extending the "
        "downstream global platform.",
        "Aluminium price/premiums + alumina/bauxite costs + energy + production "
        "volume -> metal realisations and conversion margins -> upstream/downstream "
        "EBITDA -> consolidated earnings and cash flow.",
        "Do not use a simple price correlation. Calculate LME/SHFE/Indian aluminium "
        "returns, realised price, alumina and energy inputs, production/sales volume, "
        "rolling spreads and segment EBITDA. Estimate rolling beta, lagged response, "
        "margin sensitivity and event-study effects. Separate upstream, downstream "
        "and recycling economics.",
        (
            "LME aluminium price",
            "aluminium premium",
            "alumina price",
            "bauxite cost",
            "production volume",
            "realisation per tonne",
            "EBITDA per tonne",
            "Novelis recycling margin",
        ),
        (
            "aluminium price shocks",
            "LME inventory changes",
            "smelter outages",
            "bauxite/alumina disruptions",
            "major capacity additions",
            "trade tariffs and sanctions",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),
    "Copper": _mc(
        "Copper",
        "Core operating metal plus electrification and downstream-growth signal.",
        "Direct exposure through Birla Copper: cathodes, rods, wires, tubes and "
        "specialty alloys. Demand is linked to electrification, railways, power, "
        "EVs, renewables, consumer durables and industrial infrastructure.",
        "Copper price/treatment economics + concentrate availability + energy -> "
        "smelter economics -> cathode/rod/tube volumes and margins -> copper EBITDA. "
        "Separately, electrification demand -> higher downstream volumes and capacity "
        "utilisation -> growth.",
        "Track LME copper, treatment/refining charges where available, copper "
        "production/sales, realised price, downstream mix, capacity utilisation and "
        "segment EBITDA. Use lagged models and event studies. Separate price beta "
        "from volume/demand growth and expansion effects.",
        (
            "LME copper price",
            "copper TC/RC",
            "copper cathode/rod volume",
            "realisation",
            "downstream product mix",
            "EBITDA per tonne",
            "capacity utilisation",
        ),
        (
            "copper supply disruptions",
            "smelter expansions",
            "electrification capex",
            "renewable/grid investment",
            "EV adoption",
            "copper recycling expansion",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q", "6M", "1Y"),
    ),
    "Crude Oil": _mc(
        "Crude Oil",
        "Energy, freight and input-cost sensitivity across a mining/manufacturing value chain.",
        "Indirect-to-material exposure through freight, fuel, petrochemical-linked "
        "inputs, packaging, mining operations and global inflation. Effects differ "
        "between upstream metal production and downstream customer demand.",
        "Crude -> fuel/freight and input costs -> production/conversion cost; crude -> "
        "global inflation/growth -> aluminium/copper demand -> realised prices and "
        "volumes -> earnings.",
        "Measure crude shocks against Hindalco's energy/freight costs, EBITDA per tonne, "
        "sales volume and margins. Use lagged regression with aluminium/copper prices, "
        "USD/INR and global industrial controls. Test asymmetric oil spikes versus "
        "declines.",
        (
            "Brent/WTI return",
            "oil volatility",
            "freight-cost proxy",
            "energy cost per tonne",
            "aluminium/copper prices",
            "EBITDA per tonne",
        ),
        (
            "OPEC+ decisions",
            "geopolitical supply shocks",
            "fuel-price shocks",
            "freight disruptions",
            "global recession/inflation shocks",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Electricity": _mc(
        "Electricity",
        "Critical direct operating input and structural cost-curve variable.",
        "Direct and high-importance exposure because aluminium smelting is electricity-"
        "intensive. Hindalco also has captive power and energy-security investments, "
        "so the relevant variable is net power cost and reliability, not merely a "
        "national electricity price.",
        "Power price/availability + captive generation -> smelting cost per tonne -> "
        "global cost-curve position -> EBITDA per tonne and production volume.",
        "Use plant-level or segment-level power cost wherever available. Compare "
        "power cost per tonne with aluminium realisation and EBITDA per tonne. Model "
        "outages separately from price changes and distinguish captive generation "
        "from grid exposure.",
        (
            "power cost per tonne",
            "captive power generation",
            "coal/fuel cost",
            "plant utilisation",
            "smelting cost per tonne",
            "EBITDA per tonne",
        ),
        (
            "power shortages",
            "captive-power expansion",
            "renewable PPAs/projects",
            "coal supply changes",
            "major plant outages",
            "electricity tariff changes",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q"),
    ),
    "Gold": _mc(
        "Gold",
        "Precious-metals by-product and macro precious-metals signal.",
        "Direct secondary exposure because Hindalco's copper operations recover "
        "precious metals including gold from copper concentrates. It is also an "
        "indirect macro/risk-sentiment variable.",
        "Gold recovery volume + gold price -> precious-metals by-product revenue/margin; "
        "gold -> safe-haven/risk sentiment -> USD, rates and broader metal-market "
        "conditions -> Hindalco valuation.",
        "Separate physical gold by-product economics from macro gold correlation. "
        "Track recovered gold volume, realised gold price and by-product contribution "
        "where disclosed. Test stock response to gold after controlling for copper, "
        "aluminium, USD/INR and NIFTY.",
        (
            "gold price",
            "gold recovery volume",
            "precious-metal realisation",
            "gold/copper relationship",
            "USD/INR",
            "Hindalco relative return",
        ),
        (
            "large gold-price moves",
            "geopolitical risk",
            "central-bank policy",
            "precious-metal demand changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "NIFTY 50": _mc(
        "NIFTY 50",
        "Systematic Indian-equity and industrial-cycle benchmark.",
        "Direct stock-market exposure through beta, liquidity and risk appetite; "
        "indirectly captures Indian infrastructure, industrial and investment-cycle "
        "conditions relevant to metals demand.",
        "NIFTY -> market liquidity/risk appetite -> Hindalco valuation/flows; "
        "NIFTY/economic cycle -> infrastructure/industrial demand -> aluminium/copper "
        "volumes and realised prices -> earnings.",
        "Calculate rolling correlation, beta, downside beta, relative strength, "
        "drawdown and residual return versus NIFTY. For fundamentals, combine NIFTY "
        "with metal prices, USD/INR, global industrial indicators and company EBITDA.",
        (
            "NIFTY return",
            "rolling beta",
            "metals-sector relative strength",
            "volume",
            "volatility",
            "drawdown",
        ),
        (
            "RBI policy",
            "Union Budget/fiscal policy",
            "infrastructure spending",
            "index rebalancing",
            "global risk-off events",
        ),
        ("5m", "15m", "1H", "1D", "1W", "1M", "1Q", "1Y"),
    ),
    "Natural Gas": _mc(
        "Natural Gas",
        "Industrial-energy and chemical-process cost signal.",
        "Indirect-to-material exposure through energy markets and industrial "
        "customers. Gas can affect the cost structure of selected processes and "
        "the economics of industrial customers, although electricity and captive "
        "power are more central to aluminium smelting.",
        "Natural gas -> industrial energy/chemical input costs -> production costs "
        "and customer demand -> metal demand/margins -> Hindalco earnings.",
        "Use gas as a secondary energy factor. Model it alongside electricity, coal, "
        "crude and metal prices. Test whether gas adds independent explanatory power "
        "for segment margins and stock returns.",
        (
            "natural-gas price",
            "gas volatility",
            "industrial energy proxy",
            "aluminium/copper prices",
            "segment EBITDA",
            "Hindalco return",
        ),
        (
            "LNG/gas supply disruptions",
            "global gas-price shocks",
            "industrial gas-policy changes",
            "manufacturing-cycle changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Silver": _mc(
        "Silver",
        "Precious-metal by-product plus industrial/electrification-cycle signal.",
        "Direct secondary exposure because silver can be recovered as a precious-"
        "metal by-product from copper operations. Indirectly, silver also reflects "
        "industrial, solar and electronics demand.",
        "Silver recovery volume + silver price -> by-product revenue; silver industrial "
        "cycle -> electrical/solar demand -> copper/aluminium downstream demand.",
        "Track recovered silver volume and realised price where disclosed. Separately "
        "test silver's industrial-cycle relationship with copper, aluminium and "
        "Hindalco stock returns using lagged multivariate models.",
        (
            "silver price",
            "silver recovery volume",
            "silver/gold ratio",
            "copper price",
            "industrial-demand proxy",
            "Hindalco relative return",
        ),
        (
            "solar demand changes",
            "electronics demand changes",
            "precious-metal shocks",
            "copper-cycle changes",
        ),
        ("1D", "1W", "1M", "1Q"),
    ),
    "Zinc": _mc(
        "Zinc",
        "Industrial-metals and steel-cycle demand signal.",
        "Indirect exposure through construction, galvanising, infrastructure, "
        "automotive and industrial customers. Zinc is not a core Hindalco production "
        "metal in the same way as aluminium and copper.",
        "Zinc -> steel/galvanising/construction cycle -> industrial demand -> customer "
        "orders for aluminium/copper and broader metal-market sentiment -> Hindalco.",
        "Use zinc as a cross-metal industrial-cycle factor. Test lagged correlation "
        "and multivariate regression with aluminium, copper, steel, NIFTY and global "
        "industrial indicators.",
        (
            "zinc price",
            "steel price",
            "construction proxy",
            "industrial-production proxy",
            "aluminium/copper demand",
            "Hindalco return",
        ),
        (
            "infrastructure spending",
            "construction-cycle changes",
            "steel-cycle changes",
            "zinc supply disruptions",
        ),
        ("1D", "1W", "1M", "1Q", "6M"),
    ),
}


COMPANY_CHARACTER = CompanyCharacter(
    symbol="HINDALCO",
    company_name="Hindalco Industries Limited",
    sector="Metals & Mining / Aluminium / Copper / Specialty Materials",
    industry_character=(
        "Vertically integrated global metals and advanced-materials platform. "
        "Hindalco's character is driven by the full aluminium value chain, a major "
        "copper business, specialty alumina, downstream value-added products and "
        "Novelis' global rolling/recycling platform. This makes metal prices, "
        "energy, conversion spreads, volumes, downstream mix and capital efficiency "
        "central to the research model."
    ),
    business_character=(
        "Integrated mine-to-market character: bauxite mining -> alumina refining -> "
        "smelting -> casting -> rolling/extrusion/foil -> downstream applications "
        "and recycling. Copper adds concentrate/smelting -> cathode/rod/wire/tube "
        "and specialty products, with precious-metal recovery. Novelis adds a large "
        "global flat-rolled and recycling platform. Specialty alumina adds higher-"
        "value applications. The company therefore must be analysed by business "
        "chain rather than as one simple aluminium-price proxy."
    ),
    demand_drivers=(
        "global aluminium demand",
        "Indian infrastructure and construction",
        "automotive and commercial transport",
        "electric vehicles",
        "railway electrification",
        "power-grid and transmission investment",
        "renewable-energy investment",
        "consumer durables",
        "packaging demand",
        "aerospace and defence",
        "semiconductor and advanced-material applications",
        "circular/recycled aluminium demand",
        "global industrial production",
    ),
    revenue_drivers=(
        "primary aluminium volumes and realisation",
        "alumina volumes and realisation",
        "downstream flat-rolled products",
        "extrusions",
        "foil and packaging products",
        "recycled aluminium volumes",
        "Novelis volumes and EBITDA per tonne",
        "copper cathode and rod volumes",
        "copper downstream tubes/wires/alloys",
        "specialty alumina volumes and product mix",
        "gold and silver by-product recovery",
        "value-added product mix",
    ),
    cost_drivers=(
        "electricity and captive power",
        "coal and fuel",
        "bauxite mining",
        "alumina refining costs",
        "caustic soda and process inputs",
        "carbon/anode materials",
        "freight and logistics",
        "copper concentrate and treatment/refining economics",
        "employee costs",
        "maintenance",
        "recycling feedstock costs",
        "environmental and compliance costs",
        "capital expenditure",
    ),
    supply_chain_character=(
        "bauxite mines",
        "alumina refineries",
        "captive coal mines",
        "captive power generation",
        "aluminium smelters",
        "copper concentrate and smelter ecosystem",
        "rolling and extrusion facilities",
        "recycling facilities",
        "rail and logistics network",
        "global Novelis manufacturing network",
        "automotive, aerospace, packaging and construction customers",
        "electrical, power and renewable-energy customers",
    ),
    strategic_drivers=(
        "aluminium capacity expansion",
        "copper capacity expansion",
        "downstream value-added products",
        "Novelis growth and recycling",
        "resource security and captive inputs",
        "cost-curve leadership",
        "electrification and renewable-energy demand",
        "EV and mobility applications",
        "advanced alloys and specialty materials",
        "copper tubes, wires and battery/solar applications",
        "copper recycling",
        "decarbonisation and circularity",
        "capital efficiency and free cash flow",
        "global capacity and geographic diversification",
    ),
    key_indicators=(
        "LME aluminium price",
        "LME copper price",
        "aluminium premium",
        "alumina price",
        "copper TC/RC",
        "primary aluminium production",
        "aluminium sales volume",
        "copper cathode/rod volume",
        "downstream volume",
        "Novelis shipments",
        "Novelis EBITDA per tonne",
        "segment EBITDA",
        "EBITDA per tonne",
        "power cost per tonne",
        "coal/fuel cost",
        "capacity utilisation",
        "net debt",
        "capex",
        "operating cash flow/free cash flow",
        "HINDALCO return, volume and relative strength",
    ),
    key_events=(
        "quarterly and annual results",
        "LME aluminium/copper price shocks",
        "alumina/bauxite supply events",
        "smelter/refinery capacity changes",
        "captive coal/power developments",
        "Novelis plant commissioning/restart",
        "major downstream capacity additions",
        "copper smelter expansion",
        "copper recycling expansion",
        "large capex announcements",
        "tariffs and international trade restrictions",
        "mining/environmental regulations",
        "major customer contracts",
        "EV/renewable/grid demand developments",
        "management guidance and capital-allocation changes",
    ),
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete HINDALCO company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return HINDALCO's character/exposure model for one tracked market."""
    try:
        return COMPANY_CHARACTER.market_characters[market]
    except KeyError as exc:
        raise ValueError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        ) from exc


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all 9 market character definitions."""
    return dict(COMPANY_CHARACTER.market_characters)


def validate_character() -> bool:
    """
    Validate structure only.

    This module does not calculate historical linkage, correlation, rank,
    percentage change, probability or a trading decision.
    """
    if COMPANY_CHARACTER.symbol != "HINDALCO":
        return False

    if tuple(COMPANY_CHARACTER.market_characters.keys()) != TRACKED_MARKETS:
        return False

    for market in TRACKED_MARKETS:
        item = COMPANY_CHARACTER.market_characters[market]
        if item.market != market:
            return False
        if not item.character or not item.exposure_character:
            return False
        if not item.impact_path or not item.calculation_logic:
            return False
        if not item.relevant_indicators or not item.relevant_events:
            return False
        if not item.expected_timeframes:
            return False

    return True


if __name__ == "__main__":
    print("HINDALCO character valid:", validate_character())
    print("Tracked markets:", ", ".join(TRACKED_MARKETS))
    print("Company:", COMPANY_CHARACTER.company_name)
