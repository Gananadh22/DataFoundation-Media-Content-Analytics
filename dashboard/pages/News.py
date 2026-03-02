import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- Helper ----------
def format_km(value):
    if value >= 1_000_000:
        return f"{value/1_000_000:.1f}M"
    elif value >= 1_000:
        return f"{value/1_000:.1f}K"
    else:
        return str(value)

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
st.markdown("### 📊 Key Performance Indicators")

kpi1, kpi2, kpi3 = st.columns(3)

def kpi_card(title, value):
    return f"""
    <div style="
        padding:16px;
        border-radius:10px;
        background-color:#111827;
        text-align:center;
    ">
        <div style="
            font-size:14px;
            color:#9CA3AF;
            margin-bottom:6px;
        ">
            {title}
        </div>
        <div style="
            font-size:32px;
            font-weight:600;
            color:white;
        ">
            {value}
        </div>
    </div>
    """

total_articles = len(news_df)
total_categories = news_df["category"].nunique()
top_category = news_df["category"].value_counts().idxmax()

with kpi1:
    st.markdown(
        kpi_card("Total Articles", format_km(total_articles)),
        unsafe_allow_html=True
    )

with kpi2:
    st.markdown(
        kpi_card("Total Categories", total_categories),
        unsafe_allow_html=True
    )

with kpi3:
    st.markdown(
        kpi_card("Top Category", top_category),
        unsafe_allow_html=True
    )

st.markdown("---")

# ---------- Category Composition (ALL 42 CATEGORIES PIE) ----------
st.markdown("### 🥧 Category Composition (All Categories)")

category_counts = (
    news_df["category"]
    .value_counts()
    .reset_index()
)

category_counts.columns = ["category", "article_count"]

fig_pie = px.pie(
    category_counts,
    names="category",
    values="article_count",
    color_discrete_sequence=px.colors.qualitative.Alphabet
)

fig_pie.update_traces(
    textinfo="percent",
    hovertemplate="<b>%{label}</b><br>Articles: %{value}<br>Share: %{percent}",
    marker=dict(line=dict(color="#F0F2F7", width=1))
)

fig_pie.update_layout(
    height=520,
    showlegend=True,
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(size=13)
)

st.plotly_chart(fig_pie, use_container_width=True)

# ---------- Category Distribution (Top 10) ----------
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
    yaxis=dict(autorange="reversed")
)

st.plotly_chart(fig_bar, use_container_width=True)

# ---------- Publishing Trends Over Time ----------
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
    xaxis=dict(title="Year", tickmode="linear"),
    yaxis=dict(title="Number of Articles"),
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