#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : 01_shp2pg.py
#   Created         : 25th September 2019
#   Last Modified	: 25th September 2019
#   Version		    : 1.0
#
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : This script will search any *.shp files in the given directory by list (in file_list_shp.txt ) and convert to EPSG:SRID 4326 and load to postgresql+postgis
# converting by using this utility : ogr2ogr -t_srs EPSG:4326 input_4236.shp input.shp


import os                   # Load the Library Module
import os.path

from sridentify import Sridentify

from time import strftime   # Load just the strftime Module from Time
#import logging
from datetime import datetime

global dir_shp_in
global dir_shp_out
global program_ogr2ogr

dir_shp_in = "c:\\test"
dir_shp_out = "c:\\test2"
program_ogr2ogr = "ogr2ogr"
#shp2pg_program = "shp2pg"


def dir_clear(dir_out =''):
    if len(str(dir_out)) == 0:
        dir_out = os.getcwd()
    filelist = [f for f in os.listdir(dir_out)]
    for f in filelist:
        os.remove(os.path.join(dir_out, f))


def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    dir_clear(dir_shp_out)

    #os.system(program_ogr2ogr + " -t_srs EPSG:4326 " +  file_in +" "+ file_out)

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()