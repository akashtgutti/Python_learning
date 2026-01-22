
"""
    data credit_data1;
    set credit_data;
    if exposure_amount > 10000 then high = 1;
    else high = 0;

    /* Calculate remaining balance */
    remaining_amount = exposure_amount - outstanding_balance;

    
run;
    
"""

import pandas as pd
import numpy as np

#instead of if else we can use numpy where
df = pd.read_csv(r"C:\ATG_python_with_ETL\24_11_2025\Python_learning\Pandas_in_Python\credit_risk_data_1000.csv")
print(df.head())
print(df.info())
df['high'] = np.where(df['exposure_amount'] > 10000,1,0)
print(df['high'].head())