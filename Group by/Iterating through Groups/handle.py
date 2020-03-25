import pandas as pd

fortune = pd.read_csv("../fortune1000.csv", index_col = "Rank")
sectors = fortune.groupby("Sector")
print(fortune.head(3))
print("----------------------------------------")
print(len(fortune))
print("----------------------------------------")
print(fortune.tail(3))
print("========================================")

df = pd.DataFrame(columns = fortune.columns)
print(df ) 
print("----------------------------------------")
for sector, data in sectors:
    highest_revenue_company_in_group = data.nlargest(1, "Revenue")
    df = df.append(highest_revenue_company_in_group)
print(df)
print("========================================")

cities = fortune.groupby("Location")
df = pd.DataFrame(columns = fortune.columns)
print(df)
print("----------------------------------------")
for city, data in cities:
    highest_revenue_in_city = data.nlargest(1, "Revenue")
    df = df.append(highest_revenue_in_city)

print(df)