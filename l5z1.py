import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

start = dt.datetime(2013, 1, 1)
end = dt.datetime.today()
df_DJI = web.DataReader('^DJI', 'stooq', start=start, end=end)
df_DJI = df_DJI.drop(['Volume'], axis=1)
print(df_DJI.head())
df_DJI.plot(grid=True)
plt.show()
df_DAX = web.DataReader('^DAX', 'stooq', start=start, end=end)
df_DAX = df_DAX.drop(['Volume'], axis=1)
print(df_DAX.head())
df_DAX.plot(grid=True)
plt.show()
df_NDQ = web.DataReader('^NDQ', 'stooq', start=start, end=end)
df_NDQ = df_NDQ.drop(['Volume'], axis=1)
print(df_NDQ.head())
df_NDQ.plot(grid=True)
plt.show()