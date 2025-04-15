"""
This module provides a simple function to add two numbers and demonstrates its usage.
"""
def add(number1: int, number2: int) -> int:
    """
    Add two numbers and return the result.

    Args:
        number1 (int): The first number to add.
        number2 (int): The second number to add.

    Returns:
        int: The sum of number1 and number2.
    """
    return number1 + number2

NUM1 = 4
NUM2 = 5

TOTAL = add(NUM1, NUM2)

print(f"The sum of {NUM1} and {NUM2} is {TOTAL}")
