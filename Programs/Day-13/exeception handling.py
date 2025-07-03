
a = int(input("enter first number :"))
b = int(input("enter  the second number : "))

try :
    c = a / b
    print("Result : ",c)
except ZeroDivisionError:
    print(" Cannot divisible by zero ..")
     