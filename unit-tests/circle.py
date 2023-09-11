#!/usr/bin/python3
from math import pi

def circle_area(r):
    """
    Calculates area of a circle given a radius.
    :param r: the radius.
    :return: area
    """
    if type(r) not in [int, float]:
        raise TypeError("Radius MUST be a non negative real number")
    if r < 0:
        raise ValueError("Radius cannot be zero")
    return pi * (r**2)

"""
# Test function
radii = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Are of circles with r = {radius} is {area}."
for r in radii:
    A = circle_area(r)
    print(message.format(radius=r, area=A))



# print(circle_area(7))
"""
