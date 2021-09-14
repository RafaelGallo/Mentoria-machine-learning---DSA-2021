import numpy as np
import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

from yahoofinancials import YahooFinancials
import warnings
warnings.filterwarnings("ignore")

bitcoin = YahooFinancials('BTC-USD')

df = bitcoin.get_historical_price_data(start_date='2014-01-01', 
                                                  end_date='2021-09-12', 
                                                  time_interval='weekly')

df = pd.DataFrame(df['BTC-USD']['prices'])

df.to_csv("BTC-Train.csv")