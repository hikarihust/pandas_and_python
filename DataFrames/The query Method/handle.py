import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

bond.info()

print("==============================")
bond.columns = [column_name.replace(" ", "_") for column_name in bond.columns]
print(bond.head(1))

print("==============================")
print(bond.query('Actor == "Sean Connery"'))
print("==============================")
print(bond.query("Director == 'Terence Young'"))
print("==============================")
print(bond.query("Actor != 'Roger Moore'"))

print("==============================")
print(bond.query("Box_Office > 600"))

print("==============================")
print(bond.query("Actor == 'Roger Moore' and Director == 'John Glen'"))

print("==============================")
print(bond.query("Actor in ['Timothy Dalton', 'George Lazenby']"))

print("==============================")
print(bond.query("Actor not in ['Sean Connery', 'Roger Moore']"))