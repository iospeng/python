# -*- coding: utf-8 -*-
# @Project : hegui_allure
# @File    : datas_demo.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/8/11 13:53
import yaml


def dates():
    with open('data/datas.yml') as f:
        dates = yaml.safe_load(f)
    print(dates['user'][1])


if __name__ == '__main__':
    dates()
