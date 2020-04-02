import pandas as pd

baby_names = pd.read_csv("https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv")
print(baby_names.head(3))
print("----------------------------------")
print(type(baby_names))
print("==================================")
girls = baby_names[baby_names["Gender"] == "FEMALE"]
boys = baby_names[baby_names["Gender"] == "MALE"]

excel_file = pd.ExcelWriter("Baby Names.xlsx")
girls.to_excel(excel_file, sheet_name = "Girls", index = False)
boys.to_excel(excel_file, sheet_name = "Boys", index = False, columns = ["Gender", "Child's First Name", "Count"])

excel_file.save()