import pandas as pd

bigmac = pd.read_csv("../bigmac.csv", parse_dates = ["Date"], index_col = ["Date", "Country"])
bigmac.sort_index(inplace = True)
print(bigmac.head(3))
bigmac.info()

print("================================")
print(bigmac.loc[("2010-01-01", "Brazil")])

print("================================")
print(bigmac.loc[("2010-01-01", "Brazil"), "Price in US Dollars"])

print("================================")
print(bigmac.loc[("2015-07-01", "Chile"), "Price in US Dollars"])

