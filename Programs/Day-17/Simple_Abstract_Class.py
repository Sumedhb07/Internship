#  Simple Abstract Class

# Create an abstract class named Animal.

# Inside it, define an abstract method called sound().

# Create two concrete subclasses:

# Dog that implements sound() method to print: “Woof”

# Cat that implements sound() method to print: “Meow”

# Instantiate both and call the sound() method.

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("woof")
class Cat(Dog):
    def sound(self):
        print("meow")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()