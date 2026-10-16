import pytest

from calculator import add, subtract, multiply, divide, calculate


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_calculate_addition():
    assert calculate(10, "+", 5) == 15


def test_calculate_subtraction():
    assert calculate(10, "-", 5) == 5


def test_calculate_multiplication():
    assert calculate(10, "*", 5) == 50


def test_calculate_division():
    assert calculate(10, "/", 5) == 2


def test_invalid_operator():
    with pytest.raises(ValueError):
        calculate(10, "%", 5)