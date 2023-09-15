#!/usr/bin/python3
class Person:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def get_name(self):  # getter method
        return self._name

    def set_name(self, new_name):  # setter method
        self._name = new_name

person = Person("Arthur")
print(person.get_name())
person.set_name("Gg")
print(person.get_name())
