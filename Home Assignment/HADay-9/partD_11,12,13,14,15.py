# Part D: Advanced Applications
# 11.Word Frequency Counter
# Input a sentence from the user.
# Count how many times each word occurs using a dictionary.
sentence = input("Enter a sentence: ")
# Convert to lowercase and split into words
words = sentence.lower().split()

# Create an empty dictionary to store word frequencies
word_count = {}
# Count occurrences
for word in words:
    #word = word.strip(".,!?")  # Optional: remove punctuation
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the result
print("Word Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# 12.Character Frequency
# Input a string.
# Count how many times each character occurs.
# Input a string from the user
text = input("Enter a string: ")

# Create an empty dictionary to store character counts
char_count = {}

# Count occurrences of each character
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Display the result
print("Character Frequency:")
for char, count in char_count.items():
    print(f"{repr(char)}: {count}")

# 13.Grades Lookup
# Create a dictionary where keys are roll numbers and values are student names.
# Ask user for a roll number and print the corresponding name.
# Dictionary with roll numbers as keys and student names as values
students = {
    101: "Prasad",
    102: "Aditya",
    103: "Sumedh",
    104: "Piyush"}
roll_number = int(input("Enter a roll number: "))

if roll_number in students:
    print(f"Student Name: {students[roll_number]}")
else:
    print("Roll number not found.")

# 14.Nested Dictionary
# Create a nested dictionary:
# student = {
#     	"name": "Ravi",
#     	"marks": {
#         	"math": 88,
#         	"science": 92
#     	}
# }
# Access "science" marks from the nested dictionary.
student = {"name": "Ravi", "marks": {"math": 88,"science": 92}}
science_marks = student["marks"]["science"]
print(f"Science Marks: {science_marks}")

# 15.Dictionary from Two Lists
# Given:
# keys = ["name", "age", "city"]
# values = ["Sam", 30, "Delhi"]
# Combine into a dictionary using a loop or zip().
keys = ["name", "age", "city"]
values = ["Sam", 30, "Delhi"]
person = {}

for i in range(len(keys)):
    person[keys[i]] = values[i]

print(person)