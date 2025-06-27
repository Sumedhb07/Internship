#  Part A: Core Try-Except Practice
# 1.Basic Input Validation
# oAsk the user to enter a float number.
# oCatch ValueError and print "Invalid input. Please enter a decimal number."
try:
    number = float(input("Enter a decimal number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input. Please enter a decimal number.")

# 2.String to Integer Conversion
# oTake a string input and try converting it to an integer.
# oCatch exceptions and print the type of error using type(e).
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    print(f"Conversion successful! Integer: {number}")
except Exception as e:
    print(f"An error occurred: {type(e)}")

# 3.List Index Validation
# colors = ["red", "blue", "green"]
# oAsk user to input an index and print the color at that index.
# oCatch IndexError.
colors = ["red", "blue", "green"]
try:
    index = int(input("Enter an index (0 to 2): "))
    print(f"The color at index {index} is {colors[index]}")
except IndexError:
    print("Oops! That index is out of range.")
