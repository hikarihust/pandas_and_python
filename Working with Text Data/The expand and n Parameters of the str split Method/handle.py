import pandas as pd 

chicago = pd.read_csv("../chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.info()
print(chicago.tail(3))

print("================================")
chicago[["First Name", "Last Name"]] = chicago["Name"].str.split(",", expand = True)
print(chicago.head(3))

print("================================")
chicago[["First Title Word", "Remaining Word"]] = chicago["Position Title"].str.split(" ", expand = True, n = 1)
print(chicago.head(3))

print("================================")
print(chicago["Position Title"].str.split(" ", expand = True, n = 1)[0])
