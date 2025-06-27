# Part B: Working with Multiple Errors
# 4.Math and File Operations Combined
# oAsk user to input a number and a file name.
# oPerform division 100 / number and open the given file.
# oCatch ZeroDivisionError and FileNotFoundError in separate except blocks.
num = int(input("Enter a Number:- "))
f_name = input("Enter a Filr Name:- ")
try:
    division = 100 / num
    print(f"Result of Division:- {division}")

    with open(filename , "r") as file:
        print("File Content: ")
        print(file.read())

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except FileNotFoundError:
    print("Error: The file you specified was not found.")


# 5.Nested Try Blocks
# oIn outer try: convert user input to integer.
# oIn inner try: divide a fixed number by the input.
# Catch errors in appropriate places and explain with print statements.
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print("Conversion to integer successful.")

    try:
        result = 100 / number
        print(f"Division result: {result}")
    except ZeroDivisionError:
        print("Inner Error: Cannot divide by zero.")

except ValueError:
    print("Outer Error: Invalid input. Please enter an integer.")