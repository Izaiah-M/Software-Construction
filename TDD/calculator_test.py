#Red Phase

import unittest
from calculator import Calculator  # Importing the Calculator class from calculator.py

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()  # Creating an instance of the Calculator class for each test method

    def test_addition(self):
        # Testing the addition method of the Calculator class
        self.assertEqual(self.calculator.add(7, 3), 10)  # Asserting that 7 + 3 equals 10

    def test_subtraction(self):
        # Testing the subtraction method of the Calculator class
        self.assertEqual(self.calculator.subtract(4, 2), 2)  # Asserting that 4 - 2 equals 2

    def test_multiplication(self):
        # Testing the multiplication method of the Calculator class
        self.assertEqual(self.calculator.multiply(5, 4), 20)  # Asserting that 5 * 4 equals 20

    def test_division(self):
        # Testing the division method of the Calculator class
        self.assertEqual(self.calculator.divide(14, 2), 7)  # Asserting that 14 / 2 equals 7
        # Asserting that dividing by 0 raises a ValueError
        self.assertRaises(ValueError, self.calculator.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()  # Running the tests if the script is executed directly
