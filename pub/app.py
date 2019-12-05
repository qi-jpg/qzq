import hashlib
import json
import time
from urllib import parse
from config.readconfig import config


#获取当前时间
def nowTime():
    self = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    nowTime_str = '{}'.format(self)
    return nowTime_str

#固定参数
param = {
    "app_key": config.app_key,
  #  "format": "json",
    "timestamp": nowTime(),
    "version": "",
}


#读json文件
def get_data(self):
    data = []
    with open(self,'r') as f:
        dict_data = json.loads(f.read())

    return dict_data

#生成md5
def md5(self):
    md5 = hashlib.md5()
    md5.update(self.encode(encoding='utf-8'))
    return md5.hexdigest()

# 计算sign签名
# （1.key正序排列，2.去掉空格，冒号等后，拼接成一个字符串，
# 3.收尾都加上secret的值，测试环境是123456，4.然后md5加密，取32位大写）
def get_sign(param):
    #对param进行排序
    param_sort = sorted(param.items(),key = lambda x:x[0])

    dic = ''

    #去掉空格，冒号等后，拼接成一个字符串，
    for param_list in iter(param_sort):
        for i in param_list:
            dic = dic + i

    param_all = config.app_secret + dic + config.app_secret
#    param_all_md5 = md5(param_all).upper()

    return md5(param_all).upper()

#老接口封装date
def getParam(key,value):
    mydict = {}

    for i in range(len(key)):
        for j in range(len(value)):
            if i == j:
                mydict[key[i]] = value[j]

    datjson = json.dumps(mydict)
    date = "data={\"param\":" + datjson + "}"

    return date

#展业接口封装date
def getForm(key,value):
    mydict = ''

    for i in range(len(key)):
        for j in range(len(value)):
            if i == j:
                mydict = mydict+key[i] + "=" + value[j] + "&"

    return mydict[:-1]

#新接口封装date
def getData(name,data):
    # 判断当前param是否有sign,name,data，若有，删掉
    dic = ['sign','name','data']

    for key in dic:
        if key in param.keys():
            del param[key]

    # 把name和data传入param
    param['name'] = name
    param['data'] = parse.quote("{" + data + "}", 'utf-8')
    # 生成sign值,把sign值传入param
    param['sign'] = get_sign(param)
    # 将param编码成字符串
    param_json = json.dumps(param)


    return param_json
