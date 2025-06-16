#7.write a small calculator program:
num1 = float(input("Enter First Number:- "))
num2 = float(input("Enter Seconf Number:- "))

operator = input("Enter operator(+,-,*,/):- ")
if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}") 
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by Zero.")
else:
    print("Invalid operator! plaese Enter one of +,-,*,/")