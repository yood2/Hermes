from assetAnalysis import *
import pandas as pd
import yfinance as yf

def main():
    symbol = 'MSFT'
    data = yf.Ticker(symbol)
    ts = data.history(start='2021-01-01', end='2023-12-31')
    df = pd.DataFrame(ts)
    df

if __name__ == '__main__':
    main()