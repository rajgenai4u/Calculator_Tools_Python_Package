from .exceptions import InvalidOperationError

def _validate_numeric(value):
    if not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric input, got {type(value).__name__}")

def celsius_to_fahrenheit(celsius):
    _validate_numeric(celsius)
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    _validate_numeric(fahrenheit)
    return (fahrenheit - 32) * 5/9

def convert_units(value, unit_from, unit_to):
    _validate_numeric(value)
    unit_from = str(unit_from).lower()
    unit_to = str(unit_to).lower()
    
    conversions = {
        ("km", "miles"): value * 0.621371,
        ("miles", "km"): value / 0.621371,
        ("kg", "lbs"): value * 2.20462,
        ("lbs", "kg"): value / 2.20462,
    }
    
    if unit_from == unit_to:
        return value
        
    key = (unit_from, unit_to)
    if key in conversions:
        return conversions[key]
        
    raise InvalidOperationError(f"Unsupported unit conversion from '{unit_from}' to '{unit_to}'.")