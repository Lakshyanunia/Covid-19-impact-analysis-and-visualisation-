#OBJECTIVE 5:-
#  Visualize the proportion of total COVID-19 cases contributed by each NYC borough using a pie chart.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_excel("covid19dataset_cleaned.xlsx")

# Strip whitespace and standardize column names
df.columns = df.columns.str.strip().str.lower()

# Ensure borough-level case columns exist
borough_columns = [
    'bx_case_count', 'bk_case_count', 'mn_case_count',
    'qn_case_count', 'si_case_count'
]

# Check if all required borough columns are present
missing_cols = [col for col in borough_columns if col not in df.columns]
if missing_cols:
    raise ValueError(f"Missing columns in dataset: {missing_cols}")

# Calculate total cases per borough
total_cases = {
    'Bronx': df['bx_case_count'].sum(),
    'Brooklyn': df['bk_case_count'].sum(),
    'Manhattan': df['mn_case_count'].sum(),
    'Queens': df['qn_case_count'].sum(),
    'Staten Island': df['si_case_count'].sum()
}

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(total_cases.values(), labels=total_cases.keys(),
        autopct='%1.1f%%', startangle=140,
        colors=sns.color_palette("Purples"))
plt.title("Proportion of Total COVID-19 Cases by NYC Borough")
plt.tight_layout()
plt.axis('equal')
plt.show()

