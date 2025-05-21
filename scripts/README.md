# Solar Challenge Week 1 – MoonLight Energy

## Project Overview
This project analyzes solar radiation datasets from three countries in West Africa: **Benin**, **Sierra Leone**, and **Togo**. It involves:

- Data profiling and cleaning  
- Exploratory Data Analysis (EDA) to identify trends and insights  
- Cross-country comparison of solar radiation metrics  
- An interactive dashboard built with Streamlit to visualize the data  

The goal is to help MoonLight Energy Solutions identify high-potential regions for solar installations based on solar irradiance and related environmental factors.

## Dataset Description
The datasets contain hourly measurements of solar radiation and weather parameters including:

- **Timestamp:** Date and time of observation (YYYY-MM-DD HH:mm)  
- **GHI (Global Horizontal Irradiance)**  
- **DNI (Direct Normal Irradiance)**  
- **DHI (Diffuse Horizontal Irradiance)**  
- Ambient temperature, humidity, wind speed, pressure, and sensor module readings  
- Cleaning events and precipitation rates  

Each country’s dataset was cleaned and processed for analysis.

## Folder Structure
├── app/ # Streamlit dashboard source code
│ └── main.py # Main Streamlit app script
├── notebooks/ # Jupyter notebooks with EDA and data cleaning
│ ├── benin_eda.ipynb
│ ├── sierra_leone_eda.ipynb
│ └── togo_eda.ipynb
├── data/ # Cleaned CSV files (ignored in git)
├── scripts/ # Utility scripts (optional)
├── .github/
│ └── workflows/ # CI/CD GitHub Actions workflows
├── requirements.txt # Project dependencies
├── README.md # Project documentation (this file)
└── .gitignore # Files and folders to exclude from git



## Author

**Dagmawit Andargachew**
