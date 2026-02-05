import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Codex Streamlit Demo", layout="wide")

st.title("Codex Streamlit Dashboard Demo")
st.caption("Minimal scaffold: data + filter + chart")

# ---- Sample data (can be replaced later) ----
df = pd.DataFrame({
    "month": pd.date_range("2025-01-01", periods=12, freq="MS").strftime("%Y-%m"),
    "region": ["North", "South", "East", "West"] * 3,
    "sales": [120, 80, 95, 110, 140, 75, 105, 125, 160, 90, 115, 135],
})

# ---- Sidebar filters ----
st.sidebar.header("Filters")
region = st.sidebar.selectbox("Region", ["All"] + sorted(df["region"].unique().tolist()))

if region != "All":
    df_plot = df[df["region"] == region].copy()
else:
    df_plot = df.copy()

# ---- Main layout ----
c1, c2 = st.columns(2)

with c1:
    st.metric("Rows", len(df_plot))
with c2:
    st.metric("Total sales", int(df_plot["sales"].sum()))

fig = px.line(df_plot, x="month", y="sales", color="region" if region == "All" else None,
              markers=True, title="Monthly sales")
st.plotly_chart(fig, use_container_width=True)

with st.expander("Preview data"):
    st.dataframe(df_plot, use_container_width=True)
