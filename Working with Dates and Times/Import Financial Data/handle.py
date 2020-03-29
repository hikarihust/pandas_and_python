import pandas as pd
import datetime as dt

stocks = pd.read_csv("../date_time_data.csv", index_col='Date')
stocks.index = pd.DatetimeIndex(stocks.index)

print(stocks.head(3))
print("================================")
print(stocks.values)

print("================================")
print(stocks.columns)

print("================================")
print(stocks.index)
print("--------------------------------")
print(stocks.index[0])
print("--------------------------------")
print(type(stocks.index[0]))

print("================================")
print(stocks.axes)
