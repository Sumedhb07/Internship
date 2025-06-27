
# Task: 
# Create a parent class Vehicle with:

# An attribute brand.

# A method describe() that returns: "This is a vehicle."

# Create a child class Car that inherits from Vehicle and:

# Adds an attribute model.

# Overrides the describe() method to return: "This is a [brand] [model]."

# Test it:
# Create an object of Car and call its describe() method.
class Vehical:
    def __init__(self,brand):
        self.brand = brand
    def describe(self):
        return"This is a vehical"
class Car(Vehical):
    def __init__(self , model):
        self.model = model
        return f"This is a {self.brand} {self.model}"
car = Car("BMW","M5")
print(car.brand)
print(car.model)
print(car.describe())

    