#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          :   Viacheslav Zamaraev
#   email           :   zamaraev@gmail.com
#   Script Name     : 01_shp2pg.py
#   Created         : 25th September 2019
#   Last Modified	: 25th September 2019
#   Version		    : 1.0
#
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : This script will search some *.shp files in the given directory by list (in file_list_shp.txt ) and load to postgresql+postgis

import os                   # Load the Library Module
import os.path

from sridentify import Sridentify

from time import strftime   # Load just the strftime Module from Time
#import logging
from datetime import datetime

global shpdir
shpdir = "c:\\test"
shp2pg_program = "shp2pg"


def shp_list_prj(shpdir):
    str_log = 'FILENAME, PRJ, SRID'
    print(str_log)
    #for file in os.listdir(shpdir):                               # Find all the shp files in the directory
    for root, subdirs, files in os.walk(shpdir):
        for file in os.listdir(root):
            file_path = str(os.path.join(root, file))
            str_log = ''
            ext = '.'.join(file.split('.')[1:]).lower()
            if ext == "shp":
                str_log = file_path
                file_name = file_path.split('.')[0]
                file_prj = file_name + '.prj'
                if os.path.isfile(file_prj):
                    str_log = str_log + ',' + 'YES'
                    ident = Sridentify()
                    ident.from_file(file_prj)
                    srid = ident.get_epsg()
                    if len(str(srid)):
                        str_log = str_log + ',' + str(srid)
                    else:
                        str_log = str_log + ',' + ''
                else:
                    str_log = str_log + ',' + 'NO'
            if len(str_log):
                print(str_log)
            # if ext == "prj":
            #     str_log = str_log + ',' + 'prj'
                #files1 = files + "." + strftime("%Y-%m-%d") + ".zip"
                #os.chdir(logsdir)
                #os.system(zip_program + " " + files1 + " " + files)
                #os.remove(files)


def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    #global LOGGER
    #LOGGER = InitLogFile()


    shp_list_prj(shpdir)


    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')
    #LOGGER.info("Duration scan script: " + str(time2 - time1))


if __name__ == '__main__':
    main()