import pandas as pd
import datetime as dt

times = pd.date_range(start = "2016-01-01", end = "2016-01-10", freq = "D")
print(times)
print(type(times))
print("------------------------------------------------")
print(times[0])
print(type(times[0]))

print("================================================")
print(pd.date_range(start = "2016-01-01", end = "2016-01-15", freq = "W"))
