# Task: Property Decorators
# Instructions:

# Create a class Student.

# Private attribute: __name.

# Use @property for getting the name.

# Use @name.setter for setting the name, ensuring it’s not an empty string.

# Try creating instances and setting names.
class Student:
    def __name(self):
        self.__name = ""
    @property
    def name(self):
        print(self.__name)

    @name.setter
    def name(self, value):
        if value:
            self.__name = value
        else:
            print("Invalid Name")
s = Student()
s.name = "Sumedh"
print(s.name)
s.name = ""
