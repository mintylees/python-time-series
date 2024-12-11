https://blog.mlq.ai/python-for-finance-time-series-analysis/#:~:text=The%20most%20popular%20Python%20library,tests%2C%20and%20statistical%20data%20exploration.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

from google.colab import files
uploaded = files.upload()
df = pd.read_csv('TSLA.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# mean value based off the end of the year resampling
df.resample(rule='A').mean()

# quarterly resampling
df.resample(rule='Q').mean()

df.shift(periods=1).head()
df['Open'].plot(figsize=(16,6))
df.rolling(7).mean().head(14)

df['Open'].plot()
df.rolling(7).mean()['Close'].plot(figsize=(16,6))

df['Close'].expanding().mean().plot(figsize=(16,6))

# Close 20 MA
df['Close: 20 Day Mean'] = df['Close'].rolling(20).mean()

# Upper = 20MA + 2*std(20)
df['Upper'] = df['Close: 20 Day Mean'] + 2*(df['Close'].rolling(20).std())

# Lower = 20MA - 2*std(20)
df['Lower'] = df['Close: 20 Day Mean'] - 2*(df['Close'].rolling(20).std())

# Plot Close
df[['Close','Close: 20 Day Mean','Upper','Lower']].plot(figsize=(16,6))



