# DataFoundation – Media Content Analytics Platform

## Project Overview

DataFoundation is an end-to-end media content analytics platform designed to analyze and visualize YouTube content performance alongside news category trends. The project demonstrates a complete data lifecycle, encompassing data ingestion, transformation, storage, modeling, and visualization.

Multiple heterogeneous data sources—including REST APIs and static datasets—are integrated, processed using Python, stored in a cloud-based analytical warehouse (BigQuery), and presented through interactive dashboards built with Streamlit. The platform enables data-driven insights into audience engagement and content trends.

---

## Objectives

The primary objectives of this project are to:

* Analyze media content performance and audience engagement patterns
* Integrate and process heterogeneous data sources (API and file-based)
* Apply robust data cleaning and transformation techniques
* Design scalable analytical schemas in a cloud data warehouse
* Develop interactive dashboards for business intelligence and decision-making

---

## Technology Stack

The platform is built using a modern data analytics stack:

* **Python** – Data ingestion, processing, and transformation
* **Pandas** – Data manipulation and cleaning
* **Google BigQuery** – Cloud-based analytical data warehouse
* **SQL** – Schema design and analytical querying
* **Streamlit** – Interactive dashboard development
* **Plotly** – Data visualization and charting
* **REST APIs** – YouTube Data API integration
* **Data Formats** – CSV and JSON

---

## Project Structure

```
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
```

---

## End-to-End Data Pipeline

### Data Sources

The platform integrates two primary data sources:

* **YouTube Data API**
  Provides video-level metrics such as views, likes, and comments

* **News Category Dataset (Kaggle)**
  Contains article metadata including category, title, and publication date

---

### Data Ingestion

Data ingestion is handled through Python scripts located in the `scripts/` directory:

* `youtube_fetch.py` retrieves YouTube metrics via REST API calls
* `load_news_data.py` loads raw news dataset files

All data is ingested in its original form to preserve source integrity.

---

### Raw Data Storage

Raw datasets are stored in:

```
data/raw/
```

This layer ensures:

* Preservation of original data
* Reproducibility of transformations
* Flexibility for reprocessing

---

### Data Cleaning and Transformation

Data preprocessing is performed using Python and Pandas, including:

* Handling missing and inconsistent values
* Standardizing column naming conventions
* Parsing and normalizing date formats
* Deriving calculated metrics such as engagement rate

---

### Processed Data Layer

Cleaned and transformed datasets are stored in:

```
data/processed/
```

Files include:

* `news_clean.csv`
* `youtube_metrics.csv`

These datasets are optimized for analytical consumption.

---

## Data Warehouse (BigQuery)

### Dataset

* **Dataset Name:** `media_content_dw`
* Serves as the centralized analytical storage layer

---

### Schema Design

The project adopts a domain-driven modeling approach, ensuring logical separation between distinct data domains rather than enforcing a single unified schema.

---

### Tables

#### fact_youtube_metrics

Stores quantitative performance metrics for YouTube content:

* view_count
* like_count
* comment_count
* engagement_rate

---

#### dim_news_content

Stores descriptive attributes for news content:

* article_title
* category
* publication_date

---

### Design Consideration

The YouTube and News datasets are modeled independently to reflect real-world analytical practices, where unrelated domains are not forced into a single schema. This improves scalability, maintainability, and clarity.

---

### SQL Definitions

SQL scripts are located in the `bigquery/` directory:

* `dataset.sql` – Dataset creation
* `fact_youtube_metrics.sql` – Fact table definition
* `dim_news_content.sql` – Dimension table definition

---

## Analytics and Visualization

### Streamlit Dashboard

The interactive dashboard is implemented using Streamlit and organized as follows:

* **Home.py**
  Provides an overview of the platform

* **pages/News.py**
  Displays news category distribution, publishing trends, and content analysis

* **pages/YouTube.py**
  Presents video performance metrics, engagement analysis, and trending insights

---

### Visualization Features

The dashboard includes:

* KPI indicators for key metrics
* Bar charts for category comparisons
* Line charts for trend analysis
* Pie charts for distribution insights
* Time-series analysis for performance tracking

---

## Security and Configuration

Sensitive credentials are managed securely:

* Located in `credentials/service_account.json`
* Excluded from version control using `.gitignore`

---

## Data Lifecycle Coverage

| Stage                   | Status    |
| ----------------------- | --------- |
| Data Generation         | Completed |
| Data Ingestion          | Completed |
| Raw Data Storage        | Completed |
| Data Cleaning           | Completed |
| Data Transformation     | Completed |
| Processed Data Storage  | Completed |
| Data Modeling           | Completed |
| Data Warehousing        | Completed |
| Data Analysis           | Completed |
| Data Visualization      | Completed |
| Automation & Scheduling | Partial   |

---

## Setup and Execution

### Prerequisites

Ensure Python and virtual environment tools are installed.

---

### Installation

```
# Activate virtual environment
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt
```

---

### Run the Application

```
streamlit run dashboard/Home.py
```

---

## Key Learnings

This project demonstrates:

* Integration of real-world APIs and external datasets
* Practical data cleaning and transformation workflows
* Domain-driven data modeling techniques
* Cloud-based data warehousing using BigQuery
* Development of interactive analytics dashboards

---

## Project Status

* **Status:** Completed
* **Scope:** End-to-end analytics pipeline
* **Level:** Industry-aligned data analytics project

---

## Future Enhancements

Potential improvements include:

* Workflow orchestration using Airflow or similar tools
* Automated scheduling for data ingestion pipelines
* Incremental data loading strategies
* Advanced analytics and machine learning integration
* Deployment using containerization (Docker)

---
