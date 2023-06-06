#!/usr/bin/python3
"""defines a square"""


class Square:
    """Square with the private instance attribute size"""

    def __init__(self, size=0):
        """
        Args:
            size: size of the square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('Size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('Size must be an interger')
