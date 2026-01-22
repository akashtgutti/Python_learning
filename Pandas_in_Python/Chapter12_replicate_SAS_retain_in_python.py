# data claims_cumsum;
#     set claims;
#     retain cum_claim_amount 0;
#     cum_claim_amount + claim_amount;
# run;


import pandas as pd

# Sample claims data
claims = pd.DataFrame({
    'claim_id': [1, 2, 3, 4],
    'claim_amount': [1000, 2000, 1500, 3000]
})

claims['cum_sum'] = claims['claim_amount'].cumsum()

print(claims)

# Cumulative Sum by Group (Advanced)
# In health insurance, we often do cumulative sum per member or policy. In SAS, you might do it with a by statement:

# proc sort data=claims;
#     by policy_id;
# run;

# data claims_cumsum;
#     set claims;
#     by policy_id;
#     retain cum_claim_amount 0;
#     if first.policy_id then cum_claim_amount=0;
#     cum_claim_amount + claim_amount;
# run;

claims1 = pd.DataFrame({
    'policy_id': [101, 101, 102, 102, 102],
    'claim_amount': [1000, 2000, 1500, 500, 2500]
})

claims1['cum_sum_grp'] = claims1.groupby('policy_id')['claim_amount'].cumsum()

print(claims1)

