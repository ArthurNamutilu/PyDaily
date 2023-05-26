# Guessing Game

secret_number = 42
guess = 0
attempts = 0

print("Welcome to the Guessing Game!")
print("Try to guess the secret number.")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You found the secret number in {attempts} attempts!")

