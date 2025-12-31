from calculator.logic import add, subtract, multiply, divide
import pytest


def test_addition():
    assert add(10, 5) == 15
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtraction():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0


def test_multiplication():
    assert multiply(10, 5) == 50
    assert multiply(-1, 1) == -1


def test_division():
    assert divide(10, 5) == 2
    assert divide(-1, 1) == -1
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
