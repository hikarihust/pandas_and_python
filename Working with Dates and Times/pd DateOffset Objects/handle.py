import pandas as pd
import datetime as dt

stocks = pd.read_csv("../date_time_data.csv", index_col='Date')
stocks.index = pd.DatetimeIndex(stocks.index)

stocks = stocks.sort_index()
print(stocks.head(3))
print("================================")
print(stocks.index)
print("--------------------------------")
stocks.index = stocks.index + pd.DateOffset(months = 8, years = 5, days = 12, hours = 3, minutes = 42)
print(stocks.index)
