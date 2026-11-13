# OBJECTIVE 1:
# Analyze the COVID-19 dataset and summarize key information.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('covid19dataset_cleaned.xlsx')

date_col = next((col for col in df.columns if str(col).strip().lower() in ('date', 'date_of_interest')), None)
confirmed_col = next((col for col in df.columns if str(col).strip().lower() in ('confirmed', 'case_count')), None)
deaths_col = next((col for col in df.columns if str(col).strip().lower() in ('deaths', 'death_count')), None)
country_col = next((col for col in df.columns if str(col).strip().lower() in ('country', 'country_region')), None)

print('=== COVID-19 DATA ANALYSIS ===')
print(f'Dataset size: {df.shape[0]:,} rows x {df.shape[1]} columns')

print('\n=== DATA PREVIEW ===')
print(df.head().to_string(index=False))

print('\n=== COLUMN TYPES AND NON-NULL COUNTS ===')
df.info()

print('\n=== NUMERIC SUMMARY STATISTICS ===')
numeric_df = df.select_dtypes(include='number')
if numeric_df.empty:
    print('No numeric columns are available.')
else:
    print(numeric_df.describe().T.to_string())

print('\n=== MISSING VALUES ===')
missing = df.isnull().sum()
missing = missing[missing > 0]
if missing.empty:
    print('No missing values found.')
else:
    print(missing.to_string())

if date_col and confirmed_col:
    plot_data = df[[date_col, confirmed_col]].copy()
    plot_data[date_col] = pd.to_datetime(plot_data[date_col], errors='coerce')
    plot_data[confirmed_col] = pd.to_numeric(plot_data[confirmed_col], errors='coerce')
    plot_data = plot_data.dropna().sort_values(date_col)

    plt.figure(figsize=(12, 6))
    plt.plot(plot_data[date_col], plot_data[confirmed_col], color='royalblue', linewidth=1.5)
    plt.title('Confirmed COVID-19 Cases Over Time')
    plt.xlabel('Date')
    plt.ylabel('Confirmed Cases')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if not numeric_df.empty:
    plt.figure(figsize=(10, 7))
    sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f', cmap='Oranges', center=0)
    plt.title('Correlation Between Numeric Measures')
    plt.tight_layout()
    plt.show()

if confirmed_col and deaths_col:
    scatter_data = df[[confirmed_col, deaths_col]].apply(pd.to_numeric, errors='coerce').dropna()
    if not scatter_data.empty:
        plt.figure(figsize=(10, 6))
        sns.regplot(
            x=confirmed_col,
            y=deaths_col,
            data=scatter_data,
            scatter_kws={'alpha': 0.5},
            line_kws={'color': 'red'},
        )
        plt.title('Relationship Between Confirmed Cases and Deaths')
        plt.xlabel('Confirmed Cases')
        plt.ylabel('Deaths')
        plt.tight_layout()
        plt.show()

if country_col and confirmed_col:
    country_totals = df.groupby(country_col)[confirmed_col].sum()
    if not country_totals.empty:
        top_country = country_totals.idxmax()
        print(
            f'\n=== KEY FINDING ===\n'
            f'Highest reported confirmed-case total: {top_country} '
            f'({country_totals.max():,.0f} cases)'
        )

print('\nAnalysis complete.')
