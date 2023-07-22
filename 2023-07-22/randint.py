#!/usr/bin/python3
import random


def roll_dice(sides):
    return random.randint(1, sides)


print(roll_dice(5))
