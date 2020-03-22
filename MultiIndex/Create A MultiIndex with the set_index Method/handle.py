import pandas as pd

bigmac = pd.read_csv("../bigmac.csv", parse_dates = ["Date"])
print(bigmac.head(3))
bigmac.info()

print("================================")
bigmac.set_index(keys = ["Date", "Country"], inplace = True)
print(bigmac)

print("================================")
bigmac.sort_index(inplace = True)
print(bigmac.head(3))

print("================================")
print(bigmac.index)
print(bigmac.index.names)
print(type(bigmac.index))
print(bigmac.index[0])
