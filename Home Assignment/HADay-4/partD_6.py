# 6.Ask for a username and password:
# o	If both are correct → "Login successful"
# o	If username is correct but password is wrong → "Wrong password"
# o	If username is wrong → "User not found"
# Predefined correct credentials
correct_username = "admin"
correct_password = "password123"

# Ask the user for their username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check login credentials
if username == correct_username:
    if password == correct_password:
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")
