#!/usr/bin/python3

def print_hi(name):
    print(f'Hi, {name}')


# __name__ special var containing name of current module
# When the script is executed directly, its __name__ is set to '__main__'
if __name__ == '__main__':
    print_hi('PyCharm')
