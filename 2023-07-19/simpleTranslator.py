#!/usr/bin/python3

phrase = input("Enter phrase to translate: ")


def translate(phrase):
    vowels = "aeiou"
    translation = ""
    for letter in phrase:
        if letter.lower() in vowels:
            if letter.isupper():
                translation = translation + 'G'
            else:
                translation = translation + 'g'
        else:
            translation = translation + letter
    return translation


print(translate(phrase))
