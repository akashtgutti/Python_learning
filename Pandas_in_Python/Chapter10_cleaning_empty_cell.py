import pandas as pd

# One way to deal with empty cells is to remove rows that contain empty cells.

#This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

df = pd.read_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\data1.csv")

print(df)

new_df = df.dropna()
print(new_df)

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

# If you want to change the original DataFrame, use the inplace = True argument:


df.dropna(inplace = True)

print(df.to_string())


# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:


import pandas as pd

df1 = pd.read_csv('C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\data1.csv')

df1.fillna(130, inplace = True)

# Replace Only For Specified Columns
# The example above replaces all empty cells in the whole Data Frame.

# To only replace empty values for one column, specify the column name for the DataFrame:


import pandas as pd

df2 = pd.read_csv('C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\data1.csv')

df2.fillna({"Calories": 130}, inplace=True)

print(df2.to_string())

# Data of Wrong Format
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

import pandas as pd

df3 = pd.read_csv('C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\data1.csv')

df3['Date'] = pd.to_datetime(df3['Date'], format='mixed')

print(df3.to_string())

# Removing Rows
# The result from the converting in the example above gave us a NaT value, 
# which can be handled as a NULL value, and we can remove the row by using the dropna() method.

df3.dropna(subset=['Date'], inplace = True)
print(df3.to_string())


# Replacing Values
# One way to fix wrong values is to replace them with something else.

# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just 
# insert "45" in row 7:

df3.loc[7, 'Duration'] = 45
print(df3.to_string())


# Removing Duplicates

# Returns True for every row that is a duplicate, otherwise False:

print(df3.duplicated())

# Removing Duplicates

df3.drop_duplicates(inplace = True)
print(df3.to_string())




