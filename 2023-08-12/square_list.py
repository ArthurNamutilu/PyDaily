#!/usr/bin/python3
squares = [1, 4, 9, 16, 25, 36]
test = squares[:] + [49, 64, 81, 100]
a = ['a', 'b', 'c', 'd']
print(test)

# nesting list
nested_list = [squares, a]
print(nested_list)

# remove elements from list
print(squares)
squares[1:4] = []
print(squares)

# understanding list.append()
print(f"List a of length {len(a)} and values {a}")
a[4:] = 'X'  # same as list.append(x)
print('After appending X')
print(f"List a of length {len(a)} and values {a}")

print(a)
a.pop()
print(a)
