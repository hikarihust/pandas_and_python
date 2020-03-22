import pandas as pd

bigmac = pd.read_csv("../bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
print(bigmac.head(3))
bigmac.info()

print("================================")
bigmac = bigmac.transpose()
print(bigmac)

print("================================")
print(bigmac.head(1))

print("================================")
print(bigmac.loc["Price in US Dollars", ("2016-01-01", "Denmark")])
