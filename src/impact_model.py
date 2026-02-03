import pandas as pd
import numpy as np

def estimate_event_impact(indicator, event_type):
    """
    Returns (magnitude, lag_months) based on comparable country evidence
    (e.g., Kenya's M-Pesa or Tanzania's mobile money boom).
    """
    matrix = {
        ('ACC_OWNERSHIP', 'product_launch'): (4.5, 12),  # +4.5pp after 1 year
        ('USG_DIGITAL_PAYMENT', 'policy_change'): (3.0, 6), # +3pp after 6 months
        ('ACC_MM_ACCOUNT', 'product_launch'): (12.0, 24)   # Aggressive MM growth
    }
    return matrix.get((indicator, event_type), (1.0, 12))

# Example Logic for Task 3 Notebook:
# 1. Identify "Pre-Event" trend (2011-2020)
# 2. Identify "Post-Event" actuals (2021-2024)
# 3. The "Residual" (Difference) is your modeled Impact Magnitude.