# -*- coding: utf-8 -*-
# @Project : hegui_po
# @File    : driver_seal.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/14 14:15
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class DriverSeal:
    def __init__(self, driver=None):
        if driver is None:
            # 通过remote 复用浏览器操作
            # chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            # chrome_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            # 打开浏览器
            self.driver.get('http://192.168.90.101/login/login.html?service=http://192.168.90.162:9800/illegal-pro/')
            # 隐式等待
            self.driver.implicitly_wait(3)
        else:
            # 给self.driver 添加一个WebDriver对象注解，解决在其他文件中调用self.driver不提示的问题
            # 注解本身没有任何赋值作用，仅方便IDE操作
            self.driver: WebDriver = driver

    # 封装find_element、解包元祖
    def findtext(self, by, locator = None):
        # 如果传参只有一个元祖，则解元祖
        if locator is None:
            return self.driver.find_element(*by)
        # 适配多种传参方式
        else:
            return self.driver.find_element(by= by, value= locator)
