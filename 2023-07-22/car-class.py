#!/usr/bin/python3

class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year


    def myfunc(self):
        print(f"{self.model} car model {self.color} in color was manufactured in the year {self.year}")


mercedes = Car("G-class", "grey", 2021)
mercedes.myfunc()
