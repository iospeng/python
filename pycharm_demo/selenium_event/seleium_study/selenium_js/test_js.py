# -*- coding: utf-8 -*-
# @Project : selenium_event
# @File    : test_js.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/9/26 15:26
from time import sleep

import pytest

from seleium_study.selenium_js.base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium测试')
        # execute_script 执行js代码
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)

    def test_datetime(self):
        # 使用js代码操作时间空间
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("a=document.getElementById('train_date').value='2021-9-23'")
        self.driver.find_element_by_xpath('//*[@id="search_one"]').click()
