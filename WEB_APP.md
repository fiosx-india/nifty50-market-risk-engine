# Web App

This branch adds a thin Streamlit presentation layer over the existing engine.

## Local run

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

The local URL is normally http://localhost:8501.

## Streamlit Community Cloud

Deploy this repository using branch `web-app` and entrypoint `app.py`.
