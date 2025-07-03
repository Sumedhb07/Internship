# Ask the user to input a number and a file name.
# Divide 100 by the number.
# If successful, try to open the given file in read mode.
# Use try, except, and else to structure the code
try:
    num = int(input("Enter a number: "))
    result = 100 / num  
    file_name = input("Enter file name: ")
    file = open(file_name, "r")
except ZeroDivisionError:
    print("number cannot divide by zero.")
except FileNotFoundError:
    print("File not found...")
else:
    print(result)
    print("file found successfully")

