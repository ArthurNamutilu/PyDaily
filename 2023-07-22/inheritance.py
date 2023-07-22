#!/usr/bin/python3

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"Hello {self.firstname} {self.lastname} welcome")


class Student(Person):
    pass


gg =Student("Arthur", "Namutilu")
gg.printname()
