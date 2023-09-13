#!/usr/bin/python3

with open('languages.txt', 'r') as languages:
    for language in languages.readlines():
        print(language)
print(languages.closed)
