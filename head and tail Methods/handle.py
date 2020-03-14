import pandas as pd

pokemon = pd.read_csv("pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("google_stock_price.csv", squeeze = True)

print(pokemon.head(1))
print(google.tail(1))