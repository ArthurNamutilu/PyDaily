#!/usr/bin/python3
class Square:
    """ A square class """
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Finds the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Prints to stdout the square with character # """
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print("#" * self.__size)