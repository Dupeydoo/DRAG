"""
A module containing generic mathematics functions.

    Author:
        James

    Version:
        1.0.0
"""


def is_even(number):
    """
    Determines whether the argument is an even number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if it is even, False if not.
    """
    return number % 2 == 0


if __name__ == "__main__":
    from DRAGTests.integrityscripts import integritydragmaths

    integritydragmaths.integrity_drag_maths()
