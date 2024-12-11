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
