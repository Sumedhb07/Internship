# 🐍 DAY 18 – HOME ASSIGNMENTS: Encapsulation, Abstraction, and Interfaces
# (Private Attributes, Getters & Setters, Abstract Classes, Interfaces (using abstract methods), and Polymorphic Designs.)

# 🔐 Part A: Encapsulation Basics
# 1.BankAccount Class:
# oMake balance a private attribute.
# oAdd deposit() and withdraw() methods.
# oPrevent withdrawals if balance is insufficient.
# 2.Student Class:
# oMake name and age private.
# oUse get_name(), set_name() and get_age(), set_age() methods.
# oValidate age to be a positive integer.
# 3.Product Class:
# oMake price private.
# oUse a method to apply discount (without direct access).
class BankAccount:
    def __init__(self, balance = 0):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}rs. Current balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}rs. Current balance: {self.__balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            print("Invalid age. Please enter a positive integer.")

class Product:
    def __init__(self, price):
        self.__price = price

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            discounted_price = self.__price * (1 - discount_percentage / 100)
            return f"Discounted price: {discounted_price}"
        else:
            return "Invalid discount percentage."
# Test the classes
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(f"Current balance: {account.get_balance()}")

student = Student("Sumedh", 20)
print(student.get_name())
print(student.get_age())
student.set_age(25)
print(student.get_age())

product = Product(100)
print(product.apply_discount(20))


