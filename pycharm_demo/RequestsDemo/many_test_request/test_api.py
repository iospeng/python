# -*- coding: utf-8 -*-
# @Project : RequestsDemo
# @File    : test_api.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/12/15 14:51
import json
import re

import requests
import yaml

from many_test_request import env_demo


class TestApi:
    # 读取yaml文件
    date = yaml.safe_load(open("../YamlFill/env.yaml"))

    def test_send(self):
        api = env_demo.Api()
        r = api.get_many(self.date)
        print(r.json())
        assert r.json()["returnFlag"] == "200"
        # urls = 'http://192.168.90.101/sso-auth/rest/sso/login?username=csgdcl&password=123456&service=http://192.168.90.162:8090/ims-pro/&action=login&rememberMe=false&callback=beyond_callback_17'
        # header = {
        #         "Host": "192.168.90.101",
        #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
        #         "Accept": "*/*",
        #         "Referer": "http://192.168.90.101/login/login.html?service=http://192.168.90.162:8090/ims-pro/",
        #         "Accept-Encoding": "gzip, deflate",
        #         "Accept-Language": "zh-CN,zh;q=0.9",
        #         "Cookie": "JSESSIONID=9966FBA251638A3F92911D9A8D742122",
        #         "Connection": "keep-alive",
        #     }
        #
        #
        # # r = requests.request(method='get', url=urls, headers=env["header"])
        # r = requests.get(urls, params=header)
        # un = eval(r.text[19:-1])
        # print(un['data'])

