import pandas as pd 

chicago = pd.read_csv("../chicago.csv")
chicago["Department"] = chicago["Department"].astype("category")
chicago.info()

print(chicago)
print(chicago.head(3))

print("==============================")
print(chicago["Department"].nunique())

print("==============================")
print(chicago["Department"].count())

