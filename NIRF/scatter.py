import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("NIRF/NIRF.csv")

plt.figure(figsize=(7, 5))
plt.scatter(
    df["Score"],
    df["Rank"],
    alpha=0.6,
    edgecolors="black"
)

plt.title("scatter plot")
plt.xlabel("scores")
plt.ylabel("ranks")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()