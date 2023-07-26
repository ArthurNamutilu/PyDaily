#!/usr/bin/python3

for n in range(2, 100):
    for m in range(2, n):
        if n % m == 0:
            print(n, 'equals', m, '*', n//m)
            break
    else:
        print(n, 'is a prime number')
