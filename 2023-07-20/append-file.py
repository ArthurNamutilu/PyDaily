#!/usr/bin/python3

lines = ["Continue from this line","Additional text to text file in python", "\n"]
with open('REAME.md', 'a') as new_file:
    new_file.write('\n'.join(lines))
