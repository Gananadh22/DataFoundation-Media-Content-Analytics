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
    page_title="YouTube Analytics",
    layout="wide"
)

st.title("🎥 YouTube Analytics")
st.caption("Content performance and audience engagement overview")

# ---------- Load Data ----------
df = pd.read_csv("data/processed/youtube_metrics.csv")

if df.empty:
    st.warning("No YouTube data available.")
    st.stop()

# ---------- Feature Engineering ----------
df["engagement_rate"] = (
    (df["like_count"] + df["comment_count"]) / df["view_count"]
)

# ---------- KPI Section ----------
st.markdown("### 📊 Key Performance Indicators")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

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

with kpi1:
    st.markdown(
        kpi_card("Total Videos", len(df)),
        unsafe_allow_html=True
    )

with kpi2:
    st.markdown(
        kpi_card("Total Views", format_km(df["view_count"].sum())),
        unsafe_allow_html=True
    )

with kpi3:
    st.markdown(
        kpi_card(
            "Avg Engagement Rate",
            f"{df['engagement_rate'].mean()*100:.2f}%"
        ),
        unsafe_allow_html=True
    )

with kpi4:
    st.markdown(
        kpi_card(
            "Top Video Views",
            format_km(df["view_count"].max())
        ),
        unsafe_allow_html=True
    )

# ---------- Top Performing Videos ----------
st.markdown("### 🏆 Top Performing Videos")

top_videos = (
    df.sort_values("view_count", ascending=False)
      .head(10)
      .reset_index(drop=True)
)

top_videos["S.No"] = top_videos.index + 1
top_videos["engagement_rate"] = (
    top_videos["engagement_rate"] * 100
).round(2)

st.dataframe(
    top_videos[
        ["S.No", "title", "view_count", "like_count", "comment_count", "engagement_rate"]
    ],
    use_container_width=True,
    hide_index=True
)

# ---------- Views Comparison ----------
st.markdown("### 📊 Views Comparison (Top 10 Videos)")

top_videos["short_title"] = top_videos["title"].str.slice(0, 40) + "..."

fig_views = px.bar(
    top_videos.sort_values("view_count", ascending=True),
    x="view_count",
    y="short_title",
    orientation="h",
    text="view_count",
    color="view_count",
    color_continuous_scale="Blues",
)

fig_views.update_traces(
    texttemplate="%{text:,}",
    textposition="inside"
)

fig_views.update_layout(
    height=500,
    xaxis_title="Total Views",
    yaxis_title="",
    showlegend=False
)

st.plotly_chart(fig_views, use_container_width=True)

# ---------- Engagement Analysis ----------
st.markdown("### ❤️ Engagement Analysis")
st.caption("Relationship between views, likes, and comments")

fig_engagement = px.scatter(
    df,
    x="view_count",
    y="like_count",
    size="comment_count",
    hover_name="title",
    labels={
        "view_count": "Views",
        "like_count": "Likes",
        "comment_count": "Comments"
    },
    title="Likes vs Views (Bubble size represents comments)",
    color="engagement_rate",
    color_continuous_scale="Viridis"
)

fig_engagement.update_layout(
    height=500,
    xaxis_title="Total Views",
    yaxis_title="Total Likes",
    showlegend=False
)

st.plotly_chart(fig_engagement, use_container_width=True)

# ---------- Engagement Rate Ranking ----------
st.markdown("### 📈 Engagement Rate by Video")

engagement_rank = (
    df.sort_values("engagement_rate", ascending=False)
      .head(10)
      .reset_index(drop=True)
)

engagement_rank["short_title"] = engagement_rank["title"].str.slice(0, 40) + "..."
engagement_rank["engagement_rate_pct"] = (
    engagement_rank["engagement_rate"] * 100
).round(2)

fig_rate = px.bar(
    engagement_rank.sort_values("engagement_rate_pct", ascending=True),
    x="engagement_rate_pct",
    y="short_title",
    orientation="h",
    text="engagement_rate_pct",
    labels={"engagement_rate_pct": "Engagement Rate (%)"},
    color="engagement_rate_pct",
    color_continuous_scale="Teal"
)

fig_rate.update_traces(
    texttemplate="%{text}%",
    textposition="inside"
)

fig_rate.update_layout(
    height=500,
    xaxis_title="Engagement Rate (%)",
    yaxis_title="",
    showlegend=False
)

st.plotly_chart(fig_rate, use_container_width=True)