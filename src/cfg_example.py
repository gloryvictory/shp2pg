#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          :   Viacheslav Zamaraev
#   email           :   zamaraev@gmail.com
#   Script Name     : cfg.py
#   Created         : 25th September 2019
#   Last Modified	: 25th September 2019
#   Version		    : 1.0
#   PIP             :
#   RESULT          :
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : just rename cfg_example to cfg.py
import time

file_csv = str(time.strftime("%Y-%m-%d") + "_shp_info_in_folder_" + ".csv")
folder_win = 'c:\\test'
folder_linux = '/mnt/gisdata/'
schema = 'GISSCHEMA'
host = 'localhost'
user = 'test'
user_password = 'test'
database_gis = 'gisdb'
csv_delimiter = ';'
value_yes = 'YES'
value_no = 'NO'
value_error = 'ERROR'

HOST_MAIL = "localhost"
HOST_MAIL_PORT = 25
SEND_FROM = 'Zamaraev@gmail.com'
SEND_TO = 'Zamaraev@gmail.com, Zamaraev@someserver.com'
SEND_TEXT = 'Excel file - ситуация с шейп-файлами'
