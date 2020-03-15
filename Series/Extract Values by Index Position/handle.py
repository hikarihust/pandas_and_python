import pandas as pd

pokemon = pd.read_csv("../pokemon.csv", usecols = ["Pokemon"], squeeze = True)
google = pd.read_csv("../google_stock_price.csv", squeeze = True)

print(pokemon.head(3))
print(pokemon[[100, 200, 300]])
print(pokemon[50:101])
print(pokemon[:50])
print(pokemon[-30:])
print(pokemon[-30 : -10])
