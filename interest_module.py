# REQUIRES: initialValue > 0, interestRate > 0, numPeriods > 0
# EFFECT: calculates future value of compounding cash flows
def compound(initial_value, interest_rate, num_periods):
    return initial_value * (1+interest_rate)**num_periods

# REQUIRES: initialValue > 0, interestRate > 0, numPeriods > 0
# EFFECT: calculates present value of future cash flow
def discount(future_value, interest_rate, num_periods):
    return future_value * 1/(1+interest_rate)**num_periods

# REQUIRES: apr > 0, periods > 0, cash_flows > 0
# EFFECT: calculates EAR using APR, number of periods, and cash flows per year
def calculate_effective_annual_rate(apr, periods, cash_flows):
    return (1 + apr/periods)**(periods) - 1