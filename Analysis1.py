#OBJECTIVE 1:-
# To analyze the provided COVID-19 dataset and extract meaningful insights
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel('covid19dataset_cleaned.xlsx')
# Display the first few rows of the dataset
print(df.head())
# Get basic information about the dataset
print(df.info())
# Get summary statistics for numerical columns
print(df.describe())
# Check for missing values
print(df.isnull().sum())
# Plot the distribution of confirmed cases over time
if 'Date' in df.columns and 'Confirmed' in df.columns:
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Confirmed'], label='Confirmed Cases')
    plt.title('Confirmed COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Confirmed Cases')
    plt.legend()
    plt.show()

# Plotting the correlation matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='Oranges')
plt.title('Correlation Matrix')
plt.show()

# For instance, if there's a strong correlation between 'Deaths' and 'Confirmed', we can explore that relationship.
if 'Deaths' in df.columns and 'Confirmed' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Confirmed', y='Deaths', data=df)
    plt.title('Relationship Between Confirmed Cases and Deaths')
    plt.xlabel('Confirmed Cases')
    plt.ylabel('Deaths')
    plt.show()

# Example: Identify the country with the highest number of confirmed cases
if 'Country' in df.columns and 'Confirmed' in df.columns:
    country_max_cases = df.loc[df['Confirmed'].idxmax()]
    print(f"The country with the highest number of confirmed cases is: {country_max_cases['Country']} with {country_max_cases['Confirmed']} cases.")

# Based on the analysis, we can define the best objective.
# For example, if the goal is to predict future cases, we might proceed with a time series forecasting model.
# If the goal is to understand the factors contributing to the spread, we might explore regression or clustering.

# Example Objective: Predicting future COVID-19 cases based on historical data.
print("Objective: Predict future COVID-19 cases based on historical data.")
