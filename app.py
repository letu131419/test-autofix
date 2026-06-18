"""Simple calculator app with a known bug."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b  # float division

def pow(a, b):
    """Return a raised to the power of b."""
    return a ** b
