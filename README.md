📊 DataFoundation – Media Content Analytics Platform
📌 Project Overview

DataFoundation is a media content analytics platform designed to analyze and visualize YouTube content performance and News category trends.
The project demonstrates an end-to-end data lifecycle, from data ingestion and transformation to data warehousing and interactive visualization.

The system integrates multiple data sources, processes them using Python, stores them in a BigQuery analytical warehouse, and exposes insights via Streamlit dashboards.

🎯 Objectives

Analyze media content performance and audience engagement

Process heterogeneous data sources (API + dataset)

Apply data cleaning, transformation, and modeling

Design analytical schemas in BigQuery

Build interactive dashboards for business insights

🛠️ Tech Stack

Python – Data ingestion, cleaning, transformation

Pandas – Data processing

Google BigQuery – Data warehouse

SQL – Schema and analytical queries

Streamlit – Dashboard & visualization

Plotly – Interactive charts

REST API – YouTube Data API

CSV / JSON – Data formats

📂 Project Structure
media_content_analytics/
│
├── bigquery/
│   ├── dataset.sql
│   ├── dim_news_content.sql
│   └── fact_youtube_metrics.sql
│
├── credentials/
│   └── service_account.json
│
├── data/
│   ├── raw/
│   │   └── News_Category_Dataset_v3.json
│   │
│   └── processed/
│       ├── news_clean.csv
│       └── youtube_metrics.csv
│
├── dashboard/
│   ├── Home.py
│   └── pages/
│       ├── News.py
│       └── YouTube.py
│
├── scripts/
│   ├── load_news_data.py
│   └── youtube_fetch.py
│
├── venv/
│
├── requirements.txt
├── README.md
└── test.py
🔁 End-to-End Data Flow
1️⃣ Data Sources

YouTube Data API

Video metrics: views, likes, comments

Kaggle News Category Dataset

Article metadata and category labels

2️⃣ Data Ingestion

📁 scripts/

youtube_fetch.py

Fetches YouTube metrics using REST API

load_news_data.py

Loads raw news dataset

Raw data is stored without modification.

3️⃣ Raw Data Storage

📁 data/raw/

Stores original datasets

Preserves source integrity

Enables reprocessing if needed

4️⃣ Data Cleaning & Transformation

Using Python + Pandas:

Handle missing values

Normalize column names

Parse and standardize dates

Calculate derived metrics (e.g., engagement rate)

5️⃣ Processed Data Storage

📁 data/processed/

news_clean.csv

youtube_metrics.csv

These files represent analytics-ready datasets.

🏗️ Data Warehouse (BigQuery)
Dataset

Dataset Name: media_content_dw

Acts as the analytical warehouse layer

Schema Design

The project uses domain-driven modeling rather than forcing unrelated datasets into a single star schema.

Tables
🟦 fact_youtube_metrics

Stores measurable YouTube performance data

Metrics:

view_count

like_count

comment_count

engagement_rate

🟨 dim_news_content

Stores descriptive news content data

Attributes:

article title

category

publication date

📌 Note:
YouTube and News datasets are modeled separately because they represent different business domains, which is a valid and real-world data modeling approach.

SQL Files

📁 bigquery/

dataset.sql – Creates BigQuery dataset

fact_youtube_metrics.sql – Creates YouTube fact table

dim_news_content.sql – Creates News dimension table

(Data is assumed to be successfully loaded into these tables.)

📊 Analytics & Visualization Layer
Streamlit Dashboard

📁 dashboard/

Home.py

Overview of platform

pages/News.py

Category composition

Publishing trends

Category distribution

pages/YouTube.py

Video performance metrics

Engagement analysis

Trending videos

Visualizations Include

KPI cards

Bar charts

Line charts

Pie charts

Time-based trend analysis

🔐 Credentials & Configuration

📁 credentials/

service_account.json

Used for secure BigQuery access

Not exposed publicly

🔄 Data Lifecycle Coverage
Lifecycle Stage	Status
Data Generation	✅
Data Ingestion	✅
Raw Data Storage	✅
Data Cleaning	✅
Data Transformation	✅
Processed Data Storage	✅
Data Modeling	✅
Data Warehousing	✅
Data Analysis	✅
Data Visualization	✅
Automation & Scheduling	⚠ Partial
🚀 How to Run the Project
# Activate virtual environment
source venv/bin/activate   # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run dashboard/Home.py
🧠 Key Learnings

Working with real-world APIs and datasets

Data cleaning and transformation best practices

Domain-based data modeling

BigQuery analytical design

Building end-user analytics dashboards

✅ Project Status

Status: ✔ Completed
Scope: End-to-end analytics pipeline
Level: Industry-aligned analytics project