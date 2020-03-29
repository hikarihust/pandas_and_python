import pandas as pd
import datetime as dt

stocks = pd.read_csv("../date_time_data.csv", index_col='Date')
stocks.index = pd.DatetimeIndex(stocks.index)
print(stocks.head(3))

print("================================")
someday = stocks.index[1]
print(someday)
print(type(someday))
print("--------------------------------")
print(someday.day)
print(someday.month)
print(someday.year)
print(someday.day_name())
print(someday.is_month_end)
print(someday.is_month_start)

print("================================")
stocks.insert(0, "Day of Week", stocks.index.day_name())
print(stocks)
print("--------------------------------")
stocks.insert(1, "Is Start of Month", stocks.index.is_month_start)
print(stocks)
print("--------------------------------")
print(stocks[stocks["Is Start of Month"]])
