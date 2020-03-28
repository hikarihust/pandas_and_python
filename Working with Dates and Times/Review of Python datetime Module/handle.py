import pandas as pd
import datetime as dt

someday = dt.date(2010, 1, 20)
print(someday)
print(someday.year)
print(someday.month)
print(someday.day)
print(dt.datetime(2010, 1, 10))
print(dt.datetime(2010, 1, 10, 17, 13, 57))
print(str(dt.datetime(2010, 1, 10, 17, 20, 30)))
print(str(someday))

print("=======================================")
sometime = dt.datetime(2010, 1, 10, 17, 13, 57)
print(sometime)
print(sometime.year)
print(sometime.month)
print(sometime.day)
print(sometime.hour)
print(sometime.minute)
print(sometime.second)
