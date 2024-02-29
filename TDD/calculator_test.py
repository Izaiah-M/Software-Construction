import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(8, 3), 5)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(5, 3), 15)

    def test_division(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertRaises(ValueError, self.calculator.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
