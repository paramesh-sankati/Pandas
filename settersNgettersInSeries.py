'''
#Accessing elements of series:
            -By using indices
            -by using label(s)
            -Sub set of series of Elements--By using Indices Range/Slicing
            -Sub set of series of elements--By using Labels Range/Slicing
            -Sub set of series of elements-By using Random indices

#Changing the Values of series:
            -changing single element by using index
            -changing single element by using label
            -changing multiple element by using indices
            -changing multiple element by using labels
             

'''
import numpy as np
import pandas as pd
lst=["abhi","ind","aus","rishi"]
s=pd.Series(lst)
s1=pd.Series(lst,index=["name1","name2","name3","name4"])
print(s)
print(s1)

#accessing using labels 
print(s1["name1":"name5"])
print(s1[::2])

#accessing random elements of series by using random indices
print(s[[0,2,3]])

#accessing random elements of series by using random label name
print(s1[["name3","name2","name4"]])

#changing values of series 
s[1]="hello"    #using index
print(s)

#using slicing
s[:2]=["ok","xyz"]
print(s)

#using label
print(s1)
s1["name1"]="ok"
print(s1)

#using label slicing
s1["name1":"name2"]=["abc","pqr"]
print(s1)

#changing random multiple elements
s[[0,2,3]]=["nik","mac","leo"]
print(s)