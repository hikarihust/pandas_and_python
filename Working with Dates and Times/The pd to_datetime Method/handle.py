import pandas as pd
import datetime as dt

print(pd.to_datetime("2001-04-19"))
print(pd.to_datetime(dt.date(2015, 1, 1)))
print(pd.to_datetime(dt.datetime(2015, 1, 1, 14, 35, 20)))
print(pd.to_datetime(["2015-01-03", "2014/02/08", "2016", "July 4th, 1996"]))

print("========================================")
times = pd.Series(["2015-01-03", "2014/02/08", "2016", "July 4th, 1996"])
print(times)
print("----------------------------------------")
print(pd.to_datetime(times))

dates = pd.Series(["July 4th, 1996", "10/04/1991", "Hello", "2015-02-31"])
print(dates)
print("----------------------------------------")
print(pd.to_datetime(dates, errors = "coerce"))

print("========================================")
print(pd.to_datetime([1349720105, 1349806505, 1349892905, 1349979305, 1350065705], unit = "s"))
