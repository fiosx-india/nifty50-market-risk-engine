"""
MARUTI_9_MARKETS_CHARACTER
Maruti Suzuki India Limited (MARUTI)

Character layer for the NIFTY 50 / 9-market research engine.

This module describes the company's business character and the mechanism by
which each tracked market can affect demand, revenue, cost, supply chain,
capital expenditure, exports or valuation.

It intentionally does NOT store:
- RANK
- PCT_CHANGE
- LINKAGE_SCORE
- fixed RELATION labels
- fixed correlation/beta/probability
- trading decisions

Those values belong to the later historical calculation engine and must be
derived from actual observations.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


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
    impact_path: List[str]
    calculation_logic: List[str]
    relevant_indicators: List[str]
    relevant_events: List[str]
    expected_timeframes: List[str]


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
    market_characters: Dict[str, MarketCharacter] = field(default_factory=dict)


def _mc(
    market: str,
    character: str,
    exposure_character: str,
    impact_path: List[str],
    calculation_logic: List[str],
    relevant_indicators: List[str],
    relevant_events: List[str],
    expected_timeframes: List[str],
) -> MarketCharacter:
    return MarketCharacter(
        market=market,
        character=character,
        exposure_character=exposure_character,
        impact_path=impact_path,
        calculation_logic=calculation_logic,
        relevant_indicators=relevant_indicators,
        relevant_events=relevant_events,
        expected_timeframes=expected_timeframes,
    )


# ---------------------------------------------------------------------------
# MARUTI SUZUKI COMPANY CHARACTER
# ---------------------------------------------------------------------------

COMPANY_CHARACTER = CompanyCharacter(
    symbol="MARUTI",
    company_name="Maruti Suzuki India Limited",
    sector="Automobiles & Auto Components",
    industry_character=(
        "High-volume passenger-vehicle manufacturer whose character is driven "
        "by domestic vehicle demand, model mix, affordability, financing, "
        "commodity/input costs, localisation, production capacity, supplier "
        "availability, exports, foreign-exchange conditions and the transition "
        "across petrol, CNG and battery-electric powertrains."
    ),
    business_character=[
        "Large-scale passenger-vehicle manufacturing with a broad small-car, compact, SUV and van portfolio.",
        "Light commercial vehicle exposure through Super Carry.",
        "Domestic retail and wholesale/OEM sales channels supported by a large dealer and service ecosystem.",
        "Large export business serving more than 100 countries with a diversified model portfolio.",
        "Multi-powertrain character spanning petrol, CNG and battery-electric vehicles.",
        "e VITARA represents the company's battery-electric vehicle manufacturing/export pathway.",
        "High localisation and a large supplier ecosystem are central to production economics.",
        "Manufacturing-capacity expansion is strategically important because demand can be constrained by available capacity.",
    ],
    demand_drivers=[
        "Indian passenger-vehicle demand and replacement cycle.",
        "Urban and rural income/consumption conditions.",
        "Vehicle affordability and financing availability.",
        "Interest rates and auto-loan affordability.",
        "Fuel-cost environment and consumer preference between petrol/CNG/EV.",
        "SUV and utility-vehicle demand.",
        "Small-car demand and entry-level affordability.",
        "Government taxation, GST and automotive policy.",
        "Export-market demand and country mix.",
        "New model launches, refreshes and product acceptance.",
    ],
    revenue_drivers=[
        "Domestic vehicle volumes.",
        "Export volumes.",
        "Average selling price and model mix.",
        "SUV/utility-vehicle mix.",
        "Premium product mix.",
        "CNG and other powertrain mix.",
        "Battery-electric vehicle volumes as the EV portfolio expands.",
        "OEM sales.",
        "Accessories, service and related automotive ecosystem revenue where applicable.",
    ],
    cost_drivers=[
        "Steel and ferrous-material prices.",
        "Aluminium and non-ferrous metal prices.",
        "Copper and electrical-system input costs.",
        "Plastic, rubber, glass and other auto-component costs.",
        "Crude-linked petrochemical, plastic, rubber and logistics costs.",
        "Electricity and manufacturing energy costs.",
        "Natural-gas/energy costs at selected manufacturing operations.",
        "Imported component costs and foreign exchange.",
        "Freight and logistics.",
        "Wages and manufacturing labour.",
        "Battery and EV-component costs as EV production scales.",
    ],
    supply_chain_character=[
        "OEM assembly depends on a large tiered supplier network.",
        "High localisation reduces some import dependence but increases sensitivity to domestic supplier continuity.",
        "Semiconductors and electronic components can create production bottlenecks.",
        "Steel, aluminium, copper, plastics, rubber and other materials flow through tiered suppliers.",
        "Production capacity and supplier availability jointly determine volume conversion.",
        "Export logistics depend on ports, shipping rates, destination-market conditions and FX.",
        "New EV production adds battery, power-electronics and EV-component dependencies.",
    ],
    strategic_drivers=[
        "Capacity expansion toward materially higher annual production capability.",
        "SUV portfolio expansion.",
        "Multi-powertrain strategy.",
        "Battery-electric vehicle localisation and exports.",
        "Export-hub development in India.",
        "Deeper supplier localisation.",
        "Manufacturing efficiency and scale economics.",
        "Technology and safety upgrades.",
        "Network expansion and customer reach.",
    ],
    key_indicators=[
        "Monthly domestic sales",
        "Monthly export sales",
        "Total sales volume",
        "Production volume",
        "Dealer inventory",
        "Pending customer orders",
        "Model-wise sales mix",
        "SUV share",
        "CNG share",
        "EV volume",
        "Average selling price",
        "Material cost per vehicle",
        "EBIT / operating margin",
        "Capacity utilisation",
        "Capacity additions",
        "Working capital",
        "Export share",
        "FX exposure",
    ],
    key_events=[
        "Monthly sales releases",
        "Monthly production releases",
        "Quarterly and annual financial results",
        "New model launches",
        "Major SUV launches",
        "EV launches and export milestones",
        "Capacity expansion announcements",
        "Plant commissioning",
        "Supplier disruption or semiconductor shortage",
        "GST/tax changes affecting automobiles",
        "Fuel-price or CNG policy changes",
        "Major export-market policy changes",
        "Import/export tariff changes",
        "Major commodity-cost shocks",
        "Large recalls or regulatory actions",
    ],
    market_characters={},
)


# ---------------------------------------------------------------------------
# NINE MARKET CHARACTERS
# ---------------------------------------------------------------------------

MARKET_CHARACTERS: Dict[str, MarketCharacter] = {

    "NIFTY 50": _mc(
        "NIFTY 50",
        "Broad Indian equity-market, liquidity and domestic risk-appetite character.",
        "Direct market-beta/valuation channel plus an indirect signal for Indian "
        "consumption, financing and macro conditions.",
        [
            "NIFTY regime → equity risk appetite → MARUTI valuation",
            "NIFTY/macroeconomic regime → household confidence → vehicle demand",
            "Equity/liquidity conditions → financing environment → auto demand",
        ],
        [
            "Calculate MARUTI returns versus NIFTY returns.",
            "Estimate rolling correlation and rolling beta.",
            "Estimate downside beta during market stress.",
            "Separate market return from company-specific residual return.",
            "Test lead/lag effects instead of assuming same-day causation.",
        ],
        [
            "MARUTI return",
            "NIFTY return",
            "Rolling beta",
            "Rolling correlation",
            "Volatility",
            "Relative strength",
        ],
        [
            "Major NIFTY regime changes",
            "RBI/liquidity events",
            "Large macro announcements",
            "Automotive policy/tax announcements",
            "Global risk-off events",
        ],
        ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Crude Oil": _mc(
        "Crude Oil",
        "Fuel, petrochemical-input, logistics and consumer-affordability character.",
        "Mixed operating-cost and demand exposure. Crude can affect fuel "
        "affordability, logistics, plastics/rubber inputs and inflation.",
        [
            "Crude price → petrol/diesel economics → consumer running cost",
            "Crude price → transport/logistics cost → supply-chain cost",
            "Crude price → petrochemical/plastic/rubber input costs → vehicle cost",
            "Crude/inflation → household purchasing power → vehicle demand",
        ],
        [
            "Measure lagged MARUTI/crude returns.",
            "Estimate sensitivity during large crude shocks.",
            "Use fuel-price series separately from crude because retail fuel "
            "prices do not move one-for-one with crude.",
            "Control for NIFTY and domestic auto-demand indicators.",
            "Test whether crude affects volumes, margins or both.",
        ],
        [
            "Brent/WTI return",
            "Domestic petrol price",
            "Diesel price",
            "Freight-cost proxy",
            "Petrochemical-input proxy",
            "MARUTI volume",
            "Operating margin",
        ],
        [
            "OPEC+ decisions",
            "Large crude-price shocks",
            "Domestic fuel-price changes",
            "Major logistics/freight disruptions",
            "Inflation shocks",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Gold": _mc(
        "Gold",
        "Safe-haven, wealth-effect, real-rate and risk-aversion character.",
        "Mostly indirect. Gold is a macro/wealth/risk signal rather than a core "
        "automotive raw material.",
        [
            "Gold/risk regime → household wealth sentiment → discretionary demand",
            "Gold/rates → financial conditions → vehicle financing environment",
            "Gold/USD/rates → global macro regime → export-market sentiment",
        ],
        [
            "Test MARUTI/gold rolling correlation after controlling for NIFTY.",
            "Use gold as a regime variable rather than an input-cost variable.",
            "Test high-gold-volatility periods separately.",
            "Check whether gold moves precede changes in auto-sector risk appetite.",
        ],
        [
            "Gold return",
            "Gold volatility",
            "Real-rate proxy",
            "USD index",
            "MARUTI relative return",
            "Auto-sector return",
        ],
        [
            "Safe-haven shocks",
            "Major rate decisions",
            "Global geopolitical stress",
            "Large liquidity/risk-off episodes",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Silver": _mc(
        "Silver",
        "Precious-metal plus industrial-cycle character.",
        "Indirect. Silver is more useful as an industrial/global-growth signal "
        "than as a major direct MARUTI input.",
        [
            "Silver industrial cycle → manufacturing activity → auto demand",
            "Silver/risk regime → market sentiment → MARUTI valuation",
            "Silver/electronics cycle → component demand/supply conditions",
        ],
        [
            "Measure rolling MARUTI/silver relationship.",
            "Compare silver with copper as industrial-cycle variables.",
            "Control for NIFTY and broad auto-sector performance.",
            "Test whether silver leads changes in industrial/auto sentiment.",
        ],
        [
            "Silver return",
            "Gold/silver ratio",
            "Industrial-metal index",
            "Auto-sector return",
            "MARUTI volume",
        ],
        [
            "Industrial-cycle shocks",
            "Large silver volatility events",
            "Global manufacturing slowdown/recovery",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Natural Gas": _mc(
        "Industrial energy, manufacturing-cost and global energy-transition character.",
        "Indirect operating-cost exposure plus a smaller macro signal. Natural gas "
        "can affect selected plant energy costs and supplier economics.",
        [
            "Gas price → industrial energy cost → supplier/manufacturing cost",
            "Gas price → inflation/energy regime → household purchasing power",
            "Gas availability/volatility → industrial production → component supply",
            "Gas/energy transition → EV/power infrastructure ecosystem",
        ],
        [
            "Use an appropriate natural-gas benchmark.",
            "Test lagged MARUTI/gas relationships.",
            "Separate direct manufacturing-cost effects from macro effects.",
            "Control for crude, electricity and NIFTY.",
            "Use supplier/industrial-production variables where available.",
        ],
        [
            "Natural-gas return",
            "Gas volatility",
            "Industrial energy-cost proxy",
            "Manufacturing PMI",
            "MARUTI production",
            "Operating margin",
        ],
        [
            "Major gas-price shocks",
            "Industrial energy disruptions",
            "Global gas/LNG supply events",
            "Large manufacturing-cost changes",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Copper": _mc(
        "Electrical, electronics, wiring and vehicle-electrification industrial-input character.",
        "Direct-ish input exposure through wiring/electrical systems and vehicle "
        "electronics, with stronger relevance as electrification increases.",
        [
            "Copper price → electrical/component cost → vehicle manufacturing cost",
            "Copper demand → industrial cycle → auto demand",
            "Copper supply disruption → component availability → production risk",
            "EV adoption → copper intensity → longer-term input sensitivity",
        ],
        [
            "Measure lagged copper sensitivity in MARUTI returns and margins.",
            "Where data permits, compare copper moves with material cost per vehicle.",
            "Test high copper-volatility periods.",
            "Separate conventional-vehicle and EV-related exposure.",
            "Control for NIFTY and broad metal prices.",
        ],
        [
            "Copper return",
            "Copper volatility",
            "Electrical-component cost proxy",
            "Production volume",
            "Material-cost ratio",
            "EV production",
        ],
        [
            "Copper supply disruptions",
            "Large copper price shocks",
            "EV production ramp-up",
            "Major electronics/component shortages",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Aluminium": _mc(
        "Lightweight vehicle, body/component and non-ferrous automotive-input character.",
        "Meaningful direct input exposure because aluminium is used across vehicle "
        "body, wheels, castings, engine/transmission and other components; exposure "
        "also changes with model/powertrain mix.",
        [
            "Aluminium price → component/body input cost → vehicle cost",
            "Aluminium price → supplier margin → OEM procurement economics",
            "Aluminium demand → industrial/auto cycle → vehicle demand",
            "EV/lightweighting → aluminium intensity → long-term sensitivity",
        ],
        [
            "Estimate rolling MARUTI/aluminium sensitivity.",
            "Test lagged relationships because supplier procurement can have contracts.",
            "Relate aluminium moves to material-cost/margin data when available.",
            "Compare periods by model/powertrain mix.",
            "Control for steel, copper, crude and NIFTY.",
        ],
        [
            "Aluminium return",
            "Aluminium volatility",
            "Auto metal-cost index",
            "Material-cost ratio",
            "Vehicle production",
            "Operating margin",
        ],
        [
            "Major aluminium price shocks",
            "Smelter/supply disruptions",
            "Large auto-material cost changes",
            "EV/lightweighting product changes",
        ],
        ["1D", "1W", "1M", "3M", "6M", "1Y"],
    ),

    "Zinc": _mc(
        "Galvanised steel, corrosion protection and automotive-material-cycle character.",
        "Indirect-to-moderate input exposure through galvanised/coated steel and "
        "automotive component supply chains, plus an industrial-cycle signal.",
        [
            "Zinc price → galvanised steel/component cost → vehicle input cost",
            "Zinc demand → industrial/manufacturing cycle → auto demand",
            "Zinc supply shock → coated-steel supply chain → production economics",
        ],
        [
            "Calculate lagged MARUTI/zinc sensitivity.",
            "Compare zinc with steel as a vehicle-material proxy.",
            "Test whether zinc shocks affect margins after controlling for steel.",
            "Control for NIFTY and auto-demand variables.",
        ],
        [
            "Zinc return",
            "Zinc volatility",
            "Steel price",
            "Galvanised-steel proxy",
            "Material-cost ratio",
            "Production volume",
        ],
        [
            "Zinc supply disruptions",
            "Steel/metal price shocks",
            "Auto material-cost inflation",
            "Major supplier disruptions",
        ],
        ["1D", "1W", "1M", "3M", "6M"],
    ),

    "Electricity": _mc(
        "Manufacturing energy, plant utilisation and industrial-operating-cost character.",
        "Direct operating exposure through vehicle manufacturing plants and supplier "
        "operations; also an indirect signal of industrial activity.",
        [
            "Electricity cost → plant operating cost → vehicle gross margin",
            "Power reliability → plant uptime → production volume",
            "Electricity/industrial demand → economic activity → auto demand",
            "Power transition → EV charging/manufacturing ecosystem",
        ],
        [
            "Use reliable regional/industrial electricity-price data.",
            "Measure electricity-price sensitivity with appropriate lags.",
            "Test production/plant disruptions separately from price effects.",
            "Compare electricity effects with crude and aluminium.",
            "Use plant-level data when available; otherwise use regional proxies.",
        ],
        [
            "Industrial electricity price",
            "Power demand",
            "Peak demand",
            "Plant production",
            "Capacity utilisation",
            "Energy cost",
            "Operating margin",
        ],
        [
            "Power shortages",
            "Electricity-price shocks",
            "Plant disruptions",
            "New manufacturing-plant commissioning",
            "Renewable/captive-power developments",
        ],
        ["intraday", "1D", "1W", "1M", "3M", "6M", "1Y"],
    ),
}


# Bind the nine market characters to the company character.
COMPANY_CHARACTER = CompanyCharacter(
    symbol=COMPANY_CHARACTER.symbol,
    company_name=COMPANY_CHARACTER.company_name,
    sector=COMPANY_CHARACTER.sector,
    industry_character=COMPANY_CHARACTER.industry_character,
    business_character=COMPANY_CHARACTER.business_character,
    demand_drivers=COMPANY_CHARACTER.demand_drivers,
    revenue_drivers=COMPANY_CHARACTER.revenue_drivers,
    cost_drivers=COMPANY_CHARACTER.cost_drivers,
    supply_chain_character=COMPANY_CHARACTER.supply_chain_character,
    strategic_drivers=COMPANY_CHARACTER.strategic_drivers,
    key_indicators=COMPANY_CHARACTER.key_indicators,
    key_events=COMPANY_CHARACTER.key_events,
    market_characters=MARKET_CHARACTERS,
)


def get_company_character() -> CompanyCharacter:
    """Return the complete Maruti Suzuki company character."""
    return COMPANY_CHARACTER


def get_market_character(market: str) -> MarketCharacter:
    """Return one of the nine Maruti market characters."""
    key = market.strip()
    if key not in MARKET_CHARACTERS:
        raise KeyError(
            f"Unsupported market: {market!r}. "
            f"Expected one of: {', '.join(TRACKED_MARKETS)}"
        )
    return MARKET_CHARACTERS[key]


def get_all_market_characters() -> Dict[str, MarketCharacter]:
    """Return all nine market characters."""
    return dict(MARKET_CHARACTERS)


def validate_character() -> dict:
    """Structural validation; no market score calculation is performed."""
    expected = set(TRACKED_MARKETS)
    actual = set(MARKET_CHARACTERS)

    missing = sorted(expected - actual)
    extra = sorted(actual - expected)

    return {
        "symbol": COMPANY_CHARACTER.symbol,
        "markets_expected": 9,
        "markets_found": len(MARKET_CHARACTERS),
        "missing_markets": missing,
        "extra_markets": extra,
        "valid": not missing and not extra and len(MARKET_CHARACTERS) == 9,
        "calculated_fields_present": False,
        "note": (
            "RANK/PCT_CHANGE/LINKAGE_SCORE/RELATION are not hard-coded. "
            "Historical relationships must be calculated later from real data."
        ),
    }


if __name__ == "__main__":
    print(validate_character())
    for market in TRACKED_MARKETS:
        print(f"{market}: {get_market_character(market).character}")
