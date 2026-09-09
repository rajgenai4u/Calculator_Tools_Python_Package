# Import core arithmetic functions (add, subtract, multiply, divide, calculate_percentage) 
# from the internal '.arithmetic' module using relative import notation (.)
from .arithmetic import add, subtract, multiply, divide, calculate_percentage

# Import the statistical calculation function 'calculate_average' 
# from the internal '.statistics' module
from .statistics import calculate_average

# Import unit and temperature conversion functions (celsius_to_fahrenheit, fahrenheit_to_celsius, convert_units) 
# from the internal '.converter' module
from .converter import celsius_to_fahrenheit, fahrenheit_to_celsius, convert_units

# Import the custom exception class 'InvalidOperationError' 
# from the internal '.exceptions' module
from .exceptions import InvalidOperationError

# Define the '__all__' dunder variable list, which controls public API exports.
# When a user imports everything using 'from calculator_tools import *', 
# only the specified items in this list will be exposed to the user namespace.
__all__ = [
    "add",                     # Export the addition function
    "subtract",                # Export the subtraction function
    "multiply",                # Export the multiplication function
    "divide",                  # Export the division function
    "calculate_percentage",    # Export the percentage calculation function
    "calculate_average",       # Export the average calculation function
    "celsius_to_fahrenheit",   # Export the Celsius to Fahrenheit conversion function
    "fahrenheit_to_celsius",   # Export the Fahrenheit to Celsius conversion function
    "convert_units",           # Export the general unit converter function
    "InvalidOperationError"    # Export the custom exception class
]
