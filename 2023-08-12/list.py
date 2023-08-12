#!/usr/bin/python3
squares = [i ** 2 for i in range(1, 15)]
print(squares)

# list comprehension

combs = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)
