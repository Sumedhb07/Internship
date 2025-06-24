
try:
    num = int(input("Enter a Number:- "))
    file = (input("Enter a File Name:- "))
    result = 100 / num
    print("Result: ",result)
    file = open("file","r") 
except ZeroDivisionError:
    print("Cannot divide by Zero")
except FileNotFoundError:
    print("File Not Found ")

else:
    print("Division is: ",result)
    print("file opened successful")
    print(file,"r")
    file.close
    
