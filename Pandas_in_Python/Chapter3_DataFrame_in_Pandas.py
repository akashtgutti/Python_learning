# DataFrame

# DataFrame : It is a two-dimensional labeled data structure with columns of potentially different types.
# It is similar to a spreadsheet or SQL table, or a dictionary of Series objects.
# DataFrame is generally the most commonly used pandas object.

import pandas as pd

l = [1, 2, 3, 4, 5]

df = pd.DataFrame(l)
print(df)
print(type(df))

s = {"Name":["Akash","Shivani","Samarth"],"age":[23,24,25]}
df1 = pd.DataFrame(s)
print(df1)

df2= pd.DataFrame(s,columns=["Name"])
print(df2)

# Print specific row with column value
print(df2["Name"][2])


#Using Series to create a DataFrame
sr = {"s":pd.Series([1,2,3,5]), "t":pd.Series([4,5,6,7])}
df3 = pd.DataFrame(sr)
print(df3)