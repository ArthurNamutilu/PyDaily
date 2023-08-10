#!/usr/bin/python3
def greet():
    print('Hello from my module!')

if __name__ == '__main__':
    print('mymodule.py file run directly')
    greet()
else:
    print('!!!!external file!!!')
    greet()
