"""
A module containing generic mathematics functions.

    Author:
        James

    Version:
        1.0.0
"""


def iseven(number):
    """
    Determines whether the argument is an even number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if it is even, False if not.
    """
    return number % 2 == 0
