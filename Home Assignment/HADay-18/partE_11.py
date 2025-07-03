# Part E: Encapsulation + Abstraction Combined
# 11.Build a Bank System:
# oAbstract class Account:
# Private balance
# Abstract method: calculate_interest()
# oSubclasses:
# SavingsAccount: 4% interest.
# CurrentAccount: 1% interest.
# oMethods:
# get_balance() – Returns the balance.
# set_balance() – Updates balance with checks.
# calculate_interest() – Returns calculated interest.
# oTest by creating instances and invoking methods.
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount.")

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def calculate_interest(self):
        interest_rate = 0.04
        interest = self.get_balance() * interest_rate
        return interest

class CurrentAccount(Account):
    def calculate_interest(self):
        interest_rate = 0.01
        interest = self.get_balance() * interest_rate
        return interest

# Test instances
savings_account = SavingsAccount(1000)
print(f"Savings account balance: {savings_account.get_balance()}")
print(f"Savings account interest: {savings_account.calculate_interest()}")

current_account = CurrentAccount(500)
print(f"Current account balance: {current_account.get_balance()}")
print(f"Current account interest: {current_account.calculate_interest()}")

# Update balance and test again
savings_account.set_balance(1500)
print(f"Updated savings account balance: {savings_account.get_balance()}")
print(f"Updated savings account interest: {savings_account.calculate_interest()}")
