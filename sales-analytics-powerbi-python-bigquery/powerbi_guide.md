# Power BI Template & Connection Guide

This guide explains how to create a Power BI report using the provided `sales_data.csv` or by connecting to Google BigQuery.

Option A — Use CSV (quick):
1. Open Power BI Desktop -> Get Data -> Text/CSV -> select sales_data.csv
2. Load data, then create visuals:
   - Time series: Date vs Revenue (line chart)
   - Top products by revenue (bar chart)
   - Regional sales map (filled map or shape map)
   - Customer segment distribution (pie or stacked bar)
3. Add slicers for region, product_category, sales_channel, and date range.
4. Save as .pbix

Option B — Connect to BigQuery (recommended for production):
1. Publish sales_data.csv to BigQuery (see BigQuery guide).
2. In Power BI Desktop: Get Data -> Google BigQuery -> sign in with your Google account.
3. Select your project.dataset.table and load.
4. To schedule refresh: publish the PBIX to Power BI Service and configure a scheduled refresh with an on-premises data gateway if necessary.

Notes:
- For larger data, import mode may be slow. Consider DirectQuery or aggregated tables.
- Use parameterized queries or views in BigQuery for efficient filtering.