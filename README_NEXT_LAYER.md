# NIFTY 50 Market Risk Engine — Next Python Layer

## Upload folders
- indicators/
- global_effects/
- relationship_engine/
- news_events/
- historical/
- context/
- orchestration/
- tests/

## Architecture
Company Character + Market Character
-> indicators / global effects / events
-> historical relationship calculations
-> shared MarketContext
-> CentralBrain

## Important
No RANK, PCT_CHANGE, LINKAGE_SCORE, RELATION, fixed beta, fixed correlation,
probability or BUY/SELL result is stored as a hard-coded market relationship.
Those values must be calculated from historical observations.
