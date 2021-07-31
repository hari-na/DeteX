import pandas as pd, numpy as np

df = pd.read_excel("HalloSaar2.xlsx")
df = df.drop(['ID', 'candidate', 'date'], axis = 1)
df['units'] = df['units'].apply(np.int64)
df = pd.get_dummies(df, columns=["event"])
print(df.head())