# multiple Except blocks , file not found error handling

try :
    file1 = input("Enter file name : ")
    num = int(input("Enter number  : "))
    
    result = 100 / num
    file = open(file1,"r")
    
except ZeroDivisionError:
    print("cannot divisible by zero ..")
    
except FileNotFoundError:
    print("File not found .. ")
    
    

    