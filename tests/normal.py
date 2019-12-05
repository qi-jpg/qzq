import hashlib
import json
import time
from urllib import parse
import requests
import configparser
import os

#获取全局变量
root_dir = os.path.dirname(os.path.abspath('.'))
cf = configparser.ConfigParser()
cf.read(root_dir+"/config/config.ini")


#获取当前时间
def nowTime():
    self = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    nowTime_str = '{}'.format(self)
    return nowTime_str

#固定参数
param = {
    "app_key": cf.get('normal','app_key'),
    "format": "json",
    "timestamp": nowTime(),
    "version": "",
}


def md5(self):
    md5 = hashlib.md5()
    md5.update(self.encode(encoding='utf-8'))
    return md5.hexdigest().upper()


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

    param_all = cf.get('normal','app_secret') + dic + cf.get('normal','app_secret')
    param_all_md5 = md5(param_all)

    return param_all_md5

#name = "ac.activity.add"
#data = "%7B%0A%09%22name%22:%20%22111%22,%0A%09%22startTime%22:%20%222019-11-04%2021:48:41%22,%0A%09%22pictureUrl%22:%20%22https://pic.newbanker.cn/img/2401/2019/11/25/9de0d04923f34cebb0bd76a2ae49a342.jpg%22,%0A%09%22endTime%22:%20%222019-11-27%2021:48:43%22,%0A%09%22typeId%22:%2051,%0A%09%22summary%22:%20%22324%22,%0A%09%22deptCode%22:%20%7B%0A%09%09%22id%22:%201,%0A%09%09%22code%22:%20%22GTEAMM0001%22,%0A%09%09%22parentCode%22:%20None,%0A%09%09%22name%22:%20%22%E6%80%BB%E8%A3%81%E5%8A%9E%22,%0A%09%09%22empCnt%22:%200,%0A%09%09%22departmentTypeCode%22:%201,%0A%09%09%22childs%22:%20%5B%5D%0A%09%7D,%0A%09%22shareCfg%22:%201,%0A%09%22signUpResult%22:%201,%0A%09%22shareChannel%22:%20%5B1,%202%5D,%0A%09%22evaluationPeriod%22:%2030,%0A%09%22scope%22:%20%7B%0A%09%09%22innerAdvisorScope%22:%20%7B%0A%09%09%09%22officeIds%22:%20%5B%5D,%0A%09%09%09%22deptCodes%22:%20%5B%5D,%0A%09%09%09%22labelIds%22:%20%5B%5D,%0A%09%09%09%22type%22:%20-1%0A%09%09%7D,%0A%09%09%22outsideAdvisorScope%22:%20%7B%0A%09%09%09%22type%22:%20-1%0A%09%09%7D,%0A%09%09%22customerScope%22:%20%7B%0A%09%09%09%22labelIds%22:%20%5B-1%5D,%0A%09%09%09%22type%22:%20-1%0A%09%09%7D%0A%09%7D%0A%7D"
def getData(name,data):
    # 判断当前param是否有sign,name,data，若有，删掉
    dic = ['sign','name','data']

    for key in dic:
        if key in param.keys():
            del param[key]

    # 把name和data传入param
    param['name'] = name
    data_url = parse.quote("{" + data + "}", 'utf-8')
    param['data'] = data_url

    # 生成sign值
    param_sign = get_sign(param)
    # 把sign值传入param
    param['sign'] = param_sign
    # 将param编码成字符串
    param_json = json.dumps(param)


    return param_json


def requestAs(name,self):
    headers = {'Content-Type': "text/plain"}
    response = requests.request("POST", cf.get('normal','url') + "/passport/api", data=getData(name, self), headers=headers)
    return response


def requestAsToken(name, self,token):
    headers = {'Content-Type': "text/plain",'token':token}
    response = requests.request("POST", cf.get('normal','url') + "/passport/api", data=getData(name, self), headers=headers)
    return response



def login(mobile,pwd):
    name = "passport.login.security"
    data = '"account":"{}","password":"{}","returnUrl":"{}"'.format(mobile,md5(pwd),cf.get('normal','url'))
    response = requestAs(name, data)
    return response.text


def login_code(mobile,pwd):
    name = "passport.userinfo.bycode"
    dict = json.loads(login(mobile, pwd))
    # 截取返回值=号后面的内容
    value = dict['value'].split('=')
    data = '"code":"{}"'.format(value[-1])
    response = requestAs(name, data)

    getToken_dict = json.loads(response.text)
    # 获取value里面的token,####两个字典嵌套
    token = getToken_dict['value']['token']
    return token


#读json文件
def get_data(self):
    data = []
    with open(self,'r') as f:
        dict_data = json.loads(f.read())

    return dict_data
