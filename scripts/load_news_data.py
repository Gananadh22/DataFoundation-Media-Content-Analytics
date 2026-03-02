import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- Page Setup ----------
st.set_page_config(
    page_title="News Analytics",
    layout="wide"
)

st.title("📰 News Analytics")
st.caption("Content distribution and publishing trends")

# ---------- Load Data ----------
news_df = pd.read_csv("data/processed/news_clean.csv")

if news_df.empty:
    st.warning("No news data available.")
    st.stop()

# ---------- Basic Prep ----------
news_df["date"] = pd.to_datetime(news_df["date"], errors="coerce")

# ---------- KPI Section ----------
st.markdown("### 📊 Key Metrics")

col1, col2, col3 = st.columns(3)

total_articles = len(news_df)

with col1:
    st.metric("Total Articles", f"{total_articles/1000:.1f}K")

with col2:
    st.metric("Total Categories", news_df["category"].nunique())

with col3:
    top_category = news_df["category"].value_counts().idxmax()
    st.metric("Top Category", top_category)

st.markdown("---")

# ---------- Category Composition (Pie Chart) ----------
st.markdown("### 🥧 Category Composition (Top 5)")

category_counts = (
    news_df["category"]
    .value_counts()
    .reset_index()
)

category_counts.columns = ["category", "article_count"]

top_5 = category_counts.head(5)
others_count = category_counts["article_count"][5:].sum()

if others_count > 0:
    top_5 = pd.concat(
        [
            top_5,
            pd.DataFrame(
                [{"category": "Other", "article_count": others_count}]
            )
        ],
        ignore_index=True
    )

fig_pie = px.pie(
    top_5,
    names="category",
    values="article_count",
    hole=0.45,
)

fig_pie.update_traces(
    textinfo="percent+label"
)

fig_pie.update_layout(
    height=450,
    showlegend=True
)

st.plotly_chart(fig_pie, use_container_width=True)

# ---------- Category Distribution (Bar Chart) ----------
st.markdown("### 📊 Category Distribution (Top 10)")

top_10_categories = (
    category_counts
    .sort_values("article_count", ascending=False)
    .head(10)
)

fig_bar = px.bar(
    top_10_categories,
    x="article_count",
    y="category",
    orientation="h",
    text="article_count",
    color="article_count",
    color_continuous_scale="Blues",
)

fig_bar.update_traces(
    texttemplate="%{text:,}",
    textposition="inside"
)

fig_bar.update_layout(
    height=500,
    xaxis_title="Number of Articles",
    yaxis_title="",
    showlegend=False,
    yaxis=dict(autorange="reversed")  # 🔑 THIS LINE FIXES IT
)

st.plotly_chart(fig_bar, use_container_width=True)

# ---------- Publishing Trends Over Time (Bar Chart) ----------
st.markdown("### 📊 Publishing Trends Over Time")

news_df["year"] = news_df["date"].dt.year

yearly_counts = (
    news_df.groupby("year")
    .size()
    .reset_index(name="article_count")
    .dropna()
    .sort_values("year")
)

fig_trend = px.bar(
    yearly_counts,
    x="year",
    y="article_count",
    text="article_count",
    labels={
        "year": "Year",
        "article_count": "Number of Articles"
    },
    title="Articles Published Per Year",
    color="article_count",
    color_continuous_scale="Blues"
)

fig_trend.update_traces(
    texttemplate="%{text:,}",
    textposition="outside"
)

fig_trend.update_layout(
    height=500,
    xaxis=dict(
        title="Year",
        tickmode="linear"
    ),
    yaxis=dict(
        title="Number of Articles"
    ),
    showlegend=False
)

st.plotly_chart(fig_trend, use_container_width=True)

# ---------- Category Trends Over Time ----------
st.markdown("### 📊 Category Trends Over Time (Top 5 Categories)")

top_categories = (
    news_df["category"]
    .value_counts()
    .head(5)
    .index
)

category_trend_df = news_df[
    news_df["category"].isin(top_categories)
]

category_yearly = (
    category_trend_df
    .groupby(["year", "category"])
    .size()
    .reset_index(name="article_count")
)

fig_category_trend = px.line(
    category_yearly,
    x="year",
    y="article_count",
    color="category",
    markers=True,
    labels={
        "year": "Year",
        "article_count": "Number of Articles",
        "category": "Category"
    },
    title="Publishing Trends by Category"
)

fig_category_trend.update_layout(
    height=500,
    xaxis_title="Year",
    yaxis_title="Number of Articles",
)

st.plotly_chart(fig_category_trend, use_container_width=True)