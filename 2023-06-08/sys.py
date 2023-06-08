import sys

def main():
    arg_num = len(sys.argv) - 1  # Subtracting to exclude script name
    arg_lst = sys.argv[1:]  # Slicing to exclude script name


    print("Number of arguments {}".format(arg_num))
    print("Argument list:", arg_lst)

if __name__ == "__main__":
    main()
