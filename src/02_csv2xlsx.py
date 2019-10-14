#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : 02_csv2xlsx.py
#   Created         : 25th September 2019
#   Last Modified	: 25th September 2019
#   Version		    : 1.0
#   PIP             : pip install pandas
#   RESULT          : Excel File
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : This script will conver csv file to Excel file

import os.path
from datetime import datetime

try:
    import pandas as pd
except:
    print("we need pands. try: pip install pandas")


#some global configurations
import cfg


def csv2xls(filename=''):
    if (os.path.exists(filename) and os.path.isfile(filename)):
        file_excel = filename.split('.')[0] + '.xlsx'
        df_new = pd.read_csv(cfg.file_csv, sep=cfg.csv_delimiter)
        writer = pd.ExcelWriter(file_excel)
        df_new.to_excel(writer, index=False)
        writer.save()
    else:
        print('ERROR! can\'t read a file OR file does not exist. File: ' + filename)

# ---------------- do main --------------------------------
def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    csv2xls(cfg.file_csv)

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()