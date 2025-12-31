# Shape of an Array
# The shape of an array is the number of elements in each dimension.

# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr1 = np.array([1, 2, 3, 4], ndmin=5)

print(arr1)
print('shape of array :', arr1.shape)