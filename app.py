import streamlit as st
import pandas as pd
from filters import load_data, apply_filters
import charts

st.set_page_config(page_title="🌍 OWID Energy Dashboard", layout="wide")
st.title("🌍 Our World in Data — Energy Dashboard")
st.caption("Exploratory Data Analysis | Instructor: Ali Hassan Sherazi")

df = load_data()

st.sidebar.header("🔧 Filters")
all_countries = sorted(df["country"].dropna().unique().tolist())
selected_countries = st.sidebar.multiselect("Select Countries", all_countries,
                     default=["Pakistan", "India", "China", "United States"])
year_min, year_max = int(df["year"].min()), int(df["year"].max())
year_range = st.sidebar.slider("Year Range", year_min, year_max, (2000, 2022))
search_text = st.sidebar.text_input("🔍 Search Country")
numeric_cols = [c for c in df.select_dtypes(include="number").columns
                if "energy" in c or "renewable" in c or "gdp" in c]
energy_col = st.sidebar.selectbox("Primary Energy Column", numeric_cols)
if st.sidebar.button("🔄 Reset Filters"):
    st.rerun()

filtered = apply_filters(df, selected_countries, year_range, energy_col, search_text)

st.subheader("📊 Summary KPIs")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", f"{len(filtered):,}")
col2.metric("Countries", filtered["country"].nunique())
col3.metric(f"Avg {energy_col[:15]}", f"{filtered[energy_col].mean():.2f}")
col4.metric("Year Span", f"{year_range[0]}–{year_range[1]}")

st.markdown("---")

c1, c2 = st.columns(2)
with c1:
    st.pyplot(charts.line_chart(filtered, energy_col))
with c2:
    st.pyplot(charts.area_chart(filtered))

c3, c4 = st.columns(2)
with c3:
    st.pyplot(charts.bar_chart(filtered, energy_col))
with c4:
    st.pyplot(charts.pie_chart(filtered, energy_col))

c5, c6 = st.columns(2)
with c5:
    st.pyplot(charts.histogram(filtered, energy_col))
with c6:
    st.pyplot(charts.scatter_plot(filtered))

c7, c8 = st.columns(2)
with c7:
    st.pyplot(charts.box_plot(filtered, energy_col))
with c8:
    st.pyplot(charts.violin_plot(filtered, energy_col))

st.subheader("🔥 Correlation Heatmap")
st.pyplot(charts.heatmap(filtered))

st.subheader("🔢 Record Count by Country")
st.pyplot(charts.count_plot(filtered))

st.markdown("---")
st.caption("Data Source: Our World in Data | owid-energy-data.csv")