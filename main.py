# Import specific functions and custom exceptions from the 'calculator_tools' package
from calculator_tools import (
    add,                   # Function to handle addition of two numbers
    subtract,              # Function to handle subtraction of two numbers
    multiply,              # Function to handle multiplication of two numbers
    divide,                # Function to handle division of two numbers
    calculate_percentage,  # Function to calculate percentage values
    calculate_average,     # Function to compute the average of a list/dataset
    celsius_to_fahrenheit, # Function to convert Celsius to Fahrenheit
    fahrenheit_to_celsius, # Function to convert Fahrenheit to Celsius
    convert_units,         # Utility function for unit conversions (e.g., km to miles)
    InvalidOperationError  # Custom exception class for handling invalid mathematical operations
)

# Define the primary demonstration function that executes test cases
def run_demonstration():
    # Print section header for basic arithmetic operations
    print("--- 1. Basic Arithmetic ---")
    
    # Call add(10, 5) and print the sum (15)
    print("10 + 5 =", add(10, 5))
    
    # Call subtract(10, 5) and print the result (5)
    print("10 - 5 =", subtract(10, 5))
    
    # Call multiply(10, 5) and print the product (50)
    print("10 * 5 =", multiply(10, 5))
    
    # Call divide(10, 5) and print the quotient (2.0)
    print("10 / 5 =", divide(10, 5))
    
    # Calculate what percentage 20 is of 50 using calculate_percentage(20, 50) and print (40.0 %)
    print("20 out of 50 is:", calculate_percentage(20, 50), "%")

    # Print section header for statistical operations
    print("\n--- 2. Statistics ---")
    
    # Define a list of numerical values to use as a dataset
    dataset = [12, 18, 24, 30]
    
    # Compute and print the average of the dataset list (21.0) using calculate_average()
    print(f"Average of {dataset}:", calculate_average(dataset))

    # Print section header for unit conversion functions
    print("\n--- 3. Conversions ---")
    
    # Convert 0°C to Fahrenheit using celsius_to_fahrenheit(0) and print (32.0)
    print("0°C to °F:", celsius_to_fahrenheit(0))
    
    # Convert 100°F to Celsius, round the result to 2 decimal places, and print (37.78)
    print("100°F to °C:", round(fahrenheit_to_celsius(100), 2))
    
    # Convert 5 km to miles using convert_units(), round to 2 decimal places, and print (3.11)
    print("5 km to miles:", round(convert_units(5, "km", "miles"), 2))
    
    # Convert 150 lbs to kg using convert_units(), round to 2 decimal places, and print (68.04)
    print("150 lbs to kg:", round(convert_units(150, "lbs", "kg"), 2))

    # Print section header for error handling test cases
    print("\n--- 4. Error Handling Demonstrations ---")

    # Test handling for division by zero
    try:
        divide(10, 0)  # Attempt to divide 10 by 0, which should raise InvalidOperationError
    except InvalidOperationError as e:
        # Catch and display the custom InvalidOperationError message
        print("[Caught InvalidOperationError]:", e)

    # Test handling for invalid data types
    try:
        add(10, "five")  # Attempt to add an integer and a string, which should raise TypeError
    except TypeError as e:
        # Catch and display the standard Python TypeError message
        print("[Caught TypeError]:", e)

    # Test handling for incompatible unit conversions
    try:
        convert_units(10, "km", "liters")  # Attempt distance-to-volume conversion
    except InvalidOperationError as e:
        # Catch and display the custom InvalidOperationError message
        print("[Caught InvalidOperationError]:", e)

    # Test handling for empty dataset statistical calculations
    try:
        calculate_average([])  # Attempt to find average of an empty list, which should raise ValueError
    except ValueError as e:
        # Catch and display the standard ValueError message
        print("[Caught ValueError]:", e)

# Standard Python boilerplate check to verify if the file is being run directly as a script
if __name__ == "__main__":
    # Execute the demonstration function when run directly
    run_demonstration()
