# -*- coding: utf-8 -*-
# @Project : selenium_event
# @File    : test_alert.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/9/26 17:16
from selenium.webdriver import ActionChains

from seleium_study.selenium_js.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切换frame
        self.driver.switch_to.frame('iframeResult')
        top = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        end = self.driver.find_element_by_xpath('//*[@id="droppable"]')
        # 拖拽元素top到元素end
        action = ActionChains(self.driver)
        action.drag_and_drop(top, end).perform()
        # 焦点切换到弹出框上,点击弹出框上的确定
        self.driver.switch_to.alert.accept()
        # 切换回默认的frame
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('//*[@id="submitBTN"]').click()
