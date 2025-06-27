# Part C: File Handling Modes Practice
# 7.Using 'r' Mode
# oTry to read a file that doesn't exist using 'r'.
# oWhat error is shown?
# Trying to read a non-existent file
with open("nonexistent.txt", "r") as file:
    content = file.read()

# 8.Using 'w' Mode
# oOpen a file with 'w' mode and write some content.
# oThen open it again with 'r' and print it.
# oNotice: Does previous data persist?
# Step 1: Write content to the file using 'w' mode
with open("demo.txt", "w") as file:
    file.write("This is the original content.")
# Step 2: Open the same file in 'r' mode and print the content
with open("demo.txt", "r") as file:
    print(file.read())

# 9.Using 'a' Mode
# Use 'a' mode to keep adding new lines to a file every time the program runs.
# Appending a new line each time the script is executed
with open("log.txt", "a") as file:
    file.write("This is a new line added.\n")
import datetime

with open("log.txt", "a") as file:
    now = datetime.datetime.now()
    file.write(f"New entry at {now}\n")