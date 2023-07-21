#!/usr/bin/python3

lines = ["Creating new text file in python", "Line 2"]
with open('REAME.md', 'w') as new_file:
    for line in lines:
        new_file.write(line)
        new_file.write('\n')
