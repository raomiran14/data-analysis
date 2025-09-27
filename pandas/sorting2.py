import pandas as pd
data={
    "name":["ali","ahmed","khuzaima","shuja","zeeshan"],
    "age":[30,25,22,38,21],
    "salary":[3000,2000,6000,500,700]
}
df=pd.DataFrame(data)
print(df)
df.sort_values(by=["name","age"],ascending=[True,False],inplace=True)
print("sorted name and age in ascending order")
print(df)