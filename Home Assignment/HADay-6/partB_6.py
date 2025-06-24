# 6.Armstrong Number Checker
# Function is_armstrong(n) returns True if number is an Armstrong number.
# (e.g., 153 → 1³ + 5³ + 3³ = 153)
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == n

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")