#Objective 4:
#Analyze the borough with the highest cumulative death rate (deaths vs cases) and visualize it using a horizontal bar chart.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("covid19dataset_cleaned.xlsx")
df.columns = df.columns.str.strip().str.lower()

# Check for required columns
death_cols = ['bx_death_count', 'bk_death_count', 'mn_death_count', 'qn_death_count', 'si_death_count']
case_cols = ['bx_case_count', 'bk_case_count', 'mn_case_count', 'qn_case_count', 'si_case_count']

missing_death = [col for col in death_cols if col not in df.columns]
missing_case = [col for col in case_cols if col not in df.columns]
if missing_death or missing_case:
    raise ValueError(f"Missing columns: {missing_death + missing_case}")

# Calculate total deaths and cases by borough
boroughs = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
total_deaths = [df[col].sum() for col in death_cols]
total_cases = [df[col].sum() for col in case_cols]

# Calculate death rate (%)
death_rates = [(d / c * 100) if c != 0 else 0 for d, c in zip(total_deaths, total_cases)]

# Plot horizontal bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x=death_rates, y=boroughs, palette='Reds_r')
plt.title("COVID-19 Death Rate by Borough (%)")
plt.xlabel("Death Rate (%)")
plt.ylabel("Borough")
plt.tight_layout()
plt.grid(axis='x')
plt.show()
