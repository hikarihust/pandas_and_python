import pandas as pd

bigmac = pd.read_csv("../bigmac.csv", parse_dates = ["Date"])
print(bigmac.head(3))
bigmac.info()