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

## Modular structure
The dashboard is split into small, focused modules: `src/data_loader.py` owns data creation/loading,
`src/plots.py` owns Plotly chart construction, and `app.py` coordinates layout and user interaction.
This keeps logic isolated for teaching and makes it easier to extend without changing the UI wiring.

## How to run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
