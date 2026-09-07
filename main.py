from calculator_tools import (
    add, subtract, multiply, divide, calculate_percentage,
    calculate_average, celsius_to_fahrenheit, fahrenheit_to_celsius,
    convert_units, InvalidOperationError
)

def run_demonstration():
    print("--- 1. Basic Arithmetic ---")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
    print("20 out of 50 is:", calculate_percentage(20, 50), "%")

    print("\n--- 2. Statistics ---")
    dataset = [12, 18, 24, 30]
    print(f"Average of {dataset}:", calculate_average(dataset))

    print("\n--- 3. Conversions ---")
    print("0°C to °F:", celsius_to_fahrenheit(0))
    print("100°F to °C:", round(fahrenheit_to_celsius(100), 2))
    print("5 km to miles:", round(convert_units(5, "km", "miles"), 2))
    print("150 lbs to kg:", round(convert_units(150, "lbs", "kg"), 2))

    print("\n--- 4. Error Handling Demonstrations ---")
    
    # Division by Zero
    try:
        divide(10, 0)
    except InvalidOperationError as e:
        print("[Caught InvalidOperationError]:", e)

    # Invalid Data Type
    try:
        add(10, "five")
    except TypeError as e:
        print("[Caught TypeError]:", e)

    # Unsupported Conversion
    try:
        convert_units(10, "km", "liters")
    except InvalidOperationError as e:
        print("[Caught InvalidOperationError]:", e)

    # Empty sequence average
    try:
        calculate_average([])
    except ValueError as e:
        print("[Caught ValueError]:", e)

if __name__ == "__main__":
    run_demonstration()