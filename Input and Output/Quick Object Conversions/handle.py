import pandas as pd

baby_names = pd.read_csv("https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv")
print(baby_names.head(3))

print("==================================")
print(type(baby_names))
print("----------------------------------")
print(baby_names["Child's First Name"])
print("----------------------------------")
# print(", ".join(str(name) for name in baby_names["Child's First Name"]))
print(", ".join(baby_names["Child's First Name"]))
