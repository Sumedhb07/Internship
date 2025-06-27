# 🐍 DAY 14 – HOME ASSIGNMENTS: Introduction to NumPy
# Part A: Creating NumPy Arrays
# 1.Import NumPy and:
# oCreate a 1D array with numbers from 1–10.
# oCreate a 2D array of shape (3, 3) with numbers from 1–9.
import numpy as np

array_1d = np.array([1,2,3,4,5,6,7,8,9,10]) 
print("1D array of number from 1-10: ",array_1d)                       

array_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n",array_2d)


# 2.Create an array of:
# oAll zeros (shape = (3, 3))
# oAll ones (shape = (2, 5))
# oAll random numbers (shape = (4,))
import numpy as np

array = np.array([1,2,3,4,5,6,7,8,9,10])
zeros = np.zeros((3,3))
print("\n",zeros)

ones = np.ones((2,5))
print("\n",ones)

r_number = np.random.rand(4,)
print("\n",r_number)
