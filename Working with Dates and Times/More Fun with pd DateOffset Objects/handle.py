import pandas as pd
import datetime as dt
from pandas.tseries.offsets import *

stocks = pd.read_csv("../date_time_data.csv", index_col='Date')
stocks.index = pd.DatetimeIndex(stocks.index)

stocks = stocks.sort_index()
print(stocks.head(3))
print("================================")
print(stocks.index - MonthEnd())
print("--------------------------------")
print(stocks.index - BMonthEnd())
print("--------------------------------")
print(stocks.index - QuarterEnd())
print("--------------------------------")
print(stocks.index - QuarterBegin())
print("--------------------------------")
print(stocks.index + YearBegin())
