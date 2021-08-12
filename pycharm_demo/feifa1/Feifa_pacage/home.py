
import time
import os
import unittest
from BeautifulReport import BeautifulReport
from Feifa_pacage.LY_Login import Logins
from Feifa_pacage.SY_ShouYe import ShouYe
from Feifa_pacage.loggers import Log

obj_log = Log()

if __name__ == '__main__':
    # 得到当前系统时间
    new = time.strftime('%Y-%m-%d %H%M%S', time.localtime())
    # 获得本文件目录位置
    # local_path = os.getcwd()
    log_path = os.path.dirname(os.getcwd())
    # 设置文件保存路径
    log_path = os.path.join(log_path, 'Reports')
    print('本文件目录位置：' + log_path)

    # 实例化unittest.TestSuite()
    ts = unittest.TestSuite()
    # 按类加载全部测试用例
    # ts.addTest(unittest.makeSuite(Homes))
    try:
        # 按函数加载全部测试用例
        ts.addTest(Logins('test_log'))
        ts.addTest(ShouYe('test_Control'))
    except:
        Log.write_error('加载用例失败')

    # 报告命名
    filename = new + '.html'
    # 加载用例生产测试报告
    result = BeautifulReport(ts)
    # 定义报告属性
    result.report(description='非法营运测试报告', filename=filename, report_dir=log_path, theme='theme_default')
