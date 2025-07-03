#  Part C: Multilevel Inheritance
# 6.Create a parent class Animal:
# oMethod: sound() returns Generic Animal Sound.
# 7.Create a child class Dog inherits from Animal:
# oOverride sound() returns Bark.
# 8.Create a grandchild class Puppy inherits from Dog:
# oOverride sound() returns Yip.
# 9.Test by creating instances of Animal, Dog, and Puppy and invoking their sound() methods.
class Animal:
    def sound(self):
        return "Generic Animal Sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
class Puppy(Dog):
    def sound(self):
        return "Yip"
animal = Animal()
dog = Dog()
puppy = Puppy()
print(animal.sound())
print(dog.sound())
print(puppy.sound())