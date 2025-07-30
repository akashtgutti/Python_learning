# Functions in Pandas

import pandas as pd

# Functions in Pandas are used to perform operations on DataFrames and Series.

df = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv")

df.index
#Index of the dataframe it will return the index of start from 0 to n-1 where n is the number of rows in the dataframe.
# Also, it returns step, which is increment as 1 by default.
print(df.index)

# Print dataframe columns
print(df.columns)

#If we want to get overall summary of dataframe then we can use describe() function.
# It will return the summary of all the columns in the dataframe.

print(df.describe())

# if we want particular header then we can use the head() function.
# It will return the first 5 rows of the dataframe by default.

print(df.head(2))

# If we want to get the last 5 rows of the dataframe then we can use the tail() function.
# It will return the last 5 rows of the dataframe by default.

print(df.tail())

# If we want to get last 2 rows.
print(df.tail(2))

print(df[:2])

# How to convert index into Array?
print(df.index.array)

# How to convert into NumPy array?
print(df.to_numpy())

import numpy as np

ar = np.asarray(df)
print(ar)

print(df.sort_index(axis=0,ascending=False))

# How access particular column row data?
print(df["Name"][1])

# How to change particular column row data?
df.loc[1, "Name"] = "Akkku"
print(df)

# Indexing wise column data extraction
print(df.loc[[1,2],["ID","Name"]])

print(df.loc[[1,2],:])


# First we have to pass index of row (start from 0), then column index which is start from 0.
print(df.iloc[1,2])

# How to remove row and column using drop() function.

df2 = df.drop("Salary", axis=1)

df3 = df.drop(1, axis=0, inplace=True)

print(df3)