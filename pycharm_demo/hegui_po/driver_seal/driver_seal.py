# -*- coding: utf-8 -*-
# @Project : hegui_po
# @File    : driver_seal.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/14 14:15
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class DriverSeal:
    # 添加base_url，可以支持测试用例灵活配置起始页
    base_url = ''

    def __init__(self, driver=None):
        if driver is None:
            # selenium 是根据坐标定位的，如果浏览器是缩放状态，定位会不准确
            # 通过remote 复用浏览器操作
            chrome_arg = webdriver.ChromeOptions()
            # 加入调试地址
            chrome_arg.debugger_address = '127.0.0.1:9222'
            # 实例化driver对象
            self.driver = webdriver.Chrome(executable_path='D:\Down\python\chromedriver.exe', options=chrome_arg)
            self.driver.maximize_window()
            # 打开浏览器
            self.driver.get(self.base_url)
            # 隐式等待
            self.driver.implicitly_wait(3)
        else:
            # 给self.driver 添加一个WebDriver对象注解，解决在其他文件中调用self.driver不提示的问题
            # 注解本身没有任何赋值作用，仅方便IDE操作
            self.driver: WebDriver = driver

    # 封装find_element、解包元祖
    def findtext(self, by, locator=None):
        # 如果传参只有一个元祖，则解元祖
        if locator is None:
            return self.driver.find_element(*by)
        # 适配多种传参方式
        else:
            return self.driver.find_element(by=by, value=locator)

    # 封装iframe切换
    def frame_switch(self, iframeID, locator=None):
        """

        :param iframeID:只传入一个参数，当做iframe的ID来用，直接通过ID切换iframe
        :param locator:传入两个参数，第二个参数代表的是iframe的坐标，是列表的第几个，第一个参数是iframe定位的标签也就是‘iframe’
        :return:
        """
        if locator is None:
            return self.driver.switch_to.frame(iframeID)
        else:
            return self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, iframeID)[locator])
