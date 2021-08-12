#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import logging
from utils.read_config import conf
from utils.get_path import *



class MyLogger(logging.Logger):

    def __init__(self, file=None):
        # 设置输出级别、输出渠道、输出日志格式
        super().__init__(conf.get("log", "name"), conf.get("log", "level"))

        # 日志格式
        self.msg = None
        fmt = '%(levelname)s %(name)s %(asctime)s %(filename)s [第%(lineno)d行] 日志详情：%(message)s'
        formatter = logging.Formatter(fmt)
        # 控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)

        if file:
            # 文件渠道
            handle2 = logging.FileHandler(file, encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)



if conf.getboolean("log", "file_ok"):
    FilePath = logger_dir
else:
    FilePath = None

logger = MyLogger(FilePath)

if __name__ == '__main__':
    MyLogger()
    logger.info("测试，我自己封装的日志类")
