import pandas as pd


def load_sales_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "month": pd.date_range("2025-01-01", periods=12, freq="MS").strftime("%Y-%m"),
            "region": ["North", "South", "East", "West"] * 3,
            "sales": [120, 80, 95, 110, 140, 75, 105, 125, 160, 90, 115, 135],
        }
    )
