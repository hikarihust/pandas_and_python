import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

bond.info()

print("==============================")
bond.rename(columns = {"Year" : "Release Date", "Box Office" : "Revenue"}, inplace = True)
print(bond.head(1))

print("==============================")
bond.rename(index = {"Dr. No" : "Doctor No", 
                     "GoldenEye" : "Golden Eye",
                    "The World Is Not Enough" : "Best Bond Movie Ever"}, inplace = True)
print(bond.loc["Best Bond Movie Ever"])
print(bond.head(1))
print(bond.columns)

print("==============================")
bond.columns = ["Year of Release", "Actor", "Director", "Gross", "Cost", "Salary"]
print(bond.head(3))