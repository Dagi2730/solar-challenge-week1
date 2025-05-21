import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Solar Dashboard – Benin", layout="wide")
st.title("☀️ Benin Solar Radiation Dashboard")

DATA_PATH = os.path.join("data", "benin_cleaned.csv")

@st.cache_data
def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    return None

data = load_data()

if data is not None:
    st.success("Data loaded successfully!")
    st.write("### Preview of Data")
    st.dataframe(data.head())

    st.write("### Summary Statistics")
    st.write(data.describe())
else:
    st.error(f"CSV not found at `{DATA_PATH}`. Please check the file path.")
