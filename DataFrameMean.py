import pandas as pd

#mean of a df col
#print(df["col name"].mean())


#no.of free apps 
#df[df["type"]="free"].shape[0]    --->"type" is col name 

'''
no.of paid apps:
    print(len(df[df["type"]="paid"])

or
s=df['type'].value_counts()
print(s["free"])
'''