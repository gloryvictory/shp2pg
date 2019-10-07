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
#   RESULT          : csv file with columns: FILENAME, PRJ, SRID, METADATA, CODEPAGE
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : This script will search some *.shp files in the given directory by list (in file_list_shp.txt ) and load to postgresql+postgis

import os                   # Load the Library Module
import os.path

from sridentify import Sridentify
from time import strftime   # Load just the strftime Module from Time
from sys import platform as _platform
import sys
import os
from datetime import datetime
import argparse
import cfg #some global configurations

#get some configs
dir_shp_in_win = cfg.folder_win
dir_shp_in_linux = cfg.folder_linux
_delimiter = cfg.csv_delimiter


file_csv = str(strftime("%Y-%m-%d") + "_shp_info_in_folder_" + ".csv")


# # get first line from file
# def file_get_first_line(filename=''):
#     first_line = 'NO'
#     if len(str(filename)):
#         with open(filename) as f:
#             first_line = f.readline()
#             f.close()
#     return first_line


# def get_encoding():
#     file_dbf = 'c:\\Glory\\MyPrj\\PycharmProjects\\dbf_test\\Lov.dbf'
#     import glob
#     from chardet.universaldetector import UniversalDetector
#
#     detector = UniversalDetector()
#     # for filename in glob.glob('*.dbf'):
#     filename = file_dbf
#     print(filename.ljust(60)),
#     detector.reset()
#     with open(filename, "rb") as f:
#         lines = f.readlines()
#         for line in lines:
#             detector.feed(line)
#             if detector.done: break
#         detector.close()
#         result = detector.result['encoding']
#         print(result)
#
# def do_shp_dir():
#     if os.path.isfile(file_csv):
#         os.remove(file_csv)
#
#     with open(file_csv, "a", errors='ignore') as file_csv_output:
#         str_log = 'FILENAME' + _delimiter + 'PRJ' + _delimiter + 'SRID' + _delimiter + 'METADATA' + _delimiter + 'CODEPAGE' + _delimiter + 'HAS_DEFIS'
#         print(str_log)
#         file_csv_output.write(str_log)
#         file_csv_output.write('\n')
#         #for file in os.listdir(dir_shp_in):                               # Find all the shp files in the directory
#         for root, subdirs, files in os.walk(dir_shp_in):
#             for file in os.listdir(root):
#                 file_path = str(os.path.join(root, file))
#                 str_log = ''
#                 ext = '.'.join(file.split('.')[1:]).lower()
#                 if ext == "shp":
#                     str_log = file_path
#                     file_name = file_path.split('.')[0]
#
#                     # Prj file exist
#                     file_prj = file_name + '.prj'
#                     if os.path.isfile(file_prj):
#                         str_log = str_log + _delimiter + 'YES'
#                         try:
#                             ident = Sridentify()
#                             ident.from_file(file_prj)
#                             srid = ident.get_epsg()
#                             if len(str(srid)):
#                                 str_log = str_log + _delimiter + str(srid)
#                             else:
#                                 str_log = str_log + _delimiter + 'NO'
#                         except:
#                             str_log = str_log + _delimiter + 'ERROR'
#                     else:
#                         str_log = str_log + _delimiter + 'NO' + _delimiter + 'NO'
#
#                     # Metadata exist
#                     file_prj = file_name + '.shp.xml'
#                     if os.path.isfile(file_prj):
#                         str_log = str_log + _delimiter + 'YES'
#                     else:
#                         str_log = str_log + _delimiter + 'NO'
#
#                     # Codepage exist
#                     file_cp = file_name + '.cpg'
#                     if os.path.isfile(file_cp):
#                         str_log = str_log + _delimiter + str(file_get_first_line(file_cp))
#                     else:
#                         str_log = str_log + _delimiter + 'NO'
#
#                     # defis symbol has found in file name
#                     file_1 = str(file)
#                     if file_1.find('-') != -1:
#                         str_log = str_log + _delimiter + 'YES'
#                     else:
#                         str_log = str_log + _delimiter + 'NO'
#
#                 if len(str_log):
#                     file_csv_output.write(str_log)
#                     file_csv_output.write('\n')
#                     print(str_log)
#         file_csv_output.close()


def get_input_directory():
    if len(sys.argv) == 2:
        dir_shp_in = str(sys.argv[1:][0])
        if os.path.isdir(dir_shp_in):
            return dir_shp_in
        else:
            print(
                dir_shp_in + " is not a Directory (Folder). Please specify an input directory. correctly. We use config file parameters.")
            # Linux platform
            if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
                dir_shp_in = dir_shp_in_linux
            # Windows or Windows 64-bit
            if _platform == "win32" or _platform == "win64":
                dir_shp_in = dir_shp_in_win
            else:
                dir_shp_in = str(os.getcwd())
                print(
                    'Input directories from config wrong: ' + dir_shp_in_win + ' or ' + dir_shp_in_linux + ' Using current directory: ' + dir_shp_in)
            print('Input directory: ' + dir_shp_in)
    else:
        print("Arguments much more than 1! Please use only path as an argument. (Script.py /mnt/some_path) ")
        print(sys.argv, len(sys.argv))
        exit(1)
    return dir_shp_in

# ---------------- do main --------------------------------
def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    dir_input = get_input_directory()

    #do_shp_dir():

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()