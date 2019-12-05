import requests

import json
from urllib import parse

from data import test_code_data
from normal import url,getData,param,login_code,getData1

import pytest
'''
url = "https://service-wbs310.newtamp.cn/passport/api"

payload = "{\"timestamp\":\"2019-11-02 12:42:56\",\"app_key\":\"test\",\"format\":\"json\",\"version\":\"\",\"access_token\":\"3eda5e8e7-ef9e-48af-b04b-ed27b0e24b09\",\"name\":\"passport.employee.add\",\"data\":\"%7B%22gender%22%3A%22%22%2C%22deptIds%22%3A%5B99%5D%2C%22defaultDept%22%3A%22%22%2C%22documentType%22%3A%2299%22%2C%22joinDate%22%3A%222019-11-06%22%2C%22roleIds%22%3A%5B%5D%2C%22education%22%3A%222%22%2C%22married%22%3A%22%22%2C%22employeeNo%22%3A%22%22%2C%22positionId%22%3A43%2C%22name%22%3A%22zqzd002%22%2C%22documentNo%22%3A%2217658580000%22%2C%22mobile%22%3A%2217658580000%22%2C%22managers%22%3A%5B%5D%2C%22email%22%3A%22%22%7D\",\"sign\":\"AB5D495DCA63A2F88A1C4D47E08202F7\"}"
headers = {
    'token': "3eda5e8e7-ef9e-48af-b04b-ed27b0e24b09",
    'Content-Type': "text/plain",
    'User-Agent': "PostmanRuntime/7.19.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "ceef8530-14dd-4fe4-97f3-19316420898a,8e2951c1-ab0d-4a18-bf7f-32fccc807235",
    'Host': "service-wbs310.newtamp.cn",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "652",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

'''
@pytest.mark.parametrize("mobile,pwd",test_code_data)
def test_insertEmployee(mobile, pwd):

    loginUrl = url+ "/passport/api"
    name = "passport.employee.add"
    getCode = login_code(mobile,pwd)
    print("getCode = ")
    #getCode.text是一个字符串,将它转化为字典
    print(getCode.text)
    getToken_dict = json.loads(getCode.text)
    #获取value里面的token,####两个字典嵌套
    token = getToken_dict['value']['token']
 #   print("token = " + token)

 #   data = '"id":"65043"'
    data = '"%7B%22gender%22%3A%22%22%2C%22deptIds%22%3A%5B99%5D%2C%22defaultDept%22%3A%22%22%2C%22documentType%22%3A%2299%22%2C%22joinDate%22%3A%222019-11-06%22%2C%22roleIds%22%3A%5B%5D%2C%22education%22%3A%222%22%2C%22married%22%3A%22%22%2C%22employeeNo%22%3A%22%22%2C%22positionId%22%3A43%2C%22name%22%3A%22zqzd002%22%2C%22documentNo%22%3A%2217658580000%22%2C%22mobile%22%3A%2217658580000%22%2C%22managers%22%3A%5B%5D%2C%22email%22%3A%22%22%7D"'
    data_url = parse.quote("{" + data + "}")

    param_json = getData1(param, name, data_url,token)
    print("==========================================================================================")
    print(param_json)
    headers = {'Content-Type': "text/plain",'token':token}
    response = requests.request("POST", loginUrl, data=param_json, headers=headers)
    print(response.text)

  #  print(response.text)

