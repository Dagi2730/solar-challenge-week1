import streamlit as st
import pandas as pd
import plotly.express as px
import os

# 1. SET PAGE CONFIG - MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(page_title="☀️ Solar Radiation Insights", layout="wide")

# 2. Load Data Function with caching
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    # Convert Timestamp to datetime if exists, else 'date' column
    if "Timestamp" in df.columns:
        df["date"] = pd.to_datetime(df["Timestamp"])
    elif "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
    else:
        st.error("No date or Timestamp column found in dataset.")
        st.stop()
    return df

# 3. Define data path
data_path = "C:/Users/HP/Desktop/solar-challenge-week1/notebooks/data/compare_solar_clean.csv"

if not os.path.exists(data_path):
    st.error(f"❌ File not found: {data_path}")
    st.stop()

# 4. Load data
df = load_data(data_path)

# 5. Sidebar filters
st.sidebar.header("Filters")

# Country filter (if column exists)
if "country" in df.columns:
    countries = df["country"].unique()
    selected_countries = st.sidebar.multiselect("Select Countries", countries, default=countries)
    df = df[df["country"].isin(selected_countries)]

# Date range filter with calendar widget
min_date = df["date"].min().date()
max_date = df["date"].max().date()
date_range = st.sidebar.date_input("Select Date Range", value=(min_date, max_date), min_value=min_date, max_value=max_date)

if len(date_range) == 2:
    start_date, end_date = date_range
    df = df[(df["date"].dt.date >= start_date) & (df["date"].dt.date <= end_date)]
else:
    st.warning("Please select a start and end date for filtering.")

# Additional dropdown to preview cleaned data columns
st.sidebar.header("Cleaned Data Preview Options")
preview_column = st.sidebar.selectbox("Select Column to Preview", options=df.columns)

# 6. Main page title
st.title("☀️ Solar Radiation Insights Dashboard")

# 7. Display filtered cleaned data preview interactively
st.subheader(f"Cleaned Data Preview - Column: {preview_column}")
st.dataframe(df[[preview_column]].dropna().reset_index(drop=True))

# 8. Visualization section
st.subheader("Visualizations")

# Histogram of GHI with color by 'country' if exists
if "GHI" in df.columns:
    if "country" in df.columns:
        fig1 = px.histogram(df, x="GHI", nbins=40, color="country", title="Histogram of GHI by Country")
    else:
        fig1 = px.histogram(df, x="GHI", nbins=40, title="Histogram of GHI")
    st.plotly_chart(fig1, use_container_width=True)
else:
    st.info("GHI column not found in data for histogram.")

# Line chart of average GHI over time
if "GHI" in df.columns:
    ghi_time = df.groupby("date")["GHI"].mean().reset_index()
    fig2 = px.line(ghi_time, x="date", y="GHI", title="Average GHI Over Time")
    st.plotly_chart(fig2, use_container_width=True)

# Scatter plot: GHI vs DNI colored by country if exists
if {"GHI", "DNI"}.issubset(df.columns):
    if "country" in df.columns:
        fig3 = px.scatter(df, x="GHI", y="DNI", color="country", title="GHI vs DNI by Country")
    else:
        fig3 = px.scatter(df, x="GHI", y="DNI", title="GHI vs DNI")
    st.plotly_chart(fig3, use_container_width=True)

# 9. Summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())

# 10. Footer
st.markdown("---")
st.markdown("© 2025 Solar Challenge Week 1 — Built with Streamlit by DAGMAWIT.A")

