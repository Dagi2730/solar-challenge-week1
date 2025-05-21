# ☀️ Solar Challenge Week 1 – MoonLight Energy

Welcome to the Week 1 repository for the **10 Academy Solar Challenge**, led by **MoonLight Energy**. This challenge focuses on evaluating solar energy potential in West African countries using real-world solar radiation data.

## 📌 Project Objective

The goal of this project is to analyze, clean, and compare solar radiation datasets from **Benin**, **Sierra Leone**, and **Togo**, and derive insights to inform renewable energy solutions.

We use Python for:
- Exploratory Data Analysis (EDA)
- Data cleaning and profiling
- Cross-country statistical comparison
- Interactive dashboard creation using **Streamlit**

---

## 📁 Repository Structure

solar-challenge-week1/
│
├── .github/ # CI workflows
│ └── workflows/
│ └── unittests.yml
├── .vscode/ # Editor configuration
│ └── settings.json
├── app/ # Streamlit dashboard app
│ └── main.py
├── data/ # Raw data (Git-ignored)
├── notebooks/ # EDA and analysis notebooks
│ ├── benin_analysis.ipynb
│ ├── sierra_leone_analysis.ipynb
│ ├── togo_analysis.ipynb
│ ├── compare_solar.ipynb
│ └── data/
├── scripts/ # Utility Python scripts
├── tests/ # Test files (optional)
├── dashboard_screenshots/ # Final dashboard screenshots
│
├── .gitignore
├── requirements.txt
├── README.md
└── report/
└── Solar_Challenge_Week1_Report.pdf

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

To reproduce the environment locally:

**Clone the repository**
```bash
git clone https://github.com/Dagi2730/solar-challenge-week1.git
cd solar-challenge-week1
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
# On Windows PowerShell:
venv\Scripts\Activate.ps1
# On Mac/Linux:
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit Dashboard

bash
Copy
Edit
cd app
streamlit run main.py
✅ Completed Tasks
Task 1: Git & Environment Setup
Initialized Git repository

Created .gitignore, requirements.txt, and GitHub Actions CI

Set up virtual environment

Established clean repository structure

Task 2: Data Profiling, Cleaning, and EDA
Cleaned and validated raw solar radiation data for three countries

Conducted exploratory analysis

Generated visual insights and summaries

Task 3: Cross-Country Comparison
Created compare_solar_clean.csv for unified analysis

Compared key metrics (GHI, DNI, DHI, Temp)

Visualized and interpreted differences in solar potential

Task 4 (Optional): Streamlit Dashboard
Built an interactive dashboard to showcase data insights

🔗 Live Dashboard: [Insert your Streamlit app link here]

📊 Sample Visuals
Screenshots and comparative charts are available in the dashboard_screenshots/ and notebooks/ folders.

📄 Final Report
The project report is available under report/Solar_Challenge_Week1_Report.pdf. It includes:

Setup documentation

Visual EDA summaries

Statistical comparisons

Reflections and challenges

🙌 Acknowledgements
10 Academy for organizing the challenge
