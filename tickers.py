import pandas as pd

table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
tickerList = table[0]['Symbol']

for ticker in tickerList:
    if '.' in ticker:
        for i in range(500):
            if ticker == tickerList[i]:
                tickerList[i] = ticker.replace('.', '-')
                break