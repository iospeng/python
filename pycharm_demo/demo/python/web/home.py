
from selenium import webdriver
import HTMLTestRunner
import time
import unittest

class HomeClass(unittest.TestCase):
    '''
        使用 “classmethod” 修饰符修饰 “setUpClass” 方法，
        这样 “setUpClass” 方法仅运行一次，
        “setUpClass” 方法和 “classmethod”并存，必须一起使用
        “setUp”方法运行多次

    '''
    @classmethod
    def setUpClass(self):
        #设置使用的浏览器并打开浏览器
        self.driver = webdriver.Chrome()
        #浏览器最大化
        self.driver.maximize_window()
        #设置需要测试的网址
        self.url = 'http://hz.topws.cn'

    #测试用例
    def test_Home(self):
        u"""首页登录按钮"""  #生成HTML格式的测试报告，在测试用例名称后面追加中文名字
        #打开浏览器
        self.driver.get(self.url)
        #定位首页登录按钮
        LogBut = self.driver.find_element_by_id('ECS_MEMBERZONE').find_element_by_xpath('//a[1]')
        # LogBut = self.driver.find_element_by_class_name('ecsc-login').find_element_by_xpath('//a[1]')
        #点击登录按钮
        LogBut.click()

    def test_log(self):
        u"""登录页"""
        time.sleep(2)       #暂停两秒3
        self.driver.get(self.url+'/user.php')
        #获得新页面的句柄
        now_handle = self.driver.current_window_handle
        #定位 用户名、密码、登录按钮；输入用户名和密码
        # self.driver.find_element_by_name('formLogin').find_element_by_name('loginname').sen.keys('15671278825')
        # self.driver.find_element_by_name('formLogin').find_element_by_id('nloginpwd').send_keys('sjq123456')
        # self.driver.find_element_by_name('formLogin').find_element_by_id('loginSubmit').click()
        self.driver.find_element_by_name('formLogin').find_element_by_id('loginname').send_keys('15671278825')
        self.driver.find_element_by_name('formLogin').find_element_by_id('nloginpwd').send_keys('sjq123456')
        self.driver.find_element_by_name('formLogin').find_element_by_id('loginSubmit').click()

        '''
                使用“classmethod”修饰符修饰，使用tearDownClass 方法，tearDownClass方法仅运行一次，tearDownClass方法必须使用classmethod修饰符修饰。
                tearDown方法会运行多次。
        '''
    @classmethod
    def tearDownClass(cls):
        # def tearDown(self):
        pass

if __name__ == '__main__':
    #路径
    test_dir = 'D:\python\python\web'
    #创建保存测试用例对象
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='home.py')
    #定义单元测试（测试用例）容器
    test = unittest.TestSuite()
    test.addTest(HomeClass('test_Home'))
    test.addTest(HomeClass('test_log'))
    #保存测试用例
    fieName = 'D:\\python\\python\\web\\errorimg\\web.html'
    fp = open(fieName,'wb')
    #测试报告标题
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试报告')
    runner.run(discover)
    fp.close()

