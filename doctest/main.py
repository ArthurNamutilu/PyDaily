#!/usr/bin/python3
def factorial(n):
    """
    Calculates the factorial of a number.

    Args:
        n: The number to calculate factorial of.

    Returns:
        The factorial of n.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(factorial(6))
