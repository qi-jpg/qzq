import requests

import json
from urllib import parse

from data import test_code_data
from normal import url,getData,param,login_code

import pytest

@pytest.mark.parametrize("mobile,pwd",test_code_data)
def test_findEmployee(mobile, pwd):

    loginUrl = url+ "/passport/api"
    name = "passport.employee.detail"
    getCode = login_code(mobile,pwd)
    print("getCode = ")
    #getCode.text是一个字符串,将它转化为字典
    print(getCode.text)
    getToken_dict = json.loads(getCode.text)
    #获取value里面的token,####两个字典嵌套
    token = getToken_dict['value']['token']
 #   print("token = " + token)

    data = '"id":"65043"'
    data_url = parse.quote("{" + data + "}")

    param_json = getData1(param, name, data_url,token)
    print("==========================================================================================")
    print(param_json)
    headers = {'Content-Type': "text/plain",'token':token}
    response = requests.request("POST", loginUrl, data=param_json, headers=headers)
    print(response.text)

  #  print(response.text)

