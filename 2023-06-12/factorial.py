#!/usr/bin/python3
# factorial of a number using recursive function

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))
