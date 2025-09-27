import pandas as pd
data={
    "name":['ali','ahmed','amjad','faizan','subhan','tanveer','hasin','salman'],
     "age":[25,55,33,23,34,45,55,36],
    "salary":[25000,34000,50000,65000,28000,22000,55000,45000],
    "performance score":[80,86,95,88,66,78,94,83]
}
df=pd.DataFrame(data)
print(df)
df["bonus"]=df["salary"]*0.1
print(df)
#using insert
df.insert(0,"employee id",[10,20,30,40,50,60,70,80])
print(df)
