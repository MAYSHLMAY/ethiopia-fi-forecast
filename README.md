# Forecasting Financial Inclusion in Ethiopia

**Project Status:** Final Submission (Tasks 1–5 Complete)  
**Author:** Mikiyas Dawit  
**Date:** February 3, 2026  

---

## 📌 Project Overview
This project delivers a comprehensive forecasting system tracking Ethiopia's digital financial transformation. As a Data Scientist for **Selam Analytics**, I have developed a model to predict financial inclusion trajectories for the 2025–2027 period.

The system bridges the gap between sparse triennial survey data (Global Findex) and high-frequency market events. By quantifying the "shocks" of major milestones—such as the **Telebirr launch**, **M-Pesa entry**, and **National ID (Fayda) rollout**—the model provides a scenario-based outlook on Ethiopia's path toward a 60% inclusion rate.

## 🚀 Interactive Dashboard
The core deliverable is a **Streamlit Dashboard** that allows stakeholders to explore event impacts and toggle between economic scenarios in real-time.

**To run the dashboard locally:**
1. Ensure you have the requirements installed:
   ```bash
   pip install -r requirements.txt

```

2. Launch the application:
```bash
streamlit run dashboard/app.py

```



## 📂 Repository Structure

```text
ethiopia-fi-forecast/
├── dashboard/
│   └── app.py              # Interactive Streamlit application
├── data/
│   ├── raw/                # Enriched starter datasets (Task 1)
│   └── processed/          # Generated forecasts (CSV format)
├── notebooks/
│   ├── Task2_EDA.ipynb     # Exploratory Data Analysis & Gender Gap
│   ├── Task3_Impact.ipynb  # Event Impact Modeling (Association Matrix)
│   └── Task4_Forecast.ipynb # 2025-2027 Scenario Generation
├── reports/
│   ├── figures/            # Visualizations (Heatmaps, Forecast Plots)
│   └── Final_Report.md     # Blog-style executive summary
├── data_enrichment_log.md  # Detailed log of Task 1 data additions
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies (pandas, plotly, streamlit)

```

## 🔑 Key Technical Deliverables

* **Event-Indicator Association Matrix:** A modeled heatmap quantifying how specific policy and product launches drive "Access" (Ownership) vs "Usage" (Digital Payments).
* **Scenario-Based Forecasts:** Projections for 2025–2027 covering **Base, Optimistic, and Pessimistic** economic outlooks.
* **Unified Schema:** An enriched data structure that links historical observations with major national events and disaggregated gender data.

## 📈 Summary of Insights

* **The 60% Threshold:** Ethiopia is projected to hit the national target of 60% account ownership by late 2027 only under the **Optimistic Scenario**, requiring aggressive merchant digitization.
* **Usage Gap:** Digital payment adoption (Usage) currently lags behind Account Ownership (Access) by approximately 14 percentage points, highlighting the need for increased ecosystem interoperability.
* **Primary Catalyst:** Telebirr remains the single largest driver of mobile money penetration, with a modeled impact magnitude of **12.5%** on total mobile money accounts.

---

**Selam Analytics | 10 Academy Financial Inclusion Project**