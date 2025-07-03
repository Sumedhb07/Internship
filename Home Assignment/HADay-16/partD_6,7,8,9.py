#  Part D: Real-World Simulation Challenges
# 6.Car Service Center
# oCreate a class Car:
# Attributes:
# brand, model, speed, fuel_level.
# Methods:
# accelerate() – Increases speed.
# brake() – Decreases speed.
# add_fuel(amount) – Increases fuel_level.
# status() – Prints the status of the car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
        self.fuel_level = 50  # Initial fuel level (out of 100)

    def accelerate(self):
        if self.fuel_level > 0:
            self.speed += 10
            self.fuel_level -= 5
            print(f"Accelerating... Current speed: {self.speed} km/h, Fuel level: {self.fuel_level}%")
        else:
            print("Out of fuel. Cannot accelerate.")
    def brake(self):
        if self.speed > 0:
            self.speed -= 10
            if self.speed < 0:
                self.speed = 0
            print(f"Braking... Current speed: {self.speed} km/h")
        else:
            print("Car is already stopped.")

    def add_fuel(self, amount):
        if amount > 0:
            self.fuel_level += amount
            if self.fuel_level > 100:
                self.fuel_level = 100
            print(f"Added {amount}% fuel. Current fuel level: {self.fuel_level}%")
        else:
            print("Invalid fuel amount.")

    def status(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Speed: {self.speed} km/h")
        print(f"Fuel level: {self.fuel_level}%")

# Example usage:
car = Car("Toyota", "Tata")
car.status()
car.accelerate()
car.accelerate()
car.brake()
car.add_fuel(20)
car.status()


# 7.Employee Class
# Attributes:
# Class Attribute: company_name = "TechCorp"
# Instance Attributes: name, salary
# Method:
# give_raise(percent) – Increases the employee’s salary by the given percentage.
# display() – Prints employee details.
class Employee:
    company_name = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        percent > 0
        self.salary *= (1 + percent / 100)
        print(f"Given {percent}% raise to {self.name}. New salary: {self.salary}rs")
        # else:
        #     print("Invalid raise percentage.")

    def display(self):
        print(f"Company: {Employee.company_name}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

# Example usage:
employee1 = Employee("piyush", 50000)
employee2 = Employee("sumedh", 60000)
print("Initial Details:")
employee1.display()
print()
employee2.display()

employee1.give_raise(10)
employee2.give_raise(15)

print("\nUpdated Details:")
employee1.display()
print()
employee2.display()



# 8.Library Book Tracker
# oCreate a class Book:
# Attributes:
# title, author, copies_available.
# Methods:
# issue() – Decrease copies if available.
# return_book() – Increase copies.
# status() – Shows book status.
class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def issue(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print(f"Issued '{self.title}' by {self.author}. Copies available: {self.copies_available}")
        else:
            print(f"'{self.title}' by {self.author} is currently out of stock.")

    def return_book(self):
        if self.copies_available >= 0:
            self.copies_available += 1
            print(f"Returned '{self.title}' by {self.author}. Copies available: {self.copies_available}")
        else:
            print("Error: Copies available cannot be negative.")

    def status(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Copies available: {self.copies_available}")


book1 = Book("Chatrapati Shivaji maharaj", "Sumedh Badgujar", 5)
book2 = Book("key of Succes", "john deo", 3)

print("Initial Status:")
book1.status()
print()
book2.status()

book1.issue()
book1.issue()
book2.issue()
book2.return_book()

print("\nUpdated Status:")
book1.status()
print()
book2.status()

# 9.Online Shopping Cart Simulation
# oCreate a class Cart:
# Attribute: items (dictionary with item_name: price).
# Methods:
# add_item(name, price)
# remove_item(name)
# get_total()
# display()
class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if name in self.items:
            print(f"'{name}' is already in your cart. Use update quantity instead.")
        else:
            self.items[name] = price
            print(f"Added '{name}' to your cart.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Removed '{name}' from your cart.")
        else:
            print(f"'{name}' is not in your cart.")

    def get_total(self):
        return sum(self.items.values())

    def display(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Your Cart:")
            for item, price in self.items.items():
                print(f"{item}: ${price:.2f}")
            print(f"Total: ${self.get_total():.2f}")

# Example usage:
cart = Cart()
cart.display()
cart.add_item("Apple Watch", 249.99)
cart.add_item("iPhone Case", 19.99)
cart.add_item("Apple Watch", 249.99)  # Duplicate item
cart.display()
cart.remove_item("iPhone Case")
cart.display()

