import pandas as pd

about_me = ["Smart", "Handsome", "Charming", "Brilliant", "Humble"]
s = pd.Series(about_me)
print(s)
print(s.values)
print(s.index)
print(s.dtype)