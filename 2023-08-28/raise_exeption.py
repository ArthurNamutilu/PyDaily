#!/usr/bin/python3
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

print(validate_age(-3))
