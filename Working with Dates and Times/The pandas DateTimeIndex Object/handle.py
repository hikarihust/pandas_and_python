import pandas as pd
import datetime as dt

dates = ["2016/01/02", "2016/04/12", "2009/09/07"]
print(pd.DatetimeIndex(dates))
print("----------------------------------")
dates = [dt.date(2016, 1, 10), dt.date(1994, 6, 13), dt.date(2003, 12, 29)]
dtIndex = pd.DatetimeIndex(dates)
print(dtIndex)

values = [100, 200, 300]
print(pd.Series(data = values, index = dtIndex))
