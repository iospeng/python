# -*- coding: utf-8 -*-
# @Project : Compliance
# @File    : logins.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/26 15:03
from time import sleep

from selenium.webdriver.common.by import By

from po.drivers import Drivers


class Logins(Drivers):
    base_url = 'http://192.168.90.101/login/login.html?service=http://192.168.90.162:8090/ims-pro/'

    def logins(self):
        self.cookies = None
        sleep(1)
        self.findtext(By.ID, 'username').send_keys('csgdcl1')
        sleep(1)
        self.findtext(By.ID, 'password').send_keys('123456')
        sleep(1)
        self.findtext(By.ID, 'login-Button').click()
        sleep(3)
        print('-----', self.driver.get_cookies())
        titles = self.findtext(By.XPATH, '/html/body/div[1]/nav/div/div[1]/div/span').text
        sleep(3)
        return titles
