#!/usr/bin/python3
import sys

def main():
    arg_num = len(sys.argv) - 1
    arg_lst = sys.argv[1:]

    if arg_num == 0:
        print("{} arguments".format(arg_num))
    elif arg_num == 1:
        print("{} argument:".format(arg_num))
        print("{}: {}".format(arg_num, sys.argv[arg_num]))
    else:
        for arg in arg_lst:
            print("{} arguments".format(arg_num))
            print(arg)
#    print(arg_num)


if __name__ == "__main__":
    main()
