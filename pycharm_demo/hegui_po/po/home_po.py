# -*- coding: utf-8 -*-
# @Project : hegui_po
# @File    : home_po.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/14 14:54
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from driver_seal.driver_seal import DriverSeal


class HomePo(DriverSeal):
    # 添加base_url，可以支持测试用例灵活配置起始页
    base_url = 'http://192.168.90.162:9800/illegal-pro/'

    # 切换到待核查车辆列表
    def home_po(self):
        sleep(3)
        self.findtext(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[1]/div/span').click()
        # /html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[1]/div/span
        # /html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[2]/div/span
        # /html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[3]/div/span
        sleep(5)
        # 切换到ifram
        # self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME, "iframe")[1])
        self.frame_switch('iframe', 1)
        ele = self.driver.find_element(By.XPATH, '//*[@id="tblResult"]/tbody/tr[1]/td[2]/span').text
        # 切换回原始fram
        self.driver.switch_to.default_content()
        return ele

    # 通过车辆类型筛选车辆
    def vehicle_type_search(self):
        sleep(5)
        self.findtext(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[2]/div/ul/li[2]/ul/li[1]/div/span').click()
        sleep(5)
        # 切换iframe
        print(self.frame_switch('iframe', 1))
        self.findtext(By.XPATH, '//*[@id="defaultForm"]/div/div[3]/div/div/span/span[1]/span').click()
        self.findtext(By.XPATH, '//*[@id="select2-vehicleType-results"]/li[6]').click()
        self.findtext(By.XPATH, '//*[@id="col-control"]/div/div/button[2]').click()
        ele = self.findtext(By.XPATH, '//*[@id="tblResult"]/tbody/tr[1]/td[5]/span').text
        # 切换回默认iframe
        self.driver.switch_to.default_content()
        return ele
