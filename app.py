import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="SolarView: Solar Radiation Dashboard", layout="wide")
st.title("SolarView: Solar Radiation Dashboard")

st.markdown("""
This dashboard shows solar radiation data (GHI, DNI, DHI) for Benin, Sierra Leone, and Togo.
Select a country to explore its solar data statistics and visualization.
""")

@st.cache_data  # Cache to speed up reloads
def load_data(country):
    path = f'notebooks/{country.lower().replace(" ", "_")}_cleaned.csv'  # use underscores for spaces in filename
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"Data file for {country} not found at {path}")
        df = pd.DataFrame()  # empty dataframe fallback
    return df

country = st.selectbox("Select a country", ["Benin", "Sierra Leone", "Togo"])
data = load_data(country)

if not data.empty:
    # Convert 'Timestamp' column to datetime
    try:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    except Exception as e:
        st.error(f"Error parsing 'Timestamp' column: {e}")

    # Show basic stats
    st.subheader(f"{country} - Solar Radiation Stats")
    stats = data[['GHI', 'DNI', 'DHI']].describe().loc[['mean', '50%', 'min', 'max']]
    stats.rename(index={'50%': 'median'}, inplace=True)
    st.dataframe(stats)

    # Smaller boxplot for GHI distribution
    st.subheader(f"{country} - GHI Distribution")
    fig1, ax1 = plt.subplots(figsize=(4, 4))  # smaller size
    sns.boxplot(y=data['GHI'], ax=ax1, color='skyblue')
    ax1.set_ylabel('Global Horizontal Irradiance (GHI)')
    st.pyplot(fig1)

    # Time series plot for GHI over time
    st.subheader(f"{country} - GHI Over Time")
    fig2, ax2 = plt.subplots(figsize=(8, 3))  # wider but short height
    ax2.plot(data['Timestamp'], data['GHI'], color='orange')
    ax2.set_xlabel('Timestamp')
    ax2.set_ylabel('Global Horizontal Irradiance (GHI)')
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

else:
    st.warning("No data available to display.")
