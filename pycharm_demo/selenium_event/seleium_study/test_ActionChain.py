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
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.keys import Keys


class TestActionChain():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

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

    @pytest.mark.skip
    # 输入空格 加删除一个字符
    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        el = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        el.click()
        action = ActionChains(self.driver)
        action.send_keys('username').pause(1)
        # 导入Keys,使用SPACE输入空格
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('tom').pause(1)
        # 输入删除键
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

    # touchaction 滑动页面，可操作H5页面
    def test_touchaction_scrollbottom(self):
        self.driver.get('http://www.baidu.com')
        el = self.driver.find_element_by_id('kw')
        el.send_keys('username')
        el_search = self.driver.find_element_by_id('su')
        action = TouchActions(self.driver)
        # tap 是 TouchActions 的点击事件
        action.tap(el_search)
        action.scroll_from_element(el, 0, 1000).perform()
        sleep(3)

