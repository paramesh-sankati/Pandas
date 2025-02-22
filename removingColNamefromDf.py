#Removing the colName from dataframe obj
'''
dataFrameObj.drop(columns="colname")
dataFrameObj.drop(columns=[colName1,colName2,...])
dataFrameObj.drop(columns=[colName1,colName2,...],inplace=True)
dataFrameObj.drop(columns=dataFrameObj.columns[colNumber1,colNum2,..],inplace=True)

'''
#df.drop(columns="hno",inplace=True)
#remove multiple cols
#df.drop(columns=['total','maths'],inplace=True)

#Remove the col by col number
'''
df.drop(columns=df.columns[9]) --removes col-9

df.drop(columns=df.columns[9],inplace=True)

'''
#removing the rows from a dataFrameObj

'''
DataframeObj.drop(labels=index value,axis=0)
DataframeObj.drop(labels=[index value1,index val2,index val3,..],axis=0)

'''
#removing the row 10 from dataFrameObj
#df.drop(labels=10,axis=0,inplace=True)

#removes multiple rows
#df.drop(labels=[2,3,5],axis=0,inplace=True)
