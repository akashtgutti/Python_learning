# Differences between CSV and XLS (excel) file formats :

# CSV format is a plain text format in which values are separated by commas (Comma Separated Values).

# XLS file format is an Excel Sheets binary file format which holds 
# information about all the worksheets in a file, including both content formatting.

import pandas as pd

X  = {"A":[1,2,3,4,5],"B":["Akash","Gutti","T","Kumar","Reddy"],"C":[10,20,30,40,50]}

df = pd.DataFrame(X)

print(df)

df.to_csv("C:\ATG_python_with_ETL\Python_learning\Pandas_in_Python\data.csv", index=False)
