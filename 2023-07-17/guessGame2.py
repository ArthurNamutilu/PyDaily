#!/usr/bin/python3

secred_word = "CODE"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuesses = False


while guess.upper() != secred_word and not outOfGuesses:
    if guessCount < guessLimit:
        guess = input("Enter a guess: ")
        guessCount += 1
    else:
        outOfGuesses = True

if outOfGuesses:
    print("Out of guesses You Loose :(")
else:
    print(f"Correct the guess is {guess.upper()}")
