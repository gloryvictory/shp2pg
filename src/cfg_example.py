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
folder_out_win = 'C:\\out'
folder_out_linux = '/tmp/'
schema = 'GISSCHEMA'
host = 'localhost'
user = 'testuser'
user_password = 'test'
database_gis = 'gisdb'
csv_delimiter = ';'
value_yes = 'YES'
value_no = 'NO'
value_error = 'ERROR'

server_mail = "localhost"
server_mail_port = 25
send_from = 'Zamaraev@gmail.com'
send_to = 'Zamaraev@gmail.com, Zamaraev@someserver.com'
