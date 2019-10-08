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
#   RESULT          : csv file with columns: FILENAME;PRJ;SRID;METADATA;CODEPAGE;HAS_DEFIS;DATA_CREATION;DATA_MODIFY;DATA_LASTACCESS
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : This script will search some *.shp files in the given directory and makes CSV file with some information

import os                   # Load the Library Module
import os.path
import sys
from sys import platform as _platform
from time import strftime   # Load just the strftime Module from Time
from datetime import datetime
from sridentify import Sridentify
import csv
from chardet.universaldetector import UniversalDetector


import cfg #some global configurations

#get some configs
_delimiter = cfg.csv_delimiter


# get first line from file
def file_get_first_line(filename=''):
    first_line = cfg.value_no
    if len(str(filename)):
        with open(filename) as f:
            first_line = f.readline()
            f.close()
    return first_line


def get_encoding(file_dbf=''):
    #file_dbf = 'c:\\Glory\\MyPrj\\PycharmProjects\\dbf_test\\Lov.dbf'
    result = cfg.value_no
    if os.path.isfile(file_dbf):
        detector = UniversalDetector()
        filename = file_dbf
        print(filename.ljust(60)),
        detector.reset()
        with open(filename, "rb") as f:
            lines = f.readlines()
            for line in lines:
                detector.feed(line)
                if detector.done: break
            detector.close()
            result = detector.result['encoding']
            print(result)
            f.close()
    return result

def get_input_directory():
    # get from config
    dir_shp_in_win = cfg.folder_win
    dir_shp_in_linux = cfg.folder_linux
    dir_shp_in = str(os.getcwd())
    # if only run the script (1 argument)
    if len(sys.argv) == 1:  # there is only one argument in command line
        # Linux platform
        if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
            dir_shp_in = dir_shp_in_linux
            return dir_shp_in
        if _platform == "win32" or _platform == "win64":  # Windows or Windows 64-bit
            dir_shp_in = dir_shp_in_win
            return dir_shp_in
        else:
            dir_shp_in = str(os.getcwd())
            print('Input directories from config wrong: ' + dir_shp_in_win + ' or ' + dir_shp_in_linux + ' Using current directory: ' + dir_shp_in)
        print('Input directory from a config file: ' + dir_shp_in)
        return dir_shp_in

    if len(sys.argv) == 2:                  # there is only one argument in command line
        dir_shp_in = str(sys.argv[1:][0])
        if os.path.isdir(dir_shp_in):
            return dir_shp_in
        else:
            print(dir_shp_in + " is not a Directory (Folder). Please specify an input directory. correctly. We use config file parameters.")
            if _platform == "linux" or _platform == "linux2" or _platform == "darwin": # Linux platform
                dir_shp_in = dir_shp_in_linux
                return dir_shp_in
            if _platform == "win32" or _platform == "win64": # Windows or Windows 64-bit
                dir_shp_in = dir_shp_in_win
                return dir_shp_in
            else:
                dir_shp_in = str(os.getcwd())
                print('Input directories from config wrong: ' + dir_shp_in_win + ' or ' + dir_shp_in_linux + ' Using current directory: ' + dir_shp_in)
            print('Input directory from a config file: ' + dir_shp_in)
            return dir_shp_in

    if len(sys.argv) > 2:  # there is only one argument in command line
        print("Arguments much more than 1! Please use only path as an argument. (Script.py /mnt/some_path) ")
        print(sys.argv, len(sys.argv))
        exit(1)

    return dir_shp_in


def do_shp_dir(dir_input=''):
    _yes = cfg.value_yes
    _no = cfg.value_no
    _error = cfg.value_error

    file_csv = str(strftime("%Y-%m-%d") + "_shp_info_in_folder_" + ".csv")
    if os.path.isfile(file_csv):
        os.remove(file_csv)

    csv_dict = {'FILENAME': '', 'PRJ': '', 'SRID': '', 'METADATA': '', 'CODEPAGE': '', 'HAS_DEFIS': '', 'DATA_CREATION': '', 'DATA_MODIFY': '', 'DATA_LASTACCESS': ''} #  'CODEPAGE_DBF': '', # CODEPAGE_DBF -  work a long time

    with open(file_csv, 'w', newline='', encoding='utf-8') as csv_file:  # Just use 'w' mode in 3.x

        csv_file_open = csv.DictWriter(csv_file, csv_dict.keys(), delimiter=cfg.csv_delimiter)
        csv_file_open.writeheader()
        for root, subdirs, files in os.walk(dir_input):
            for file in os.listdir(root):
                file_path = str(os.path.join(root, file))
                ext = '.'.join(file.split('.')[1:]).lower()
                if ext == "shp":
                    csv_dict['FILENAME'] = file_path
                    file_name = file_path.split('.')[0]

                    csv_dict['DATA_CREATION'] = str(datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d'))
                    csv_dict['DATA_MODIFY'] = str(datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d'))
                    csv_dict['DATA_LASTACCESS'] = str(datetime.fromtimestamp(os.path.getatime(file_path)).strftime('%Y-%m-%d'))

                    # Prj file exist
                    file_prj = file_name + '.prj'
                    if os.path.isfile(file_prj):
                        csv_dict['PRJ'] = _yes
                        try:
                            ident = Sridentify(call_remote_api=False)  #Sridentify() # if we need  remote call
                            ident.from_file(file_prj)
                            srid = ident.get_epsg()
                            if len(str(srid)):
                                csv_dict['SRID'] = str(srid)
                            else:
                                csv_dict['SRID'] = _no
                        except:
                            csv_dict['SRID'] = _error
                    else:
                        csv_dict['PRJ'] = _no
                        csv_dict['SRID'] = _no

                    # Metadata exist
                    file_prj = file_name + '.shp.xml'
                    if os.path.isfile(file_prj):
                        csv_dict['METADATA'] = _yes
                    else:
                        csv_dict['METADATA'] = _no

                    # Codepage exist
                    file_cp = file_name + '.cpg'
                    if os.path.isfile(file_cp):
                        csv_dict['CODEPAGE'] = str(file_get_first_line(file_cp))
                    else:
                        csv_dict['CODEPAGE'] = _no

                    # Codepage DBF - work long time
                    # file_dbf = file_name + '.dbf'
                    # if os.path.isfile(file_dbf):
                    #
                    #     csv_dict['CODEPAGE_DBF'] = get_encoding(file_dbf)
                    # else:
                    #     csv_dict['CODEPAGE_DBF'] = _no

                    # defis symbol has found in file name
                    file_1 = str(file)
                    if file_1.find('-') != -1:
                        csv_dict['HAS_DEFIS'] = _yes
                    else:
                        csv_dict['HAS_DEFIS'] = _no

                #if len(str_log):
                    csv_file_open.writerow(csv_dict)
                    print(str(csv_dict.values()))
        csv_file.close()




# ---------------- do main --------------------------------
def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    dir_input = get_input_directory()

    do_shp_dir(dir_input)

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()