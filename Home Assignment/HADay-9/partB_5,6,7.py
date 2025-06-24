# Part B: Dictionary Operations
# 5.Loop Through Dictionary
# Write a loop to print each key and its value in the student dictionary.
# 6.Check Key Existence
# oUse in keyword to check if "name" exists in student.
# 7.Get with Default
# oUse get() to retrieve "grade" from the dictionary.
# Provide default value "Not Assigned".

#5.Loop Through Dictionary
# Write a loop to print each key and its value in the student dictionary.
# Loop through the dictionary and print each key and its value
for key, value in student.items():
    print(key, ":", value)

#6.Check Key Existence
# oUse in keyword to check if "name" exists in student.
if "name" in student:
    print("The key 'name' exists in the student dictionary.")
else:
    print("The key 'name' does not exist.")


# 7.Get with Default
# oUse get() to retrieve "grade" from the dictionary.
# Provide default value "Not Assigned".
# Retrieve "grade" with a default value
grade = student.get("grade", "Not Assigned")
print("Grade:", grade)