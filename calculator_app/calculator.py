"""A Calculator Application to perform basic Calculations"""
class Calculator:
    """A Class of the calculator to enable various functions"""
    def add(self, a, b):
        """Returns the the sum of two added numbers"""
        return a + b

    def subtract(self, a, b):
        """Returns the result after subtracting two numbers"""
        return a - b

    def multiply(self, a, b):
        """Returns the multiple of two numbers"""
        return a * b

    def divide(self, a, b):
        """Returns the division of two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
