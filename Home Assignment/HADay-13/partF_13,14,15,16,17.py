# Part F: Real-World Practice
# 13.Create a string_utils.py:
# ocount_characters(s) → returns character count.
# ocount_words(s) → returns word count.
# oreverse_string(s) → returns the reversed version.
# oImport and test these in main.py.
# string_utils.py

def count_characters(s):
    return len(s)

def count_words(s):
    return len(s.split())

def reverse_string(s):
    return s[::-1]
import string_utils

text = "Hello Python World"
print("Characters:", string_utils.count_characters(text))
print("Words:", string_utils.count_words(text))
print("Reversed:", string_utils.reverse_string(text))

# 14.Create a shapes.py:
# oarea_of_rectangle(length, breadth).
# oarea_of_circle(radius).
# oarea_of_square(side).
# oImport and test these in main.py.
# shapes.py

def area_of_rectangle(length, breadth):
    return length * breadth

def area_of_circle(radius):
    import math
    return math.pi * radius * radius

def area_of_square(side):
    return side * side
import shapes

print("Rectangle area:", shapes.area_of_rectangle(10, 5))
print("Circle area:", shapes.area_of_circle(7))
print("Square area:", shapes.area_of_square(4))


# 15.Create a config.py module:
# oStore variables like HOST = "127.0.0.1", PORT = 8080.
# oImport in main.py and print the settings.
# config.py

HOST = "127.0.0.1"
PORT = 8080
import config

print("Server running at:", config.HOST, "on port", config.PORT)

# 16.Create a text_utils.py:
# oFunctions:
# count_vowels(sentence)
# count_consonants(sentence)
# oImport and test both.
# text_utils.py

def count_vowels(sentence):
    return sum(1 for char in sentence.lower() if char in "aeiou")

def count_consonants(sentence):
    return sum(1 for char in sentence.lower() if char.isalpha() and char not in "aeiou")
import text_utils

s = "Python is amazing"
print("Vowels:", text_utils.count_vowels(s))
print("Consonants:", text_utils.count_consonants(s))

# 17.Practice creating a package:
# oDirectory structure:
# myproject/
#   		__init__.py
#   		math_utils.py
#   		text_utils.py
# oImport both in main.py and test their functions.
def square(n):
    return n * n
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())
from myproject import math_utils, text_utils

print("Square of 6:", math_utils.square(6))
print("Capitalized:", text_utils.capitalize_words("hello from shree"))