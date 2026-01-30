import pandas as pd
import matplotlib.pyplot as plt

msme = pd.read_csv("MSME/msme.csv")

state = msme.groupby("state_name")["total"].sum()
statesList = state.index.tolist()
totalList = state.values.tolist()

plt.pie(totalList, labels=statesList, autopct="%1.1f%%")
plt.title("msme states")
plt.show()