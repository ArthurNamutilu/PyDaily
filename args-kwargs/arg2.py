"""
This module tests the use of *arg
"""


def test_args_kwargs(arg1, *args):
    """
    checks use of args
    :param arg1: first argument
    :param args: subsequent args
    :return: arguments
    """
    print(f"first argument is {arg1}")
    for arg in args:
        print(f"another argument is {arg}")


test_args_kwargs("Python", "Javascript", "C#", "Java")
