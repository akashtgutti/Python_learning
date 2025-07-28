# Series

# Series : It is defined as a one-dimensional array that is capable of storing various data types.

import sys
print(sys.executable)

import pandas as pd

x = pd.Series([1, 2, 3, 4, 5])
print(x)
print(type(x))

print(x[3])

x = pd.Series([1, 2, 3, 4, 5],index=['a', 'b', 'c', 'd', 'e'])
print(x)
print(type(x))


x = pd.Series([1, 2, 3, 4, 5],index=['a', 'b', 'c', 'd', 'e'],dtype=float)
print(x)
print(type(x))

x = pd.Series([1, 2, 3, 4, 5],index=['a', 'b', 'c', 'd', 'e'],dtype=float,name="my_series")
print(x)
print(type(x))


# Using a dictionary to create a Series

z = {"name":["Python", "Java", "C++"], "rank":[1, 3,2]}

x1 = pd.Series(z)
print(x1)

print(x1["name"])