#partC:Logical Operator
#4.Create a login check
correct_username = "admin"
correct_passward = "1234"

username = input("Enter usename:- ")
passward = input("Enter passward:- ")

if username == correct_username and passward == correct_passward:
    print("Login Successful")
else:
    print("Invalid Credentials")