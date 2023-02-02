#Import Data via yahoo Finance
from pandas_datareader import data as pdr
import sys
import pandas as pd
import yfinance as yf
import datetime
import os

################################################################
# run with args pythonfile -func parameter
# fucn -y use to import data from yahoo Finance, parameter is symbol : python ImportData.py -y EURUSD
# func -i import data from .excel/.csv, parameter is file name : python ImportData.py -i tesla.csv
# fucn -e export data to excel, parameter is extension and symbol : python ImportData.py -e .csv EURUSD
################################################################


def ImportDataFromYahoo(symbol):
    yf.pdr_override()
    data = pdr.get_data_yahoo(f"{symbol}=x", start='2019-01-01', end= datetime.datetime.now())
    print(data)
    return data

def ImportFile(filename):
    path = f"{os.getcwd()}/data/"
    data = ""
    if filename.endswith(".csv"):
        data = pd.read_csv(f"{path}{filename}")
    elif filename.endswith(".xlsx") or filename.endswith(".xls"):
        data = pd.read_csv(f"{path}{filename}")
    else:
        print(f"can't import this file ({filename})")
    print(data)

def ExportFile(extension, symbol):
    data = ImportDataFromYahoo(symbol)
    path = f"{os.getcwd()}/data/"
    if extension == ".csv":
        data.to_csv(f"{path}{symbol}{extension}")
    elif extension in [".xlsx", ".xls"]:
        data.to_excel(f"{path}{symbol}{extension}")

if __name__ == '__main__':
    if sys.argv[1] == '-y':
        ImportDataFromYahoo(sys.argv[2])
    elif sys.argv[1] == '-i':
        ImportFile(sys.argv[2])
    elif sys.argv[1] == '-e':
        ExportFile(sys.argv[2], sys.argv[3])
    







    