#!/usr/bin/python3
""" Rectangle class"""


class Rectangle:
    """ rectangle class with width attribute """
    def __int__(self, width=0, height=0):
        """Initializing this rectangle class
                Args:
                    width: represents the width of the rectangle
                    height: represents the height of the rectangle
                Raises:
                    TypeError: if size is not integer
                    ValueError: if size is less than zero
                """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrives width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets height attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrives height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value