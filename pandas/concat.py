import pandas as pd
df_region1=pd.DataFrame({
    "customerid":[1,2],
    "name":["ali","ahmed"]
})
df_region2=pd.DataFrame({
    "customerid":[3,4],
    "name":["arman","kamran"]
})
df_concat=pd.concat([df_region1,df_region2],axis=0,ignore_index=True)
print(df_concat)