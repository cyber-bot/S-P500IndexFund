import yfinance as yf
from tickers import tickerList
from datetime import date, timedelta

investPerStock = 1000 # Investing $1000 Per Stock in S&P500
source = 'yahoo'
start = (date.today() - timedelta(days = 1)).strftime('%y-%m-%d')
end = (date.today()).strftime('%y-%m-%d')
sharesToBuy = {}

for ticker in tickerList:
    stockData = yf.download(tickers=ticker,period='2d', interval='1d')
    sharesToBuy[ticker] = investPerStock / stockData['Close'][-1]

print(sharesToBuy)