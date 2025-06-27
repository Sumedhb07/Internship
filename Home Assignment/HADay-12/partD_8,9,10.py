#  Part D: Real-World Inspired Tasks
# 8.Student Marks Entry
# oAsk the user to enter a student’s mark (0–100).
# oIf out of range, raise ValueError.
# oCatch the error and print "Invalid mark. Must be between 0 and 100."
try:
    mark = int(input("Enter the student's mark (0–100): "))
    if mark < 0 or mark > 100:
        raise ValueError
    print(f"The entered mark is: {mark}")
except ValueError:
    print("Invalid mark. Must be between 0 and 100.")

# 9.User Registration
# oAsk for username and password.
# oIf username is empty, raise ValueError.
# oIf password is less than 6 characters, raise ValueError.
# oCatch and display both errors.
try:
    username = input("Enter your username: ")
    if not username.strip():
        raise ValueError("Username cannot be empty.")

    password = input("Enter your password: ")
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")

    print("Registration successful!")

except ValueError as e:
    print(f"Error: {e}")

# 10.Simple File Reader with Fallback
# oAsk user for a file name.
# oIf file doesn’t exist, catch FileNotFoundError and create a new file with default content.
# oPrint "New file created."
filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        print("File content:")
        print(file.read())

except FileNotFoundError:
    with open(filename, "w") as file:
        file.write("This is a newly created file with default content.")
    print("New file created.")