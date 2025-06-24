num1 = int(input("Enter a First Number:- "))
num2 = int(input("Enter a Second Number:-"))
try:
    result = num1 / num2
    print(f"Divivsion of {num1} & {num2} is {result}")
except ZeroDivisionError:
    print("Cannot divide by zero")



