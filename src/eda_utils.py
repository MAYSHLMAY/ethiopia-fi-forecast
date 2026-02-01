# src/eda_utils.py
import pandas as pd

def calculate_sparsity(df):
    """Calculates the percentage of missing indicator-year combinations."""
    pivot = df.pivot_table(index='indicator_code', columns='year', values='value_numeric', aggfunc='count').fillna(0)
    return round(((pivot == 0).sum().sum() / pivot.size) * 100, 2)

def get_gender_gap(df):
    """Extracts the latest gender gap percentage points."""
    gender_df = df[df['gender'].isin(['male', 'female'])]
    latest_year = gender_df['observation_date'].dt.year.max()
    latest = gender_df[gender_df['observation_date'].dt.year == latest_year]
    male = latest[latest['gender'] == 'male']['value_numeric'].values[0]
    female = latest[latest['gender'] == 'female']['value_numeric'].values[0]
    return male - female