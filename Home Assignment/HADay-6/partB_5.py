#Part B: Math Logic
#Sum of Digits
#Function sum_of_digits(n) returns the sum of all digits in a number.
#Example: 123 → 6
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
        return total 
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"sum of Digits of {number} is {result}") 
