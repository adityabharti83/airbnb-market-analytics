# Airbnb Market Analytics Project

This project analyzes Airbnb listing and review data to generate business insights on pricing, demand trends, and property performance.

The pipeline processes raw datasets, structures them into relational tables, loads them into SQL Server, and visualizes insights using Power BI dashboards.

---

## Project Workflow

1. Raw data ingestion
2. Data cleaning and transformation using Python
3. Database loading (SQL Server)
4. Analysis using SQL
5. Interactive dashboards in Power BI

---

## Project Structure

data_clean/
Cleaned and structured datasets used for analysis

notebooks/
Data processing and table normalization

PowerBI/
Interactive dashboards for analysis and reporting

SQL_Upload.py
ETL script for loading data into SQL Server

SQLQuery1.sql
Analytical SQL queries

screenshots/
Dashboard preview images

---

## Data Pipeline

Raw Data:
- Listings.csv (279k+ rows)
- Reviews.csv (5M+ rows)

Processed Data:
- listings_table.csv
- reviews_score.csv
- amenities_table.csv
- listing_amenities.csv
- Listing_Reviews.csv

---

## Data Model

The project converts flat files into a relational structure:

- Listings
- Hosts
- Review Scores
- Amenities
- Reviews

This structure enables efficient analytics and reporting.

---

## Tools & Technologies

Python (Pandas, SQLAlchemy)  
SQL Server  
Power BI  
Jupyter Notebook  

---

## Dashboard Insights

The dashboards provide:

- Market overview and listing distribution
- Pricing and rating analysis
- Demand and peak month trends
- Host performance insights
- Location-level comparisons

---

## Screenshots

(Add dashboard images here)

---

## Key Learning Outcomes

- Data cleaning and normalization
- ETL pipeline development
- SQL-based analytics
- Dashboard design and storytelling
- Handling large real-world datasets
