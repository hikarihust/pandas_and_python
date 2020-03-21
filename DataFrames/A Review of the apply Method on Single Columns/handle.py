import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

bond.info()
def convert_to_string_and_add_millions(number):
    return str(number) + " MILLIONS!"

print("==============================")
print(bond["Box Office"].apply(convert_to_string_and_add_millions))

print("==============================")
columns = ["Box Office", "Budget", "Bond Actor Salary"]
for col in columns:
    bond[col] = bond[col].apply(convert_to_string_and_add_millions)
print(bond.head(3))

print("==============================")
bond.info()