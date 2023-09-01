#!/usr/bin/python
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_integers += 1
        except (ValueError, TypeError):
            pass
#        printed_integers += 1
    print()
    return printed_integers
