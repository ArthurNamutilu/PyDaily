#!/usr/bin/python3
import random

choices = ['rock', 'paper', 'scissors']

def winner(player_choice, comp_choice):
    if player_choice == comp_choice:
        return f"TIE Both computer and player choice is: {comp_choice}"
    elif (player_choice == 'rock' and comp_choice == 'scissors') or (player_choice == 'paper' and comp_choice == 'rock') or (player_choice == 'scissors' and comp_choice == 'paper'):
        return f"your choice {player_choice} computer choice is {comp_choice} CONGRATS YOU WIN!"
    else:
        return f"your choice {player_choice} computer choice is {comp_choice} COMPUTER  WINS!"

player_choice = input('choose rock / paper / scissors: ')

if player_choice not in choices:
    print("Inavalid choice. Try again.")

else:
    comp_choice = random.choice(choices)
    result = winner(player_choice, comp_choice)
    print(result)
