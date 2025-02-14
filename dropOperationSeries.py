import numpy as np
import pandas as pd
a=pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
print(a)

#dropping ele using label 
a=a.drop(["c"])
print(a) 

#or directly
a.drop(["d"],inplace=True)    #a is modified directly 
print(a)

a.drop(["a","b"],inplace=True)    #a is modified directly 
print(a)

#Dealing with Null values
a=pd.Series([100,200,np.nan,300,400,500],index=["a","b","c","d","e","f"])
print("No.of Null Values: ",a.size-a.count())