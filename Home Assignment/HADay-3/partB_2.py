#partB: Comparison Operators
#2.Take age as input from the user and check if:
#the person is 18 or elder
#the person is a senior citizen(>=60)
age = int(input("Enter your age:- "))
if age >= 18:
    print("you are 18 or older. ")
else:
    print("you are under 18. ")
if age >= 60:
    print("you are a senior citizen. ")
else:
    print("you are not a senior citizen.")