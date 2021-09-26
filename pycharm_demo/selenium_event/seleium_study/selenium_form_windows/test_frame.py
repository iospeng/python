# -*- coding: utf-8 -*-
# @Project : selenium_event
# @File    : test_frame.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/9/26 13:30
import pytest

from seleium_study.selenium_form_windows.base import Base


# 定位frame元素，frame嵌套定位
class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切换frame
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element_by_xpath('//*[@id="draggable"]').text)
        # 切换回原来的frame
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_xpath('//*[@id="submitBTN"]').text)


if __name__ == '__main__':
    pytest.main(['-s', 'test_frame.py'])
