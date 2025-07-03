# Part B: Inspecting Arrays
# 3.Given:
# arr = np.arange(12).reshape(3, 4)
# oPrint its shape, size, ndim, and dtype.
# 4.Change the dtype of an array from float64 to int32.
import numpy as np

arr = np.arange(12).reshape(3, 4)
print("Shape:", arr.shape)     # (3, 4)
print("Size:", arr.size)       # 12
print("Number of dimensions:", arr.ndim)  # 2
print("Data type:", arr.dtype)           

float_array = np.array([1.5, 2.3, 3.7], dtype=np.float64)
int_array = float_array.astype(np.int32)
print("Converted array:", int_array)
print("New dtype:", int_array.dtype)