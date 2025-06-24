# value Error Exception 

try:
    num = int(input("Enter a Integer Value:- "))
    print(f"{num} Number is Integer :-")
except ValueError:
    print("Number is not an Integer")