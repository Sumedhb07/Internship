#multiple Except Block

num = int(input("Enter a Number:- "))
file = (input("Enter a File Name:- "))
try:
    result = 100 / num
    print("Result: ",result)
    file = open("file","r")
    
except FileNotFoundError:
    print("File Not Found ")
except ZeroDivisionError:
    print("Cannot divide by Zero")
   
    
