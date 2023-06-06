#!/usr/bin/python3
"""defines a square"""


class Square:
    """ square with private instance attrbute """

    def __init__(self, size=0):
        """
        initializes a square
        Args:
            size:size of the side of the square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an interger')

    def area(self)
        """
        finds area of a square
        Returns:
                the area of a square
        """

        return self.__size ** 2
