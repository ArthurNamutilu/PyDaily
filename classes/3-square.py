#!/usr/bin/python3
""" Square class """


class Square:
    """ A class representing a square"""

    def __init__(self, size=0):
        """
        Initializes square with optional size.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Finds area of the square
        """
        return self.__size ** 2