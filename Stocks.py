import matplotlib.pyplot as plt
import mpld3


import datetime as dt


import pandas_datareader.data as web



def validSymbol(symbol):
    try:
        df = web.DataReader(symbol,'yahoo',dt.date.today() - dt.timedelta(1), dt.date.today())
    except:
        return False
    return True

def getPrice(symbol1,symbol2,startDate = dt.date.today() - dt.timedelta(days=180),endDate = dt.date.today()):
    df = web.DataReader(symbol1, 'yahoo', startDate,endDate)
    df2 = web.DataReader(symbol2, 'yahoo', startDate,endDate)

    prices = df['Adj Close'].pct_change()
    prices2 = df2['Adj Close'].pct_change()

    fig,ax = plt.subplots()
    fig.set_figheight(6)
    fig.set_figwidth(10)
    ax.plot(prices,label=symbol1)
    ax.plot(prices2,label=symbol2)
    ax.legend()

    return mpld3.fig_to_html(fig)

