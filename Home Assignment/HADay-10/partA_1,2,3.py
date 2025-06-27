# Part A: Indexing & Slicing
# 1.Basic Indexing
# Given: text = "PythonProgramming"
# oPrint the first, fifth, and last character using indexing.
# Given string
text = "PythonProgramming"

first_char = text[0]
fifth_char = text[4]
last_char = text[-1]

print(f"First character: {first_char}")
print(f"Fifth character: {fifth_char}")
print(f"Last character: {last_char}")

# 2.Basic Slicing
# From the same string:
# oPrint the substring "Python"
# oPrint the substring "Programming"
# oPrint every second character (::2)
# oReverse the string using slicing
text = "PythonProgramming"
# Substring "Python"
print(text[0:6])
# Substring "Programming"
print(text[6:])
# Every second character
print(text[::2])
# Reverse the string
print(text[::-1])

# 3.Custom Substring
# Input a string from the user and print:
# oFirst 3 characters
# oLast 3 characters
# oMiddle 5 characters
# Input a string from the user
text = input("Enter a string: ")
# Get the first 3 characters
first_three = text[:3]
# Get the last 3 characters
last_three = text[-3:]
# Get the middle 5 characters
start_index = (len(text) - 5) // 2
middle_five = text[start_index:start_index + 5]
# Display the results
print(f"First 3 characters: {first_three}")
print(f"Last 3 characters: {last_three}")
print(f"Middle 5 characters: {middle_five}")