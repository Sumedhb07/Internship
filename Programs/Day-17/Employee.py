# Partially Implemented Abstract Class
# Instructions:

# Create an abstract class named Employee:

# Abstract method: calculate_salary().

# Concrete method: display_role() (prints role).

# Create concrete classes:

# FullTimeEmployee with a calculate_salary() method.

# PartTimeEmployee with a calculate_salary() method.

# Instantiate both and test both methods.
from abc import ABC, abstractmethod
class Employee:
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def display_role(self):
        print("")
class PartTimeEmployee(FullTimeEmployee):
    def calculate_salary(self):
        