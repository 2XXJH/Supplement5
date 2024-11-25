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



























def test_should_return_square_root():
    assert square_root(4) == 2
    assert square_root(16) == 4
    assert square_root(0) == 0
    try:
        square_root(-1)
    except ValueError as e:
        assert str(e) == "Cannot calculate square root of a negative number"
