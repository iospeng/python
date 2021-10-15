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
        # 切换到ifram
        # self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[1])
        self.frame_switch('iframe', 1)
        ele = self.driver.find_element(By.XPATH, '//*[@id="tblResult"]/tbody/tr[1]/td[2]/span').text
        # 切换回原始fram
        self.driver.switch_to.default_content()
        return ele
