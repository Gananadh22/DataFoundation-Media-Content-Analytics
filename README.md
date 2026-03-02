DataFoundation – Media Content Analytics Platform
Project Overview

DataFoundation is an end-to-end media content analytics platform designed to analyze and visualize YouTube content performance and News category trends.

The project demonstrates the complete data lifecycle — from data ingestion and transformation to data warehousing and interactive visualization. Multiple data sources are integrated, processed using Python, stored in a BigQuery analytical warehouse, and exposed through Streamlit dashboards for insight generation.

Objectives

Analyze media content performance and audience engagement

Process heterogeneous data sources (REST API and static datasets)

Apply data cleaning, transformation, and modeling techniques

Design analytical schemas in BigQuery

Build interactive dashboards for business insights

Technology Stack

Python – Data ingestion, cleaning, transformation

Pandas – Data processing

Google BigQuery – Data warehouse

SQL – Schema definition and analytical queries

Streamlit – Dashboard and visualization

Plotly – Interactive charts

REST API – YouTube Data API

CSV / JSON – Data formats

Project Structure
media_content_analytics/
├── bigquery/
│   ├── dataset.sql
│   ├── dim_news_content.sql
│   └── fact_youtube_metrics.sql
├── credentials/
│   └── service_account.json
├── data/
│   ├── raw/
│   │   └── News_Category_Dataset_v3.json
│   └── processed/
│       ├── news_clean.csv
│       └── youtube_metrics.csv
├── dashboard/
│   ├── Home.py
│   └── pages/
│       ├── News.py
│       └── YouTube.py
├── scripts/
│   ├── load_news_data.py
│   └── youtube_fetch.py
├── requirements.txt
└── README.md
End-to-End Data Flow
1. Data Sources

YouTube Data API

Video metrics: views, likes, comments

Kaggle News Category Dataset

Article metadata and category labels

2. Data Ingestion

Scripts located in scripts/:

youtube_fetch.py
Fetches YouTube metrics using REST APIs

load_news_data.py
Loads raw news dataset

Raw data is ingested without modification.

3. Raw Data Storage

Directory: data/raw/

Stores original datasets

Preserves source integrity

Enables reprocessing when required

4. Data Cleaning and Transformation

Performed using Python and Pandas:

Handle missing values

Normalize column names

Parse and standardize dates

Calculate derived metrics (e.g., engagement rate)

5. Processed Data Storage

Directory: data/processed/

news_clean.csv

youtube_metrics.csv

These files represent analytics-ready datasets.

Data Warehouse (BigQuery)
Dataset

Dataset Name: media_content_dw

Serves as the analytical warehouse layer

Schema Design

The project follows domain-driven modeling rather than forcing unrelated datasets into a single star schema.

Tables

fact_youtube_metrics

Stores measurable YouTube performance data

Metrics:

view_count

like_count

comment_count

engagement_rate

dim_news_content

Stores descriptive news content data

Attributes:

Article title

Category

Publication date

Note:
YouTube and News datasets are modeled separately because they represent different business domains. This reflects real-world analytical design practices.

SQL Files

Located in bigquery/:

dataset.sql – Creates BigQuery dataset

fact_youtube_metrics.sql – Creates YouTube fact table

dim_news_content.sql – Creates News dimension table

(Data is assumed to be successfully loaded into these tables.)

Analytics and Visualization Layer
Streamlit Dashboard

Located in dashboard/:

Home.py

Platform overview

pages/News.py

Category composition

Publishing trends

Category distribution

pages/YouTube.py

Video performance metrics

Engagement analysis

Trending videos

Visualizations

KPI cards

Bar charts

Line charts

Pie charts

Time-based trend analysis

Credentials and Configuration

Directory: credentials/

service_account.json

Used for secure BigQuery access

Excluded from version control

Data Lifecycle Coverage
Lifecycle Stage	Status
Data Generation	Completed
Data Ingestion	Completed
Raw Data Storage	Completed
Data Cleaning	Completed
Data Transformation	Completed
Processed Data Storage	Completed
Data Modeling	Completed
Data Warehousing	Completed
Data Analysis	Completed
Data Visualization	Completed
Automation & Scheduling	Partial
How to Run the Project
# Activate virtual environment
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run dashboard/Home.py
Key Learnings

Working with real-world APIs and datasets

Data cleaning and transformation best practices

Domain-based data modeling

BigQuery analytical design

Building end-user analytics dashboards

Project Status

Status: Completed

Scope: End-to-end analytics pipeline

Level: Industry-aligned analytics project