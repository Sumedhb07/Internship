# DAY 16 – HOME ASSIGNMENTS: Classes, Objects, __init__, self, Attributes, Methods, and Static Methods
# 🐍 Part A: Classes with Logic
# 1.Bank Account Simulation
# oCreate a class BankAccount:
# Attributes: account_number, account_holder, balance.
# Methods:
# deposit(amount)
# withdraw(amount) (check for insufficient balance)
# display() (prints account details)
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        amount > 0
        self.balance += amount
        print(f"Deposited {amount}rs. New balance: {self.balance}rs")
        
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}rs. New balance:{self.balance}rs")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient balance.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}rs")

# Example usage:
account = BankAccount("123456789", "Sumedh", 1000.0)
account.display()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(1500.0)  # Insufficient balance
account.display()



# 2.Inventory Item
# Create a class Item:
# Attributes: name, price, quantity.
# Methods:
# add_stock(amount) – Increase quantity.
# sell_stock(amount) – Decrease quantity if available.
# get_total_value() – Returns total value of stock (price * quantity).
class Item:
    def __init__(self , name , price , quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def add_stock(self , amount):
        amount > 0
        self.quantity += amount
        print(f"Added {amount} {self.name}(s) to stock. New quantity: {self.quantity}")
        

    def sell_stock(self, amount):
        if 0 < amount <= self.quantity:
            self.quantity -= amount
            print(f"Sold {amount} {self.name}(s). New quantity: {self.quantity}")
        elif amount <= 0:
            print("Invalid amount to sell.")
        else:
            print(f"Insufficient stock of {self.name}(s).")

    def get_total_value(self):
        total_value = self.price * self.quantity
        return f"Total value of {self.name}(s): {total_value}rs"

# Example usage:
item = Item("Apple", 1.00, 100)
print(item.get_total_value())
item.add_stock(50)
item.sell_stock(20)
print(item.get_total_value())


