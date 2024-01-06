import unittest

from interest_module import *

class TestInterestModule(unittest.TestCase):

    def test_compound_positive_values(self):
        initial_value = 1000
        interest_rate = 0.05
        num_periods = 5
        result = round(compound(initial_value, interest_rate, num_periods),2)
        expected_result = 1276.28
        self.assertEquals(result, expected_result)

    def test_compound_negative_values(self):
        initial_value = -500
        interest_rate = 0.1
        num_periods = 3
        result = round(compound(initial_value, interest_rate, num_periods),2)
        exepcted_result = -665.50
        self.assertEquals(result, exepcted_result)

if __name__ == '__main__':
    unittest.main()