# Forecasting Financial Inclusion in Ethiopia

**Project Status:** Interim Submission (Task 1 & 2 Complete)  
**Author:** Mikiyas Dawit
**Date:** February 2026

---

## 📌 Project Overview
This project aims to build a forecasting system that tracks and predicts Ethiopia's digital financial transformation. Working as a Data Scientist for **Selam Analytics**, the goal is to forecast two core dimensions of financial inclusion for the years 2025–2027:
1.  **Access:** Account Ownership Rate (% of adults)
2.  **Usage:** Digital Payment Adoption Rate (% of adults)

The system utilizes a **Unified Schema** to combine sparse survey data (Global Findex) with high-frequency event data (product launches, policy changes) to model the impact of "shocks" like the Telebirr launch and M-Pesa market entry.

## 📂 Repository Structure
```text
ethiopia-fi-forecast/
├── data/
│   ├── raw/
│   │   └── ethiopia_fi_unified_data.csv   # The enriched dataset (Task 1)
│   └── reference_codes.csv                # Schema definitions
├── notebooks/
│   └── EDA.ipynb                          # Exploratory Data Analysis (Task 2)
├── reports/
│   ├── figures/                           # Generated PNG visualizations
│   └── Interim_Report.pdf                 # Final PDF Report
├── data_enrichment_log.md                 # Log of added data points
├── README.md                              # Project documentation
└── requirements.txt                       # Python dependencies
