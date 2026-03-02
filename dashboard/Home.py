import streamlit as st

# Page config (important)
st.set_page_config(
    page_title="Media Content Analytics",
    layout="wide"
)

# Centered layout using columns (NO HTML)
left, center, right = st.columns([1, 3, 1])

with center:
    st.markdown(
        """
        <h1 style="text-align:center; color:#EAEAEA; font-weight:700;">
            Media Content Analytics
        </h1>
        <h3 style="text-align:center; color:#9BB3C3; font-weight:400;">
            A unified analytics platform for evaluating digital media performance and audience engagement
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <p style="font-size:18px; line-height:1.7; color:#D6D6D6; text-align:justify;">
        Digital media platforms generate massive volumes of content and engagement data every day.
        Without structured analysis, it becomes difficult to understand what drives audience behavior,
        identify meaningful trends, and measure real performance.
        </p>

        <p style="font-size:18px; line-height:1.7; color:#D6D6D6; text-align:justify;">
        This platform is designed to consolidate analytics from multiple media sources into a single,
        structured environment. The focus is on clean data pipelines, reliable metrics, and professional
        presentation that supports data-driven decision making.
        </p>

        <p style="font-size:18px; line-height:1.7; color:#D6D6D6; text-align:justify;">
        YouTube analytics are powered by structured data collected from the YouTube Data API, including
        video-level metrics such as views, likes, comments, publishing timelines, and engagement trends.
        News analytics leverage categorized datasets to enable large-scale, topic-based media analysis.
        </p>

        <p style="font-size:18px; line-height:1.7; color:#D6D6D6; text-align:justify;">
        Together, these datasets form a clean analytical foundation designed for clarity, accuracy,
        and professional insight generation.
        </p>
        """,
        unsafe_allow_html=True
    )