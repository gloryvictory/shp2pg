#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : 05_shp2pgsql.py
#   Created         : 30th October 2019
#   Last Modified	: 30th October 2019
#   Version		    : 1.0
#
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : This script will search any *.shp files in the given directory by list (in file_list_shp.txt ) and convert to EPSG:SRID 4326 and load to postgresql+postgis
# converting by using this utility : shp2pgsql -d -I -W "cp1251" -s 4024:4326  c:\test\sta.shp "GISSCHEMA"."sta" -h 127.0.0.1 -u GISUSER |psql -d GISTEST -U GISUSER

import os                   # Load the Library Module
import os.path
import sys
from sridentify import Sridentify
#from time import strftime   # Load just the strftime Module from Time
import logging
from datetime import datetime
from sys import platform as _platform
import cfg #some global configurations



# get first line from file
def file_get_first_line(filename=''):
    first_line = ''
    if len(str(filename)):
        with open(filename, errors='ignore') as f:
            first_line = f.readline().lower().strip()
    return str(first_line)


def get_codepage_from_file(filename=''):
    str_result = ''
    first_line = file_get_first_line(filename)

    if first_line.endswith('1251') or first_line.endswith('utf-8'):
        if first_line.endswith('1251'):
            str_result = 'cp1251'
        if first_line.endswith('utf-8'):
            str_result = 'utf-8'
    else:
        str_result = first_line
    #print(str_result)

    return str_result.upper()


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
            print(
                'Input directories from config wrong: ' + dir_shp_in_win + ' or ' + dir_shp_in_linux + ' Using current directory: ' + dir_shp_in)
        print('Input directory from a config file: ' + dir_shp_in)
        return dir_shp_in

    if len(sys.argv) == 2:  # there is only one argument in command line
        dir_shp_in = str(sys.argv[1:][0])
        if os.path.isdir(dir_shp_in):
            return dir_shp_in
        else:
            print(
                dir_shp_in + " is not a Directory (Folder). Please specify an input directory. correctly. We use config file parameters.")
            if _platform == "linux" or _platform == "linux2" or _platform == "darwin":  # Linux platform
                dir_shp_in = dir_shp_in_linux
                return dir_shp_in
            if _platform == "win32" or _platform == "win64":  # Windows or Windows 64-bit
                dir_shp_in = dir_shp_in_win
                return dir_shp_in
            else:
                dir_shp_in = str(os.getcwd())
                print(
                    'Input directories from config wrong: ' + dir_shp_in_win + ' or ' + dir_shp_in_linux + ' Using current directory: ' + dir_shp_in)
            print('Input directory from a config file: ' + dir_shp_in)
            return dir_shp_in

    if len(sys.argv) > 2:  # there is only one argument in command line
        print("Arguments much more than 1! Please use only path as an argument. (Script.py /mnt/some_path) ")
        print(sys.argv, len(sys.argv))
        exit(1)
    return dir_shp_in


def get_output_directory():
    dir_out = str(os.getcwd())
    # Linux platform
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        dir_out = cfg.folder_out_linux
        if os.path.exists(dir_out) and os.path.isdir(dir_out):
            return dir_out
    if _platform == "win32" or _platform == "win64":  # Windows or Windows 64-bit
        dir_out = cfg.folder_out_win
        if os.path.exists(dir_out) and os.path.isdir(dir_out):
            return dir_out
    else:
        dir_out = str(os.getcwd())
        print(
            'Output directories from config wrong: ' + cfg.folder_out_win + ' or ' + cfg.folder_out_linux + ' Using current directory: ' + dir_out)
    print('Using Output directory: ' + dir_out)
    return dir_out

def do_shp_dir(dir_input=''):
    #do log file
    file_csv = str(os.path.join(get_output_directory(), cfg.file_log)).lower()
    print(file_csv)
    logging.basicConfig(filename=file_csv, format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG, filemode='w')

    #do main part
    try:
        for root, subdirs, files in os.walk(dir_input):
            for file in os.listdir(root):
                _srid=''
                _codepage=''
                file_path = str(os.path.join(root, file)).lower()
                ext = '.'.join(file.split('.')[1:]).lower()
                if file_path.endswith('shp'):  # ext == "shp":
                    file_name = file_path.split('.')[0]
                    file_prj = file_name + '.prj'
                    file_cp = file_name + '.cpg'
                    if os.path.isfile(file_prj) and os.path.isfile(file_cp):
                        logging.info(file_path)

                        if os.path.isfile(file_cp):

                            _codepage = get_codepage_from_file(file_cp)
                            str_err = file_cp + ' has codepage ' + _codepage
                            logging.info(str_err)
                            print(str_err)

                        if os.path.isfile(file_prj):
                            try:
                                ident = Sridentify(call_remote_api=False)  # Sridentify() # if we need  remote call
                                ident.from_file(file_prj)
                                _srid = ident.get_epsg()
                                if str(srid) != 'None':
                                    srid_source = ' -s ' + str(_srid) + ':4326 '
                                    cmd_line = program_shp2pgsql + ' -d -I -W "cp1251"' + srid_source + ' ' + file_in + ' \"' + schema + '\".\"' + table_name + "\"" + ' -h ' + cfg.host + ' -u ' + cfg.user + ' |psql -d ' + cfg.database_gis + ' -U ' + cfg.user
                                    print(cmd_line)
                            except:
                                print('Ошибка в файле: ' + file_prj)


                    else:
                        logging.error("Filename " + file_prj + ' or ' + file_cp + ' does not exist.')

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        logging.exception(e)

# ---------------- do main --------------------------------
def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    dir_input = get_input_directory()

    do_shp_dir(dir_input)
    #print(dir_input)

    # csv2xls()

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()
