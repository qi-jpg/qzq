import configparser
import os

#def readconfig():
class config(object):
    #获取当前文件所在目录的上一级目录
#    root_dir = os.path.dirname(os.path.abspath('.'))
    root_dir = os.path.dirname(os.path.abspath(__file__))
    print(root_dir)
    #初始化实例
    cf = configparser.ConfigParser()
    #拼接得到config.ini文件的路径
    cf.read(root_dir+"/config.ini")

    url = cf.get("normal", "url")
    app_key = cf.get("normal","app_key")
    app_secret = cf.get("normal","app_secret")

    cid = cf.get("app","cid")
    did = cf.get("app","did")


#    [mysql]
    host = cf.get("mysql","host")
    user = cf.get("mysql","user")
    pwd = cf.get("mysql","pwd")
    markdb = cf.get("mysql","markdb")


    #[wx]微信
    unionId = cf.get("wx","unionId")
    userId = cf.get("wx","userId")  #买买

#print("-------")
#print(config.root_dir)
#print(config.url)
#print("-------")


#    return cf

    #获取文件中所有的section配置项
   # secs = cf.sections()
    #print(secs)

    #获取配置项的值
    #app_key = cf.get("normal","app_key")
    #app_secret = cf.get("normal","app_secret")
    #url = cf.get("normal","url")
    #return app_key,app_secret,url

