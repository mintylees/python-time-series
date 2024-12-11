https://intro.quantecon.org/commod_price.html
!pip install yfinance
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import brentq
from scipy.stats import beta

s = yf.download('CT=F', '2016-1-1', '2023-4-1')['Adj Close']
fig, ax = plt.subplots()

ax.plot(s, marker='o', alpha=0.5, ms=1)
ax.set_ylabel('cotton price in USD', fontsize=12)
ax.set_xlabel('date', fontsize=12)

plt.show()

