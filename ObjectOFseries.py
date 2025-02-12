import pandas as pd
a=10
s=pd.Series(a)
print(s,type(s))

a=10.45
s=pd.Series(a)
print(s,type(s))

a=True
s=pd.Series(a)
print(s,type(s))

r=range(10,21,2)
s=pd.Series(r)
print(s,type(s))

lst=[1,2.98,"abhi",True]
s=pd.Series(lst)
print(s,type(s))

#Creating Series object with programmer defined index names
lst=[100,"abhi",43.34,"ind",True]
s=pd.Series(lst,index=["EID","NAME","SAL","COUNTRY","STATUS"])
print(s,type(s))