# -*- coding: utf-8 -*-
# @Project : hegui_po
# @File    : login_po.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/14 14:39
from selenium.webdriver.common.by import By
from driver_seal.driver_seal import DriverSeal
from time import sleep
from po.home_po import HomePo


class LoginPo(DriverSeal):
    username_ele = (By.ID, 'username')
    password_ele = (By.ID, 'password')
    logbut_ele = (By.ID, 'login-Button')
    # 添加base_url，可以支持测试用例灵活配置起始页
    base_url = 'http://192.168.90.101/login/login.html?service=http://192.168.90.162:9800/illegal-pro/'
    # base_url = 'http://192.168.90.101/login/login.html?service=http://192.168.90.162:8090/ims-pro/'
    def login_po(self, name, password):
        # 加*解包元祖，传入两个参数
        # 如果不解包，传入‘(By.ID, 'username')’，解包则传入By.ID, 'username'
        # self.driver.find_element(*self.username_ele).send_keys(name)
        self.findtext(self.username_ele).send_keys(name)
        sleep(2)
        # self.driver.find_element(*self.password_ele).send_keys(password)
        self.findtext(self.password_ele).send_keys(password)
        sleep(1)
        # self.driver.find_element(*self.logbut_ele).click()
        self.findtext(*self.logbut_ele).click()
        return HomePo(self.driver)
