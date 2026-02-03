# AI-Assisted Data Quality & Exploratory Data Analysis (EDA) Engine

This project is an interactive data analysis tool built to help quickly understand the **quality and structure of a dataset** before using it for analytics or machine learning.  
It focuses on clarity, usability, and explainability rather than generating large automated reports.

The application is built using Python and Streamlit and is designed to work with **any CSV dataset**, including large files.

---

## Why I Built This

In most real-world data projects, the first challenge is not modeling — it is understanding the data.

Common questions usually include:
- Is the data clean?
- Are there missing values or anomalies?
- What type of features does the dataset contain?
- Is the data even suitable for machine learning?

Many EDA tools either overwhelm users with too many statistics or provide raw numbers without context.  
This project aims to solve that by providing **guided, readable insights** that help users make decisions faster.

---

## What the Application Does

After uploading a CSV file, the application performs a series of controlled analyses that work for most datasets.

### Dataset Overview
- Displays number of rows and columns
- Lists column names
- Identifies data types (numerical vs categorical)

This gives an immediate understanding of the dataset structure.

---

### Missing Value Analysis
- Detects missing values for each column
- Calculates missing percentages
- Presents results in a clean tabular format

This helps identify whether data cleaning or imputation is required.

---

### Outlier Detection
- Uses an IQR-based statistical method
- Automatically applies only to numerical columns
- Safely skips when numerical data is limited

This avoids forcing assumptions on unsuitable datasets.

---

### Cleaning Suggestions
Based on data quality signals, the system provides simple recommendations such as:
- No action needed
- Review or impute missing values
- Consider dropping low-quality columns

These suggestions are rule-based and explainable.

---

### AI-Assisted Insights
Instead of using free-form text generation, the application produces **deterministic analytical insights** derived from dataset characteristics.

Examples include:
- Overall data quality assessment
- Suitability for analytics vs machine learning
- Identification of fields that may need validation (emails, phone numbers, dates)

This approach avoids hallucination while still providing **AI-style reasoning**.

---

### Visual Explorations
The application includes a small set of visualizations that are useful across most datasets:
- Missing values heatmap
- Numerical feature distributions
- Categorical value dominance charts
- Correlation heatmap (when applicable)

These visuals help users quickly spot patterns without cluttering the interface.

---

## User Experience

- Built with Streamlit for simplicity and speed
- Sidebar controls allow users to select which analyses to run
- Visualizations are optional and user-controlled
- Works well for both small and large datasets

The interface is designed to be practical rather than flashy.

---

## Technology Stack

- **Python**
- **Pandas & NumPy** for data processing
- **Matplotlib & Seaborn** for visualization
- **Streamlit** for the interactive UI

No external APIs or cloud services are required.

---

## How to Run the Project

```bash
pip install -r requirements.txt
streamlit run app.py
```
## Application Workflow

The diagram below illustrates the complete workflow of the AI-Assisted EDA Engine, from dataset upload to insights and visualization.

![AI-Assisted EDA Workflow](workflow.png)

