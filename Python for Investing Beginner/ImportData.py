#Import Data via yahoo Finance
from pandas_datareader import data as pdr
import sys
import pandas as pd
import yfinance as yf
import datetime


################################################################
# run with args pythonfile -func parameter
# fucn -y use to import data from yahoo Finance, parameter is symbol
# func -i import data from .excel/.csv, parameter is file name and file extension
# fucn -e export data to excel, parameter is file name and symbol
################################################################


def ImportDataFromYahoo(symbol):
    yf.pdr_override()
    #download data to dataframe
    data = pdr.get_data_yahoo(f"{symbol}=x", start='2019-01-01', end= datetime.datetime.now())
    print(data)


if __name__ == '__main__':
    if sys.argv[1] == '-y':
        ImportDataFromYahoo(sys.argv[2])







    