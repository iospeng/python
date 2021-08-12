import unittest

from unittest_demo1.util.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    # 生成测试报告
    report_title = '用例执行报告 标题'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = './result.html'

    # 方法四：指定测试用例文件，直接执行文件中的所有测试用例
    test_dir = './unittest_demo1'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
