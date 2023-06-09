#!/usr/bin/python3
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original letters {}".format(letters))

# replace some elements
letters[2:5] = ['C', 'D', 'E']
print("Letters list after deletion {}".format(letters))

# remove some elements
letters[1:4] = []
print("Letters list after some deletes {}".format(letters))

# remove all elements
letters[:] = []
print("list after del {}".format(letters))
