import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("NIRF/NIRF.csv")

plt.figure(figsize=(12, 8))
sns.barplot(data=df, x="Score", y="Name", palette="viridis")
plt.title("nirf rankings")
plt.xlabel("Score")
plt.ylabel("Institute Name")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
