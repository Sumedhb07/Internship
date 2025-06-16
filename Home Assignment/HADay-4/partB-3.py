#Part B: If-Elif-Else
# 3.Ask the user to enter marks (0–100) and display grade:
# o	90–100: Grade A
# o	75–89: Grade B
# o	50–74: Grade C
# o	Below 50: Fail
# Ask the user to enter marks
marks = int(input("Enter your marks (0–100): "))

# Determine the grade
if 90 <= marks <= 100:
    print("Grade A")
elif 75 <= marks <= 89:
    print("Grade B")
elif 50 <= marks <= 74:
    print("Grade C")
elif 0 <= marks < 50:
    print("Fail")
else:
    print("Invalid marks entered. Please enter a number between 0 and 100.")
