# src/cleaning_suggestions.py

def suggest_cleaning(missing_df):
    suggestions = {}

    for col, row in missing_df.iterrows():
        if row["missing_percent"] > 40:
            suggestions[col] = "Consider dropping this column (>40% missing)"
        elif row["missing_percent"] > 0:
            suggestions[col] = "Impute missing values (mean/median/mode)"
        else:
            suggestions[col] = "No action needed"

    return suggestions
