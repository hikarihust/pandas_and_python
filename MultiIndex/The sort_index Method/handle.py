import pandas as pd

bigmac = pd.read_csv("../bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
print(bigmac.head(3))
bigmac.info()

print("================================")
bigmac.sort_index(ascending = [True, False], inplace = True)
print(bigmac.head(3))
