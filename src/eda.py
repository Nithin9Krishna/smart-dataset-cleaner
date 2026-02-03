import pandas as pd

def column_types(df):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
    return numeric_cols, categorical_cols


def missing_values(df):
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100

    return pd.DataFrame({
        "missing_count": missing,
        "missing_percent": missing_percent
    })


def detect_outliers_iqr(df, numeric_cols):
    outlier_summary = {}

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        outlier_summary[col] = len(outliers)

    return outlier_summary
