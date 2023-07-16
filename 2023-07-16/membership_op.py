#!/usr/bin/python3

num = int(input("Enter a number: "))

my_list = [1, 2, 3, 4, 5]

if (num in my_list):
    print(f"{num} is in the given list")
    print(f"The list ->{my_list}")
else:
    print(f"{num} is not available in this list -> {my_list}")
