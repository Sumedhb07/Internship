# 23.Zoo Simulation:
# oCreate parent class Animal:
# Methods: sound(), move().
# oCreate child classes:
# Lion: sound() -> Roar.
# Snake: move() -> Slither.
# Parrot: sound() -> Talk.
# oMaintain a list of animals and call their methods.
class Animal:
    def sound(self):
        pass  # Base class method for sound

    def move(self):
        pass  # Base class method for movement

class Lion(Animal):
    def sound(self):
        return "Roar"

class Snake(Animal):
    def move(self):
        return "Slither"

class Parrot(Animal):
    def sound(self):
        return "Talk"

# Zoo Simulation
class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
def simulate(self):
        for animal in self.animals:
            print(f"{type(animal).__name__}:")
            print(f"  Sound: {animal.sound() if hasattr(animal, 'sound') and callable(animal.sound) else 'Unknown'}")
            print(f"  Movement: {animal.move() if hasattr(animal, 'move') and callable(animal.move) else 'Unknown'}")

# Test the Zoo Simulation
zoo = Zoo()

zoo.add_animal(Lion())
zoo.add_animal(Snake())
zoo.add_animal(Parrot())

zoo.simulate()


# 24.Custom Exceptions with Inheritance:
# oCreate a parent exception BankError.
# oCreate child exceptions:
# InsufficientBalanceError.
# InvalidAmountError.
# oSimulate a bank withdrawal method that raises these errors appropriately.
class BankError(Exception):
    """Base class for bank-related exceptions."""
    pass

class InsufficientBalanceError(BankError):
    """Raised when the account balance is insufficient for a transaction."""
    def __init__(self, balance, amount):
        message = f"Insufficient balance: ${balance:.2f} (attempted to withdraw ${amount:.2f})"
        super().__init__(message)

class InvalidAmountError(BankError):
    """Raised when the transaction amount is invalid (e.g., negative or zero)."""
    def __init__(self, amount):
        message = f"Invalid amount: ${amount:.2f} (amount must be positive)"
        super().__init__(message)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(amount)
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")

# Test the Bank Account
account = BankAccount(1000)

try:
    account.withdraw(500)
    account.withdraw(600)  # This will raise InsufficientBalanceError
except BankError as e:
    print(e)

try:
    account.withdraw(-200)  # This will raise InvalidAmountError
except BankError as e:
    print(e)



# 25.Library System:
# oCreate parent class LibraryItem.
# oCreate child classes:
# Book: title, author.
# Magazine: title, issue_number.
# DVD: title, duration.
# oImplement a method display() for each.
class LibraryItem:
    def __init__(self, title):
        self.title = title

    def display(self):
        pass  # Base class method

class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def display(self):
        print(f"Book: {self.title}")
        print(f"Author: {self.author}")

class Magazine(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number

    def display(self):
        print(f"Magazine: {self.title}")
        print(f"Issue Number: {self.issue_number}")

class DVD(LibraryItem):
    def __init__(self, title, duration):
        super().__init__(title)
        self.duration = duration
#Library System
class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_items(self):
        for item in self.items:
            item.display()
            print()  # Empty line for better formatting

# Test the Library System
library = Library()

library.add_item(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_item(Magazine("National Geographic", 123))
library.add_item(DVD("The Shawshank Redemption", 142))

library.display_items()



