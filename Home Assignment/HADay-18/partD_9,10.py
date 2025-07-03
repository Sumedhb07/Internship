#  Part D: Polymorphism with Abstraction
# 9.Create an abstract class Animal:
# oAbstract method: make_sound()
# 10.Subclasses:
# oDog: Returns Woof
# oCat: Returns Meow
# oCow: Returns Moo
# oTest polymorphism by looping over instances and calling make_sound().
from abc import ABC , abstractmethod 
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Woof"
class Cat(Dog):
    def make_sound(self):
        return "Meow"
class Cow(Cat):
    def make_sound(self):
        return "Moo"
dog = Dog()
print(f"Dog: {dog.make_sound()}")
cat = Cat()
print(f"Cat: {cat.make_sound()}")
cow = Cow()
print(f"Cow: {cow.make_sound()}")




