import pytest
from app import add, subtract, multiply, divide, pow

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(-3, -4) == 12
    assert multiply(5, -2) == -10

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_pow_positive():
    assert pow(2, 3) == 8
    assert pow(3, 2) == 9
    assert pow(10, 0) == 1

def test_pow_zero():
    assert pow(0, 5) == 0
    assert pow(0, 0) == 1

def test_pow_negative_base():
    assert pow(-2, 3) == -8
    assert pow(-2, 2) == 4
