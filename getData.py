import glob
import pandas as pd

def loadData(dataPath):
    path = dataPath
    allFile = glob.glob(path +'/*.csv')
    frame = pd.DataFrame()
    list_ = []
    for file_ in allFile:
        df = pd.read_csv(file_, index_col=None, header=0)
        list_.append(df)
    frame = pd.concat(list_)    
    frame.columns =  ['Symbol', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    
    return frame

def getStock(name, frame):
    stock = frame.loc[frame['Symbol']==name]
    stock = stock.sort_values(by='Date')
    stock['Date'] = pd.to_datetime(stock['Date'], format='%Y%m%d')
    stock = stock.set_index(['Date'])
    del stock['Symbol']
    
    return stock
