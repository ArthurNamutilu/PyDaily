#!/usr/bin/python3

try:
    myList = [1, 2, 3]
    print(myList[3])
except IndexError as err:
    print('Unreached index: ', err)
