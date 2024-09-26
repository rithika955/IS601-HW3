import pytest
from calculator import add, subtract, multiply, divide
from typing import Callable, List, Union

class Operation:
    """Base class for operations, utilizing polymorphism for extendability."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> Union[float, str]:
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"


class Calculation:
    """Encapsulates a single calculation, storing the operation and its operands."""
    
    def __init__(self, a: float, b: float, operation: Callable[[float, float], Union[float, str]]):
        self.a = a
        self.b = b
        self.operation = operation
        self.result = None

    def compute(self) -> Union[float, str]:
        """Executes the calculation and stores the result."""
        self.result = self.operation(self.a, self.b)
        return self.result

    def __repr__(self) -> str:
        """Custom string representation to show the operation and result."""
        operation_name = self.operation.__name__.capitalize()
        return f"{operation_name}({self.a}, {self.b}) = {self.result}"


class CalculationsHistory:
    """Manages a history of calculations."""
    
    history: List[Calculation] = []
    
    @classmethod
    def add_history(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()


class Calculator:
    """Integrates components to perform calculations and manage history."""
    
    def perform_calculation(self, a: float, b: float, operation: Callable[[float, float], Union[float, str]]) -> Union[float, str]:
        """Perform the calculation, store it in history, and return the result."""
        calculation = Calculation(a, b, operation)
        result = calculation.compute()
        CalculationsHistory.add_history(calculation)
        return result

    def get_calculation_history(self) -> List[Calculation]:
        """Retrieve the calculation history."""
        return CalculationsHistory.get_history()

    def clear_history(self) -> None:
        """Clear the calculation history."""
        CalculationsHistory.clear_history()


# Test cases
@pytest.fixture
def calculator():
    """creating a Calculator instance."""
    calc = Calculator()
    calc.clear_history()  # Ensure history is cleared at the start of each test
    return calc

def test_add(calculator):
    result = calculator.perform_calculation(3, 2, Operation.add)
    assert result == 5, f"Expected 5 but got {result}"
    assert calculator.get_calculation_history()[-1].result == 5, "Add operation failed"

def test_subtract(calculator):
    result = calculator.perform_calculation(10, 4, Operation.subtract)
    assert result == 6, f"Expected 6 but got {result}"
    assert calculator.get_calculation_history()[-1].result == 6, "Subtract operation failed"

def test_multiply(calculator):
    result = calculator.perform_calculation(6, 5, Operation.multiply)
    assert result == 30, f"Expected 30 but got {result}"
    assert calculator.get_calculation_history()[-1].result == 30, "Multiply operation failed"

def test_divide(calculator):
    result = calculator.perform_calculation(10, 2, Operation.divide)
    assert result == 5.0, f"Expected 5.0 but got {result}"
    assert calculator.get_calculation_history()[-1].result == 5.0, "Divide operation failed"

def test_divide_by_zero(calculator):
    result = calculator.perform_calculation(10, 0, Operation.divide)
    assert result == "Error: Division by zero", "Expected error message for division by zero"
    assert calculator.get_calculation_history()[-1].result == "Error: Division by zero", "Division by zero test failed"

def test_get_calculation_history(calculator):
    calculator.perform_calculation(3, 2, Operation.add)
    calculator.perform_calculation(10, 5, Operation.subtract)
    history = calculator.get_calculation_history()
    
    assert len(history) == 2, "History should contain 2 calculations"
    assert history[0].result == 5, "First calculation result should be 5"
    assert history[1].result == 5, "Second calculation result should be 5"

def test_clear_history(calculator):
    calculator.perform_calculation(3, 2, Operation.add)
    calculator.clear_history()
    assert calculator.get_calculation_history() == [], "History should be empty after clearing"


pytest.main()
