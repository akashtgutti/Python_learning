# Access Array Elements
# Array indexing is the same as accessing an array element.

# You can access an array element by referring to its index number.

# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

print(arr[1]+arr[3])

print(arr[0:2])


# Access 2-D Arrays
# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

# Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

arr2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(arr2[0,1])
print(arr2[0,0:2])

# Access 3-D Arrays
# To access elements from 3-D arrays we can use comma separated integers representing the dimensions
# and the index of the element

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr3[0,1,2])