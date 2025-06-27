# Part C: Indexing and Slicing
# 5.Create an array:
# arr = np.arange(1, 21).reshape(4, 5)
# oPrint the first row.
# oPrint the last column.
# oSlice the subarray of the first 2 rows and first 3 columns.
import numpy as np

# Creating the array
arr = np.arange(1, 21).reshape(4, 5)

# Print the first row
first_row = arr[0]
print("First row:", first_row)

# Print the last column
last_column = arr[:, -1]
print("Last column:", last_column)

# Slice the subarray of the first 2 rows and first 3 columns
subarray = arr[:2, :3]
print("Subarray (first 2 rows, first 3 columns):")
print(subarray)