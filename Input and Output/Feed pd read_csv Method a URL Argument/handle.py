import pandas as pd

baby_names = pd.read_csv("https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv")
print(baby_names.head(3))
