# -*- coding: utf-8 -*-
# @Project : hegui_po
# @File    : test_check.py
# @Software: PyCharm
# @Author  : Lizhipeng
# @Email   : 1907878011@qq.com
# @Time    : 2021/10/14 15:33
from driver_seal.driver_seal import DriverSeal
from po.home_po import HomePo
from po.login_po import LoginPo
import pytest


class TestCheck:
    def test_check(self):
        test_home = LoginPo()
        assert "豫V89CH9" in test_home.login_po('system', 'linkcld12345678').home_po()

    def test_veh_type_search(self):
        test_veh = HomePo()
        assert "大型普通客车" in test_veh.vehicle_type_search()
