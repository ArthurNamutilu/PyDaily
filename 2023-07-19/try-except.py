#!/usr/bin/python3

try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}")

except ValueError as err:
    print(err)
