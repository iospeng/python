
from selenium import webdriver
import time
import HTMLTestRunner
import unittest
from topws_sjq1 import sjq1

class sjq(unittest.TestCase):
    def setUp(self):
        # 设置所使用的浏览器
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        # 设置网址
        self.url = 'http://hz.topws.cn'
        print('打开浏览器')

    def test_Home(self):
        # 打开浏览器
        self.driver.get('http://hz.topws.cn')
        print('首页登录按钮')
        xt = self.driver.find_element_by_id('ECS_MEMBERZONE').find_element_by_xpath('//a[1]')
        xt.click()
        u"""测试用例中文说明"""

    def test_log(self):
        time.sleep(2)
        print('登录页')
        self.driver.get(self.url+'/user.php')
        now_handle = self.driver.current_window_handle
        self.driver.find_element_by_name('formLogin').find_element_by_id('loginname').send_keys('15671278825')
        self.driver.find_element_by_name('formLogin').find_element_by_id('nloginpwd').send_keys('sjq123456')
        self.driver.find_element_by_name('formLogin').find_element_by_id('loginSubmit').click()

    def tearDown(self):
        pass

if __name__ == '__main__':
    print('name')
    test_dir = 'D:\python\python\demo2'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='topws_sjq.py')
    # 定义单元测试（测试用例）容器
    test = unittest.TestSuite()
    test.addTest(sjq("test_Home"))
    test.addTest(sjq('test_log'))
    test.addTest(sjq1('test_shou'))
    suit = unittest.makeSuite(sjq)
    # print('保存测试结果')
    fileName = 'D:\\python\\python\\demo2\\errorImg\\file2.html'
    fp = open(fileName, 'wb')
    print('gggg测试结果', fp)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试报告')
    runner.run(discover)
    fp.close()