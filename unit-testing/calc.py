def add(a, b):
    """ add function """
    return a + b


def sub(a, b):
    """ subtract function """
    return a - b


def mul(a, b):
    """ multiply function """
    return a * b


def div(a, b):
    """ divide function """
    if b == 0:
        raise ValueError('Number cannot be divided by zero')
    return a / b
