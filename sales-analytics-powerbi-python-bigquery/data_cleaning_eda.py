"""
Data Cleaning & EDA template
Save this as a script or convert to a notebook.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv", parse_dates=["date"])
# Basic checks
print("Rows:", len(df))
print(df.info())
print(df.describe(include="all"))

# Example EDA: monthly revenue
df["month"] = df["date"].dt.to_period("M")
monthly = df.groupby("month")["revenue"].sum().reset_index()
print(monthly.head())

# Simple plot (save to file)
plt.figure()
monthly.plot(x="month", y="revenue", legend=False)
plt.title("Monthly Revenue")
plt.savefig("monthly_revenue.png")