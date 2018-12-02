import pandas as pd
import numpy as np
d = {'d' : 1, 'c' : 2, 'b' : 3, 'a' : 4}

ser = pd.Series(d)
#print (ser)
#print(ser[:2])
#print(ser[[3]])
#print(np.exp(ser))
#print(ser['c'])
#ser = ser * 3
#print(ser)

#inputdata = {'first' : ser, 'second' : pd.Series([2.,3.,4.], index=['a','c','e'])}
#df = pd.DataFrame(inputdata)
#print(df)

#data = np.zeros((2))
#print(data)

#Adding lamda function
newdata = pd.DataFrame([{'a' : 3, 'b' : 4, 'c' : 5}, {'a' : 0.3, 'b' : 0.4, 'c' : 0.5}], index = {'row1','row2'})
print(newdata)
#Assigning new column without lemda function of multiplication

newdata_wo_lambda = newdata.assign(multi_no_lamda_function = newdata['a'] * newdata['b'])
print(newdata_wo_lambda)

newdata_lambda = newdata.assign(multi_with_lamda_function = lambda x: (x['a'] * x['b']))
print(newdata_lambda)

newdata_wo_lambda.at['row2', 'b'] = 0.9
newdata_lambda.at['row2', 'b'] = 0.9

print(newdata_wo_lambda)
print(newdata_lambda)

print(newdata_lambda['a'])
