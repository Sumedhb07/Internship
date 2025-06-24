# Part D: List Comprehension
# 11.Create a list of squares from 1 to 10 using list comprehension.
# Example: [1, 4, 9, ..., 100]
# 12.From a list of numbers 1 to 20, create a new list that contains only even numbers using list comprehension.
# 13.Given words = ["Apple", "banana", "Cherry"], create a new list with all words in lowercase using list comprehension. (hint: use lower())
# 14.From a string "python", create a list of characters using list comprehension.
# 15.Create a list of numbers from 1 to 50 that are divisible by both 3 and 5 using list comprehension.

#11.Create a list of squares from 1 to 10 using list comprehension.

squares = [x**2 for x in range(1, 11)]
print(squares)

#12.From a list of numbers 1 to 20, create a new list that contains only even numbers using list comprehension.
# Example: [1, 4, 9, ..., 100]
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

#13.Given words = ["Apple", "banana", "Cherry"], create a new list with all words in lowercase using list comprehension. (hint: use lower())
words = ["Apple", "banana", "Cherry"]
lowercase_words = [word.lower() for word in words]
print(lowercase_words)

# 14.From a string "python", create a list of characters using list comprehension.
word = "python"
char_list = [char for char in word]
print(char_list)

# 15.Create a list of numbers from 1 to 50 that are divisible by both 3 and 5 using list comprehension.
number = [x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0]
print("Divisible by 3 & 5: ",number)