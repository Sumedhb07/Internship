# Task: Getters and Setters
# Instructions:

# Create a class Person.

# Add a private attribute __age.

# Create:

# A method set_age(value) that validates if the age is a positive number.

# A method get_age() to return the age.

# Try setting both valid and invalid ages.
class person:
    def __init__(self):
        self.__age = 0 

    def set_age(self , value):
        if value > 0:
            self.__age = value
        else:
            print("Invalid age")
    def get_age(self):
        print(self.__age)

p = person()
p.set_age(18)
p.get_age()
p.set_age(-18)
#p.get_age()


