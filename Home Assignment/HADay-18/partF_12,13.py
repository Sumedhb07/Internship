#  Part F: Realistic Challenges
# 12.Online Shopping System:
# oAbstract class: User
# Abstract method: get_user_type()
# oSubclasses:
# Customer returns Customer for user type.
# Admin returns Admin for user type.
# oEncapsulate user_id and user_email as private.
# 13.Employee Hierarchy with Encapsulation:
# oAbstract class: Employee
# Abstract method: calculate_salary()
# Private attribute: base_salary
# oSubclasses:
# FullTimeEmployee (adds benefits and bonuses).
# PartTimeEmployee (hourly rate and hours worked).
from abc import ABC, abstractmethod

# Online Shopping System
class User(ABC):
    def __init__(self, user_id, user_email):
        self.__user_id = user_id
        self.__user_email = user_email

    def get_user_id(self):
        return self.__user_id

    def get_user_email(self):
        return self.__user_email

    @abstractmethod
    def get_user_type(self):
        pass

class Customer(User):
    def get_user_type(self):
        return "Customer"

class Admin(User):
    def get_user_type(self):
        return "Admin"

# Employee Hierarchy
class Employee(ABC):
    def __init__(self, base_salary):
        self.__base_salary = base_salary

    def get_base_salary(self):
        return self.__base_salary

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, base_salary, benefits, bonuses):
        super().__init__(base_salary)
        self.__benefits = benefits
        self.__bonuses = bonuses

    def calculate_salary(self):
        return self.get_base_salary() + self.__benefits + self.__bonuses

class PartTimeEmployee(Employee):
    def __init__(self, base_salary, hourly_rate, hours_worked):
        super().__init__(base_salary)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return self.get_base_salary() + (self.__hourly_rate * self.__hours_worked)

# Test instances
customer = Customer(1, "customer@example.com")
print(f"User ID: {customer.get_user_id()}, User Email: {customer.get_user_email()}, User Type: {customer.get_user_type()}")

admin = Admin(2, "admin@example.com")
print(f"User ID: {admin.get_user_id()}, User Email: {admin.get_user_email()}, User Type: {admin.get_user_type()}")

full_time_employee = FullTimeEmployee(50000, 10000, 5000)
print(f"Full-time employee salary: {full_time_employee.calculate_salary()}rs")

part_time_employee = PartTimeEmployee(20000, 50, 100)
print(f"Part-time employee salary: {part_time_employee.calculate_salary()}rs")


