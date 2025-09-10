"""
Customer segmentation template:
- RFM features
- KMeans, DBSCAN, Hierarchical
"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("sales_data.csv", parse_dates=["date"])
# RFM aggregation per customer
snapshot_date = df["date"].max()
df["date"] = pd.to_datetime(df["date"])
agg = df.groupby("customer_id").agg({
    "date": lambda x: (snapshot_date - x.max()).days,
    "order_id": "nunique",
    "revenue": "sum"
}).reset_index().rename(columns={"date":"recency","order_id":"frequency","revenue":"monetary"})

# Preprocessing
X = agg[["recency","frequency","monetary"]].fillna(0)
scaler = StandardScaler()
Xs = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=4, random_state=42).fit(Xs)
agg["segment"] = kmeans.labels_
print(agg.head())