#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from configparser import ConfigParser
from utils.get_path import *
import os



class ReadConfig(ConfigParser):

    def __init__(self, path):
        super().__init__()
        self.read(path, encoding="utf-8")


file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), r"config") #获取当前脚本路径拼接配置文件
conf = ReadConfig(file_path)
conf = ReadConfig(ini_file)



# print(conf)

if __name__ == '__main__':
    pass
    conf = ReadConfig("../config/pytest.ini")
    print(conf.get("log", "name"))
    print(conf.get("log", "level"))
    print(conf.get("mysql","username"))
    print(type(conf.get("mysql", "password")))
    print(conf.get("mysql", "host"))
    print(type(conf.get("mysql", "port")))
    print(conf.get("mysql", "database"))
    print(type(conf.get("log", "name")))
