import unittest
from models.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.addition = Calculator.add(2, 3)
        self.addition_neg = Calculator.add(2, -3)
        self.subtraction = Calculator.subtract(10, 3)
        self.multiplication = Calculator.multiply(2, 3)
        self.multiplication_neg = Calculator.multiply(2, -3)
        self.division = Calculator.divide(6, 3)
        self.division_zero = Calculator.divide(6, 0)

    def test_addition_2_3_result_5(self):
        self.assertEqual(5, self.addition)

    def test_addition_2_neg3_result_5(self):
        self.assertEqual(-1, self.addition_neg)

    def test_subtraction_10_3_result_7(self):
        self.assertEqual(7, self.subtraction)

    def test_multiplication_2_3_result_6(self):
        self.assertEqual(6, self.multiplication)

    def test_multiplication_2_neg_3_result_6(self):
        self.assertEqual(-6, self.multiplication_neg)

    def test_division_6_3_result_2(self):
        self.assertEqual(2, self.division)

    def test_division_6_0_result_0(self):
        self.assertEqual("cannot divide by zero", self.division_zero)
