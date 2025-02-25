import numpy as np
import pandas as pd
d={'first score':[100,90,np.nan,95],
   'Second Score':[30,45,56,np.nan],
   'Third Score':[np.nan,40,80,90]}
print(d)     #dict 

#convert dict data into dataframe
df=pd.DataFrame(d)
print(df)

#filling nan values with 0 for entire dataFrame obj
df.fillna(0,inplace=True)
print(df)

df.replace(to_replace=np.nan,value=0)
print(df)

#for specified col
df["first score"].fillna(0,inplace=True)
print(df)

#for specified row 
df.loc[1].fillna(0,inplace=True)
print(df)