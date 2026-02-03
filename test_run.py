from src.load_data import load_csv, basic_info
from src.eda import column_types, missing_values, detect_outliers_iqr
from src.cleaning_suggestions import suggest_cleaning
from src.ai_insights import generate_insights

# =========================
# LOAD DATA
# =========================
df = load_csv("data/sample.csv")

# =========================
# CORE ANALYSIS
# =========================
info = basic_info(df)
num_cols, cat_cols = column_types(df)
missing_df = missing_values(df)
outliers = detect_outliers_iqr(df, num_cols)
suggestions = suggest_cleaning(missing_df)

# =========================
# AI-ASSISTED INSIGHTS
# =========================
ai_insights = generate_insights(
    df=df,
    num_cols=num_cols,
    cat_cols=cat_cols,
    missing_df=missing_df,
    outliers=outliers
)

# =========================
# OUTPUT
# =========================
print("\n=== BASIC INFO ===")
print(info)

print("\n=== OUTLIERS ===")
print(outliers)

print("\n=== CLEANING SUGGESTIONS ===")
print(suggestions)

print("\n=== AI INSIGHTS ===")
for i, insight in enumerate(ai_insights, 1):
    print(f"{i}. {insight}")
