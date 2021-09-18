# -*- coding: utf-8 -*-
# @Project : location_demo
# @File    : test_location.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/9/7 13:16
from time import sleep

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLocation:
    def setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.get('https://www.baidu.com/')
        # 隐式等待，每次定位前都会等待
        self.driver.implicitly_wait(3)

    def test_loc(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('baidu')
        # 显示等待，当元素出现会立刻点击，无需等到等待时间结束
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#su')))
        self.driver.find_element(By.CSS_SELECTOR, '#su').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="s_tab"]/div/a[1]')))
        # sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="s_tab"]/div/a[1]').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="1"]/div/h3/a')))
        self.driver.find_element(By.XPATH, '//*[@id="1"]/div/h3/a').click()
