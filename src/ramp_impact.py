def calculate_ramp_impact(current_date, event_date, magnitude, lag_months=12):
    """
    Calculates the impact of an event at a specific point in time.
    Impact is 0 before event_date and reaches full magnitude after lag_months.
    """
    months_passed = (current_date.year - event_date.year) * 12 + (current_date.month - event_date.month)
    
    if months_passed < 0:
        return 0
    elif months_passed >= lag_months:
        return magnitude
    else:
        return magnitude * (months_passed / lag_months)

# Example: Telebirr (May 2021) impact on Dec 2022
import datetime
impact_val = calculate_ramp_impact(datetime.datetime(2022, 12, 31), datetime.datetime(2021, 5, 17), 12.5)
print(f"Modeled Impact of Telebirr by end of 2022: {impact_val:.2f} percentage points")