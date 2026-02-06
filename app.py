import streamlit as st

from src.data_loader import load_sales_data
from src.plots import make_monthly_sales_line, make_sales_by_region_bar

st.set_page_config(page_title="Codex Streamlit Demo", layout="wide")

st.title("Codex Streamlit Dashboard Demo")
st.caption("Minimal scaffold: data + filter + chart")

# ---- Sample data (can be replaced later) ----
df = load_sales_data()

# ---- Sidebar filters ----
st.sidebar.header("Filters")
regions = sorted(df["region"].unique().tolist())
selected_regions = st.sidebar.multiselect("Regions", regions, default=regions)

if selected_regions:
    df_plot = df[df["region"].isin(selected_regions)].copy()
else:
    df_plot = df.iloc[0:0].copy()

csv_data = df_plot.to_csv(index=False)
st.sidebar.download_button(
    "Download CSV",
    data=csv_data,
    file_name="filtered_sales.csv",
    mime="text/csv",
)

# ---- Main layout ----
c1, c2 = st.columns(2)

with c1:
    st.metric("Rows", len(df_plot))
with c2:
    st.metric("Total sales", int(df_plot["sales"].sum()))

line_fig = make_monthly_sales_line(df_plot, color_by_region=len(selected_regions) != 1)
st.plotly_chart(line_fig, use_container_width=True)

bar_fig = make_sales_by_region_bar(df_plot)
st.plotly_chart(bar_fig, use_container_width=True)

with st.expander("Preview data"):
    st.dataframe(df_plot, use_container_width=True)
