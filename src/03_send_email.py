#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#   Author          :   Viacheslav Zamaraev
#   email           :   zamaraev@gmail.com
#   Script Name     : 03_send_email.py
#   Created         : 09th October 2019
#   Last Modified	: 09th October 2019
#   Version		    : 1.0
#   PIP             :
#   RESULT          : csv file with columns: FILENAME;PRJ;SRID;METADATA;CODEPAGE;HAS_DEFIS;DATA_CREATION;DATA_MODIFY;DATA_LASTACCESS
# Modifications	: 1.1 -
#               : 1.2 -
#
# Description   : This script will send result Excel file to people

# import os                   # Load the Library Module
from datetime import datetime
from email import encoders
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
#from base64 import encodebytes
#import email
import os
from sys import platform as _platform
import os.path

import cfg


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
        print('Output directories from config wrong: ' + cfg.folder_out_win + ' or ' + cfg.folder_out_linux + ' Using current directory: ' + dir_out)
    print('Using Output directory: ' + dir_out)
    return dir_out



def send_email_with_file(file_excel=''):
    if (len(str(file_excel))):
        body_text = str('ОК - файл ' + file_excel + " Во вложении! Это результат выполнения скрипта на сервере 10.57.10.45 из папки /etc/cron.daily или /etc/cron.weekly имя скрипта: start_python_scripts.sh. Результат складывается в /tmp/shp_info/*")
        subject = 'Результат запуска скрипта. Excel file - ситуация с шейп-файлами'  # заголовок письма
        send_email(cfg.server_mail, cfg.server_mail_port, cfg.send_from, cfg.send_to, subject, body_text, file_excel)

def send_email_with_ERROR(file_excel=''):
    body_text = str('ERROR - нет такого файла ' + file_excel + " Сообщите о проблеме в службу ИТ!")
    subject = 'ERROR - Ошибка запуска скрипта'  # заголовок письма
    send_email(cfg.server_mail, cfg.server_mail_port, cfg.send_from, cfg.send_to, subject, body_text, file_excel)



def send_email(_server ='', _port='25', _from='', _to='', _subj='', _text='', _file=''):
    # Параметры SMTP-сервера
    smtp_server = _server
    smtp_port = _port
    #smtp_user = ""     # пользователь smtp
    #smtp_pwd = ""      # пароль smtp

    mail_from = _from   # отправитель
    mail_to = _to.split(',')       # получатель
    mail_text = _text
    mail_subj = _subj
    mail_coding = 'windows-1251'
    attach_file = _file  # прикрепляемый файл

    # формирование сообщения
    multi_msg = MIMEMultipart()
    multi_msg['From'] = Header(mail_from, mail_coding)
    multi_msg['To'] = Header(_to, mail_coding)
    multi_msg['Subject'] = Header(mail_subj, mail_coding)

    msg = MIMEText(mail_text.encode('cp1251'), 'plain', mail_coding)
    msg.set_charset(mail_coding)
    multi_msg.attach(msg)

    # присоединяем атач-файл
    if os.path.exists(attach_file) and os.path.isfile(attach_file):
        file = open(attach_file, 'rb')
        attachment = MIMEBase('application', "octet-stream")
        attachment.set_payload(file.read())
        encoders.encode_base64(attachment)
        file.close()
        only_name_attach = Header(os.path.basename(attach_file), mail_coding);
        attachment.add_header('Content-Disposition', 'attachment; filename="%s"' % only_name_attach)
        multi_msg.attach(attachment)
        # msg.preamble = 'excel'
        # fp = open(file_excel, 'rb')
        # xls = MIMEBase('application', 'vnd.ms-excel')
        # xls.set_payload(fp.read())
        # fp.close()
        # encoders.encode_base64(xls)
        # xls.add_header('Content-Disposition', 'attachment', filename=file_excel)
        # msg.attach(xls)
    else:
        if attach_file.lstrip() != "":
            print("Файл для атача не найден - " + attach_file)

    # отправка
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    # smtp.login(smtp_user, smtp_pwd)

    smtp.sendmail(mail_from, mail_to, multi_msg.as_string())


def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))
    file_excel = str(os.path.join(get_output_directory(), cfg.file_csv))

    file_excel = file_excel.split('.')[0] + '.xlsx'
    if os.path.isfile(file_excel):
        send_email_with_file(file_excel)
    else:
        send_email_with_ERROR(file_excel)

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()
