import pandas as pd

pokemon = pd.read_csv("../pokemon.csv", index_col = ["Pokemon"], squeeze = True)

pokemon.sort_index(inplace = True)
print(pokemon.head(3))
print(pokemon.get(key = ["Moltres", "Meowth"]))
print(pokemon.get(key = "Charizard", default = "This is not a Pokemon"))
print(pokemon.get(key = "jksajk", default = "This is not a Pokemon"))

print(pokemon.get(key = ["Moltres__", "Meowth"], default = "This is not a Pokemon 2"))