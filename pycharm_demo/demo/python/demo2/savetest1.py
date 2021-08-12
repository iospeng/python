
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
from webOne import webPy

class save(unittest.TestCase):
    # 重写初始化函数
    def setUp(self):
        pass
    def testxyz(self):
        # x = xyz()
        # self.assertEqual(6, 6)
        webPy.test_HomeLogin()
    def testnum(self):
        # self.assertEqual(6, 5)
        webPy.test_Login()
    # def all_case(self):
    #     discover = unittest.defaultTestLoader.discover('testnum', pattern='test*.py', top_level_dir=None)
    #     print("dis:", discover)
    #     return discover

    # 重写
    def tearDown(self):
        # print('保存测试结果')
        pass

if __name__ == "__main__":
    # print('gggg测试结果')
    test_dir = 'D:\python\python\demo2'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='保存测试结果.py')
    # 定义单元测试（测试用例）容器
    test = unittest.TestSuite()
    test.addTest(save('testxyz'))
    test.addTest(save('testnum'))
    suit = unittest.makeSuite(save)
    # print('保存测试结果')
    fileName = 'D:\\python\\python\\demo2\\errorImg\\file.html'
    fp = open(fileName, 'wb')
    print('gggg测试结果', fp)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试报告')
    runner.run(discover)
    fp.close()
    s = save()
