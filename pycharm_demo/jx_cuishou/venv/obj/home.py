# -*- coding:utf-8 -*-

from selenium import webdriver
import HTMLTestRunner
import time
import unittest
import HTMLTestRunner
from obj.cs_ad import cs_admin
from obj.one import Login

if __name__ == '__main__':
    #设置项目路径
    path = 'D:\install\jx_cuishou\\venv\obj'
    discover = unittest.defaultTestLoader.discover(path,pattern='home.py')
    # 定义单元测试（测试用例）容器
    test = unittest.TestSuite()
    test.addTest(Login('test_a_login'))
    test.addTest(cs_admin('test_b_query'))
    # test.addTest(cs_admin('test_c_name_query'))
    # suit = unittest.makeSuite(Login)
    fileName = 'D:\\install\\bg\\bg.html'
    fp = open(fileName, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试报告',verbosity=2)
    runner.run(discover)
    fp.close()