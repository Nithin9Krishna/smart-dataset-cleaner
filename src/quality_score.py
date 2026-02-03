def compute_quality_score(df, missing_df, num_cols):
    score = 100

    if missing_df["missing_percent"].sum() > 0:
        score -= 20

    if len(num_cols) < 2:
        score -= 10

    return max(score, 0)
