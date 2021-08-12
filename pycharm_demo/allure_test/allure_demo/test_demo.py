import os

import allure
import pytest

"""
各修饰器用法
@allure.feature 大模块标题
@allure.story 功能点标题
@allure.severity 用例优先级（）指定执行某种级别的用例
    执行时增加个参数 --allure-severities XX, XX 
with allure.step 用例中步骤标题
@allure.link 给用例加连接
allure.attach 测试结果中添加存文本信息、HTML片段、图片、视频

控制台执行命令
生成json命令
pytest test_demo.py --alluredir=./report
打开json命令
allure serve ./report
"""


@allure.feature("功能名")
class TestDemo():

    @allure.story("功能步骤名")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_add(self):
        with allure.step("print"):
            print("allure测试报告1")
        with allure.step("用户登录"):
            allure.attach('张三', '用户名')
        print("allure测试报告")

    @allure.story("功能步骤名1")
    @allure.link("http://www.baidu.com", name='连接')
    @allure.severity(allure.severity_level.NORMAL)
    def test_del(self):
        print("allure测试报告 del")

    @allure.story("功能步骤名2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add1(self):
        with allure.step("print"):
            print("allure测试报告1")
        # with allure.step("用户登录"):
        allure.attach('张三', '用户名')
        print("allure测试报告")

    def test_attach_txt(self):
        allure.attach('纯文本信息', '存文本', attachment_type=allure.attachment_type.TEXT)

    def test_attach_html(self):
        allure.attach('<body>一段html代码块<body>', 'HTML代码块', attachment_type=allure.attachment_type.HTML)

    def test_attach_img(self):
        # allure.attach.file('img/jpg格式.jpg', '图片', attachment_type=allure.attachment_type.JPG)
        allure.attach.file("D:\Down\pycharm_demo\\allure_test\img\\1.jpg", '图片', attachment_type=allure.attachment_type.JPG)


if __name__ == '__main__':
    pytest.main()
