import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="SolarView: Solar Radiation Dashboard", layout="wide")
st.title("SolarView: Solar Radiation Dashboard")

st.markdown("""
This dashboard shows solar radiation data (GHI, DNI, DHI) for Benin, Sierra Leone, and Togo.  
Select a country, metric, and date range to explore its solar data statistics and visualizations.
""")

@st.cache_data  # Cache to speed up reloads
def load_data(country):
    path = f'notebooks/{country.lower().replace(" ", "_")}_cleaned.csv'  # underscores for spaces
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"Data file for {country} not found at {path}")
        df = pd.DataFrame()  # empty fallback
    return df

country = st.selectbox("Select a country", ["Benin", "Sierra Leone", "Togo"])
data = load_data(country)

if not data.empty:
    # Convert 'Timestamp' column to datetime
    try:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    except Exception as e:
        st.error(f"Error parsing 'Timestamp' column: {e}")
        data = pd.DataFrame()  # clear data if error
    
    if not data.empty:
        # Metric selection
        metrics = ['GHI', 'DNI', 'DHI']
        metric = st.selectbox("Select metric to visualize", metrics)
        
        # Date range filter
        min_date = data['Timestamp'].min().date()
        max_date = data['Timestamp'].max().date()
        date_range = st.date_input("Select date range", [min_date, max_date], min_value=min_date, max_value=max_date)
        
        # Filter data by date range
        filtered_data = data[(data['Timestamp'].dt.date >= date_range[0]) & (data['Timestamp'].dt.date <= date_range[1])]
        
        if filtered_data.empty:
            st.warning("No data available in selected date range.")
        else:
            # Show basic stats for selected metric
            st.subheader(f"{country} - {metric} Statistics")
            stats = filtered_data[[metric]].describe().loc[['mean', '50%', 'min', 'max']]
            stats.rename(index={'50%': 'median'}, inplace=True)
            st.dataframe(stats)
            
            # Boxplot
            st.subheader(f"{country} - {metric} Distribution")
            fig1, ax1 = plt.subplots(figsize=(5, 4))
            sns.boxplot(y=filtered_data[metric], ax=ax1, color='skyblue')
            ax1.set_ylabel(f"{metric} values")
            st.pyplot(fig1)
            
            # Time series plot
            st.subheader(f"{country} - {metric} Over Time")
            fig2, ax2 = plt.subplots(figsize=(10, 4))
            ax2.plot(filtered_data['Timestamp'], filtered_data[metric], color='orange')
            ax2.set_xlabel('Timestamp')
            ax2.set_ylabel(metric)
            ax2.tick_params(axis='x', rotation=45)
            st.pyplot(fig2)
else:
    st.warning("No data available to display.")
