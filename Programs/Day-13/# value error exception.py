# value error exception

try :
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Number is not an integer .... ")