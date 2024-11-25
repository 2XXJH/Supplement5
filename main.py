import math
import random

def square_root(num):
    """
    Calculate the square root of a number.

    Args:
        num (float): The number for which to calculate the square root. 

    Returns:
        float: The square root of the input number.

    Raises:
        ValueError: If the input number is negative.
    """
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(num)

def process_random_integer():
    """
    Generate and process a random integer between 1 and 100 based on specific rules:
        - If odd, multiply by 2.
        - If divisible by 3, divide by 3.
        - If divisible by 4, multiply by 4.
        - If the result exceeds 4, raise an exception.

    Returns:
        float or int: The processed number if valid.

    Raises:
        ValueError: If the processed number exceeds 4.

        >>> process_random_integer()
        Raises ValueError or returns a processed number within the range.
    """
    num = random.randint(1, 100)

    if num % 2 == 1:
        num *= 2
    if num % 3 == 0:
        num /= 3
    if num % 4 == 0:
        num *= 4
    if num > 4:
        raise ValueError("Number exceeds the allowed limit after processing.")
    return num

























def test_should_return_square_root():
    assert square_root(4) == 2
    assert square_root(16) == 4
    assert square_root(0) == 0
    try:
        square_root(-1)
    except ValueError as e:
        assert str(e) == "Cannot calculate square root of a negative number"

def test_should_return_process_random_integer(monkeypatch):
    monkeypatch.setattr(random, 'randint', lambda a, b: 5)  
    try:
        process_random_integer()
    except ValueError as e:
        assert str(e) == "Number exceeds the allowed limit after processing."

    monkeypatch.setattr(random, 'randint', lambda a, b: 3)  
    assert process_random_integer() == 2.0

def test_find_divisors():
    assert find_divisors(10) == [1, 2, 5, 10]
    assert find_divisors(6) == [1, 2, 3, 6]
    assert find_divisors(1) == [1]
    try:
        find_divisors("string")
    except TypeError as e:
        assert str(e) == "Input must be an integer"
