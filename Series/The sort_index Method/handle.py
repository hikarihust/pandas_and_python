import pandas as pd

pokemon = pd.read_csv("../pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("../google_stock_price.csv", squeeze = True)

print(pokemon)
pokemon = pokemon.sort_index(ascending = True)
print(pokemon)