# Forecasting Financial Inclusion in Ethiopia

**Project Status:** Final Submission (Tasks 1–5 Complete)  
**Author:** Mikiyas Dawit  
**Date:** February 3, 2026  

---

## 📌 Project Overview
This project delivers a comprehensive forecasting system tracking Ethiopia's digital financial transformation. As a Data Scientist for **Selam Analytics**, I have developed a model to predict financial inclusion trajectories for the 2025–2027 period.

The system bridges the gap between sparse triennial survey data (Global Findex) and high-frequency market events. By quantifying the "shocks" of major milestones—such as the **Telebirr launch**, **M-Pesa entry**, and **National ID (Fayda) rollout**—the model provides a scenario-based outlook on Ethiopia's path toward a 60% inclusion rate.

---

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



---

## 📂 Repository Structure

```text
C:.
│   data_enrichment_log.md      # Detailed log of Task 1 data additions
│   README.md                   # Project documentation
│   requirements.txt            # Python dependencies
│
├───.github/workflows           # CI/CD Unit tests
├───dashboard
│       app.py                  # Interactive Streamlit application
│
├───data
│   ├───processed               # Enriched data & Generated forecasts
│   │       ethiopia_fi_enriched.csv
│   │       forecast_access.csv
│   │       forecast_usage.csv
│   └───raw                     # Raw unified data & reference codes
│           additional_data_points.csv
│           ethiopia_fi_unified_data.csv
│           reference_codes.csv
│
├───models                      # Saved model artifacts
├───notebooks                   # Task-specific analysis & modeling
│       EDA.ipynb
│       task1_data_exploration.ipynb
│       Task3_Impact_Modeling.ipynb
│       Task4_Forecasting.ipynb
│
├───reports/figures             # Visualizations & Key Findings
│       access_forecast_plot.png
│       impact_association_matrix.png
│       gender_gap_final.png
│       trends_final.png
│
├───src                         # Modular source code
│       eda_utils.py
│       impact_model.py
│       ramp_impact.py
│
└───tests                       # Unit testing suite

```

---

## 📊 Visual Highlights

### Event-Indicator Association

Quantifying how national milestones drive specific financial indicators.

### 2027 Access Forecast

Projected account ownership rates through 2027 with uncertainty bounds.

---

## 🔑 Key Technical Deliverables

* **Event Impact Modeling:** Developed a "Ramp-up" model in `src/ramp_impact.py` to calculate the time-lagged effect of policy changes.
* **Scenario Generation:** Projections for 2025–2027 covering **Base, Optimistic, and Pessimistic** economic outlooks.
* **Gender Analysis:** Identified a persistent ~15pp gender gap in account ownership through longitudinal EDA.

## 📈 Summary of Insights

* **The 60% Threshold:** Ethiopia is projected to hit the national target of 60% account ownership by late 2027 only under the **Optimistic Scenario**.
* **Usage Gap:** Digital payment adoption (Usage) currently lags behind Account Ownership (Access), highlighting the need for increased ecosystem interoperability.
* **Primary Catalyst:** Telebirr remains the single largest driver of mobile money penetration, with a modeled impact magnitude of **12.5%**.

---

**Selam Analytics | 10 Academy Financial Inclusion Project**
