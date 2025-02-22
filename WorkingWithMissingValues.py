import numpy as np
import pandas as pd
d={'first score':[100,90,np.nan,95],
   'Second Score':[30,45,56,np.nan],
   'Third Score':[np.nan,40,80,90]}
print(d)     #dict 

#convert dict data into dataframe
df=pd.DataFrame(d)
print(df)

#to find missing values we use isna(),isnull(),notna(),notnull()
print(df.isna())
print(df.isna().sum())

print(df.isnull())
print(df.loc[1].isna())   #row -1

#column wise
print(df["first score"].isna())   #col-1

#similarly for notna(),notnull()