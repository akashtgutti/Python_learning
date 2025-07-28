# Arithmatic Operation in pandas

import pandas as pd
S = {"Id":[1,23,45,67,89,67],"Age":[34,5,6,7,8,9]}
df = pd.DataFrame(S)
print(df)

# Adding a new column
df["Age + Id"] = df["Age"] + df["Id"]
print(df)

df["Age*Id"] = df["Age"] * df["Id"]
print(df)

df["Age/Id"] = df["Age"] / df["Id"]
print(df)

df["Age >= Id"] = df["Age"] >= df["Id"]
print(df)

df["Age <= Id"] = df["Age"] <= df["Id"]
print(df)

