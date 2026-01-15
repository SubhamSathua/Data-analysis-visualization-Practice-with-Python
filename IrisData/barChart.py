import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("IrisData/iris.data.csv")


species = df.groupby("species")[["petal_length", "sepal_length"]].mean()

# print(species)
# print(species_name)
# print(df.head())
# print(type(df))

species.plot(kind="bar", figsize=(5, 5))
plt.xlabel("Mean")
plt.ylabel("Species")
plt.title("Iris data set")
plt.show()
# plt.bar(petal_length)