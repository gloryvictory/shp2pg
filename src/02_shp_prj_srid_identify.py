#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          :   Viacheslav Zamaraev
#   email           :   zamaraev@gmail.com
#   Script Name     : 01_shp2pg.py
#   Created         : 25th September 2019
#   Last Modified	: 25th September 2019
#   Version		    : 1.0
#   PIP             : pip install sridentify
#   RESULT          : csv file with columns: FILENAME, PRJ, SRID, METADATA
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : This script will search some *.shp files in the given directory by list (in file_list_shp.txt ) and load to postgresql+postgis

import os                   # Load the Library Module
import os.path

from sridentify import Sridentify
from time import strftime   # Load just the strftime Module from Time
from sys import platform as _platform
from datetime import datetime

dir_shp_in = "c:\\test"
dir_shp_in_linux = "/mnt/gisdata"
# Linux platform
if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
    dir_shp_in = dir_shp_in_linux
# Windows or Windows 64-bit
#if _platform == "win32" or _platform == "win64":

_delimiter = ','

file_csv = str(strftime("%Y-%m-%d") + "_shp_info_in_folder_" + ".csv")


# get first line from file
def file_get_first_line(filename=''):
    first_line = 'NO'
    if len(str(filename)):
        with open(filename) as f:
            first_line = f.readline()
            f.close()
    return first_line


# ---------------- do main --------------------------------

if os.path.isfile(file_csv):
    os.remove(file_csv)

time1 = datetime.now()
print('Starting at :' + str(time1))

with open(file_csv, "a", errors='ignore') as file_csv_output:
    str_log = 'FILENAME, PRJ, SRID, METADATA,CODEPAGE, HAS_DEFIS'
    print(str_log)
    file_csv_output.write(str_log)
    file_csv_output.write('\n')
    #for file in os.listdir(dir_shp_in):                               # Find all the shp files in the directory
    for root, subdirs, files in os.walk(dir_shp_in):
        for file in os.listdir(root):
            file_path = str(os.path.join(root, file))
            str_log = ''
            ext = '.'.join(file.split('.')[1:]).lower()
            if ext == "shp":
                str_log = file_path
                file_name = file_path.split('.')[0]

                # Prj file exist
                file_prj = file_name + '.prj'
                if os.path.isfile(file_prj):
                    str_log = str_log + _delimiter + 'YES'
                    try:
                        ident = Sridentify()
                        ident.from_file(file_prj)
                        srid = ident.get_epsg()
                    except:
                        str_log = str_log + _delimiter + 'ERROR'
                    if len(str(srid)):
                        str_log = str_log + _delimiter + str(srid)
                    else:
                        str_log = str_log + _delimiter + 'NO'
                else:
                    str_log = str_log + _delimiter + 'NO' + _delimiter + 'NO'

                # Metadata exist
                file_prj = file_name + '.shp.xml'
                if os.path.isfile(file_prj):
                    str_log = str_log + _delimiter + 'YES'
                else:
                    str_log = str_log + _delimiter + 'NO'

                # Codepage exist
                file_cp = file_name + '.cpg'
                if os.path.isfile(file_cp):
                    str_log = str_log + _delimiter + str(file_get_first_line(file_cp))
                else:
                    str_log = str_log + _delimiter + 'NO'

                # defis symbol has found in file name
                file_1 = str(file)
                if file_1.find('-') != -1:
                    str_log = str_log + _delimiter + 'YES'
                else:
                    str_log = str_log + _delimiter + 'NO'

            if len(str_log):
                file_csv_output.write(str_log)
                file_csv_output.write('\n')
                print(str_log)
    file_csv_output.close()

time2 = datetime.now()
print('Finishing at :' + str(time2))
print('Total time : ' + str(time2 - time1))
print('DONE !!!!')