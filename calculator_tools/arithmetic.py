# Import custom InvalidOperationError exception from the internal '.exceptions' module
from .exceptions import InvalidOperationError

# Define a private helper function to validate that all passed arguments are numeric
def _validate_numeric(*args):
    # Iterate through every argument passed to the function
    for arg in args:
        # Check if the current argument is NOT an integer or float
        if not isinstance(arg, (int, float)):
            # Raise a TypeError specifying the invalid argument's type name
            raise TypeError(f"Expected numeric input, got {type(arg).__name__}")

# Function to add two numbers together
def add(a, b):
    # Ensure both 'a' and 'b' are numeric values
    _validate_numeric(a, b)
    # Return the sum of 'a' and 'b'
    return a + b

# Function to subtract the second number from the first
def subtract(a, b):
    # Ensure both 'a' and 'b' are numeric values
    _validate_numeric(a, b)
    # Return the difference of 'a' minus 'b'
    return a - b

# Function to multiply two numbers together
def multiply(a, b):
    # Ensure both 'a' and 'b' are numeric values
    _validate_numeric(a, b)
    # Return the product of 'a' and 'b'
    return a * b

# Function to divide the first number by the second
def divide(a, b):
    # Ensure both 'a' and 'b' are numeric values
    _validate_numeric(a, b)
    # Check if the divisor is zero
    if b == 0:
        # Raise custom exception to prevent division by zero
        raise InvalidOperationError("Cannot divide by zero.")
    # Return the quotient of 'a' divided by 'b'
    return a / b

# Function to calculate what percentage 'part' is of 'total'
def calculate_percentage(part, total):
    # Ensure both 'part' and 'total' are numeric values
    _validate_numeric(part, total)
    # Check if total is zero to prevent division by zero in percentage calculation
    if total == 0:
        # Raise custom exception when total is zero
        raise InvalidOperationError("Total cannot be zero when calculating percentage.")
    # Check if either 'part' or 'total' is negative
    if part < 0 or total < 0:
        # Raise ValueError for negative input values
        raise ValueError("Values for percentage calculation must be non-negative.")
    # Return calculated percentage value
    return (part / total) * 100
