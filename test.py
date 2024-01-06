import unittest

from interest_module import *

class TestInterestModule(unittest.TestCase):

    # tests for compound(pv, r, n)
    def test_compound_positive_values(self):
        initial_value = 1000
        interest_rate = 0.05
        num_periods = 5
        result = round(compound(initial_value, interest_rate, num_periods),2)
        expected_result = 1276.28
        self.assertEqual(result, expected_result)
    def test_compound_negative_values(self):
        initial_value = -500
        interest_rate = 0.1
        num_periods = 3
        result = round(compound(initial_value, interest_rate, num_periods),2)
        exepcted_result = -665.50
        self.assertEqual(result, exepcted_result)

    # tests for discount(fv, r, n)
    def test_discount_positive_values(self):
        initial_value = 1276.28
        interest_rate = 0.05
        num_periods = 5
        result = round(discount(initial_value, interest_rate, num_periods),2)
        expected_result = 1000.00
        self.assertEqual(result, expected_result)
    def test_discount_negative_values(self):
        initial_value = -665.50
        interest_rate = 0.1
        num_periods = 3
        result = round(discount(initial_value, interest_rate, num_periods),2)
        expected_result = -500.00
        self.assertEqual(result, expected_result)

    # tests for calculate_effective_annual_rate(r, n, c)
    def test_calculate_effective_annual_rate(self):
        apr = 0.05
        periods = 12
        cash_flows = 12
        result = round(calculate_effective_annual_rate(apr, periods, cash_flows),4)
        expected_result = 0.0512
        self.assertEqual(result, expected_result)

    # tests for present_value(cash_flows, r, n=0)
    def test_present_value(self):
        cash_flows = [100,200,150]
        discount_rate = 0.05
        result = round(present_value_of_stream(cash_flows, discount_rate),2)
        expected_result = 426.53
        self.assertEqual(result, expected_result)

    # tests for future_value(cash_flows, r, n=0)
    def test_present_value(self):
        cash_flows = [100,200,150]
        interest_rate = 0.05
        result = round(future_value_of_stream(cash_flows, interest_rate),2)
        expected_result = 470.25
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()