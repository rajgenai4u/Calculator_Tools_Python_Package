"""
statistics.py
-------------
Provides statistical calculation functions for collections of numbers.
"""

def calculate_average(numbers):
    """
    Calculates the arithmetic mean (average) of a list or tuple of numbers.
    
    Args:
        numbers (iterable): A list or tuple containing numerical values.
        
    Returns:
        float: The calculated average.
        
    Raises:
        TypeError: If input is not a list/tuple or contains non-numeric elements.
        ValueError: If the provided list or tuple is empty.
    """
    # Validate container type
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(f"Expected a list or tuple of numbers, got {type(numbers).__name__}")
        
    # Handle invalid empty list/tuple
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list or tuple.")
    
    # Validate each element inside the sequence
    for num in numbers:
        if not isinstance(num, (int, float)) or isinstance(num, bool):
            raise TypeError(f"All elements in the collection must be numeric, found: {type(num).__name__}")
            
    return sum(numbers) / len(numbers)