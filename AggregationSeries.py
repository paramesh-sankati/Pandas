import pandas as pd
#finding aggregate result of statistical operations
s=pd.Series([10,12,15,25,3,45,55])
print("Series of values:")
print(s)

print(s.agg(['max','mean','median','var','std','min','sum']))

#cumulative product
print(s.cumprod())