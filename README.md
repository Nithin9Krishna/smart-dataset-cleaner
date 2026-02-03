# AI-Assisted Data Quality & Exploratory Data Analysis (EDA) Engine

An interactive, AI-assisted data analysis application that helps users quickly understand the **quality, structure, and readiness of datasets** before analytics or machine learning.  
The system combines **statistical analysis**, **intelligent rule-based reasoning**, and **interactive visualizations** through a clean Streamlit interface.

---

## 📌 Problem Statement

In real-world data projects, a significant amount of time is spent on:
- Understanding dataset structure
- Identifying missing values and anomalies
- Deciding appropriate preprocessing steps
- Communicating dataset readiness to stakeholders

Most traditional EDA tools either:
- Generate overwhelming reports, or
- Provide raw statistics without actionable insights

This project addresses that gap by offering a **guided, explainable, and user-controlled EDA workflow**.

---

## 🎯 Project Objective

The goal of this project is to build a **lightweight yet powerful EDA engine** that:
- Works for **any CSV dataset**
- Scales to **large datasets**
- Avoids black-box AI behavior
- Produces **clear, human-readable insights**

Rather than replacing analysts, this tool **assists decision-making** by summarizing data quality and readiness.

---

## 🧠 What This Application Does

Once a dataset is uploaded, the application performs the following:

### 1️⃣ Dataset Overview
- Number of rows and columns
- Column names
- Data types (numerical vs categorical)

### 2️⃣ Missing Value Analysis
- Detects missing values per column
- Computes missing percentages
- Provides a clean tabular summary

### 3️⃣ Outlier Detection
- Applies IQR-based statistical outlier detection
- Works automatically on numerical features
- Skips gracefully when no numeric data is present

### 4️⃣ Intelligent Cleaning Suggestions
- Recommends actions such as:
  - No action required
  - Imputation
  - Column review or removal
- Based on data quality metrics, not assumptions

### 5️⃣ AI-Assisted Analytical Insights
Instead of unconstrained language generation, the system produces **deterministic, explainable insights**, such as:
- Overall data quality assessment
- Suitability for analytics vs ML
- Warnings for validation-sensitive fields (emails, phone numbers, dates)

This design avoids hallucination while still providing **AI-style reasoning**.

### 6️⃣ Universal Visual Explorations
The application includes a small set of **dataset-agnostic visualizations**:
- Missing values heatmap
- Numerical feature distributions
- Categorical value dominance
- Correlation heatmap (when applicable)

These visuals work reliably across most datasets without requiring domain assumptions.

---

## 🖥️ User Interface Highlights

- Streamlit-based interactive UI
- Sidebar controls to selectively run analyses
- Optional visualizations (user-controlled)
- Clear separation between statistics, insights, and visuals

This makes the tool suitable for:
- Data scientists
- Analysts
- Students
- Quick stakeholder demos

---

## 🛠️ Technology Stack

- **Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  
- **UI Framework:** Streamlit  

No external APIs or cloud dependencies are required.

---

## 🚀 How to Run the Application

```bash
pip install -r requirements.txt
streamlit run app.py
