# -*- coding: utf-8 -*-
# @Project : selenium_event
# @File    : base.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/9/26 10:50
import os

from selenium import webdriver


class Base():

    def setup(self):
        # os.getenv 接受执行传参 browser=chrome pytest test_frame.py
        # browser = os.getenv("browser")
        # if browser == 'chrome':
        #     self.driver = webdriver.Chrome()
        # else:
            # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass
