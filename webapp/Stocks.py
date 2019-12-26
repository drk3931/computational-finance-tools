import matplotlib.pyplot as plt
import mpld3

import Globals as globals
import datetime as dt

import pandas_datareader.data as web



def validSymbol(symbol):
    try:
        df = web.DataReader(symbol, 'yahoo', dt.datetime(2019,12,1), dt.datetime(2019,12,2))
    except:
        return False
    return True

def getPrice(symbol1,symbol2,startDate = dt.datetime(2019,1,1),endDate = dt.datetime.now()):
    df = web.DataReader(symbol1, 'yahoo', startDate,endDate)
    df2 = web.DataReader(symbol2, 'yahoo', startDate,endDate)

    prices = df['Adj Close'].pct_change()
    prices2 = df2['Adj Close'].pct_change()

    fig,ax = plt.subplots()
    ax.plot(prices,label=symbol1)
    ax.plot(prices2,label=symbol2)
    ax.legend()

    return mpld3.fig_to_html(fig)

