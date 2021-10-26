# -*- coding: utf-8 -*-
# @Project : Compliance
# @File    : seat_register.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/26 15:58
import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from po.drivers import Drivers


class SeatRegister(Drivers):
    base_url = 'http://192.168.90.162:8090/ims-pro/'

    def seat_register(self):
        sleep(2)
        self.frame_switch('iframe', 0)
        ala = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
        print('-----', ala)

        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@id="table"]/tbody/tr/td[2]')) >= 1
        WebDriverWait(self.driver, 50).until(wait)
        # sleep(1)
        ele = self.findtext(By.XPATH, '//*[@id="table"]/tbody/tr/td[2]').text
        blb = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
        print('++++', blb)
        self.driver.switch_to.default_content()
        return ele
