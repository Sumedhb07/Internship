# Create a Book Class

# Attributes:

# title, author, year.

# Method:

# get_description() — Returns a formatted description like:

# "The book 'Title' by Author was published in Year."

# Test it: Create a book and print its description.
class Book:
    def __init__(self):
        self.title = input("Enter the Title of Book:- ")
        self.author = input("Enter the Author of Book:-")
        self.year = input("Enter the Year of Book:- ")
    def get_description(self):
        print(f"The book {self.title} by {self.author} was published in {self.year}.")
book = Book()
book.get_description()