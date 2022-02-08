# -*- coding: utf-8 -*-
# @Project : RequestsDemo
# @File    : test_login_requests.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2022/1/6 13:33
import yaml

from many_test_request import env_demo


def test_login():
    # 读取yaml文件
    date = yaml.safe_load(open("../YamlFill/login.yaml"))
    request = env_demo.Api()
    r = request.get_many(date)
    print(r.text)
