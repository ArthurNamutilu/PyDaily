class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

# Create a new Car object
car = Car("Toyota", "Camry", 2023)

# Print the Car object
print(car)


''' ___ str method usage '''


class Car:
    """Car class"""
    def __init__(self, brand, year):
        ''' initializing the attributes '''
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"The {self.brand} car was manufactured in {self.year}"


# new car object
car1 = Car('Mercedes', 2021)

# print car object
print(car1)