import pandas as pd
a=pd.Series([10,2,-3,23,5,0,12,14])

#Find max using SeriesObj.max
maxv=a.max()
print("Max element:",maxv)

#Approach-2
a.sort_values(inplace=True)
print("Max:",a.values[-1])

#By using SeriesObj.nlargest(n)
maxv=a.nlargest(1)
print("Max Ele:",a.nlargest(1).values)

#2 largest Elements
maxv=a.nlargest(2)
print("2 Largest Values:",maxv.values)

#Similarly For min
minv=a.min()
print(minv)