import pandas as pd
#addition with same label names 
a=pd.Series([100,200,300],index=["a","b","c"])
b=pd.Series([10,20,30],index=["a","b","c"])
c=a.add(b)
print(c)

#addition with diff label/index names
a=pd.Series([100,200,300],index=["x","b","c"])
b=pd.Series([10,20,30],index=["a","b","y"])
c=a.add(b)
print(c)

#addition with diff labels but using fill_value
a=pd.Series([100,200,300],index=["x","b","c"])
b=pd.Series([10,20,30],index=["a","b","y"])
c=a.add(b,fill_value=0)
print(c)

#similary for Subtraction