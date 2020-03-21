import pandas as pd

bond = pd.read_csv("../jamesbond.csv", index_col = "Film")
bond.sort_index(inplace = True)
print(bond.head(3))

def good_movie(row):
    
    actor = row[1]
    budget = row[4]
    
    if actor == "Pierce Brosnan":
        return "The best"
    elif actor == "Roger Moore" and budget > 40:
        return "Enjoyable"
    else:
        return "I have no clue"
    
print("==================================")
print(bond.apply(good_movie, axis = "columns"))