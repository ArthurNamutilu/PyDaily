#!/usr/bin/python3

phrase = input("Enter phrase to translate: ")
def translate(phrase):
    vowels = "AEIOUaeiou"
    translation = ""
    for letter in phrase:
        if letter in vowels:
            translation = translation + 'g'
        else:
            translation = translation + letter
    return translation


print(translate(phrase))
