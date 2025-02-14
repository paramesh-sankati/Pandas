#Syntax: SeriesObj.sort_values(ascending,inplace)
import pandas as pd
a=pd.Series([10,2,-3,23,5,0,12,14])
print(a)

#ascending order
a.sort_values(inplace=True)
print(a)

#descending order
print(a[::-1])
a.sort_values(ascending=False,inplace=True)
print(a)

#w.r.t values/ele order of indices also changed
