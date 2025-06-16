num1 = int(input("Enter the First number:- "))
num2 = int(input("Enter the Second number:- "))
if num1 > num2:
    print(f"{num1} is Greater than {num2}.")
elif num2 > num1:
    print(f"{num2} is Greater than {num1}.")
else:
    print("Both number are Equal.")