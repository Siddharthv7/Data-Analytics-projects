# Integrated Analytics Project Package

Contents (saved in this folder):
- sales_data.csv            : Sample dataset (1 year of transactions)
- data_cleaning_eda.py     : Data cleaning & EDA template
- forecasting_models.py    : Forecasting models (ARIMA/Prophet/LSTM) template
- customer_segmentation.py : Customer segmentation templates (RFM + clustering)
- correlation_analysis.py  : Correlation / heatmap example
- automation_template.py   : Template to upload to BigQuery and trigger refreshes
- powerbi_guide.md         : Power BI connection & dashboard instructions
- bigquery_guide.md        : BigQuery upload & automation guide

To run locally:
1. Copy files to the same folder.
2. Create a virtualenv and install packages: pandas, numpy, matplotlib, scikit-learn, statsmodels, google-cloud-bigquery, jupyter
3. Open the scripts as notebooks in Jupyter or VS Code and run cells interactively.