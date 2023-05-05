

import pandas as pd
df = pd.read_csv("C:\\Users\\ADMIN\\Downloads\\m.csv")
print(df)

print(df.describe())
print("Null Values")

print(df.isnull())

print("Information")
print(df.info())
print("SHape")
df.shape
print("Unique")
print(df.nunique())

print("Sample")
df.sample()

print("Sum")
#print(df.sum())

print("Fiina")
#df.fillna()

print(df.value_counts())

print("iloc")
print(df.iloc())
#df.concat()
#print(df.count())

#df.concat()

print("Print  Gender")
print(df[df['salary']==8000])
