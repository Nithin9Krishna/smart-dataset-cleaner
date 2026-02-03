import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def plot_missing_heatmap(df):
    plt.figure(figsize=(10, 4))
    sns.heatmap(df.isnull(), cbar=False)
    plt.title("Missing Values Heatmap")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.tight_layout()
    return plt


def plot_numeric_distribution(df, column):
    plt.figure(figsize=(6, 4))
    sns.histplot(df[column].dropna(), kde=True)
    plt.title(f"Distribution of {column}")
    plt.tight_layout()
    return plt


def plot_categorical_top(df, column, top_n=10):
    value_counts = df[column].value_counts().head(top_n)

    plt.figure(figsize=(6, 4))
    sns.barplot(x=value_counts.values, y=value_counts.index)
    plt.title(f"Top {top_n} values in {column}")
    plt.tight_layout()
    return plt


def plot_correlation(df):
    numeric_df = df.select_dtypes(include=["int64", "float64"])
    if numeric_df.shape[1] < 2:
        return None

    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=False, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    return plt
