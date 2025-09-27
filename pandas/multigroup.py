import pandas as pd
data={
    "name":["ali","ahmed","khuzaima","shuja","zeeshan"],
    "age":[30,21,30,38,21],
    "salary":[3000,2000,6000,500,700]
}
df=pd.DataFrame(data)
grouped=df.groupby(["age","name"])["salary"].sum()
print(grouped)