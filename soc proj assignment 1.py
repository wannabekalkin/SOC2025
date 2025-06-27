import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os 
import nsetools as nse

tickers = ['RELIANCE']

for count in range(len(tickers)):
    tickers[count] = tickers[count] + '.NS'

end_date = datetime.today()  
print(end_date)

start_date = end_date - timedelta(days=4*365)
print(start_date)

stock_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    stock_df = data.head()

output_folder = r"D:\soc proj\Assignment 1"

output_file = os.path.join(output_folder, 'data_nse_4.csv')
stock_df.to_csv(output_file)