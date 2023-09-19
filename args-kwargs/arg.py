#!/usr/bin/python3
def test_var_arg(f_arg, *argv):
    print("First normal arg: ", f_arg)
    for arg in argv:
        print("another arg through *argv: ", arg)


test_var_arg("Nairobi", "Amsterdam", "Melbourn", "Ottawa")
