import pandas as pd
df=pd.read_json("sample_Data.json")
print("displaying the info of a dataset")
print(df.info())