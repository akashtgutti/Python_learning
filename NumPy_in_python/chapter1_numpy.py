import numpy as np

arr = np.array([1,3,4,5,6,7,8])

print(arr)

print(np.__version__)

print(type(arr))

# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

import numpy as np

arr1 = np.array(42)

print(arr1)

# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

# These are the most common and basic arrays.

arr2 = np.array([1, 2, 3, 4, 5])

print(arr2)

# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.

# These are often used to represent matrix or 2nd order tensors.

arr3 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr3)

# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.

# These are often used to represent a 3rd order tensor.

arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr4)
