# Day 11 – Home Assignments: File Handling (Text Files – .txt)
# Part A: Writing and Reading Text Files
# 1.Write a Greeting
# oCreate a file called greeting.txt
# oWrite "Hello, welcome to Python file handling!" into it.
# Create and write to a file called greeting.txt
with open("greeting.txt", "w") as file:
    file.write("Hello, welcome to Python file handling!")

# 2.Read File Content
# oOpen greeting.txt and print the content.
with open("greeting.txt", "r") as file:
    print("Original content:")
    print(file.read())

# 3.Append More Text
# oAppend "This is the second line." to greeting.txt
# oThen read and print the updated content
with open("greeting.txt", "a") as file:
    file.write("\nThis is the second line.")
with open("greeting.txt", "r") as file:
    print("\nUpdated content:")
    print(file.read())