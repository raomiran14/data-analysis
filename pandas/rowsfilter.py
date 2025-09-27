import pandas as pd
data={
    "name":['ali','ahmed','amjad','faizan','subhan','tanveer','hasin','salman'],
     "age":[25,55,33,23,34,45,55,36],
    "salary":[25000,34000,50000,65000,28000,22000,55000,45000],
    "performance score":[80,86,95,88,66,78,94,83]
}
df=pd.DataFrame(data)
filtered_rows=df[df["salary"]>40000]
print("employees having salary greater than 40000 are")
print(filtered_rows)
#filtering rows using multiple conditions
filtered_rows=df[(df["salary"]>40000)&(df["age"]>30)]
print("employees with salary greater than 40000 and age greater than 30 are")
print(filtered_rows)

#using or condition
filtered_or=df[(df["age"]>30)|(df["performance score"]>90)]
print("employees having age greater than 30 or performance score greater than 90 are")
print(filtered_or)