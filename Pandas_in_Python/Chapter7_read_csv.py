# Read CSV Files


# CSV Files :
# A simple way to store big data sets is to use CSV files (comma separated files).
# CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

import pandas as pd

# Read CSV file into DataFrame

df = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv")
print(df)

#To fiter the rows, we can use the nrows parameter to read only a specific number of rows from the CSV file.
# For example, to read only the first 2 rows:
df1 = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv",nrows=2)
print(df1)

df2 = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv",usecols=["ID","Name"])
print(df2)

# To read specific columns, we can use the usecols parameter.
# Also, to read the specific columns by their index, we can pass a list of indices to the usecols parameter.
# For example, to read the first and third columns:

df3 = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv",usecols=[0,2])
print(df3)

# If we want to skip or drop specific rows while reading the CSV file, we can use the skiprows parameter.

df4 = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv", skiprows=[0, 1])
print(df4)

# If we want to use column as index, we can use the index_col parameter.
df5 = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv", index_col="ID")
print(df5)

# If we want specific row as header, we can use the header parameter.
df6 = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv", header=1)
print(df6)

# If we don't have header in the CSV file, we can set header=None. Also, we have use prefix to automatically 
# generate column names.

df7 = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv", header=None)
df7.columns = [f"Col{i}" for i in range(df7.shape[1])]
print(df7)

#How to change data types of particular columns while reading CSV file?
df8 = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\employees_sample.csv", dtype={"ID": str, "Salary": float})
print(df8)