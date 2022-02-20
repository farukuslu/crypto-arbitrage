import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

#References
#https://www.analyticsvidhya.com/blog/2021/06/download-financial-dataset-using-yahoo-finance-in-python-a-complete-guide/

#Get BTC-USD daily data from YahooFinance for specific dates
# btc_df = yf.download('BTC-USD',
#                       start='2019-01-01',
#                       end='2022-02-20',
#                       progress=False,
# )
# btc_df.head()

#Or get BTC-USD daily data for all times
btc_df = yf.download('BTC-USD')

