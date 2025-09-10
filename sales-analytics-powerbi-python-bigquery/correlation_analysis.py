"""
Correlation analysis template
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")
num = df[["units_sold","unit_price","revenue","cost","profit"]]
corr = num.corr()
print(corr)

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True)
plt.savefig("correlation_heatmap.png")