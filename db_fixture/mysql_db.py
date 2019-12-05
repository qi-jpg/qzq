#!/usr/bin/python3

import mysql.connector
import sys, os

user = 'test_admin'
pwd = '1qaz@WSX'
host = 'rm-2ze1w9epp05wvc4j4po.mysql.rds.aliyuncs.com'
db = 'wbs246'





select_sql = "SELECT id,name FROM wbs_employee WHERE mobile = '17343057927'"

cnx = mysql.connector.connect(user=user, password=pwd, host=host, database=db)
cursor = cnx.cursor()

try:
    cursor.execute(select_sql)

except mysql.connector.Error as err:
    print("query table 'wbs_employee' failed.")
    print("select Error: {}".format(err.msg))
    sys.exit()



cnx.commit()
cursor.close()
cnx.close()

