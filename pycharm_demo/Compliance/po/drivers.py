# -*- coding: utf-8 -*-
# @Project : Compliance
# @File    : drivers.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/26 14:41
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# driver = None
# cookie = None

class Drivers:
    # 添加base_url，可以支持测试用例灵活配置起始页
    base_url = ''

    def __init__(self, drivers=None, cookie=None):
        if drivers is None:
            if cookie is None:
                # option = webdriver.ChromeOptions()
                # 不自动关闭浏览器
                # option.add_experimental_option("detach", True)
                # 实例化driver对象打开浏览器
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
                self.driver.get(self.base_url)
                # 隐式等待
                self.driver.implicitly_wait(3)
            else:
                # 实例化driver对象
                self.driver = webdriver.Chrome()
                self.driver.maximize_window()
                # 打开浏览器
                self.driver.get(self.base_url)
                # 循环遍历cookie给当前打开页面复值cookie
                for ck in cookie:
                    if 'expiry' in ck.keys():
                        ck.pop("expiry")
                    self.driver.add_cookie(ck)
                # 复值cookie后再次打开浏览器
                self.driver.get(self.base_url)
                # 隐式等待
                self.driver.implicitly_wait(3)
        else:
            # 给self.driver 添加一个WebDriver对象注解，解决在其他文件中调用self.driver不提示的问题
            # 注解本身没有任何赋值作用，仅方便IDE操作
            self.driver: WebDriver = self.driver

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
