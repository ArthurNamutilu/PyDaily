#!/usr/bin/python3
""" Rectangle class"""


class Rectangle:
    def __int__(self, value):
        self._value = value

    @property
    def width(self, value):
        return self._value

    def width(self, new_value):
        self._value = new_value

    
