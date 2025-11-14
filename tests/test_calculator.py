"""Unit Tests for the calculator application to perform basic Calculations"""
import pytest
from calculator_app.calculator import Calculator

class TestCalculator:
    """A test of the calculator class to enable various functions"""
    @pytest.fixture
    def calculator(self):
        """Creating a calculator"""
        return Calculator()

    def test_add(self, calculator):
        """A test of the add function"""
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0

    def test_subtract(self, calculator):
        """A test of the subtract function"""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(0, 1) == -1

    
    def test_multiply(self, calculator):
        """A test of the multiply function"""
        assert calculator.multiply(4, 3) == 12
        assert calculator.multiply(-1, 5) == -5

    
    def test_divide(self, calculator):
        """A test of the divide function"""
        assert calculator.divide(10, 2) == 5
        assert calculator.divide(9, 3) == 3

    def test_divide_by_zero(self, calculator):
        """A test to check division by zero"""
        with pytest.raises(ValueError) as excinfo:
            calculator.divide(5, 0)
        assert str(excinfo.value) == "Cannot divide by zero."
