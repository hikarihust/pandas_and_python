import pandas as pd
import datetime as dt

print(pd.Timestamp("2015-03-31"))
print(pd.Timestamp("2015/03/31"))
print(pd.Timestamp("2013, 11, 04"))
print(pd.Timestamp("1/1/2015"))
print(pd.Timestamp("19/12/2015"))
print(pd.Timestamp("12/19/2015"))
print(pd.Timestamp("4/3/2000"))
print(pd.Timestamp("2021-03-08 08:35:15"))
print(pd.Timestamp("2021-03-08 6:13:29 PM"))

print(pd.Timestamp(dt.date(2015, 1, 1)))

print(pd.Timestamp(dt.datetime(2000, 2, 3, 21, 35, 22)))
