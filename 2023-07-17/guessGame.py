#!/usr/bin/python3

guessLimit = 3
guessCount = 0
guess = "Red"
# userGuess = input("Guess my favorite color: ")

if guessCount < guessLimit:
    userGuess = input("Guess my favorite color: ")
    while userGuess != guess:
        guessCount += 1
        if guessCount >= guessLimit:
            break
        userGuess = input("Guess my favorite color: ")
    if userGuess == guess:
        print(f"Correct my favorite color is {userGuess}")
    else:
        print("Out of guesses")
else:
    print("Out of guesses")
