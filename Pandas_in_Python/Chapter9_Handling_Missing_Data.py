import pandas as pd

var = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv")

print(var)

# Here, wherever we have 105, we will replace it with 106.
print(var.replace(to_replace=105, value=106))

#Here, wherever we have 101, 102, 103, 104, 105, and 106, we will replace it with 0.

print(var.replace([101,102,103,104,105,106],0))

#if we want to replace values for specific columns, we can do that as well.
print(var.replace({"ID":[101,102,104]},34,regex=True))

#Forward fill method and backward fill method are used to fill missing values in a dataframe.
# Forward fill will propagate the last valid observation forward to the next valid.
print(var.replace(102,method='ffill'))

print(var.replace(103,method='bfill'))

# We can limit the nuber of forward filling or backward filling by using the limit parameter.
print(var.replace(102,method='ffill', limit=1))

#Interpolation is used to fill missing values in a dataframe.
# It will fill the missing values by using the values of the surrounding cells.
print(var.interpolate())