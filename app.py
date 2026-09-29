import streamlit as st
st.markdown("""
<style>
footer {
    visibility: hidden;
    display: none;
}

.stAppDeployButton {
    display: none;
}
</style>
""", unsafe_allow_html=True)
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Social Media Data Analysis",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #123b70 0%,
            #0d315e 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Sidebar title */
    .sidebar-title {
        text-align: center;
        font-size: 25px;
        font-weight: bold;
        padding: 10px 5px 25px 5px;
    }

    .sidebar-subtitle {
        text-align: center;
        font-size: 14px;
        margin-top: -20px;
        margin-bottom: 25px;
        opacity: 0.9;
    }

    /* KPI cards */
    .kpi-card {
        padding: 18px;
        border-radius: 12px;
        background: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        min-height: 115px;
    }

    .kpi-title {
        font-size: 15px;
        color: #555;
        margin-bottom: 8px;
    }

    .kpi-value {
        font-size: 28px;
        font-weight: bold;
        color: #123b70;
    }

    /* Section cards */
    .section-card {
        background: white;
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        margin-bottom: 15px;
    }

    /* Page title */
    .page-title {
        color: #123b70;
        font-size: 34px;
        font-weight: bold;
        margin-bottom: 0px;
    }

    .page-subtitle {
        color: #555;
        font-size: 16px;
        margin-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# DATASET FILE
# =========================================================

FILE_NAME = "DAE Social_Media_Data_Analysis_Dataset_1000.xlsx"


# =========================================================
# LOAD DATASET
# =========================================================

try:

    df = pd.read_excel(FILE_NAME)

except Exception as e:

    st.error("Unable to load the Excel file.")

    st.write(
        "Make sure the following file is in the same folder as app.py:"
    )

    st.code(FILE_NAME)

    st.write("Error:", e)

    st.stop()


# =========================================================
# BASIC CALCULATIONS
# =========================================================

total_posts = len(df)

total_columns = len(df.columns)

total_likes = df["Likes"].sum()

total_comments = df["Comments"].sum()

total_shares = df["Shares"].sum()

total_views = df["Views"].sum()

average_likes = df["Likes"].mean()

average_comments = df["Comments"].mean()

average_shares = df["Shares"].mean()

average_views = df["Views"].mean()

duplicate_rows = df.duplicated().sum()

missing_total = df.isnull().sum().sum()

category_counts = df["Category"].value_counts()

sentiment_counts = df["Sentiment"].value_counts()


# =========================================================
# HASHTAG CALCULATION
# =========================================================

hashtags = []

for value in df["Hashtag"].dropna():

    tags = re.findall(
        r"#\w+",
        str(value).lower()
    )

    hashtags.extend(tags)


hashtag_counts = Counter(hashtags)

top_hashtags = pd.DataFrame(
    hashtag_counts.most_common(10),
    columns=["Hashtag", "Frequency"]
)


# =========================================================
# WORD FREQUENCY
# =========================================================

text = " ".join(
    df["Comment"]
    .dropna()
    .astype(str)
).lower()


words = re.findall(
    r"\b[a-zA-Z]{3,}\b",
    text
)


stop_words = {
    "the",
    "and",
    "for",
    "that",
    "this",
    "with",
    "are",
    "was",
    "from",
    "have",
    "has",
    "you",
    "your",
    "about",
    "they",
    "our",
    "but",
    "not"
}


words = [
    word
    for word in words
    if word not in stop_words
]


word_counts = Counter(words)


top_words = pd.DataFrame(
    word_counts.most_common(10),
    columns=["Word", "Frequency"]
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-title">
            📊 Social Media<br>
            Data Analysis
        </div>

        <div class="sidebar-subtitle">
            DAE Project
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    navigation = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📤 Load Data",
            "📋 Data Preview",
            "🧹 Data Cleaning",
            "📊 Analysis",
            "📈 Visualization",
            "📄 Report"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown(
        """
        **DAE Project**

        Python • Pandas • NumPy  
        Matplotlib • Streamlit
        """
    )


# =========================================================
# DASHBOARD
# =========================================================

if navigation == "🏠 Dashboard":

    st.markdown(
        '<div class="page-title">Social Media Data Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Analyze social media data, engagement, hashtags and sentiment'
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # KPI CARDS
    # -----------------------------------------------------

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">👥 Total Posts</div>
                <div class="kpi-value">{total_posts:,}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">❤️ Total Likes</div>
                <div class="kpi-value">{total_likes/1000000:.2f}M</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">💬 Comments</div>
                <div class="kpi-value">{total_comments/1000:.1f}K</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">🔄 Shares</div>
                <div class="kpi-value">{total_shares/1000:.1f}K</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    with col5:

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">👁️ Views</div>
                <div class="kpi-value">{total_views/1000000:.2f}M</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    st.write("")


    # -----------------------------------------------------
    # DATASET SUMMARY
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Total Records",
        f"{total_posts:,}"
    )

    col2.metric(
        "Columns",
        f"{total_columns}"
    )

    col3.metric(
        "Missing Values",
        f"{missing_total}"
    )

    col4.metric(
        "Duplicate Rows",
        f"{duplicate_rows}"
    )


    st.divider()


    # -----------------------------------------------------
    # CATEGORY + SENTIMENT
    # -----------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("📊 Posts by Category")

        fig, ax = plt.subplots(
            figsize=(7, 4)
        )

        category_counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel("Category")

        ax.set_ylabel("Number of Posts")

        ax.set_title(
            "Category Distribution"
        )

        plt.xticks(
            rotation=30
        )

        plt.tight_layout()

        st.pyplot(fig)


    with col2:

        st.subheader("😊 Sentiment Distribution")

        fig, ax = plt.subplots(
            figsize=(7, 4)
        )

        sentiment_counts.plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90,
            ax=ax
        )

        ax.set_ylabel("")

        ax.set_title(
            "Sentiment Distribution"
        )

        plt.tight_layout()

        st.pyplot(fig)


    st.divider()


    # -----------------------------------------------------
    # HASHTAGS + ENGAGEMENT
    # -----------------------------------------------------

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("🔥 Top 5 Hashtags")

        st.dataframe(
            top_hashtags.head(5),
            use_container_width=True,
            hide_index=True
        )


    with col2:

        st.subheader("📈 Overall Engagement")

        engagement = pd.Series({
            "Likes": total_likes,
            "Comments": total_comments,
            "Shares": total_shares
        })

        fig, ax = plt.subplots(
            figsize=(7, 4)
        )

        engagement.plot(
            kind="bar",
            ax=ax
        )

        ax.set_xlabel(
            "Engagement Type"
        )

        ax.set_ylabel(
            "Count"
        )

        ax.set_title(
            "Overall Engagement"
        )

        plt.xticks(rotation=0)

        plt.tight_layout()

        st.pyplot(fig)


    st.divider()


    # -----------------------------------------------------
    # KEY INSIGHTS
    # -----------------------------------------------------

    st.subheader("💡 Key Insights")


    most_common_category = category_counts.idxmax()

    most_common_category_count = category_counts.max()

    most_common_sentiment = sentiment_counts.idxmax()

    most_common_sentiment_count = sentiment_counts.max()

    most_common_hashtag = top_hashtags.iloc[0]["Hashtag"]


    col1, col2 = st.columns(2)


    with col1:

        st.info(
            f"📚 Most popular category: "
            f"**{most_common_category}** "
            f"with {most_common_category_count} posts."
        )

        st.info(
            f"😊 Most common sentiment: "
            f"**{most_common_sentiment}** "
            f"with {most_common_sentiment_count} posts."
        )


    with col2:

        st.info(
            f"🔥 Most frequently used hashtag: "
            f"**{most_common_hashtag}**"
        )

        st.info(
            f"👁️ Total views generated: "
            f"**{total_views:,.0f}**"
        )


# =========================================================
# LOAD DATA
# =========================================================

elif navigation == "📤 Load Data":

    st.markdown(
        '<div class="page-title">Load Data</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Load and verify the social media dataset'
        '</div>',
        unsafe_allow_html=True
    )


    st.subheader("📤 Dataset File")

    st.success(
        "Dataset loaded successfully!"
    )


    st.write("Current dataset:")

    st.code(FILE_NAME)


    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Records",
        f"{total_posts:,}"
    )

    col2.metric(
        "Columns",
        f"{total_columns}"
    )

    col3.metric(
        "File Status",
        "Loaded"
    )


    st.divider()


    st.subheader("📋 Dataset Information")

    st.write(
        "The dataset contains social media posts with "
        "information about categories, comments, hashtags, "
        "likes, shares, views, followers and sentiment."
    )


# =========================================================
# DATA PREVIEW
# =========================================================

elif navigation == "📋 Data Preview":

    st.markdown(
        '<div class="page-title">Data Preview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Explore the loaded social media dataset'
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # DATASET METRICS
    # -----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "Total Records",
        f"{total_posts:,}"
    )

    col2.metric(
        "Columns",
        f"{total_columns}"
    )

    col3.metric(
        "Missing Values",
        f"{missing_total}"
    )

    col4.metric(
        "Duplicate Rows",
        f"{duplicate_rows}"
    )


    st.subheader("📋 Dataset Preview")


    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )


    st.subheader("📌 Column Names")

    st.write(
        list(df.columns)
    )


# =========================================================
# DATA CLEANING
# =========================================================

elif navigation == "🧹 Data Cleaning":

    st.markdown(
        '<div class="page-title">Data Cleaning</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Check missing values, duplicates and data quality'
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # CLEANING STATUS
    # -----------------------------------------------------

    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Missing Values",
        f"{missing_total}"
    )

    col2.metric(
        "Duplicate Rows",
        f"{duplicate_rows}"
    )

    col3.metric(
        "Clean Records",
        f"{total_posts - duplicate_rows:,}"
    )


    st.divider()


    # -----------------------------------------------------
    # MISSING VALUES
    # -----------------------------------------------------

    st.subheader("⚠️ Missing Values by Column")


    missing_table = (
        df.isnull()
        .sum()
        .reset_index()
    )


    missing_table.columns = [
        "Column",
        "Missing Count"
    ]


    st.dataframe(
        missing_table,
        use_container_width=True,
        hide_index=True
    )


    # -----------------------------------------------------
    # DUPLICATES
    # -----------------------------------------------------

    st.subheader("🔍 Duplicate Records")

    if duplicate_rows == 0:

        st.success(
            "No duplicate records found."
        )

    else:

        st.warning(
            f"{duplicate_rows} duplicate records found."
        )


    # -----------------------------------------------------
    # DATA QUALITY
    # -----------------------------------------------------

    st.subheader("✅ Data Cleaning Status")


    if missing_total == 0 and duplicate_rows == 0:

        st.success(
            "Dataset is clean. No missing values "
            "or duplicate records were found."
        )

    else:

        st.warning(
            "Dataset contains missing values or duplicates "
            "that may require preprocessing."
        )


# =========================================================
# ANALYSIS
# =========================================================

elif navigation == "📊 Analysis":

    st.markdown(
        '<div class="page-title">Data Analysis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Analyze categories, sentiment, hashtags, words and engagement'
        '</div>',
        unsafe_allow_html=True
    )


    analysis_type = st.selectbox(
        "Select Analysis",
        [
            "Category Analysis",
            "Sentiment Analysis",
            "Hashtag Analysis",
            "Word Frequency Analysis",
            "Engagement Analysis"
        ]
    )


    # -----------------------------------------------------
    # CATEGORY
    # -----------------------------------------------------

    if analysis_type == "Category Analysis":

        st.subheader("📊 Category Analysis")


        category_table = (
            category_counts
            .reset_index()
        )


        category_table.columns = [
            "Category",
            "Number of Posts"
        ]


        st.dataframe(
            category_table,
            use_container_width=True,
            hide_index=True
        )


        fig, ax = plt.subplots()

        category_counts.plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            "Social Media Posts by Category"
        )

        ax.set_xlabel("Category")

        ax.set_ylabel(
            "Number of Posts"
        )

        plt.xticks(rotation=30)

        plt.tight_layout()

        st.pyplot(fig)


    # -----------------------------------------------------
    # SENTIMENT
    # -----------------------------------------------------

    elif analysis_type == "Sentiment Analysis":

        st.subheader("😊 Sentiment Analysis")


        sentiment_table = (
            sentiment_counts
            .reset_index()
        )


        sentiment_table.columns = [
            "Sentiment",
            "Number of Posts"
        ]


        st.dataframe(
            sentiment_table,
            use_container_width=True,
            hide_index=True
        )


        fig, ax = plt.subplots()

        sentiment_counts.plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90,
            ax=ax
        )

        ax.set_ylabel("")

        ax.set_title(
            "Sentiment Distribution"
        )

        plt.tight_layout()

        st.pyplot(fig)


    # -----------------------------------------------------
    # HASHTAGS
    # -----------------------------------------------------

    elif analysis_type == "Hashtag Analysis":

        st.subheader("🔥 Hashtag Analysis")


        st.dataframe(
            top_hashtags,
            use_container_width=True,
            hide_index=True
        )


        fig, ax = plt.subplots()

        top_hashtags.set_index(
            "Hashtag"
        )["Frequency"].plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            "Top 10 Hashtags"
        )

        ax.set_xlabel("Hashtag")

        ax.set_ylabel(
            "Frequency"
        )

        plt.xticks(rotation=45)

        plt.tight_layout()

        st.pyplot(fig)


    # -----------------------------------------------------
    # WORD FREQUENCY
    # -----------------------------------------------------

    elif analysis_type == "Word Frequency Analysis":

        st.subheader("📝 Word Frequency Analysis")


        st.dataframe(
            top_words,
            use_container_width=True,
            hide_index=True
        )


        fig, ax = plt.subplots()

        top_words.set_index(
            "Word"
        )["Frequency"].plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(
            "Top 10 Frequently Used Words"
        )

        ax.set_xlabel("Word")

        ax.set_ylabel(
            "Frequency"
        )

        plt.xticks(rotation=45)

        plt.tight_layout()

        st.pyplot(fig)


    # -----------------------------------------------------
    # ENGAGEMENT
    # -----------------------------------------------------

    elif analysis_type == "Engagement Analysis":

        st.subheader("📈 Engagement Analysis")


        col1, col2, col3, col4 = st.columns(4)


        col1.metric(
            "Total Likes",
            f"{total_likes:,.0f}"
        )

        col2.metric(
            "Total Comments",
            f"{total_comments:,.0f}"
        )

        col3.metric(
            "Total Shares",
            f"{total_shares:,.0f}"
        )

        col4.metric(
            "Total Views",
            f"{total_views:,.0f}"
        )


        st.subheader(
            "Average Engagement per Post"
        )


        col1, col2, col3, col4 = st.columns(4)


        col1.metric(
            "Average Likes",
            f"{average_likes:,.2f}"
        )

        col2.metric(
            "Average Comments",
            f"{average_comments:,.2f}"
        )

        col3.metric(
            "Average Shares",
            f"{average_shares:,.2f}"
        )

        col4.metric(
            "Average Views",
            f"{average_views:,.2f}"
        )


# =========================================================
# VISUALIZATION
# =========================================================

elif navigation == "📈 Visualization":

    st.markdown(
        '<div class="page-title">Visualization</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Visual representation of social media analysis results'
        '</div>',
        unsafe_allow_html=True
    )


    visualization_type = st.selectbox(
        "Select Visualization",
        [
            "Category Distribution",
            "Sentiment Distribution",
            "Top Hashtags",
            "Word Frequency",
            "Engagement Overview"
        ]
    )


    # -----------------------------------------------------
    # CATEGORY
    # -----------------------------------------------------

    if visualization_type == "Category Distribution":

        st.subheader(
            "📊 Category Distribution"
        )


        fig, ax = plt.subplots(
            figsize=(10, 5)
        )


        category_counts.plot(
            kind="bar",
            ax=ax
        )


        ax.set_title(
            "Social Media Posts by Category"
        )

        ax.set_xlabel(
            "Category"
        )

        ax.set_ylabel(
            "Number of Posts"
        )


        plt.xticks(
            rotation=30
        )

        plt.tight_layout()

        st.pyplot(fig)


    # -----------------------------------------------------
    # SENTIMENT
    # -----------------------------------------------------

    elif visualization_type == "Sentiment Distribution":

        st.subheader(
            "😊 Sentiment Distribution"
        )


        fig, ax = plt.subplots(
            figsize=(7, 7)
        )


        sentiment_counts.plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90,
            ax=ax
        )


        ax.set_ylabel("")

        ax.set_title(
            "Sentiment Distribution"
        )


        plt.tight_layout()

        st.pyplot(fig)


    # -----------------------------------------------------
    # HASHTAGS
    # -----------------------------------------------------

    elif visualization_type == "Top Hashtags":

        st.subheader(
            "🔥 Top 10 Hashtags"
        )


        fig, ax = plt.subplots(
            figsize=(10, 5)
        )


        top_hashtags.set_index(
            "Hashtag"
        )["Frequency"].plot(
            kind="bar",
            ax=ax
        )


        ax.set_title(
            "Top 10 Hashtags"
        )

        ax.set_xlabel(
            "Hashtag"
        )

        ax.set_ylabel(
            "Frequency"
        )


        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        st.pyplot(fig)


    # -----------------------------------------------------
    # WORD FREQUENCY
    # -----------------------------------------------------

    elif visualization_type == "Word Frequency":

        st.subheader(
            "📝 Word Frequency"
        )


        fig, ax = plt.subplots(
            figsize=(10, 5)
        )


        top_words.set_index(
            "Word"
        )["Frequency"].plot(
            kind="bar",
            ax=ax
        )


        ax.set_title(
            "Top 10 Frequently Used Words"
        )

        ax.set_xlabel(
            "Word"
        )

        ax.set_ylabel(
            "Frequency"
        )


        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        st.pyplot(fig)


    # -----------------------------------------------------
    # ENGAGEMENT
    # -----------------------------------------------------

    elif visualization_type == "Engagement Overview":

        st.subheader(
            "📈 Engagement Overview"
        )


        engagement = pd.Series({
            "Likes": total_likes,
            "Comments": total_comments,
            "Shares": total_shares
        })


        fig, ax = plt.subplots(
            figsize=(10, 5)
        )


        engagement.plot(
            kind="bar",
            ax=ax
        )


        ax.set_title(
            "Overall Social Media Engagement"
        )

        ax.set_xlabel(
            "Engagement Type"
        )

        ax.set_ylabel(
            "Count"
        )


        plt.xticks(
            rotation=0
        )

        plt.tight_layout()

        st.pyplot(fig)


# =========================================================
# REPORT
# =========================================================

elif navigation == "📄 Report":

    st.markdown(
        '<div class="page-title">Project Report</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        'Summary of the Social Media Data Analysis results'
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # REPORT SUMMARY
    # -----------------------------------------------------

    st.subheader("📋 Analysis Summary")


    st.write(
        f"""
        The Social Media Data Analysis System analyzed
        **{total_posts:,} social media records** containing
        **{total_columns} features**.

        The analysis includes category distribution,
        sentiment analysis, hashtag frequency,
        word frequency and engagement analysis.
        """
    )


    # -----------------------------------------------------
    # RESULTS
    # -----------------------------------------------------

    st.subheader("📊 Key Results")


    st.write(
        f"""
        • Total Posts: **{total_posts:,}**

        • Total Likes: **{total_likes:,.0f}**

        • Total Comments: **{total_comments:,.0f}**

        • Total Shares: **{total_shares:,.0f}**

        • Total Views: **{total_views:,.0f}**

        • Most Popular Category:
        **{category_counts.idxmax()}**

        • Most Common Sentiment:
        **{sentiment_counts.idxmax()}**

        • Most Frequent Hashtag:
        **{top_hashtags.iloc[0]["Hashtag"]}**
        """
    )


    # -----------------------------------------------------
    # REPORT TEXT
    # -----------------------------------------------------

    report_text = f"""
SOCIAL MEDIA DATA ANALYSIS SYSTEM
=================================

DATASET SUMMARY
----------------
Total Records: {total_posts}
Total Columns: {total_columns}
Missing Values: {missing_total}
Duplicate Rows: {duplicate_rows}

ENGAGEMENT
----------
Total Likes: {total_likes}
Total Comments: {total_comments}
Total Shares: {total_shares}
Total Views: {total_views}

CATEGORY ANALYSIS
-----------------
Most Popular Category: {category_counts.idxmax()}
Number of Posts: {category_counts.max()}

SENTIMENT ANALYSIS
------------------
Most Common Sentiment: {sentiment_counts.idxmax()}
Number of Posts: {sentiment_counts.max()}

TOP HASHTAG
-----------
{top_hashtags.iloc[0]["Hashtag"]}

CONCLUSION
----------
The system analyzes social media data using Python,
Pandas and visualization techniques. It identifies
patterns in categories, sentiment, hashtags,
word frequency and user engagement.
"""


    st.download_button(
        label="📥 Download Analysis Report",
        data=report_text,
        file_name="Social_Media_Analysis_Report.txt",
        mime="text/plain"
    )


    # -----------------------------------------------------
    # DOWNLOAD PROCESSED DATA
    # -----------------------------------------------------

    csv_data = df.to_csv(
        index=False
    )


    st.download_button(
        label="📥 Download Dataset",
        data=csv_data,
        file_name="Social_Media_Data.csv",
        mime="text/csv"
    )


# =========================================================
# FOOTER
# =========================================================

st.sidebar.markdown("---")

st.sidebar.caption(
    "Social Media Data Analysis System"
)

st.sidebar.caption(
    "DAE Project • Python • Pandas • Matplotlib • Streamlit"
)
