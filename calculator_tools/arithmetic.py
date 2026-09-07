from .exceptions import InvalidOperationError

def _validate_numeric(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"Expected numeric input, got {type(arg).__name__}")

def add(a, b):
    _validate_numeric(a, b)
    return a + b

def subtract(a, b):
    _validate_numeric(a, b)
    return a - b

def multiply(a, b):
    _validate_numeric(a, b)
    return a * b

def divide(a, b):
    _validate_numeric(a, b)
    if b == 0:
        raise InvalidOperationError("Cannot divide by zero.")
    return a / b

def calculate_percentage(part, total):
    _validate_numeric(part, total)
    if total == 0:
        raise InvalidOperationError("Total cannot be zero when calculating percentage.")
    if part < 0 or total < 0:
        raise ValueError("Values for percentage calculation must be non-negative.")
    return (part / total) * 100