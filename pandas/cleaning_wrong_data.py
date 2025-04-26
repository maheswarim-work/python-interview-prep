import pandas as pd

df = pd.read_csv("data4.csv")
# print(type(df))

# df.loc[7, 'Duration'] = 45
# print(df.to_string())

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120
#
# print(df.to_string())

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)
#
# print(df.to_string())

# print(df.duplicated())

print(df.to_string())
df.drop_duplicates(inplace = True)
print(df.to_string())
