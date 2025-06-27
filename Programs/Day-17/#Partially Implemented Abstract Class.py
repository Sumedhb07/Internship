#Partially Implemented Abstract Class
# Instructions:

# Create an abstract class named Employee:

# Abstract method: calculate_salary().

# Concrete method: display_role() (prints role).

# Create concrete classes:

# FullTimeEmployee with a calculate_salary() method.

# PartTimeEmployee with a calculate_salary() method.

# Instantiate both and test both methods.
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_role(self):
        print(f" i am manager")

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary 

# Concrete class PartTimeEmployee
class PartTimeEmployee(Employee):
    def __init__(self, hourly_rate , work_hour):
        self.hourly_rate = hourly_rate
        self.work_hour = work_hour


        

    def calculate_salary(self):
        return self.hourly_rate * self.work_hour


    full_time_employee = FullTimeEmployee("Aditya", 120000)
    part_time_employee = PartTimeEmployee("sumedh", 50, 100)

    print("Full Time Employee:")
    full_time_employee.display_role("Software Engineer")
    print(f"Monthly Salary: {full_time_employee.calculate_salary()}")

    print("\nPart Time Employee:")
    # part_time_employee.display_role()
    print(f"Salary: ${part_time_employee.calculate_salary():.2f}")

