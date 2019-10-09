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

import os                   # Load the Library Module
from datetime import datetime
from email import encoders
from email.mime.multipart import MIMEMultipart
#from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib



import cfg


def send_email_with_file(file_excel=''):

    if (len(str(file_excel))):
        host = cfg.HOST_MAIL
        port = cfg.HOST_MAIL_PORT
        msg = MIMEMultipart()
        msg['Subject'] = cfg.SEND_TEXT
        msg['From'] = cfg.SEND_FROM
        msg['To'] = cfg.SEND_TO
        msg.preamble = 'excel'
        fp = open(file_excel, 'rb')
        xls = MIMEBase('application', 'vnd.ms-excel')
        xls.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(xls)
        xls.add_header('Content-Disposition', 'attachment', filename=file_excel)
        msg.attach(xls)
        s = smtplib.SMTP(host, port)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit()


def send_email_with_ERROR(file_excel=''):
    host = cfg.HOST_MAIL
    port = cfg.HOST_MAIL_PORT
    body_text = str('ERROR - нет такого файла ' + file_excel + " Сообщите о проблеме в службу ИТ!").encode('utf-8', 'ignore').decode('ascii', 'ignore')
    BODY = "\r\n".join((
         "From: %s" % cfg.SEND_FROM,
         "To: %s" % cfg.SEND_TO,
         "Subject: %s" % body_text,
         "",
         body_text
     ))
    msg = MIMEMultipart()
    msg['To'] = cfg.SEND_TO
    msg['From'] = cfg.SEND_FROM
    msg['Subject'] = "Добро пожаловать в реальный мир"
    #msg.attach(MIMEText(body_text, 'html', _charset='utf-8'))
    #msg = MIMEText(msg.encode('utf-8'), 'plain', 'utf-8')
    #text = msg.as_string()
    textpart = MIMEText(body_text.encode('utf-8'), 'plain', 'UTF-8')
    msg.attach(textpart)
    #msg.attach(MIMEText(body_text, 'plain'))
    msg.add_header('From', 'Monitoring')
    msg.add_header('Reply-To', 'Monitoring')
    msg.add_header('X-Mailer', 'Python')
    msg.add_header('Content-type', 'text/html charset=utf-8')

    # Добавление текста сообщения
    msg.attach(MIMEText(body_text))


    s = smtplib.SMTP(host, port)
    s.sendmail(cfg.SEND_FROM, cfg.SEND_TO, msg.as_string())
    s.quit()



def main():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    file_excel = cfg.file_csv.split('.')[0] + '.xlsx1'
    if os.path.isfile(file_excel):
        send_email_with_file(file_excel)
    else:
        send_email_with_ERROR()

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


if __name__ == '__main__':
    main()
