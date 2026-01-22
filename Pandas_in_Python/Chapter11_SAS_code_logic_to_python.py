
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


# In Pandas, we can join two datasets using the merge() function, similar to SQL joins. 
# We can perform inner, left, right, or outer joins depending on whether we want all records or only matching records

policy = pd.DataFrame({
    'policy_id': [101, 102, 103],
    'member_name': ['Alice', 'Bob', 'Charlie']
})

claims = pd.DataFrame({
    'claim_id': [1001, 1002, 1003],
    'policy_id': [101, 103, 104],
    'claim_amount': [5000, 7000, 2000]
})

# Inner join on policy_id
merged_data = pd.merge(claims, policy, on='policy_id', how='inner')
merged_data1 = pd.merge(claims, policy, on='policy_id', how='left')
merged_data2 = pd.merge(claims, policy, on='policy_id', how='right')
print(merged_data)
print(merged_data1)
print(merged_data2)