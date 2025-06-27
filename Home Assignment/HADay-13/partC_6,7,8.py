#  Part C: Creating and Using a Custom Module
# 6.Create a file math_utils.py with these functions:
# oadd(a, b) – returns the sum.
# omultiply(a, b) – returns the product.
# ois_even(n) – returns True if even.
# math_utils.py

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

# 7.In a separate script (main.py), import math_utils and test all its functions.
# main.py

import math_utils

# Test add
sum_result = math_utils.add(10, 5)
print("Sum:", sum_result)

# Test multiply
product_result = math_utils.multiply(4, 7)
print("Product:", product_result)

# Test is_even
even_check = math_utils.is_even(8)
print("Is 8 even?", even_check)

odd_check = math_utils.is_even(9)
print("Is 9 even?", odd_check)


# 8.Modify math_utils.py:
# oAdd a greet() function that takes a name and returns a greeting.
# oImport and test it in main.py.
# math_utils.py

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

def greet(name):
    return f"Hello, {name}! Welcome to math_utils."