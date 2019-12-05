import pymysql



host = 'rm-2ze1w9epp05wvc4j4po.mysql.rds.aliyuncs.com'
user = 'test_admin'
pwd = '1qaz@WSX'
db = 'mc_client246'
sql = 'select * from t_activity WHERE id = \'8a69c7976e35b645016eac6a2ca5247c\''



def test_mydb(host,user,pwd,db,sql,port=3306,charset='utf8'):
    con = pymysql.connect(host=host,port=port,user=user,passwd=pwd,db=db,charset = charset)
    cur = con.cursor()
    cur.execute(sql)

    if sql.strip()[:6].upper() == 'SELECT':
        res = cur.fetchall()

    else:
        con.commit()
        res ='ok'

    cur.close()
    con.close()
    print(res)
    return res

print(test_mydb(host,user,pwd,db,sql))