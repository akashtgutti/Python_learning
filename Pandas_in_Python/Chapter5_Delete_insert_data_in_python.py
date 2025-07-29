import pandas as pd

x = {"A":[1,2,3,4,5],"B":["Akash","Gutti","T","Kumar","Reddy"],"C":[10,20,30,40,50]}

df = pd.DataFrame(x)
print(df)

#Insert column
df.insert(1, "D","B")
print(df)

#Duplicate copy of the column

df.insert(1, "D1", df["B"])
print(df)

df["D2"] = df["B"][:4]

print(df)

#Delete column
var = df.pop("D2")

print(df)
print(var)


