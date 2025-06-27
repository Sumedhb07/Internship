# Task:
# Create a parent class Number.

# Create SumNumber and ProductNumber classes that inherit from Number.

# Create a final class FinalCalculator that inherits from both.

# Call parent methods directly:

# SumNumber.sum(self, a, b).

# ProductNumber.product(self, a, b).

# Test:

# FinalCalculator().sum(5, 10) → 15

# FinalCalculator().product(3, 4) → 12

class Number:
    #def __init__(self):
        # self.a = a
        # self.b = b
        pass
class SumNumber(Number):
    def sum(a , b):
        # self.a = a
        # self.b = b
        return a + b
class ProductNumber(Number):
    def product(a , b):
       # self.a = a
        # self.b = b
        return a * b
class FinalCalculator(SumNumber , ProductNumber):
    def __init__(self):
        SumNumber(self.a , self.b)
        ProductNumber(self.a , self.b) 
print(FinalCalculator.sum(5,3))
print(FinalCalculator.product(3,4))
