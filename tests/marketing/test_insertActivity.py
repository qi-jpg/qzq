import json
import os
from urllib import parse

import pytest
import requests
import urllib3
from pub.app import get_data,md5,getParam,getData,getForm
from config.readconfig import config
from pub.sql import test_mydb


#获取上一级的上一级目录，添加变量
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(autouse=True)
def begin():
    urllib3.disable_warnings()

    yield

#获取token
@pytest.fixture(scope='session')
def getApptoken():

    self = get_data(root_dir+'/json/login.json')
    self['password'] = md5(self['password'])
    name = "/http/advisor/login.json"

    key = ['cid','platform','did']
    value = [config.cid,'2',config.did]
    for i in self:
        key.append(i)
        value.append(self[i])

    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", config.url+name, data=getParam(key,value), headers=headers)

    token = json.loads(response.text)['data']['token']
    print(token)
    return token


def test_getPdcdetail(getApptoken):
    name = "pdc.product.advisorproductpage"
    date = "\"id\":374"

    headers = {'token': getApptoken,'Content-Type': "text/plain"}
    response = requests.request("POST", config.url + "/pdc/api", data=getData(name, date), headers=headers,verify=False)

    entityid = json.loads(response.text)['value']['outId']
    pdcname = json.loads(response.text)['value']['name']
    self = [entityid,pdcname]
    return self


def test_getuuid(getApptoken):
    headers = {'token':getApptoken}
    response = requests.request("GET", config.url+"/api/mcapi/api/v1/activity/share/uuid", headers=headers,verify=False)

    uuid = json.loads(response.text)['param']
    return uuid


def test_insertshare(getApptoken):
    key = ['type','respondent.realm','respondent.entityId','id','title']
    value = ['SHARE_CHAT','PRODUCT',test_getPdcdetail(getApptoken)[0],test_getuuid(getApptoken),parse.quote(test_getPdcdetail(getApptoken)[1])]

    headers = {'token':getApptoken,'Content-Type': "application/x-www-form-urlencoded",}
    response = requests.request("POST", config.url+"/api/mcapi/api/v1/activity", data=getForm(key,value), headers=headers,verify=False)
#    print(getForm(key,value))
    print(response.text)
    sql = 'select respondent_id,respondent_realm,title,type from t_activity WHERE id = \'' + value[3] + '\''
    print(sql)
    parentId = value[3]
    return parentId

    print(test_mydb(sql))




def getNosignData(key,value):
#    param = {}
    param = ""
    for i in range(len(key)):
        for j in range(len(value)):
            if i ==j:
#                param = "/"" + key[i] + "/"/:/"" + value[j] + "/""
                param = param+"\"%s\":\"%s\"" % (key[i],value[j])
                print(param)
#                param[key[i]] = value[j]
#                print(param)
        param = param +","
    return "{"+param[:-1] + "}"






def test_abc():
    response = {"entityId": "499fa6cb-a1a1-457d-b156-aa22b8f3e2f9","realm": "PRODUCT"}
    key = ['unionId','parentId','respondent','title','type','userId']
    value = [config.unionId,'8a69c7976e35b645016ead0fb38824a1',response,'ZTZ优选1号','VIEW',config.userId]
    print("+++++======+++++")
    print(value)

    url = 'https://investor-wbs310opensaas.newtamp.cn/marketing-api/api/v1/h5/wechat/action'
    print("abcdefg")
    a = getNosignData(key,value)

    print(a)
#    value = [config.unionId,test_insertshare(getApptoken),response,"ZTZ优选1号","VIEW",config.userId]
    headers = {'Content-Type': "application/json;charset=UTF-8"}
#    response = requests.request("POST",config.url +"/marketing-api/api/v1/h5/wechat/action",data =a,headers = headers,verify = False )
    response = requests.request("POST",url,data =a,headers = headers,verify = False )

    print(response.text)