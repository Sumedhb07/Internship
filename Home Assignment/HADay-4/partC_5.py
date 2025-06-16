# Ask the user for a number
num = float(input("Enter a number: "))

# Check the number category
if num > 0:
    if num > 100:
        print("Positive and greater than 100")
    else:
        print("Positive but not greater than 100")
elif num < 0:
    print("Negative")
else:
    print("Zero")