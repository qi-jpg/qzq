import pymysql
from config.readconfig import config

def test_mydb(sql):
    con = pymysql.connect(host=config.host,port=3306,user=config.user,passwd=config.pwd,db=config.markdb,charset = 'utf8')
    cur = con.cursor()
    cur.execute(sql)

    if sql.strip()[:6].upper() == 'SELECT':
        res = cur.fetchall()

    else:
        con.commit()
        res ='ok'

    cur.close()
    con.close()
    return res
