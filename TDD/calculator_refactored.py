
from typing import Union

class Calculator:
    def __init__(self, num1: Union[int, float], num2: Union[int, float]):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
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
