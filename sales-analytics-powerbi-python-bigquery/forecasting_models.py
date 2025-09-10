"""
Forecasting models template:
- ARIMA (statsmodels)
- Prophet (if installed)
- LSTM (Keras)
"""
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
# Prophet import may fail if not installed: from prophet import Prophet
# Keras: from tensorflow.keras.models import Sequential ...

df = pd.read_csv("sales_data.csv", parse_dates=["date"])
daily = df.groupby("date")["revenue"].sum().reset_index()
daily = daily.set_index("date").asfreq("D").fillna(0)

# ARIMA example (short)
model = ARIMA(daily, order=(5,1,0))
res = model.fit()
print(res.summary())

# Forecast next 30 days
fc = res.get_forecast(steps=30)
print(fc.predicted_mean)