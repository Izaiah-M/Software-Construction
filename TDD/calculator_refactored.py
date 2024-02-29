#Refactor Phase
from typing import Union

class Calculator:
    def __init__(self, num1: Union[int, float], num2: Union[int, float]):

        """Initialize a Calculator object with two numeric values."""
        self.num1 = num1  # Assign the first numeric value to the instance variable num1
        self.num2 = num2  # Assign the second numeric value to the instance variable num2

    def add(self):
        """Add the two numbers."""
        return self.num1 + self.num2

    def subtract(self):
        """Subtract the second number from the first."""
        return self.num1 - self.num2

    def multiply(self):
        """Multiply the two numbers."""
        return self.num1 * self.num2

    def divide(self):
        """Divide the first number by the second."""
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return self.num1 / self.num2
    

if __name__ == "__main__":
    calc = Calculator(2, 5.5)

    add = calc.add()
    print(f"Added {calc.num1} and {calc.num2} to get: {add}")

    subtract = calc.subtract()
    print(f"Subtracted {calc.num1} and {calc.num2} to get: {subtract}")
    
    divide = calc.divide()
    print(f"Divided {calc.num1} and {calc.num2} to get: {divide}")

    multiply = calc.multiply()
    print(f"Multiplied {calc.num1} and {calc.num2} to get: {multiply}")
