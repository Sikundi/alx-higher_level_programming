#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
