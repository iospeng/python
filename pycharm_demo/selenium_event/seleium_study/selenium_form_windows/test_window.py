# -*- coding: utf-8 -*-
# @Project : selenium_event
# @File    : test_window.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/9/26 10:54
from time import sleep

from seleium_study.selenium_form_windows.base import Base

# 多窗口切换（切换句柄）
class TestWindow(Base):
    def test_window(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="s-top-loginbtn"]').click()
        # # current_window_handle 当前窗口句柄
        # print(self.driver.current_window_handle)
        # # window_handles 所有窗口句柄
        # print(self.driver.window_handles)
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[2]/a').click()
        # # current_window_handle 当前窗口句柄
        # print(self.driver.current_window_handle)
        # # window_handles 所有窗口句柄
        # print(self.driver.window_handles)
        window = self.driver.window_handles
        # 切换句柄 定位新窗口的元素
        self.driver.switch_to.window(window[-1])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys('123456789')
        sleep(3)
        # 切换句柄，回到就窗口
        self.driver.switch_to.window(window[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys('12345689')
        sleep(3)
