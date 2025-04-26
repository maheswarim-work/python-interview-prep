import pandas as pd

df = pd.read_csv('data5.csv')

print(df.corr())
