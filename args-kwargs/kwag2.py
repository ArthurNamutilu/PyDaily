""" Shows the use of **Kwargs"""


def test_kwarg(**kwargs):
    """
    test kwargs
    :param kwarg: keyword arguments
    :return: kwargs
    """
    if kwargs is not None:
        for key, value in kwargs.items():
            print(f"{key} == {value}")


test_kwarg(name="Gg", School="Boma")

