#OBJECTIVE 4:-
#Visualizing Monthly Hospitalizations through Area Chart:-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean dataset
df = pd.read_excel("covid19dataset_cleaned.xlsx")
df.columns = df.columns.str.strip().str.lower()

# Convert date column
df['date_of_interest'] = pd.to_datetime(df['date_of_interest'])

# Check for hospitalization columns
hospital_cols = [
    'bx_hospitalized_count', 'bk_hospitalized_count',
    'mn_hospitalized_count', 'qn_hospitalized_count',
    'si_hospitalized_count'
]

missing_cols = [col for col in hospital_cols if col not in df.columns]
if missing_cols:
    raise ValueError(f"Missing hospitalization columns: {missing_cols}")

# Sum up hospitalizations across all boroughs
df['total_hospitalized'] = df[hospital_cols].sum(axis=1)

# Resample monthly
monthly_hospital = df.set_index('date_of_interest')['total_hospitalized'].resample('M').sum()

# Plot area chart
plt.figure(figsize=(14, 6))
plt.fill_between(monthly_hospital.index, monthly_hospital.values, color='pink', alpha=0.6)
plt.plot(monthly_hospital.index, monthly_hospital.values, color='green', linewidth=2)
plt.title("Monthly COVID-19 Hospitalizations in NYC")
plt.xlabel("Month")
plt.ylabel("Hospitalized Cases")
plt.grid(True)
plt.tight_layout()
plt.show()

