# Part F: Advanced NumPy Practice
# 11.Create an array of 100 random numbers and:
# oFind the top 5 maximum numbers
# oFind the average
# oFind the indices of all numbers > 50
# Create an array of 100 random numbers between 0 and 100
np.random.speed(0)  # For reproducibility
arr = np.random.randint(0, 100, 100)
print("Original Array:")
print(arr)

# Find the top 5 maximum numbers
top_5_max = np.sort(arr)[-5:]
print("\nTop 5 Maximum Numbers:")
print(top_5_max)

# Find the average
average = np.mean(arr)
print("\nAverage: ")
print(average)
# Find the indices of all numbers > 50
indices = np.where(arr > 50)[0]
print("\nIndices of numbers > 50:")
print(indices)

# Alternatively, find the numbers > 50
numbers = arr[arr > 50]
print("\nNumbers > 50:")
print(numbers)


# 12.Create a 5x5 array of random numbers between 10–100 and:
# oFind its transpose
# oFind the sum of its diagonal
# oExtract the diagonal elements
import numpy as np

# Create a 5x5 array of random numbers between 10 and 100
np.random.speed(0)  # For reproducibility
arr = np.random.randint(10, 100, (5, 5))
print("Original Array:")
print(arr)

# Find its transpose
transpose = arr.T
print("\nTranspose:")
print(transpose)

# Find the sum of its diagonal
diagonal_sum = np.trace(arr)
print(f"\nSum of diagonal: {diagonal_sum}")

# Extract the diagonal elements
diagonal_elements = np.diag(arr)
print("\nDiagonal elements:")
print(diagonal_elements)




# 13.Compare Lists vs NumPy:import numpy as np
# oCreate a Python list and a NumPy array of the same data.
# oCompare their memory usage using sys.getsizeof() and .nbytes.
# oCompare their performance for an operation like adding 1 to every element.
import numpy as np
import sys
import time

# Create a Python list and a NumPy array of the same data
data = list(range(1000000))
arr = np.array(data)

# Compare their memory usage
list_memory = sys.getsizeof(data)
array_memory = arr.nbytes
print(f"List memory usage: {list_memory} bytes")
print(f"NumPy array memory usage: {array_memory} bytes")

# Compare their performance for adding 1 to every element
start_time = time.time()
new_list = [x + 1 for x in data]
list_time = time.time() - start_time
print(f"List operation time: {list_time:.6f} seconds")

start_time = time.time()
new_arr = arr + 1
array_time = time.time() - start_time
print(f"NumPy array operation time: {array_time:.6f} seconds")



# 14.Prime Numbers with NumPy:
# oCreate an array of numbers from 1–100.
# oUse boolean masking to filter out only the prime numbers.
import numpy as np

# Create an array of numbers from 1 to 100
numbers = np.arange(1, 101)

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Vectorize the function
is_prime_vec = np.vectorize(is_prime)

# Use boolean masking to filter out only the prime numbers
prime_numbers = numbers[is_prime_vec(numbers)]
print("Prime numbers between 1 and 100:")
print(prime_numbers)


# 15.Moving Averages:
# oGiven an array of daily temperatures, write a NumPy script to compute a 3-day moving average.
import numpy as np

# Given array of daily temperatures
temperatures = np.array([25, 27, 23, 24, 28, 29, 26, 27, 30, 32])

# Compute 3-day moving average
def moving_average(data, window_size):
    weights = np.repeat(1.0, window_size) / window_size
    return np.convolve(data, weights, 'valid')

# Apply the moving average function
window_size = 3
moving_avg = moving_average(temperatures, window_size)

print("Daily Temperatures:")
print(temperatures)
print(f"\n{window_size}-day Moving Average:")
print(moving_avg)

