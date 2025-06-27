# Part B: Text File Operations
# 4.Write Multiple Lines
# oCreate a file bio.txt
# oWrite the following lines (each on a new line):
# Name: Ravi  
# Age: 22  
# Course: Python  
# Create and write multiple lines to bio.txt
with open("bio.txt", "w") as file:
    file.write("Name: Ravi\n")
    file.write("Age: 22\n")
    file.write("Course: Python\n")

# 5.Read Line by Line
# oRead and print each line from bio.txt using a loop.
# Read and print each line from bio.txt
with open("bio.txt", "r") as file:
    for line in file:
        print(line.strip())

# 6.Count Words, Lines, Characters
# oFrom a file sample.txt, print:
# Total lines
# Total words
# Total characters
# Initialize counters
line_count = 0
word_count = 0
char_count = 0

with open("sample.txt", "r") as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

print("Total lines:", line_count)
print("Total words:", word_count)
print("Total characters:", char_count)