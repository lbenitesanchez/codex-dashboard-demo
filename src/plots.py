import pandas as pd
import plotly.express as px


def make_monthly_sales_line(df: pd.DataFrame, color_by_region: bool) -> "px.Figure":
    return px.line(
        df,
        x="month",
        y="sales",
        color="region" if color_by_region else None,
        markers=True,
        title="Monthly sales",
    )


def make_sales_by_region_bar(df: pd.DataFrame) -> "px.Figure":
    grouped = df.groupby("region", as_index=False)["sales"].sum()
    return px.bar(
        grouped,
        x="region",
        y="sales",
        text="sales",
        title="Total sales by region",
    )
