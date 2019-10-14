#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          : Viacheslav Zamaraev
#   email           : zamaraev@gmail.com
#   Script Name     : 04_shp2pg.py
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
from sys import platform as _platform
import cfg #some global configurations

global dir_shp_in
global program_shp2pgsql

dir_shp_in = cfg.folder_win
dir_shp_in_linux = cfg.folder_linux
# Linux platform
if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
    dir_shp_in = dir_shp_in_linux
# Windows or Windows 64-bit
#if _platform == "win32" or _platform == "win64":


#global dir_shp_out
#dir_shp_out = "c:\\test2"
#global program_ogr2ogr

#program_ogr2ogr = "ogr2ogr"
#shp2pg_program = "shp2pg"
program_shp2pgsql = 'shp2pgsql'

global schema
schema = cfg.schema

# def dir_clear(dir_out =''):
#     if len(str(dir_out)) == 0:
#         dir_out = os.getcwd()
#     filelist = [f for f in os.listdir(dir_out)]
#     for f in filelist:
#         os.remove(os.path.join(dir_out, f))


def shp_to_4326(dir_in='', dir_out=''):
    if len(str(dir_in)) == 0:
        dir_in = os.getcwd()
    if len(str(dir_out)) == 0:
        dir_out = os.getcwd()

    # r=root, d=directories, f = files
    for r, d, f in os.walk(dir_in):
        for file in f:
            file_in = str(os.path.join(r, file))
            #ff = file.split(".")[0] + "_4326" + ".shp"
            #file_out = str(os.path.join(dir_shp_out, ff))
            ext = '.'.join(file.split('.')[1:]).lower()

            file_name = file_in.split('.')[0]
            table_name = file.split('.')[0]
            if ext == "shp":
                # Prj file exist
                file_prj = file_name + '.prj'
                if os.path.isfile(file_prj):
                    ident = Sridentify()
                    ident.from_file(file_prj)
                    srid = ident.get_epsg()
                    if str(srid) != 'None':
                        srid_source = ' -s ' + str(srid) + ':4326 '
                        cmd_line = program_shp2pgsql + ' -d -I -W "cp1251"' + srid_source + ' ' + file_in + ' \"' + schema + '\".\"' + table_name + "\"" + ' -h ' + cfg.host + ' -u ' + cfg.user + ' |psql -d ' + cfg.database_gis + ' -U '+ cfg.user
                        print(cmd_line)

                #print(os.path.join(r, file))
                #print(file_in)


def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    #dir_clear(dir_shp_out)
    shp_to_4326(dir_shp_in)
    #os.system(program_ogr2ogr + " -t_srs EPSG:4326 " +  file_in +" "+ file_out)

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()