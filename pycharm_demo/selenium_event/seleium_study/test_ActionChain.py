# -*- coding: utf-8 -*-
# @Project : selenium_event
# @File    : test_ActionChain.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/9/14 14:11
import time
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


class TestActionChain():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        pass

    # 调用pytest.makr.skip 不执行下面的方法
    @pytest.mark.skip
    # 鼠标事件
    def test_case_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        # 拿到需要操作的元素
        sleep(2)
        element_click = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        element_doubleclick = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        element_rightclick = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        # 创建ActonChains 容器，将元素放进相应的事件中
        action = ActionChains(self.driver)
        # 鼠标单击事件
        action.click(element_click)
        sleep(1)
        # 鼠标双击事件
        action.double_click(element_doubleclick)
        sleep(1)
        # 鼠标右击事件
        action.context_click(element_rightclick)
        # 将元素放入容器中后调用perfrom()触发事件
        action.perform()

    @pytest.mark.skip
    # 光标移动
    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com/')
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        # 移动光标到定位到的控件上
        action.move_to_element(ele)
        action.perform()

    @pytest.mark.skip
    # 拖拽元素到某个位置
    def test_dragdrop(self):
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')
        drop = self.driver.find_element_by_xpath('//*[@id="dragger"]')
        drop2 = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)
        # 将元素拖拽到另一个位置
        # action.drag_and_drop(drop, drop2).perform()

        # 点击并按住元素
        # action.click_and_hold(drop)
        # 释放元素
        # action.release(drop2)
        # action.perform()

        # 点击并按住元素
        action.click_and_hold(drop)
        # 移动光标到指定位置
        action.move_to_element(drop2)
        # 释放元素
        action.release()
        action.perform()

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
