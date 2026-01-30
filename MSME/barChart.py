import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("MSME/msme.csv")

state_totals = df.groupby("state_name")["total"].sum()
states_list = state_totals.index.tolist()
totals_list = state_totals.values.tolist()


plt.figure(figsize=(8, 5))
plt.barh(states_list, totals_list)
plt.title("MSME")
plt.xlabel("States")
plt.ylabel("Total Enterprises")
plt.show()
