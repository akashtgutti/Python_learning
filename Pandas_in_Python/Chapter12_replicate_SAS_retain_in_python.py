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