import json

from normal import md5,get_data,requestAs

def test_login():
    #读取json文件
    self = get_data('login.json')
    name = "passport.login.security"
    # 拼接data，并进行url转码
    data = '"account":"{}","password":"{}"'.format(self['mobile'], md5(self['pwd']))
    response = requestAs(name,data)

    #断言
    msg_token = json.loads(response.text)
    print(msg_token['msg'])
    assert msg_token['msg'] != "账号密码错误", "账号密码不匹配"
    assert response.status_code == 200, "internet error"