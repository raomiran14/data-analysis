import pandas as pd
data={
    "day":[1,2,3,4,5,6,7,8],
    "temperature":[23,None,26,28,32,34,None,38]
}
df=pd.DataFrame(data)
df["temperature"] = df["temperature"].interpolate(method="linear")
print(df)
