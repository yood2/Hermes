from assetAnalysis import *
import yfinance as yf
from datetime import datetime

def main():
    # CREATE TICKER INSTANCE FOR AMAZON
    amzn = yf.Ticker("AMZN")

    # GET TODAYS DATE AND CONVERT IT TO A STRING WITH YYYY-MM-DD FORMAT (YFINANCE EXPECTS THAT FORMAT)
    end_date = datetime.now().strftime('%Y-%m-%d')
    amzn_hist = amzn.history(start='2022-01-01',end=end_date)
    print(amzn_hist)

if __name__ == '__main__':
    main()