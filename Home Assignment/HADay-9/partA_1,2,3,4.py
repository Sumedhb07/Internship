#  Part A: Dictionary Basics
# 1.Create a Dictionary
# Create a dictionary named student with keys:
# o"name" → "Alice"
# o"age" → 20
# o"course" → "Python"
# oPrint the dictionary.
# 2.Access Values
# oPrint the value of "name" from the student dictionary.
# 3.Modify and Add
# oChange "age" to 21
# oAdd a new key "city" with value "Mumbai"
# 4.Delete Key
# Remove the "course" key from the dictionary using del.

#1.Create a Dictionary
# Create a dictionary named student with keys:
# o"name" → "Alice"
# o"age" → 20
# o"course" → "Python"
# oPrint the dictionary.
# Create a dictionary named student
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
# Print the dictionary
print(student)

#2.Access Values
# oPrint the value of "name" from the student dictionary.
print(student["name"])

#3.Modify and Add
# oChange "age" to 21
# oAdd a new key "city" with value "Mumbai"
# Modify the value of "age"
student["age"] = 21
student["city"] = "Mumbai"
print(student)

#4.Delete Key
# Remove the "course" key from the dictionary using del.
# Delete the "course" key
del student["course"]
print(student)