# -*- coding: utf-8 -*-
# @Project : RequestsDemo
# @File    : env_demo.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/12/15 14:21
import requests
import yaml


class Api:
    env = yaml.safe_load(open("env.yaml"))

    def many(self, date: dict):
        # 字符串替换
        date["url"] = str(date["url"].replace("192.168.90.163", self.env["ip"][self.env["default"]]))
        # 重写request
        r = requests.request(method=date["method"], url=date["url"], headers=date["header"])
        return r

