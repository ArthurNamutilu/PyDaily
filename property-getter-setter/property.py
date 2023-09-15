#!/usr/bin/python3
class Car:
    def __init__(self, brand):
        self._brand = brand

    @property  # getter method
    def brand(self):
        return self._brand

    @brand.setter  # setter method
    def brand(self, new_brand):
        self._brand = new_brand

car = Car("Mercedes")
print(car.brand)
car.brand = "BMW"
print(car.brand)
