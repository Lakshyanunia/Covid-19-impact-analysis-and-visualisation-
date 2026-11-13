# COVID-19 Data Analysis and Visualization using Python

## 📌 Project Overview

This project focuses on analyzing and visualizing COVID-19 data to understand the spread of the pandemic, hospitalization trends, death rates, and the distribution of confirmed cases across different boroughs of New York City (NYC).

Using Python libraries such as **Pandas, Matplotlib, and Seaborn**, the project performs data analysis and creates meaningful visualizations to identify trends, patterns, and insights from the COVID-19 dataset.

## 🎯 Objectives

The project covers the following analysis objectives:

1. **COVID-19 Dataset Analysis**
   - Analyze the dataset and summarize key information.
   - Examine dataset dimensions, data types, missing values, and statistical summaries.
   - Visualize confirmed cases over time.
   - Explore correlations between numerical variables.
   - Analyze the relationship between confirmed cases and deaths.

2. **Death-to-Case Ratio Analysis**
   - Calculate the death-to-case ratio.
   - Identify the time period with the highest ratio.
   - Visualize the ratio trend over time.

3. **Monthly Hospitalization Analysis**
   - Calculate total hospitalizations across NYC boroughs.
   - Aggregate hospitalization data monthly.
   - Visualize monthly hospitalization trends using an area chart.

4. **Borough-wise Death Rate Analysis**
   - Calculate cumulative cases and deaths for each borough.
   - Determine the death rate percentage.
   - Compare boroughs using a horizontal bar chart.

5. **Borough-wise COVID-19 Case Distribution**
   - Calculate total confirmed cases for each NYC borough.
   - Analyze the proportion of cases contributed by each borough.
   - Represent the distribution using a pie chart.

## 🛠️ Technologies & Libraries Used

- **Python** – Programming language
- **Pandas** – Data cleaning, manipulation, and analysis
- **Matplotlib** – Data visualization
- **Seaborn** – Statistical data visualization
- **Excel (XLSX)** – Dataset storage and input

## 📂 Project Structure

```text
COVID-19-Data-Analysis/
│
├── Analysis1.py
├── Analysis2.py
├── Analysis3.py
├── Analysis4.py
├── Analysis5.py
│
├── covid19dataset_cleaned.xlsx
│
└── README.md
```

## 📊 Dataset Information

The project uses a cleaned COVID-19 dataset containing daily records and borough-wise information.

- **Total Records:** 1,837
- **Total Columns:** 20
- **Location:** New York City, USA
- **Data Includes:**
  - Date of interest
  - Confirmed COVID-19 cases
  - Hospitalizations
  - Death counts
  - Borough-wise cases, hospitalizations, and deaths
  - Data completeness indicator

### NYC Boroughs Covered

- Bronx
- Brooklyn
- Manhattan
- Queens
- Staten Island

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 2. Navigate to the Project Directory

```bash
cd COVID-19-Data-Analysis
```

### 3. Install Required Libraries

```bash
pip install pandas matplotlib seaborn openpyxl
```

### 4. Run the Python Files

Execute each analysis separately:

```bash
python Analysis1.py
python Analysis2.py
python Analysis3.py
python Analysis4.py
python Analysis5.py
```

**Note:** Keep the Excel dataset in the same directory as the Python scripts.

## 📈 Visualizations

The project generates several visualizations to understand COVID-19 trends and patterns:

- Line Chart – Confirmed COVID-19 cases over time.
- Correlation Heatmap – Relationships between numerical variables.
- Scatter Plot with Regression Line – Relationship between cases and deaths.
- Line Chart – Death-to-case ratio over time.
- Area Chart – Monthly COVID-19 hospitalizations.
- Horizontal Bar Chart – Death rate comparison across boroughs.
- Pie Chart – Proportion of confirmed cases by borough.

## 💡 Key Learning Outcomes

- Practical experience with Python-based data analysis.
- Understanding data cleaning and preprocessing.
- Working with real-world healthcare datasets.
- Performing statistical analysis using Pandas.
- Creating meaningful visualizations using Matplotlib and Seaborn.
- Identifying trends and comparing geographical data.
- Understanding the relationship between COVID-19 cases, hospitalizations, and deaths.

## 🔮 Future Improvements

- Develop an interactive dashboard using Streamlit or Power BI.
- Add predictive analysis using Machine Learning.
- Include more geographical and demographic comparisons.
- Implement interactive charts and filters.
- Generate automated reports from the analysis.

## 👨‍💻 Author

**Lakshya Nunia**

B.Tech Computer Science and Engineering  
Software Development and Data Science

- GitHub: https://github.com/kitsunee0104
- Portfolio: https://lakshya-nunia.vercel.app

---

⭐ If you find this project useful, consider giving the repository a star!
