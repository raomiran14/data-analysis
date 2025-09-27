import pandas as pd
import numpy as np
data={
    "day":[1,2,3,4,5,6,7,8],
    "temperature":[23,np.nan,26,28,32,34,np.nan,38]
}
df=pd.DataFrame(data)
df["temperature"] = df["temperature"].interpolate(method="quadratic")
print(df)
