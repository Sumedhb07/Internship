# Part D: Real-World File Use Tasks
# 10.Save User Input
# oAsk user for their name and a short bio
# oSave it to a file user_profile.txt
# Ask for user input
name = input("Enter your name: ")
bio = input("Write a short bio: ")

# Save input to a file
with open("user_profile.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Bio: {bio}\n")

# 11.Store Even Numbers
# oWrite a program to find even numbers from 1–50
# oSave them line-by-line into even_numbers.txt
# Open the file in write mode
with open("even_numbers.txt", "w") as file:
    # Loop through numbers from 1 to 50
    for number in range(1, 51):
        if number % 2 == 0:
            file.write(f"{number}\n")

# 12.Reverse File Content
# oRead lines from sample.txt
# oReverse each line and write it to reversed.txt 
# Open the input and output files
with open("sample.txt", "r") as infile, open("reversed.txt", "w") as outfile:
    for line in infile:
        reversed_line = line.rstrip()[::-1]  # Remove trailing newline and reverse
        outfile.write(reversed_line + "\n")  # Add newline after reversing