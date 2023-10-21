class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f"{self.__class__.__name__}(make='{self.make}', model='{self.model}', year={self.year})"

# Create a new Car object
car = Car("Toyota", "Camry", 2023)

# Print the Car object using the repr() function
print(repr(car))
