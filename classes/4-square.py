#!/usr/bin/python3
""" square class"""


class Square:
    """ A class representing a square """

    def __init__(self, size=0):
        """ Defines the class """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """ Returns the squares size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets a square size value """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        finds the area of square
        """
        return self.__size ** 2
