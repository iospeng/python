# -*- coding: utf-8 -*-
# @Project : RequestsDemo
# @File    : test_festival.py.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2022/1/6 14:02
import datetime
import json

import requests
import yaml

from many_test_request import env_demo


def test_fesetival():
    # 读取配置文件
    data = yaml.load(open("../YamlFill/festival.yaml", encoding='utf-8'))
    env = env_demo.Api()
    value = env.post_many(data)
    print(value.text)
