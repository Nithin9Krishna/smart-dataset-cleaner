import streamlit as st
import pandas as pd

from src.load_data import load_csv, basic_info
from src.eda import column_types, missing_values, detect_outliers_iqr
from src.cleaning_suggestions import suggest_cleaning
from src.ai_insights import generate_insights
from src.visualization import (
    plot_missing_heatmap,
    plot_numeric_distribution,
    plot_categorical_top,
    plot_correlation
)

st.set_page_config(
    page_title="AI-Assisted Dataset Analyzer",
    layout="wide"
)

st.title("📊 AI-Assisted Data Quality & EDA Engine")

st.write(
    "Upload a dataset and selectively run data quality checks "
    "with AI-assisted analytical insights."
)

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset loaded successfully!")

    # =========================
    # BASIC INFO
    # =========================
    with st.expander("📌 Dataset Overview", expanded=True):
        info = basic_info(df)
        st.json(info)

    # =========================
    # USER CONTROLS
    # =========================
    st.sidebar.header("🔧 Analysis Controls")

    run_missing = st.sidebar.checkbox("Check Missing Values", True)
    run_outliers = st.sidebar.checkbox("Detect Outliers", True)
    run_cleaning = st.sidebar.checkbox("Cleaning Suggestions", True)
    run_ai = st.sidebar.checkbox("AI Insights", True)
    run_viz = st.sidebar.checkbox("Show Visualizations", True)

    num_cols, cat_cols = column_types(df)

    # =========================
    # MISSING VALUES
    # =========================
    if run_missing:
        st.subheader("🔍 Missing Values Analysis")
        missing_df = missing_values(df)
        st.dataframe(missing_df)
    else:
        missing_df = pd.DataFrame()

    # =========================
    # OUTLIERS
    # =========================
    if run_outliers:
        st.subheader("📉 Outlier Detection")
        outliers = detect_outliers_iqr(df, num_cols)
        st.json(outliers)
    else:
        outliers = {}

    # =========================
    # CLEANING SUGGESTIONS
    # =========================
    if run_cleaning and not missing_df.empty:
        st.subheader("🧹 Cleaning Suggestions")
        suggestions = suggest_cleaning(missing_df)
        st.json(suggestions)
    else:
        suggestions = {}

    # =========================
    # AI INSIGHTS
    # =========================
    if run_ai:
        st.subheader("🤖 AI-Assisted Insights")

        ai_insights = generate_insights(
            df=df,
            num_cols=num_cols,
            cat_cols=cat_cols,
            missing_df=missing_df,
            outliers=outliers
        )

        for i, insight in enumerate(ai_insights, 1):
            st.markdown(f"**{i}.** {insight}")

    # =========================
    # VISUALIZATIONS
    # =========================
    if run_viz:
        st.subheader("📊 Visual Explorations")

        # Missing values heatmap
        st.markdown("### Missing Values Overview")
        fig = plot_missing_heatmap(df)
        st.pyplot(fig)

        # Numeric distribution
        if num_cols:
            st.markdown("### Numeric Distribution")
            selected_num = st.selectbox(
                "Select numeric column",
                num_cols
            )
            fig = plot_numeric_distribution(df, selected_num)
            st.pyplot(fig)

        # Categorical distribution
        if cat_cols:
            st.markdown("### Categorical Distribution")
            selected_cat = st.selectbox(
                "Select categorical column",
                cat_cols
            )
            fig = plot_categorical_top(df, selected_cat)
            st.pyplot(fig)

        # Correlation heatmap
        corr_fig = plot_correlation(df)
        if corr_fig:
            st.markdown("### Feature Correlation")
            st.pyplot(corr_fig)
