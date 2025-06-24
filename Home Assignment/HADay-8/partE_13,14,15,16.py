# Part E: Tuple vs Set – Conceptual Task
# 13.Explain (in comments or writing):
# When to use a tuple over a list or set
# When to use a set over a list or tuple

# 14.Unique Words from a Sentence
# oAsk user for a sentence
# oConvert it into a set of unique words using split() and set() 

# 15.Immutable Data Storage
# oStore employee data as:
# employee = ("John", "Manager", 55000)
# oTry adding a new field to this tuple. What happens?
# 16.Set-Based Filtering
# oAsk user to enter 5 numbers (some duplicates allowed)
# oStore them in a list
# oUse a set to display only unique numbers

# 13.Explain (in comments or writing):
# When to use a tuple over a list or set
# When to use a set over a list or tuple
# Tuples are ideal when:
# - The data should not change (immutable).
# - You want to store a fixed collection of items (e.g. coordinates, RGB values, employee records).

# Sets are best when:
# - You need to eliminate duplicates.
# - You're performing operations like union, intersection, or difference.
# - The order of elements doesn’t matter, and fast membership tests are useful.


#14.Unique Words from a Sentence
# oAsk user for a sentence
# oConvert it into a set of unique words using split() and set()
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Unique words:", unique_words)

# 15.Immutable Data Storage
# oStore employee data as:
# employee = ("John", "Manager", 55000)
# oTry adding a new field to this tuple. What happens?
employee = ("John", "Manager", 55000)
# Trying to add a new field (e.g., department)
# employee[3] = "HR"  # ❌ This will raise: TypeError: 'tuple' object does not support item assignment
# Tuples are immutable — once defined, their values can’t be changed or expanded.

#16.Set-Based Filtering
# oAsk user to enter 5 numbers (some duplicates allowed)
# oStore them in a list
# oUse a set to display only unique numbers
numbers = []
# Ask user to enter 5 numbers
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
# Convert list to set to remove duplicates
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)