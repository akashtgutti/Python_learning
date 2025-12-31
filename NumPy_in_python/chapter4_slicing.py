#NumPy array slicing

# Slicing arrays

# Slicing in python means taking elements from one given index to another given index.

# We pass slice instead of index like this: [start:end].

# We can also define the step, like this: [start:end:step].

# If we don't pass start its considered 0

# If we don't pass end its considered length of array in that dimension

# If we don't pass step its considered 1

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[0:4])
print(arr[4:])  # From index 4 to the end
print(arr[-5:-2])  # Negative indexing

# STEP
# Use the step value to determine the step of the slicing:

print(arr[0:5:2]) 


# Slicing 2-D Arrays

arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr3[1, 1:4])

arr4 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr4[0:2, 2])