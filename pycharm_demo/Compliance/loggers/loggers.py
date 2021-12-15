# -*- coding: utf-8 -*-
# @Project : Compliance
# @File    : loggers.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/27 16:48
import logging
import os
import time


class Loggers(object):
    logger = logging.getLogger()
    '设置日志级别'
    logger.setLevel(level=logging.NOTSET)
    '创建一个handler,用于写入日志'
    times = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    '在当前目录下新建文件夹保存日志logs'
    # log_path = os.path.dirname(r'E:/Download/git/project/python/pycharm_demo/Compliance') + '/logs/'
    # log_path = os.getcwd() + '/logs/'
    log_path = 'E:/Download/git/project/python/pycharm_demo/Compliance' + '/logs/'
    # 判断文件是否存在 存在返回True 否则返回false
    is_log_path = os.path.exists(log_path)
    if not is_log_path:
        # 如果目录不存在，则新建目录
        os.makedirs(log_path)
    print('日志路径：' + log_path)
    '设置日志文件名,并创建文件'
    log_name = log_path + times + '.log'
    print('文件名：' + log_name)
    '写入'
    fh = logging.FileHandler(log_name, mode='w')
    '设置日志输出到文件级别'
    fh.setLevel(logging.NOTSET)
    '用于日志同时输出到控制台'
    ch = logging.StreamHandler()
    ch.setLevel(logging.NOTSET)
    '日志格式'
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    '用于日志同时输出到控制台'
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    def write_error(self, txt):
        self.logger.error(txt)
