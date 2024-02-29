
from typing import Union
=======


class Calculator:

    def _init_(self, num1: Union[int, float], num2: Union[int, float]):
        self.num1 = num1
        self.num2 = num2


    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

   
