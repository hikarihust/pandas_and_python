import pandas as pd

pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
print(pokemon)

google = pd.read_csv("google_stock_price.csv", squeeze = True)
print(google)