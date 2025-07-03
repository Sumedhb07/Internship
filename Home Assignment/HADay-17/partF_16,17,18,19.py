#  Part F: Method Overriding & Super Usage
# 16.Create a parent class Employee:
# oAttribute: name, salary.
# oMethod: display().
# 17.Create a child class Manager inherits from Employee:
# oNew Attribute: department.
# oOverride display() method and use super() to call parent method.
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
class Manager(Employee):
    def __init__(self, name,salary,department):
        super().__init__(name , salary)
        self.department = department
    def display(self):
        print(f"Department: {self.department}")

employee = Employee("Sumedh",80000)
manager = Manager("Sumedh",80000 , "Marketing")

print("Employee Details: ")
employee.display()
print("Manager Details: ")
manager.display()



# 18.Create a parent class BankAccount:
# oMethod: calculate_interest() returns some value.
# 19.Create a child class SavingsAccount:
# oOverride the method to return a different interest rate.
class BankAccount:
    def __init__(self , balance):
       self.balance = balance
    def calculate_interest(self):
        return self.balance * 0.02  # Default interest rate: 2%

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        return self.balance * 0.05  # Interest rate for SavingsAccount: 5%

# Test the classes
account = BankAccount(1000)
savings_account = SavingsAccount(1000)

print(f"BankAccount Interest: {account.calculate_interest()}rs")
print(f"SavingsAccount Interest: {savings_account.calculate_interest()}rs")

