import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("IrisData/iris.data.csv")

species = df.groupby("species")[["petal_length", "sepal_length"]].mean()

species.plot(kind="line", figsize=(5, 5), linestyle='-.')
plt.title("Iris data set")
plt.xlabel("Species")
plt.ylabel("size")

plt.show()