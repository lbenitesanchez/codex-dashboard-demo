# Codex Streamlit Dashboard Demo

## Objective
Interactive Streamlit dashboard designed to be developed and extended using Codex (cloud mode).

## Tech stack
- Python 3.11+
- Streamlit
- Pandas
- Plotly

## Project structure
- `app.py` : Streamlit entry point
- `src/`   : reusable functions (data loading, plots, UI helpers)
- `data/`  : datasets (optional). If absent, the app can simulate sample data.

## How to run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
