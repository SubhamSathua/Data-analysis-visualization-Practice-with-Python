import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("covid19/country_wise_latest.csv")
top10 = df.sort_values("Recovered / 100 Cases", ascending=False).head(10)

recovered_total = top10.groupby("Country/Region")["Recovered / 100 Cases"].sum()
country = recovered_total.index.tolist()
recovered = recovered_total.values.tolist()

# recovered_total = df.groupby("Country/Region")["Recovered / 100 Cases"].sum()
# country = recovered_total.index.tolist()
# recovered = recovered_total.values.tolist()


plt.figure(figsize=(7, 7))
plt.barh(country, recovered)
plt.title("Covid19 Recovered Data")
plt.xlabel("Countries")
plt.ylabel("Recovered")
plt.show()