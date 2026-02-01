import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

nirf = pd.read_csv("Seborn/nirf/NIRF.csv")

sns.boxplot(
    data=nirf,
    y="Score"
)

plt.title("Box Plot of NIRF")
plt.show()