import yfinance as yf
import sys, os

file = open("stonks.txt",'r')
list_of_stonks = []
ticker_objs = {}
i = 0

for line in file:
    if len(line)>1:
        list_of_stonks.append(line.strip('\n'))

for ticker in list_of_stonks:
    i = i + 1
    try:
        ticker_objs[ticker] = yf.Ticker(ticker)
        print(str(i) + "," + ticker + "," + ticker_objs[ticker].info['sector'] + "," + ticker_objs[ticker].info['industry'])
    except Exception as e:
        print(e.args)

##############################################

## More random code
# import yfinance as yf
#
# list_of_stonks = ['AAPL','MSFT','TSLA','AMD','GME']
# stock_tickers = {}
#
# for ticker in list_of_stonks:
#     print("Getting ", ticker)
#     stock_tickers[ticker] = yf.Ticker(ticker)
#
# print(stock_tickers['AAPL'].balancesheet)   # pandas dataframe