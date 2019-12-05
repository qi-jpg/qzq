import time,sys
sys.path.append('./interface')
sys.path.append('./db_fixture')


from unittest import defaultTestLoader
from HTMLTestRunner import HTMLTestRunner
from db_fixture import test_data


test_dir = './interface'

testsuit = defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__ == "__main__":
    test_data.init_data()  # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp,title='testzq',description='testzq2')

    runner.run(testsuit)