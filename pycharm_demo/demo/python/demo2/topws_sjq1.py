
from  selenium import webdriver
import time
import unittest
import HTMLTestRunner

class sjq1(unittest.TestCase):
    '''
            使用“classmethod”修饰符修饰，使用setUpClass 方法，setUpClass方法仅运行一次，setUpClass方法必须使用classmethod修饰符修饰。
            setUp方法会运行多次。
    '''
    @classmethod
    def setUpClass(self):
    # def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def test_shou(self):
        u"""首页搜索"""
        self.driver.get('http://hz.topws.cn')
        text = self.driver.find_element_by_id('keyword')
        text.clear()
        text.send_keys('2017')
        self.driver.find_element_by_class_name('ecsc-search-button').click()

    '''
            使用“classmethod”修饰符修饰，使用tearDownClass 方法，tearDownClass方法仅运行一次，tearDownClass方法必须使用classmethod修饰符修饰。
            tearDown方法会运行多次。
    '''
    @classmethod
    def tearDownClass(cls):
    # def tearDown(self):
        pass