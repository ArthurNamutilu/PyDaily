#!/usr/bin/python3
while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError as err:
        print("Oops, seems like you didn't enter a valid number, Try again:")
