import pandas as pd
import datetime as dt

bunch_of_dates = pd.date_range(start = "2000-01-01", end = "2010-12-31", freq = "24D")
print(bunch_of_dates)
print("================================================")
s = pd.Series(bunch_of_dates)
print(s.head(3))
print("================================================")
print(s.dt.day)
print("================================================")
print(s.dt.month)
print("================================================")
print(s.dt.day_name())
print("================================================")
mask = s.dt.is_quarter_start
print(s[mask])
print("================================================")
mask = s.dt.is_month_end
print(s[mask])
