#!/usr/bin/python3
def mul(a, b):
    """
    Function that multiplies two numbers.

    :param a: First digit
    :param b: Second digit
    :return: product of a and b

    >>> mul(2, 6)
    12
    >>> mul(-1, 8)
    -8
    >>> mul(7, 0)
    0
    """
    return a * b


net_pay = mul(3820, 141)
print(f"The net pay is {net_pay}")
