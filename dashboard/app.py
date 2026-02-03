import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Ethiopia FI Forecast", layout="wide")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    access_df = pd.read_csv("data/processed/forecast_access.csv")
    usage_df = pd.read_csv("data/processed/forecast_usage.csv")
    return access_df, usage_df

try:
    df_access, df_usage = load_data()
except Exception as e:
    st.error("Make sure your forecast CSVs are in data/processed/")
    st.stop()

# --- SIDEBAR CONTROLS ---
st.sidebar.title("🎛️ Control Panel")
selected_scenario = st.sidebar.selectbox(
    "Select Economic Scenario", 
    ["base", "opt", "pess"], 
    format_func=lambda x: x.capitalize()
)

# --- HEADER SECTION ---
st.title("🇪🇹 Ethiopia Financial Inclusion Forecasting System")
st.markdown("### Decision Support Tool for Selam Analytics Consortium")

col1, col2, col3 = st.columns(3)
# Dynamic metrics based on your forecast data
final_val = df_access[df_access['Year'] == 2027][selected_scenario].values[0]
col1.metric("2024 Baseline (Access)", "49%", "Findex Source")
col2.metric(f"2027 Project ({selected_scenario.upper()})", f"{final_val}%", f"{round(final_val - 49.0, 1)}% Growth")
col3.metric("Target Goal", "60%", "National Strategy", delta_color="normal")

# --- MAIN CONTENT ---
tab1, tab2, tab3 = st.tabs(["📈 Interactive Forecasts", "📊 Impact Analysis", "📑 Strategic Report"])

with tab1:
    st.subheader(f"Projected Growth: {selected_scenario.capitalize()} Scenario")
    
    # Let's plot both Access and Usage on one interactive Plotly chart
    plot_df = pd.DataFrame({
        'Year': df_access['Year'],
        'Account Ownership (Access)': df_access[selected_scenario],
        'Digital Payments (Usage)': df_usage[selected_scenario]
    })
    
    fig = px.line(plot_df, x='Year', y=['Account Ownership (Access)', 'Digital Payments (Usage)'],
                  markers=True, template="plotly_white",
                  title=f"Forecast Trends for {selected_scenario.capitalize()} Case")
    
    fig.update_layout(yaxis_title="Percentage (%)", hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)
    
    # Download Button for the CSV
    st.download_button(
        label="📥 Download Forecast Data (CSV)",
        data=df_access.to_csv(index=False),
        file_name=f"ethiopia_forecast_{selected_scenario}.csv",
        mime="text/csv"
    )

with tab2:
    st.subheader("Event-Indicator Association Matrix")
    # Using your saved image from Task 3
    if os.path.exists("reports/figures/task3_association_matrix.png"):
        st.image("reports/figures/task3_association_matrix.png")
    else:
        st.warning("Association Matrix image not found in reports/figures/")
    
    st.write("**Analysis:** Events like 'Telebirr Launch' and 'M-Pesa Entry' provide the shocks required to move the baseline above 50%.")

with tab3:
    st.subheader("Executive Insights")
    st.markdown("""
    * **The 60% Target:** Only the **Optimistic** scenario reaches the 60% goal by 2027.
    * **Leading Drivers:** Mobile money (Telebirr/M-Pesa) is the strongest catalyst for new account ownership.
    * **Gender Gap:** Structural barriers persist; gender-neutral policies are insufficient to close the ~15pp gap.
    """)

st.divider()