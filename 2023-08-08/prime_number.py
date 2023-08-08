#!/usr/bin/python3
for i in range(2, 50):
    for x in range(2, i):
        if i % x == 0:
            print(f"{i} is not a prime number")
            break
    else:
        print(f"{i} is a prime number")
