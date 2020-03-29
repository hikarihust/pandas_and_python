import pandas as pd
import datetime as dt

timeA = pd.Timestamp("2016-03-31 04:35:16 PM")
timeB = pd.Timestamp("2016-03-20 02:16:49 AM")
print(timeA)
print(type(timeA))
print(timeB)
print(type(timeB))
print("================================")
print(timeA - timeB)
print(type(timeA - timeB))

print("================================")
print(pd.Timedelta(weeks = 8, days = 3, hours = 12, minutes = 45))
print("--------------------------------")
print(pd.Timedelta("14 days 6 hours 12 minutes 49 seconds"))