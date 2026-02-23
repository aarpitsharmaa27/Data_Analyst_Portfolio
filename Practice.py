import pandas as pd

data = {
    'Location': ['Chandigarh', 'Mohali', 'Panchkula'],
    'Users': [500, 300, 200],
    'Revenue': [15000, 8000, 5000]
}

df1 = pd.DataFrame(data)
print(df1)

print(pd.melt(df1, id_vars=["Location"], value_vars=["Users", "Revenue"], value_name= "Metric", var_name="Users/Revenue"))