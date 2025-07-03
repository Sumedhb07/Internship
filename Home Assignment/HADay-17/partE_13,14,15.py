# Part E: Polymorphism
# 13.Create three classes:
# oBird (method move() returns Flies),
# oFish (method move() returns Swims),
# oDog (method move() returns Walks).
# 14.Create a function test_move(obj) that takes any of these instances and calls its move() method.
# 15.Create another example:
# oAdd method that behaves differently:
# Takes 2 numbers and returns the sum.
# Takes a list of numbers and returns the total.
class Bird:
    def move(self):
        return "Flies"
class Fish:
    def move(self):
        return "Swims"
class Dog:
    def move(self):
        return "Walks"
    def test_move(obj):
         print(f"{obj.__class__.__name__}: {obj.move()}")
bird = Bird()
fish = Fish()
dog = Dog()

# test_move(bird)
# test_move(fish)
# test_move(dog)

print(f"Bird: {bird.move()}")
print(f"Fish: {fish.move()}")
print(f"Dog: {dog.move()}")

#Create another example:
# oAdd method that behaves differently:
# Takes 2 numbers and returns the sum.
# Takes a list of numbers and returns the total.
class Calculator:
    def add(self, a, b=None):
        if b is not None:
            # Case 1: Two numbers
            return a + b
        elif isinstance(a, list):
            # Case 2: A list of numbers
            return sum(a)
        else:
            raise TypeError("Invalid input: Provide two numbers or a list of numbers")

# Testing the Calculator class
calc = Calculator()

print(calc.add(10, 5))         # Output: 15
print(calc.add([1, 2, 3, 4]))  # Output: 10