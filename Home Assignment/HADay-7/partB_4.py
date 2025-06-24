# Part B: Slicing Lists
# 4.Given numbers = [10, 20, 30, 40, 50, 60, 70], 
# print:First 3 elements
# Last 2 elements
# Elements from index 2 to 5 (excluding 5)
# Reverse the list using slicing

numbers = [10, 20, 30, 40, 50, 60, 70]

# First 3 elements
print("First 3 elements:", numbers[:3])

# Last 2 elements
print("Last 2 elements:", numbers[-2:])

# Elements from index 2 to 5 (excluding 5)
print("Index 2 to 5 (excluding 5):", numbers[2:5])

# Reverse the list using slicing
print("Reversed list:", numbers[::-1])

