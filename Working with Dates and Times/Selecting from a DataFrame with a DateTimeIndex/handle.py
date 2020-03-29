import pandas as pd
import datetime as dt

stocks = pd.read_csv("../date_time_data.csv", index_col='Date')
stocks.index = pd.DatetimeIndex(stocks.index)

print(stocks.head(3))
print("================================")
print(stocks.loc["2010-01-04"])
print("--------------------------------")
print(stocks.iloc[0])
print("--------------------------------")
print(stocks.loc["2013-10-01" : "2013-10-07"])

print("================================")
birthdays = pd.date_range(start = "1991-04-12", end = "2017-12-31", freq = pd.DateOffset(years = 1))
print(birthdays)
print("--------------------------------")
mask = stocks.index.isin(birthdays)
print(stocks[mask])
print("--------------------------------")
print(stocks.loc[mask])
