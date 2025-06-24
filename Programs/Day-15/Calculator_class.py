# Calculator Class with Static Methods
# Create a Calculator class:
# add(a, b) — Static method
# multiply(a, b) — Static method
# is_even(number) — Static method
# Test it: Call these methods without creating an object, like:
# Calculator.add(5, 3)  # Returns 8
class Calculator:
    @staticmethod
    def add(a ,b):
        print("Addition: ",a+b)
    @staticmethod   
    def multiply(a ,b):
        print("Multiplication: ",a*b)
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
a = int(input("Enter a First Number:- "))
b = int(input("Emnter a Second Number:- "))
num = int(input("Enter a Number tocheck Even Number:- "))

cal =Calculator()
cal.add(a,b)
cal.multiply(a,b)
cal.is_even(num)
