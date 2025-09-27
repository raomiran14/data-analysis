import pandas as pd
df_customers=pd.DataFrame({
    "customerid":[1,2,3],
    "name":["ali","ahmed","saim"]
})
df_orders=pd.DataFrame({
    "customerid":[1,2,4],
    "orderamount":[240,445,660]
})
df_merged=pd.merge(df_customers,df_orders,on="customerid",how="right")
print(df_merged)