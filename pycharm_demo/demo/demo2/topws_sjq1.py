
from  selenium import webdriver
import time
import unittest
import HTMLTestRunner

class sjq1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def test_shou(self):
        self.driver.get('http://hz.topws.cn')
        text = self.driver.find_element_by_id('keyword')
        text.clear()
        text.send_keys('2017')
        self.driver.find_element_by_class_name('ecsc-search-button').click()
    def tearDown(self):
        pass