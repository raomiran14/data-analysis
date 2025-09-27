import pandas as pd
df=pd.read_json("sample_Data.json")
print("displaying first 10 rows")
print(df.head(10))
print("displaying last 10 rows")
print(df.tail(10))