# -*- coding: utf-8 -*-
# @Project : RequestsDemo
# @File    : test_api.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/12/15 14:51
import yaml

from many_test_request import env_demo


class TestApi:
    # 读取yaml文件
    date = yaml.safe_load(open("env.yaml"))
    def test_send(self):
        api = env_demo.Api()
        r = api.many(self.date)
        print(r.json())
        assert r.json()["returnFlag"] == "200"
