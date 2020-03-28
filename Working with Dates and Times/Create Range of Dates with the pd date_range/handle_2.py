import pandas as pd
import datetime as dt

print(pd.date_range(start = "2012-09-09", periods = 50, freq = "6H"))
print("------------------------------------------------")
print(len(pd.date_range(start = "2012-09-09", periods = 50, freq = "6H")))
print("================================================")
