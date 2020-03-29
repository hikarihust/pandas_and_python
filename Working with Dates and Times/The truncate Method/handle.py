import pandas as pd
import datetime as dt

stocks = pd.read_csv("../date_time_data.csv", index_col='Date')
stocks.index = pd.DatetimeIndex(stocks.index)

stocks = stocks.sort_index()
print(stocks.head(3))
print("================================")
print(stocks.truncate(before = "2012-06-07", after = "2013-02-28"))
