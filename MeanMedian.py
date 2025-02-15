import pandas as pd
s=pd.Series([12,23,54,77,34,56,21,90])
print(s.mean())

#Median
print(s.median())

#Variance
print(round(s.var(),2))

#standard deviation
print(round(s.std(),2))
