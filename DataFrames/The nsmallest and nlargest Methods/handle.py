import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

bond.info()

print("==============================")
print(bond.sort_values("Box Office", ascending = False).head(3))

print("==============================")
print(bond.nlargest(3, columns = "Box Office"))

print("==============================")
print(bond.nsmallest(n = 2, columns = "Box Office"))

print("==============================")
print(bond.nlargest(3, columns = "Budget"))
# print(bond.nlargest(3, columns = "Budget", keep="all"))

bond.nsmallest(n = 6, columns = "Bond Actor Salary")

bond["Box Office"].nlargest(8)

bond["Year"].nsmallest(2)