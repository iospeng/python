# -*- coding: utf-8 -*-
# @Project : RequestsDemo
# @File    : test_yaml.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/12/15 15:19
import yaml


def test_yaml():
    env = {
        "default": "dev",
        "ip":
        {
            "dev": "192.168.90.162",
            "test": "192.168.90.163"
        },
        "method": "get",
        "url": "http://192.168.90.163:9000/rpt-company/rectifys/list?pageNum=1&pageSize=10&orderType=2",
        "header": {
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50SWQiOiI5NSIsInN1YiI6Iuays-WNl-WGnOadkeWuoui_kOS8g"
                     "eS4muerryIsImFyZWFDb2RlIjoiNDExNjAyIiwiY29tcGFueUlkIjoiNDExNjAyMDAwMDAwMDQ3MSIsImNvbXBhbnlOYW1lIjo"
                     "i5ZGo5Y-j5biC5rG96L2m6L-Q6L6T6ZuG5Zui6YCa5a6H6LSn6L-Q5pyJ6ZmQ5YWs5Y-4IiwiaWF0IjoxNjM5NTM0NjM4LCJhY2"
                     "NvdW50IjoiNDExNjAxMDAwNTAxLTI1In0.2MfUWgBi4TKa3vs6pdgTPl7WOfZnvTMZm3-mYJWnJbM"}
    }
    # 自动生成yaml文件
    with open("env.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)
