import pandas as pd

pokemon = pd.read_csv("../pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("../google_stock_price.csv", squeeze = True)

print(2 in [1, 2, 3, 4, 5])
print(100 in [1, 2, 3, 4, 5])

print(pokemon.head(3))
print(100 in pokemon)
print(100 in pokemon.index)

print(pokemon.index)
print("Digimon" in pokemon.values)
print("Bulbasaur" in pokemon.values)