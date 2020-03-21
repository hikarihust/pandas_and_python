import pandas as pd 

chicago = pd.read_csv("../chicago.csv").dropna(how="all")
chicago["Department"] = chicago["Department"].astype("category")
chicago.info()
print(chicago.tail(3))

print("=================================")
mask = chicago["Position Title"].str.lower().str.contains("water")
print(chicago[mask])

print("=================================")
mask2 = chicago["Position Title"].str.lower().str.startswith("water")
print(chicago[mask2])

print("=================================")
mask3 = chicago["Position Title"].str.lower().str.endswith("ist")
print(chicago[mask3])


print("=================================")
df = pd.DataFrame( {'c1':[pd.np.nan,'い','う'], 'c2':['か', 'き', 'く']})
print(df)
df = df[df['c1'].str.contains('う', na=False)]
print(df)
