#!/usr/bin/python3
class Person:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def get_name(self):  # getter method
        return self._name

person = Person("Arthur")
print(person.get_name())
