# Create a BankAccount Class
# Attributes
# account_holder, balance.
# Methods:
# deposit(amount) — Adds money.
# withdraw(amount) — Subtracts money if available.
# display_balance() — Shows the balance.
# Test it: Create an account, deposit money, withdraw money, and display the balance.

class BankAccount:
    def __init__(self, account_holder , balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        
            self.balance += amount
            print(f"Deposited {amount}rs. New balance: {self.balance}rs")
       
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}rs. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"{self.account_holder}'s account balance: ₹{self.balance}")

# Testing the class
account = BankAccount("Sumedh", 2000)
account.display_balance()
account.deposit(500)
account.withdraw(300)
account.display_balance()