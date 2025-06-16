#Part A: Basic If/Else
# 1.Ask the user for a number and:
# Print "Even number" if divisible by 2
# Otherwise, print "Odd number"

# Ask the user for a number
num = int(input("Enter a number: "))

# Check if the number is divisible by 2
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
