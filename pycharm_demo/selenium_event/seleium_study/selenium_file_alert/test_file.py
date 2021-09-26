# -*- coding: utf-8 -*-
# @Project : selenium_event
# @File    : test_file.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/9/26 16:58
from time import sleep

from seleium_study.selenium_js.base import Base


class TestFile(Base):
    def test_file(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_xpath('//*[@id="stfile"]').send_keys(
            "E:\Download\git\project\pycharm_demo\selenium_event\imgs\pycharm1.jpeg")
