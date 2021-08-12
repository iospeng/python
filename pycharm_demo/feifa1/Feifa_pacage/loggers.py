import os
import time
import logging


class Log(object):
    logger = logging.getLogger()
    '设置日志级别'
    logger.setLevel(level=logging.NOTSET)
    '创建一个handler，用于写入日志文件'
    rp = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    '在当前目录下新建日志文件夹logs'
    log_path = os.path.dirname(os.getcwd()) + '/logs/'
    log_name = log_path + rp + '.log'
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
