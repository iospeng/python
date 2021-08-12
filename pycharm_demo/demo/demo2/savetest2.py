
from selenium import webdriver
import unittest
import time
import HTMLTestRunner
# from 保存测试结果 import save


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        # self.assertTrue('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    # # unittest.main()
    # # 装载测试用例
    # test_cases = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # # 使用测试套件并打包测试用例
    # test_suit = unittest.TestSuite()
    # test_suit.addTests(test_cases)
    # # 运行测试套件，并返回测试结果
    # test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
    # # 生成测试报告
    # print("testsRun:%s" % test_result.testsRun)
    # print("failures:%s" % len(test_result.failures))
    # print("errors:%s" % len(test_result.errors))
    # print("skipped:%s" % len(test_result.skipped))
    # print('ceshi ')
    test_dir = 'D:\python\python\demo2'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='保存测试结果2.py')
    # 定义单元测试（测试用例）容器
    test = unittest.TestSuite()
    test.addTest(TestStringMethods('test_upper'))
    test.addTest(TestStringMethods('test_isupper'))
    suit = unittest.makeSuite(TestStringMethods)
    # print('保存测试结果')
    fileName = 'D:\\python\\python\\demo2\\errorImg\\file.html'
    fp = open(fileName, 'wb')
    print('gggg测试结果', fp)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='报告', description='测试报告')
    # runner.run(self.all_case())
    runner.run(discover)
    fp.close()
    # ta = TestStringMethods()
# if __name__ == '__name__':
    # suite = unittest.makeSuite(save)
    # fileName = 'D:\\python\\python\\demo2\\errorImg\\file.html'
    # fp = open(fileName, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试', description='ceshi')
    # runner.run(suite)