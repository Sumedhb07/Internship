#  Part B: Alias and Specific Import
# 4.Import the math module as m:
# oUse it to compute the log10 of 1000.
import math as m
result = m.log10(1000)
print("log10(1000):", result)

# 5.From the random module:
# oImport only the choice function and use it to pick a random element from a list of names.
from random import choice

names = ["Shree", "Aarav", "Mira", "Zoya", "Ishaan"]
selected_name = choice(names)
print("Randomly selected name:", selected_name)