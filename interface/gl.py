import hashlib
import time

#url = "https://service-wbsrecu.newbanker.cn"
url = "https://service-wbs310.newtamp.cn"
format = "json"
app_key = "test"
app_secret = "123456"

#获取当前时间
def nowTime():
    self = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#    nowTime_str = '“{}”'.format(self)
    nowTime_str = '{}'.format(self)
    return nowTime_str

#固定参数
#param = {"app_key":app_key,"format":format,"timestamp":nowTime(),"version":"",}
param = {
    "app_key": app_key,
    "format": format,
    "timestamp": nowTime(),
    "version": "",
}


#md5加密
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
 #       print(dic)

    param_all = app_secret + dic + app_secret
    param_all_md5 = md5(param_all)
#    print(param_all_md5)

    return param_all_md5





'''
class config_message:

    url = "https://service-wbsrecu.newbanker.cn"

    def set_url(url):
        config_message.url = url

    def get_url(self):
        return config_message.url

'''
