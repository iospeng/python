# coding utf-8
from selenium import webdriver
import time
import unittest
from Feifa_pacage.loggers import Log

obj_log = Log()


class Logins(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
        except:
            obj_log.write_error('打开浏览器错误')
        cls.driver.implicitly_wait(3)

    def test_log(self):
        """登录"""
        try:
            self.driver.get('http://192.168.90.101/login/login.html?service=http://192.168.90.163:9325/illegal/')
        except:
            obj_log.write_error('打开网址错误')
        '''
        # 元素被遮挡导致可定位但不可点击，需要透过遮挡去强行点击
        # 需要使用execute_sript("arguments[0].click(), a),去操作元素的click的监听
        # arguments[0]为固定写法，a为定位的元素

        
        time.sleep(2)
        a = self.driver.find_element_by_xpath('//*[@id="idLogin"]')
        #判断元素是否定位到，让元素高亮显示
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", a, "border: 2px solid red;")
        self.driver.execute_script("arguments[0].click();", a)

        # 账号密码登录
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('system')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('Oracle11G')
        time.sleep(2)
        logBut = self.driver.find_element_by_xpath('//*[@id="login-Button"]')
        self.driver.execute_script("arguments[0].click();", logBut)
        '''
        # time.sleep(1)
        try:
            self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('system')
        except:
            obj_log.write_error('定位输入用户名错误')
        # time.sleep(1)
        try:
            self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('12345678')
        except:
            obj_log.write_error('定位输入密码错误')
        # time.sleep(1)
        try:
            self.driver.find_element_by_xpath('//*[@id="login-Button"]').click()
        except:
            obj_log.write_error('定位登录按钮错误')

    @classmethod
    def tearDownClass(cls):
        pass
