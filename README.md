# ☀️ Solar Radiation Interactive Dashboard – MoonLight Energy | 10 Academy  
**Branch:** `dashboard-dev`

## 📊 Overview  
This Streamlit dashboard is developed as part of **Solar Challenge Week 1** by **MoonLight Energy Solutions** in collaboration with **10 Academy**.  
It provides interactive visualizations of solar radiation data from **Benin**, **Sierra Leone**, and **Togo**, offering insights to support renewable energy deployment in West Africa.

---

## 🚀 Features  
- 📅 **Date Range Picker**: Filter data by custom time ranges  
- 🌍 **Country Selector**: Choose between Benin, Sierra Leone, and Togo  
- 📈 **Dynamic Visualizations**:  
  - Line chart of solar irradiance components  
  - Histogram of GHI distribution  
  - Monthly average irradiance plot  
  - Temperature vs. GHI scatter plots  
- 🧹 **Cleaned Data Preview**: View filtered data by time, country, and more  
- 🛠️ **Responsive UI**: Built using Streamlit's wide layout with sidebar controls  

---

## 📁 Folder Structure  
```
solar-challenge-week1/
├── app/
│   └── main.py              # Main Streamlit dashboard
├── data/
│   └── compare_solar_clean.csv  # Cleaned dataset (excluded from GitHub)
├── requirements.txt         # Required packages for running dashboard
└── .gitignore               # Prevents data and backups from being pushed
```

---

## 🧪 Setup & Run Locally  

1. **Clone the repo**:
```bash
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1
git checkout dashboard-dev
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Make sure the cleaned data exists locally**:
```bash
data/compare_solar_clean.csv
```

4. **Run the dashboard**:
```bash
streamlit run app/main.py
```

---

## 📌 Notes  
- This branch contains only dashboard-related code and components.  
- Raw and cleaned data are excluded from version control but required for full functionality.

---

## 👩‍💻 Author  
**Dagmawit Andargachew**  
Solar Challenge Week 1 | 10 Academy | MoonLight Energy Solutions
