import requests
import unittest
import json
from urllib import parse

from gl import url,md5,get_sign,param
from login import login



class Login(unittest.TestCase):

    def setUp(self):
        print("login_test begin...")
        self.name = "passport.login.security"
        self.phone = "17343057927"
        self.pwd = "000000a"

    def test_login(self):
        loginUrl = url + "/passport/api"
        # md5加密
        pwd_md5 = md5(self.pwd)

        # 拼接data，并进行url转码
        data = '"account":"{}","password":"{}","returnUrl":"{}"'.format(self.phone, pwd_md5, self.mobile)
        data_url = parse.quote("{" + data + "}", 'utf-8')
        #		print(data_url)

        #把name和data传入param
        param['name'] = self.name
        param['data'] = data_url

        #生成sign值
        param_sign = get_sign(param)

        # 把sign值传入param
        param['sign'] = param_sign

        #将param编码成字符串
        param_json = json.dumps(param)
        print("param_json = " + param_json)
        headers = {'Content-Type': "text/plain"}
        response = requests.request("POST", loginUrl, data=param_json, headers=headers)
 #       response = login(self.phone,self.pwd)
  #      print("response = " + response)

  #      response_dic = eval(response)
 #       print(response_dic)

#        self.assertEqual(response_dic['code'],0,"error")
 #       self.assertNotIn("signature is invalid",response['msg'],"sign error")
 #       self.assertEqual(response['code'],0,"error")
        self.assertEqual(response.status_code,200,"status = 200")
 #       print(response.text)

    def tearDown(self):
        print("login_test end...")


if __name__ == '__main__':
    unittest.main()

