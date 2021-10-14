# -*- coding: utf-8 -*-
# @Project : hegui_po
# @File    : home_po.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/14 14:54
from time import sleep

from selenium.webdriver.common.by import By

from driver_seal.driver_seal import DriverSeal


class HomePo(DriverSeal):
    def home_po(self):
        sleep(5)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[1]/div/span').click()
        sleep(5)
        ele = self.driver.find_element(By.XPATH, '//*[@id="tblResult"]/tbody/tr[1]/td[2]/span').text
        print(ele)
        return ele
