#Objective 1:-
#Identify the time period with the highest death-to-case ratio and visualize its trend over time.
import pandas as pd
import matplotlib.pyplot as plt
file_path = "covid19dataset_cleaned.xlsx"
df = pd.read_excel(file_path)
df["DEATH_CASE_RATIO"] = df["DEATH_COUNT"] / df["CASE_COUNT"]
df.replace([float("inf"), -float("inf")], pd.NA, inplace=True)
df.dropna(subset=["DEATH_CASE_RATIO"], inplace=True)
# Sort the date to ensure proper plotting
df.sort_values("date_of_interest", inplace=True)
# date with the maximum death-to-case ratio
peak_row = df.loc[df["DEATH_CASE_RATIO"].idxmax()]
# Plotting the trend
plt.figure(figsize=(14, 6))
plt.plot(df["date_of_interest"], df["DEATH_CASE_RATIO"], label="Death-to-Case Ratio", color='blue')
plt.scatter(peak_row["date_of_interest"], peak_row["DEATH_CASE_RATIO"], color='black', zorder=5)
plt.text(peak_row["date_of_interest"], peak_row["DEATH_CASE_RATIO"],
         f" Peak: {peak_row['DEATH_CASE_RATIO']:.2f} on {peak_row['date_of_interest'].date()}",
         verticalalignment='bottom', horizontalalignment='left', fontsize=10, color='black')
plt.title("COVID-19 Death-to-Case Ratio Over Time")
plt.xlabel("Date")
plt.ylabel("Death-to-Case Ratio")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()