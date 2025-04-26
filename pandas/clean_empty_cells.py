import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()
print(new_df.to_string())

# df.dropna(inplace = True)
#
# print(df.to_string())

# df.fillna(130, inplace = True)
# print(df.to_string())
