import pandas as pd
data={
    "name":['ali',None,'amjad','faizan','subhan','tanveer','hasin','salman'],
     "age":[25,None,33,23,34,45,55,36],
    "salary":[25000,None,50000,65000,28000,22000,55000,45000],
    "performance score":[80,None,95,88,66,78,94,83]
}
df=pd.DataFrame(data)
print(df)
df.dropna(inplace=True)
print(df)