import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("IPL Data/ipl.csv")

team_runs = df.groupby("batting_team")["total_runs"].sum()
teams_list = team_runs.index.tolist()
runs_list = team_runs.values.tolist()


plt.figure(figsize=(8, 5))
plt.barh(teams_list, runs_list)
plt.title("IPL")
plt.xlabel("Teams")
plt.ylabel("Runs")
plt.show()