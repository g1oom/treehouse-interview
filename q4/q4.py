import pandas as pd
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
import numpy as np
import datetime as dt
from scipy.stats import norm

tickers = ['AAPL.O','IBM.N', 'GOOG.O', 'BP.N', 'XOM.N', 'COST.O', 'GS.N']

weights = np.array([0.15, 0.2, 0.2, 0.15, 0.1, 0.15, 0.05])

# Part b
#assuming initial investment is 1 million
initial_investment = 1000000

data = pdr.get_data_yahoo(tickers, start="2016-01-01", end=dt.date.today())['Close']

returns = data.pct_change()

cov_matrix = returns.cov()

avg_returns = returns.mean()

port_mean = avg_returns.dot(weights)

port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))

mean_investment = (1+port_mean) * initial_investment
             
stdev_investment = initial_investment * port_stdev

# confidence level is 95%
conf_level = 0.05

cutoff = norm.ppf(conf_level, mean_investment, stdev_investment)

# find Var95% over 1 day
var_95 = initial_investment - cutoff
print(var_95)

# not sure how to do rest of the parts :(