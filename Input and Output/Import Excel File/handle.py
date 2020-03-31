import pandas as pd

df = pd.read_excel("../Data - Single Worksheet.xlsx")
print(df)
print("======================================")

data = pd.read_excel("../Data - Multiple Worksheets.xlsx", sheet_name=[0, 1])
print(type(data))
print("--------------------------------------")
print(data)
print("--------------------------------------")
print(data[0])