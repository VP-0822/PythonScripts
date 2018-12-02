import pandas
import quandl
import math
import numpy as np
from sklearn import preprocessing

df = quandl.get('NSE/ASHOKLEY')

df = df[['Open','High','Low','Close','Total Trade Quantity']]
df['HL_Percent'] = (df['High'] - df['Low'])/ df['Low'] * 100.0
df['Daily_Percent_Change'] = (df['Close'] - df['Open'])/ df['Open'] * 100.0

df = df[['Close', 'HL_Percent', 'Daily_Percent_Change', 'Total Trade Quantity']]
#print(df.head())

forecast_col = 'Close'
df.fillna(-99999, inplace=True)

print('Length of df : ' + str(len(df)))
forecast_out = int(math.ceil(0.002*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)

print(df.tail(20))
