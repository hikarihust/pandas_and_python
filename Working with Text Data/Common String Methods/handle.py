import pandas as pd 

chicago = pd.read_csv("../chicago.csv")
chicago["Department"] = chicago["Department"].astype("category")
chicago.info()
print(chicago.head(3))

print("===================")
print(chicago["Name"].str.lower())

print("===================")
print(chicago["Name"].str.upper())

print("===================")
print(chicago["Name"].str.title())

print("===================")
print(chicago["Position Title"].str.title())

print("===================")
chicago["Position Title"] = chicago["Position Title"].str.title()
print(chicago.head(3))

print("===================")
print(chicago["Department"].str.len())

