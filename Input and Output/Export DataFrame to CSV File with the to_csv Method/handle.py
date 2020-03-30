import pandas as pd

baby_names = pd.read_csv("https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv")
print(baby_names.head(3))

print("==================================")
print(type(baby_names))
print("----------------------------------")
# baby_names.to_csv("../Baby Names_test.csv")
baby_names.to_csv("../Baby Names.csv", index = False, columns = ["Year of Birth", "Child's First Name", "Count"], encoding = "utf-8")