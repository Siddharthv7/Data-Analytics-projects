# Google BigQuery Integration Guide

Steps to upload the CSV and connect to Power BI:

1. Create a Google Cloud project and enable BigQuery API.
2. Create a dataset (e.g., analytics_ds).
3. Upload CSV via UI or CLI:
   - bq load --autodetect --source_format=CSV dataset.table gs://your-bucket/sales_data.csv
   OR using Python (google-cloud-bigquery library):
   See automation_template.py for a code snippet.

4. Create views / aggregated tables for performance (daily_revenue, product_summary).
5. Grant Power BI service account or user the BigQuery Data Viewer role for the dataset.
6. Connect Power BI to BigQuery (see Power BI guide).

Automation:
- Use Cloud Storage + Cloud Functions or Cloud Composer to automate load.
- Use Cloud Scheduler to trigger ingestion on schedule.