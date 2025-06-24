# 7.Fibonacci Generator
# Function fibonacci(n) returns a list of first n Fibonacci numbers.
# Example: fibonacci(5) → [0, 1, 1, 2, 3]
def fibonacci(n): 
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
num = int(input("Enter the number of Fiibonacci terms: "))
result = fibonacci(num)
print(f"First {num} Fibonacci numbers: {result}")