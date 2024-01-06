'''
Variables:
fv = future
pv = present value
r = interest rate
c = cash flow
n = number of periods
'''
# REQUIRES: pv > 0, r >= 0
# EFFECT: calculates future value of a cash flow given an interest rate and number of periods 
def compound(pv, r, n):
    return pv * (1+r)**n

# REQUIRES: fv > 0, r >= 0
# EFFECT: calculates present value of future cash flow given an interest rate and number of periods
def discount(fv, r, n):
    return fv * 1/((1+r)**n)

# REQUIRES: r > 0, n >= 1
# EFFECT: calculates EAR using APR, number of periods, and cash flows per year
def calculate_effective_annual_rate(r, n, c):
    return (1 + (r/n))**n - 1

# REQUIRES: collection of double called cash_flows, r > 0
# EFFECT: use the discount method recursively to find the present value of cash flow streams
def present_value(cash_flows, r, n=0):
    # Returns 0 if there are no more cash flows
    if n >= len(cash_flows):
        return 0
    
    # Calculates PV for current period, recursively calls method with increased period
    pv_current = discount(cash_flows[n], r, n)
    pv_remaining = present_value(cash_flows, r, n+1)
    
    # Add all the periods and return total_pv
    total_pv = pv_current + pv_remaining
    return total_pv