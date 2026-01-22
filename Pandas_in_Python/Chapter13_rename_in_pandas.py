# df.rename(columns={'old_name': 'new_name'}, inplace=True)
# columns={...} → dictionary mapping old column names to new names

# inplace=True → changes the DataFrame directly (optional, otherwise returns a new DataFrame)

import pandas as pd

df = pd.DataFrame({
    'id': [1, 2, 3],
    'claim_amt': [1000, 2000, 1500],
    'policy_no': [101, 102, 103]
})

df.rename(columns={'claim_amt':'Claim_amt_cust','policy_no' : 'Cust_policy_no'},inplace=True)

print(df)