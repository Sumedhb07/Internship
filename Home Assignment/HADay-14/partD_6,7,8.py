#  Part D: Array Operations
# 6.Elementwise operations:
# oCreate two arrays of the same shape (e.g., a = [[1,2],[3,4]], b = [[5,6],[7,8]])
# oPerform elementwise:
# Addition
# Subtraction
# Multiplication
# Division
import numpy as np

# Create two arrays of the same shape
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print("Array a: ")
print(a)
print("\nArray b: ")
print(b)
print("\nElementwise Addition: ")
print(addition)
print("\nElementwise Subtraction: ")
print(subtraction)
print("\nElementwise Multiplication: ")
print(multiplication)
print("\nElementwise Division: ")
print(division)


# 7.Find:
# oSum of all elements
# oMin, max, and average of an array
import numpy as np

array = np.array([1, 4, 9, 16, 25])

# Sum of all elements
sum_elements = np.sum(array)

# Min, max, and average of the array
min_element = np.min(array)
max_element = np.max(array)
average = np.mean(array)

print("Original Array:")
print(array)
print("\nSum of all elements: ")
print(sum_elements)
print("Min element: ")
print(min_element)
print("Max element: ")
print(max_element)
print("Average: ")
print(average)

# 8.Use NumPy to compute:
# oSquare root of every element in an array
# oSquare of every element in an array
import numpy as np

array = np.array([1, 4, 9, 16, 25])

# Square root of every element
sqrt_elements = np.sqrt(array)

# Square of every element
square_elements = np.square(array)

# Print the results
print("Original Array:")
print(array)
print("\nSquare root of every element:")
print(sqrt_elements)
print("\nSquare of every element:")
print(square_elements)


