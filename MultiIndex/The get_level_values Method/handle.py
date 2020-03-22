import pandas as pd

bigmac = pd.read_csv("../bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
print(bigmac.head(3))
bigmac.info()

print("================================")
print(bigmac.index)

print("================================")
print(bigmac.index.get_level_values(0))
print(bigmac.index.get_level_values("Date"))

print("================================")
print(bigmac.index.get_level_values(1))
print(bigmac.index.get_level_values("Country"))
