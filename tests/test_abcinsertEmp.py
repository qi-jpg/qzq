import json

from normal import get_data,login_code,requestAsToken

def test_insertEmp():
    self = get_data('insertEmp.json')
    name = "passport.employee.add"
    token = login_code('17343057927','000000a')

    #去掉{}
    response = requestAsToken(name, json.dumps(self)[1:-1],token)
    print(response.text)


