"""
statistics.py
-------------
Provides statistical calculation functions for collections of numbers.
"""  # Module-level docstring describing the purpose of this script


# Define a function to calculate the arithmetic mean of a collection of numbers
def calculate_average(numbers):
    """Calculates the arithmetic mean (average) of a list or tuple of numbers.

    Args:
        numbers (iterable): A list or tuple containing numerical values.

    Returns:
        float: The calculated average.

    Raises:
        TypeError: If input is not a list/tuple or contains non-numeric elements.
        ValueError: If the provided list or tuple is empty.
    """  # Function docstring outlining arguments, return type, and raised exceptions

    # Check if the input argument 'numbers' is neither a list nor a tuple
    if not isinstance(numbers, (list, tuple)):
        # Raise a TypeError detailing the invalid container type received
        raise TypeError(
            f"Expected a list or tuple of numbers, got {type(numbers).__name__}"
        )

    # Check if the list or tuple is empty (evaluates to False when empty)
    if not numbers:
        # Raise a ValueError to prevent division by zero on empty sequences
        raise ValueError("Cannot calculate the average of an empty list or tuple.")

    # Iterate through each element in the input collection
    for num in numbers:
        # Verify element is numeric (int or float) and explicitly exclude boolean values (since bool inherits from int)
        if not isinstance(num, (int, float)) or isinstance(num, bool):
            # Raise a TypeError if any element is non-numeric or a boolean
            raise TypeError(
                f"All elements in the collection must be numeric, found: {type(num).__name__}"
            )

    # Calculate and return the arithmetic mean by dividing the sum of all elements by the total count
    return sum(numbers) / len(numbers)
