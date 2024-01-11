from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, name):
        self.name = name

    # REQUIRES: pv > 0, r >= 0
    # EFFECT: calculates future value of a cash flow given an interest rate and number of periods 
    def compound(pv, r, n):
        return pv * (1+r)**n

    # REQUIRES: fv > 0, r >= 0
    # EFFECT: calculates present value of future cash flow given an interest rate and number of periods
    def discount(fv, r, n):
        return fv * 1/((1+r)**n)

'''
    # REQUIRES: r > 0, n >= 1
    # EFFECT: calculates EAR using APR, number of periods, and cash flows per year
    def calculate_effective_annual_rate(r, n, c):
        return (1 + (r/n))**n - 1

    # REQUIRES: collection of double called cash_flows, r > 0
    # EFFECT: use the discount method recursively to find the present value of cash flow streams
    def present_value_of_stream(cash_flows, r, n=0):
        # Returns 0 if there are no more cash flows
        if n >= len(cash_flows):
            return 0
        
        # Calculates PV for current period, recursively calls method with increased period
        pv_current = discount(cash_flows[n], r, n)
        pv_remaining = present_value_of_stream(cash_flows, r, n+1)
        
        # Add all the periods and return total_pv
        total_pv = pv_current + pv_remaining
        return total_pv

    # REQUIRES: collection of double called cash_flows, r > 0
    # EFFECT: iterate through list of cash_flows and compound each cash flow to get future value
    def future_value_of_stream(cash_flows, r):
        fv_total = 0
        n = len(cash_flows)

        for i in range(n):
            # number of periods from current cash flow to end
            periods = n - i - 1
            
            # Calculate future value of each cash flow
            fv = compound(cash_flows[i], r, periods)
            fv_total += fv
        
        return fv_total
'''

