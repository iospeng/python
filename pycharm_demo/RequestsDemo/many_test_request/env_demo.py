# -*- coding: utf-8 -*-
# @Project : RequestsDemo
# @File    : env_demo.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/12/15 14:21
import json

import requests
import yaml


class Api:
    # 读取yaml文件
    env = yaml.safe_load(open("../YamlFill/env.yaml"))

    # 封装get请求
    def get_many(self, date: dict):
        # 字符串替换
        # date["url"] = str(date["url"].replace("192.168.90.163", self.env["ip"][self.env["default"]]))
        # 重写request
        r = requests.request(method=date["method"], url=date["url"], headers=date["header"])
        return r

    # 封装post请求
    def post_many(self, date: dict):
        r = requests.request(method=date["method"], url=date["url"], headers=date["header"], data=json.dumps(date["params"]))
        return r
