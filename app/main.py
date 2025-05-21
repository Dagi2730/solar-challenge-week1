import streamlit as st
from app import utils

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("🌞 Solar Radiation Interactive Dashboard")
st.markdown("Analyze solar radiation metrics across Benin, Sierra Leone, and Togo.")

# Load data once
df = utils.load_data()

# Sidebar for filters
st.sidebar.header("Filter Options")
countries = st.sidebar.multiselect(
    "Select Countries", options=df['country'].unique(), default=df['country'].unique()
)
metrics = ['GHI', 'DNI', 'DHI']
metric = st.sidebar.selectbox("Select Metric", metrics)

if not countries:
    st.warning("Please select at least one country.")
    st.stop()

# Show boxplot
st.subheader(f"Boxplot of {metric} by Country")
img_encoded = utils.create_boxplot(df, countries, metric)
st.image(f"data:image/png;base64,{img_encoded}", use_column_width=True)

# Show summary table
st.subheader("Summary Statistics by Country")
summary = utils.get_summary(df, countries, [metric])
st.dataframe(summary.style.format({
    f'{metric}_mean': '{:.2f}',
    f'{metric}_median': '{:.2f}',
    f'{metric}_std': '{:.2f}',
}))

st.markdown("---")
st.markdown("Developed by [Your Name].")
