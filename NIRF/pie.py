import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("NIRF/NIRF.csv")

name_scores = df.groupby("Name")["Score"].sum()
names_list = name_scores.index.tolist()
scores_list = name_scores.values.tolist()

plt.pie(scores_list, labels=names_list, autopct="%1.1f%%")
plt.title("Score Distribution of NIRF Rankings")
plt.show()

