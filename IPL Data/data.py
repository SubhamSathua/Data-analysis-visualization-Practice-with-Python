import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("IPL Data/ipl.csv")
# print(df.head())

team_runs = df.groupby("batting_team")["total_runs"].sum()
print(team_runs)
teams_list = team_runs.index.tolist()
# print(teams_list)
runs_list = team_runs.values.tolist()
# print(runs_list)


# runs = [120, 95, 80, 60, 45]
# teams = ["CSK", "MI", "RCB", "KKR", "RR"]

# plt.pie(runs_list, labels=teams_list, autopct="%1.1f%%")
# plt.title("Runs Distribution of IPL Teams")
# plt.show()
