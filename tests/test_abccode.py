import json
from normal import login
from normal import get_data,requestAs

def test_code():
    self = get_data('login.json')
    name = "passport.userinfo.bycode"
    dict = json.loads(login(self['mobile'],self['pwd']))
    # 截取返回值=号后面的内容
    value = dict['value'].split('=')
    data = '"code":"{}"'.format(value[-1])
    response = requestAs(name,data)
    msg_token = json.loads(response.text)

    assert response.status_code == 200, "internet error"
    assert msg_token['msg'] != "凭证已失效", "凭证已失效，请重新登录"
    assert "signature is invalid" not in msg_token['msg'], "sign计算错误，请检查"

