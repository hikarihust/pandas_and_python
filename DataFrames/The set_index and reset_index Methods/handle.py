import pandas as pd

bond = pd.read_csv("../jamesbond.csv")
print(bond.head(3))

bond.set_index("Film", inplace = True)
print(bond.head(3))

bond.reset_index(drop = False, inplace = True)
print(bond.head(3))

bond.set_index("Film", inplace = True)
print(bond.head(3))

bond.reset_index(inplace = True)
bond.set_index("Year", inplace = True)
print(bond.head(3))
