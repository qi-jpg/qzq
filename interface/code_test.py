import requests
import unittest
import json
from urllib import parse
from gl import url,get_sign,param
from login import login


class Code(unittest.TestCase):
    def setUp(self):
        self.name = "passport.userinfo.bycode"
        self.loginCode = login("17343057927","000000a")
        del param['sign']
        self.param = param
        print("code_test begin...")

    def tearDown(self):
        print("code_test end...")

    def test_code(self):
        loginUrl = url + "/passport/api"
        #code值
        code_last = self.loginCode.split('=')
        code = code_last[-1]

        #code[:-2],截取除最后两个字符之外的所有
        data = '"code":"{}"'.format(code[:-2])
        data_url = parse.quote("{" + data + "}")

        print("self.data_url = " + data_url)
        # 把name和data传入param
        param['name'] = self.name
        param['data'] = data_url
        print("param_code =")
        print(param)

        # 生成sign值
        param_sign = get_sign(param)
        #把sign传入param
        param['sign'] = param_sign

        #转为json
        param_json = json.dumps(param)
        print("param_json = " + param_json)

        headers = {'Content-Type': "text/plain"}
        response = requests.request("POST", loginUrl, data=param_json, headers=headers)
        print(response.text)

        self.assertEqual(response.status_code,200,"status = 200")
        self.assertNotEqual(response.text,"","error")


if __name__ == '__main__':
    unittest.main()

