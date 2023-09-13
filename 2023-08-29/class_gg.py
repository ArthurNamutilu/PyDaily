#!/usr/bin/python3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def sayHi(self):
        print(f'Hi {self.name}')


p1 = Person('GG', 25)
p1.sayHi()
