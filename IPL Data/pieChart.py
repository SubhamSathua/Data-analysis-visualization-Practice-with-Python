import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("IPL Data/ipl.csv")

team_runs = df.groupby("batting_team")["total_runs"].sum()
teams_list = team_runs.index.tolist()
runs_list = team_runs.values.tolist()


# runs = [120, 95, 80, 60, 45]
# teams = ["CSK", "MI", "RCB", "KKR", "RR"]

plt.pie(runs_list, labels=teams_list, autopct="%1.1f%%")
plt.title("Runs Distribution of IPL Teams")
# plt.show()

# print(df.head())
# print(team_runs)
# print(type(team_runs))
# print(teams_list)
# print(runs_list)

