#Import Data via yahoo Finance
from pandas_datareader import data as pdr
import sys
import pandas as pd
import yfinance as yf
import datetime
import os

################################################################
# run with args pythonfile -func parameter
# fucn -y use to import data from yahoo Finance, parameter is type, symbol, start date and end date : python ImportAndExportData.py -y forex EURUSD 2016-01-01 2022-12-31
# func -i import data from .excel/.csv, parameter is file name : python ImportAndExportData.py -i tesla.csv
# fucn -e export data to excel, parameter is extension and symbol : python ImportAndExportData.py -e .csv EURUSD
################################################################


def ImportDataFromYahoo(type, symbol, startdate, enddate):
    yf.pdr_override()
    if type == 'forex':
        symbol = symbol + "=x"
    return pdr.get_data_yahoo(f"{symbol}", start= startdate, end= enddate)

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
        ImportDataFromYahoo(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif sys.argv[1] == '-i':
        ImportFile(sys.argv[2])
    elif sys.argv[1] == '-e':
        ExportFile(sys.argv[2], sys.argv[3])
    







    