# Part E: Explore and Practice
# 10.Import the os module:
# oList all files in the current directory.
# oGet the current working directory.
import os

# List all files and folders in the current directory
files = os.listdir()
print("Files in current directory:", files)

# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# 11.Import the sys module:
# oPrint the version of Python (sys.version).
# oPrint the command-line arguments (sys.argv).
# Write a greeting to greeting.txt
with open("greeting.txt", "w") as file:
    file.write("Hello, welcome to Python file handling!")

# 12.Import the statistics module:
# oCalculate the mean and median of the list [1, 2, 3, 4, 5, 100].
import statistics

numbers = [1, 2, 3, 4, 5, 100]

# Calculate mean and median
mean_value = statistics.mean(numbers)
median_value = statistics.median(numbers)

print("Mean:", mean_value)
print("Median:", median_value)