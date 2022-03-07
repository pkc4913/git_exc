import pandas
import openpyxl
import pyupbit
import time
import logging

if __name__ == '__main__':
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO)

    stream_hander = logging.StreamHandler()
    mylogger.addHandler(stream_hander)

    file_handler = logging.FileHandler('my.log')
    mylogger.addHandler(file_handler)

    mylogger.info("server start!!!")

    dataframe = pyupbit.get_ohlcv(count=7)
    print(dataframe)
    condition = dataframe["open"] == 51875000
    print(condition)
    condition.index = ["1","2","3","4","5"]
    print(condition)
    dataframe.loc[condition] = [1,1,1,1,1,1]
    print(dataframe)