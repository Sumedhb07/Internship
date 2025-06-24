# 16.Write a program that takes 5 numbers from the user and stores them in a list. Then:
# Print the sum
# Print the max and min number
# Sort the list and print it
# 17.Create a list names = ["Alice", "Bob", "Charlie", "David"]
# Use list comprehension to create a list of name lengths: [5, 3, 7, 5]
# 18.Given sentence = "Python is powerful", convert it into a list of words and then reverse the list using slicing.


#16.Write a program that takes 5 numbers from the user and stores them in a list. Then:
# Print the sum
# Print the max and min number
# Sort the list and print it
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(5)]
print("Sum:", sum(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sorted list:", sorted(numbers))

#17.Create a list names = ["Alice", "Bob", "Charlie", "David"]
# Use list comprehension to create a list of name lengths: [5, 3, 7, 5]
names = ["Alice", "Bob", "Charlie", "David"]
name_lengths = [len(name) for name in names]
print("Name Length: ",name_lengths)

#18.Given sentence = "Python is powerful", convert it into a list of words and then reverse the list using slicing.
sentence = "Python is powerful"
words = sentence.split()
reversed_words = words[::-1]
print(reversed_words)

