# -*- coding: utf-8 -*-
# @Project : RequestsDemo
# @File    : test_login_yaml.py.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2022/1/6 11:23

import yaml


def test_login_yaml():
    env = {
        "default": "",
        "method": "get",
        "url": "http://192.168.90.101/sso-auth/rest/sso/login",
        "header":
        {
                "Host": "192.168.90.101",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
                "Accept": "*/*",
                "Referer": "http://192.168.90.101/login/login.html?service=http://192.168.90.162:8090/ims-pro/",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cookie": "JSESSIONID=9599DB93C5B3AEDA3E37ABC2415A5F48",
                "Connection": "keep-alive",
        },
        "params": {
                "username": "csgdcl",
                "password": "123456",
                "service": "http://192.168.90.162:8090/ims-pro/",
                "action": "login",
                "rememberMe": "false",
                "callback": "beyond_callback_71",
        }
    }

    # 自动生成yaml文件
    with open("login.yaml", "w", encoding='utf-8') as f:
        yaml.safe_dump(data=env, stream=f, allow_unicode=True, sort_keys=False)
