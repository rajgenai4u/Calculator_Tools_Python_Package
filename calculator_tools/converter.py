# Import custom InvalidOperationError exception from the internal '.exceptions' module
from .exceptions import InvalidOperationError

# Define a private helper function to validate that an input argument is numeric
def _validate_numeric(value):
    # Check if the value is NOT an integer or float
    if not isinstance(value, (int, float)):
        # Raise a TypeError specifying the invalid input's type name
        raise TypeError(f"Expected numeric input, got {type(value).__name__}")

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Validate that the Celsius value is numeric
    _validate_numeric(celsius)
    # Calculate and return temperature in Fahrenheit using the conversion formula: (C * 9/5) + 32
    return (celsius * 9/5) + 32

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    # Validate that the Fahrenheit value is numeric
    _validate_numeric(fahrenheit)
    # Calculate and return temperature in Celsius using the conversion formula: (F - 32) * 5/9
    return (fahrenheit - 32) * 5/9

# General unit conversion function for distance and weight units
def convert_units(value, unit_from, unit_to):
    # Validate that the input numeric value is an integer or float
    _validate_numeric(value)
    # Convert starting unit to string and normalize it to lowercase
    unit_from = str(unit_from).lower()
    # Convert target unit to string and normalize it to lowercase
    unit_to = str(unit_to).lower()

    # Dictionary defining supported conversion formulas mapped by unit tuple pairs
    conversions = {
        ("km", "miles"): value * 0.621371, # Kilometers to miles calculation
        ("miles", "km"): value / 0.621371, # Miles to kilometers calculation
        ("kg", "lbs"): value * 2.20462,    # Kilograms to pounds calculation
        ("lbs", "kg"): value / 2.20462,    # Pounds to kilograms calculation
    }

    # Return the original value unchanged if source and destination units are identical
    if unit_from == unit_to:
        return value

    # Create a lookup tuple key from source and target units
    key = (unit_from, unit_to)
    # Check if the unit conversion pair exists in the dictionary
    if key in conversions:
        # Return the converted numeric result from the dictionary lookup
        return conversions[key]

    # Raise a custom exception if the requested unit pair is not supported
    raise InvalidOperationError(f"Unsupported unit conversion from '{unit_from}' to '{unit_to}'.")
