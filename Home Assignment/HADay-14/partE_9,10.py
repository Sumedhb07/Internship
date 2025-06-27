# Part E: Reshaping and Stacking
# 9.Create a 1D array with numbers from 1–12 and:
# oReshape it into a 3×4 array.
# oFlatten it back to a 1D array.
import numpy as np

# Create a 1D array with numbers from 1 to 12
arr = np.arange(1, 13)
print("Original 1D Array:")
print(arr)

# Reshape it into a 3x4 array
arr_reshaped = arr.reshape(3, 4)
print("\nReshaped 3x4 Array:")
print(arr_reshaped)

# Flatten it back to a 1D array
arr_flattened = arr_reshaped.flatten()
print("\nFlattened 1D Array:")
print(arr_flattened)



# 10.Stack arrays:
# oCreate a = [1, 2, 3] and b = [4, 5, 6]
# oStack them vertically and horizontally.
import numpy as np

# Create two arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack them vertically
vertical_stack = np.vstack((a, b))
print("Vertical Stack:")
print(vertical_stack)

# Stack them horizontally
horizontal_stack = np.hstack((a, b))
print("\nHorizontal Stack:")
print(horizontal_stack)

