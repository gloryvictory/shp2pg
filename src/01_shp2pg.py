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