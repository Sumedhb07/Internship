#Factorial of number 
def factorial(num):
        count = 1
        for i in range(1,num+1):
            count = count * i

        print(count)
n=int(input("Enter a Number: "))
factorial(n)