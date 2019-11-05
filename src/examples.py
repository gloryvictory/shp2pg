
# run sql script through the psycopg2
# def sql_run(host='localhost', dbname='', user='', password='',  sql_statement=''):
#     # import psycopg2
#     # import sys
#     conn_string = 'host=' + '\'' + host + '\'' + ' dbname=\'' + dbname + '\'' + ' user=\'' + user + '\'' \
#                   + ' password=\'' + password + '\''
#     if len(str(sql_statement)) and len(str(host)) and len(str(dbname)) and len(str(user)) and len(str(password)):
#         con = None
#         print(conn_string + sql_statement)
#         try:
#             con = psycopg2.connect(conn_string) # should be look like "host='localhost' dbname='testdb' user='pythonspot' password='password'"
#             cur = con.cursor()
#             cur.execute(sql_statement)
#             con.commit()
#         except Exception as e:
#             logging.error("Exception occurred", exc_info=True)
#             logging.exception(e)
#             if con:
#                 con.rollback()
#             print('Error %s' % e)
#             #sys.exit(1)
#             return
#         finally:
#             if con:
#                 con.close()
#     else:
#         ss = "SQL Statement is NULL. Please specify SQL Statement."
#         print(ss)
#         logging.error(conn_string)
#         logging.error(sql_statement)
#         logging.error(ss)
#         #sys.exit(1)
#         return
