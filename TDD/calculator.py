# Green Phase

# Importing the unittest module for later use in testing
import unittest

# Defining the Calculator class
class Calculator:
    # Method for addition
    def add(self, x, y):
        return x + y

    # Method for subtraction
    def subtract(self, x, y):
        return x - y

    # Method for multiplication
    def multiply(self, x, y):
        return x * y

    # Method for division
    def divide(self, x, y):
        # Handling division by zero case
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y

# Main block to execute when the script is run
if __name__ == '__main__':
    # Creating an instance of the Calculator class
    calc = Calculator()

    # Performing addition and printing the result
    result = calc.add(3, 4)
    print("Addition result: ", result)

    # Performing subtraction and printing the result
    result = calc.subtract(5, 2)
    print("Subtraction result: ", result)

    # Performing multiplication and printing the result
    result = calc.multiply(10, 10)
    print("Multiplication result: ", result)

    # Performing division and printing the result
    result = calc.divide(70, 10)
    print("Division result: ", result)



