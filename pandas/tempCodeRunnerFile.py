import pandas as pd
data={
 "Name":['ali','ahmed','rao'],
 "age":[10,20,30],
 "city":['karachi','lahore','peshawar']
}
df=pd.DataFrame(data)
print(df)
#df.to_csv("output.csv",index=False)
df.to_excel("output.xlsx",index=False)

