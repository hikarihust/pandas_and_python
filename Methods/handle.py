import pandas as pd

prices = [2.99, 4.45, 1.36]
s = pd.Series(prices)
print(s)
print(s.sum())
print(s.product())
print(s.mean())