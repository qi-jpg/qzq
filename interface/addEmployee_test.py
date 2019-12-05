import requests
import unittest
import json
from urllib import parse
from gl import url,get_sign,param
from login import login


class Code(unittest.TestCase):
    def setUp(self):

        print("code_test begin...")

    def tearDown(self):
        print("code_test end...")

    def test_AddEmployee(self):
        loginUrl = url + "/passport/api"

        payload = "{\"timestamp\":\"2019-11-02 12:42:56\",\"app_key\":\"test\",\"format\":\"json\",\"version\":\"\",\"access_token\":\"3eda5e8e7-ef9e-48af-b04b-ed27b0e24b09\",\"name\":\"passport.employee.add\",\"data\":\"%7B%22gender%22%3A%22%22%2C%22deptIds%22%3A%5B99%5D%2C%22defaultDept%22%3A%22%22%2C%22documentType%22%3A%2299%22%2C%22joinDate%22%3A%222019-11-06%22%2C%22roleIds%22%3A%5B%5D%2C%22education%22%3A%222%22%2C%22married%22%3A%22%22%2C%22employeeNo%22%3A%22%22%2C%22positionId%22%3A43%2C%22name%22%3A%22zqzd002%22%2C%22documentNo%22%3A%2217658580000%22%2C%22mobile%22%3A%2217658580000%22%2C%22managers%22%3A%5B%5D%2C%22email%22%3A%22%22%7D\",\"sign\":\"AB5D495DCA63A2F88A1C4D47E08202F7\"}"
        headers = {
            'token': "3eda5e8e7-ef9e-48af-b04b-ed27b0e24b09",
            'Content-Type': "text/plain"
        }

        response = requests.request("POST", loginUrl, data=payload, headers=headers)

        print(response.text)


if __name__ == '__main__':
    unittest.main()

