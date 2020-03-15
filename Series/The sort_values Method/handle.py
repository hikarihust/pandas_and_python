import pandas as pd

pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)

print(pokemon.sort_values().head())
print(pokemon.sort_values(ascending = False).tail())
print(pokemon.sort_values(ascending = False).head(1))
print(google.sort_values(ascending = False).head(1))
print(google)