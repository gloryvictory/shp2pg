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
# Description   : This script will search some *.shp files in the given directory  by list (in file_list_shp.txt ) and load to postgresql+postgis

import os                   # Load the Library Module
from time import strftime   # Load just the strftime Module from Time

shpdir = "c:\puttylogs"
shp2pg_program = "shp2pg"

for files in os.listdir(shpdir):                               # Find all the shp files in the directory
    if files.endswith(".shp"):
        files1 = files + "." + strftime("%Y-%m-%d") + ".zip"
        os.chdir(logsdir)
        os.system(zip_program + " " + files1 + " " + files)
        #os.remove(files)