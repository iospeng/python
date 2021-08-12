# -*- coding:utf-8 -*-

from selenium import webdriver
import HTMLTestRunner
import time
import unittest
import HTMLTestRunner
from obj.Image import Images

img = Images()

class Login(unittest.TestCase):
    '''
        使用 “classmethod” 修饰符修饰 “setUpClass” 方法，
        这样 “setUpClass” 方法仅运行一次，
        “setUpClass” 方法和 “classmethod”并存，必须一起使用
        “setUp”方法运行多次

    '''
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_a_login(self):
        u"""登录"""
        self.driver.get('http://47.98.200.113:8082/back/login')
        self.driver.find_element_by_xpath('//*[@id="userAccount"]').send_keys('administrator')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="userPassword"]').send_keys('123456')
        time.sleep(1)
        yzm = input()
        self.driver.find_element_by_xpath('//*[@id="captcha"]').send_keys(yzm)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="jvForm"]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td/input').click()
        # 获取当前页面URL
        web_url = self.driver.current_url
        # 判断是否登陆成功并截图
        img.get_img('登陆成功,当前地址为：', '登陆失败，当前地址为：', web_url, 'http://47.98.200.113:8082/back/indexBack?APP_NAME=%E5%80%9F%E4%BA%AB')

    '''
                  使用“classmethod”修饰符修饰，使用tearDownClass 方法，tearDownClass方法仅运行一次，tearDownClass方法必须使用classmethod修饰符修饰。
                  tearDown方法会运行多次。
    '''
    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass
