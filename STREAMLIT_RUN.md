# Streamlit Web Application

This is a thin presentation layer over the existing NIFTY 50 Market Risk Engine.
The existing calculation, indicator, relationship, context and orchestration
modules are preserved.

## Local Windows run

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL shown by Streamlit, normally:

http://localhost:8501

## Streamlit Community Cloud

Use:
- Repository: your GitHub repository
- Branch: `web-app` (or the branch containing this file)
- Main file: `app.py`

The current app accepts OHLCV CSV data because the repository does not yet
contain a concrete live-market API provider. Do not add fake/live-looking data.

## CSV columns

Required:
- Open
- High
- Low
- Close
- Volume

Optional:
- Timestamp / Date / Datetime / Time

## Architecture rule

The UI calls the existing `MarketContext` and `CentralBrain`. It does not
create an independent decision engine.
