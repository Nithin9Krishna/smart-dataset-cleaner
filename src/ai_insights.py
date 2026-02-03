def generate_insights(df, num_cols, cat_cols, missing_df, outliers):
    insights = []

    if missing_df["missing_count"].sum() == 0:
        insights.append(
            "The dataset shows strong data quality with no missing values, "
            "indicating reliable upstream data collection."
        )

    if len(num_cols) <= 1:
        insights.append(
            "The dataset is predominantly categorical, which makes it more suitable "
            "for customer analytics, segmentation, or rule-based systems than "
            "numerical predictive modeling."
        )

    if any(outliers.values()):
        insights.append(
            "Outliers were detected in numerical columns and should be reviewed "
            "before downstream analysis."
        )
    else:
        insights.append(
            "No significant outliers were detected in the numerical features."
        )

    insights.append(
        "Fields such as email, phone number, and dates should be validated "
        "and standardized before use in analytics or ML pipelines."
    )

    return insights
