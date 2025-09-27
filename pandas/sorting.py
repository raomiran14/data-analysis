import pandas as pd
data={
    "name":["ali","ahmed","khuzaima","shuja","zeeshan"],
    "age":[30,25,22,38,21],
    "salary":[3000,2000,6000,500,700]
}
df=pd.DataFrame(data)
print(df)
df.sort_values(by="age",ascending=True,inplace=True)
print("sorted age in ascending order")
print(df)